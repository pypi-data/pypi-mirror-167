from dataclasses import dataclass
import functools
from inspect import Parameter, signature
from typing import Any, Callable, Dict

from validargs.exceptions import ValidationError


@dataclass
class Validator:
    """ Validator class used to differentiate between a regular default
    value and one that needs to be validated by a given validation rule.
    """
    validator_func: Callable
    default_value: Any = Parameter.empty

    def validate(self, arg: Any):
        if self.validator_func:
            self.validator_func(arg)


def get_args_dict(func: Callable, args: tuple, kwargs: dict) -> Dict[str, Any]:
    """ Constructs a dict with names/values of all passed arguments.

    NOTE: It requires that the Signature.parameters are ordered.

    Args:
        func (Callable): The decorated function
        args (tuple): Positional arguments passed in the decorated function
        kwargs (dict): Keyword arguments passed in the decorated function

    Returns:
        args_dict (dict): A name/value dictionary for all the arguments that
                            were passed in the decorated function
    """
    arg_names = [
        param.name
        for param in signature(func).parameters.values()
        if param.kind in (
            Parameter.POSITIONAL_ONLY,
            Parameter.POSITIONAL_OR_KEYWORD,
        )
    ]

    args_dict = {}
    for arg_name, arg_value in zip(arg_names, args):
        args_dict[arg_name] = arg_value

    args_dict.update(kwargs)

    return args_dict


def validated(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        args_dict = get_args_dict(func, args, kwargs)

        new_args = []
        new_kwargs = {}

        for param in signature(func).parameters.values():
            validator = param.default if isinstance(param.default, Validator) else None

            if param.name in args_dict:
                # Argument has been provided
                param_value = args_dict.get(param.name)

                if validator:
                    try:
                        validator.validate(param_value)
                    except Exception as exc:
                        raise ValidationError(f"Validation failed for argument: '{param.name}'") from exc

                if param.name in kwargs:
                    new_kwargs[param.name] = param_value
                else:
                    new_args.append(param_value)

            else:
                # Argument has not been provided. Try to assign defaults
                if validator:
                    default_value = validator.default_value
                else:
                    default_value = param.default

                if default_value == Parameter.empty:
                    raise TypeError(f"{func.__name__}() missing 1 required positional argument: '{param.name}'")

                if validator:
                    try:
                        validator.validate(default_value)
                    except Exception as exc:
                        raise ValidationError(f"Validation failed for argument: '{param.name}'") from exc

                if param.kind in (Parameter.KEYWORD_ONLY, Parameter.POSITIONAL_OR_KEYWORD):
                    new_kwargs[param.name] = default_value
                elif param.kind == Parameter.POSITIONAL_ONLY:
                    new_args.append(default_value)

        return func(*new_args, **new_kwargs)

    return wrapped
