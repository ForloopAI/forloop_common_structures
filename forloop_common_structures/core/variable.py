from dataclasses import dataclass
from numbers import Number
from typing import Optional, Union

import pandas as pd

VariableValueTypes = Union[str, Number, pd.DataFrame, list, dict]


def get_digits(num: Number) -> int:
    """
    Returns the number of digits in a given number.

    Args:
        num (Number): The number for which to calculate the number of digits.

    Returns:
        int: The number of digits in the integer part of the number.

    Notes:
        - If the number is 0, the function returns 1 since the number '0' has 1 digit.
        - The function uses logarithmic computation (base 10) to determine the number of digits.
        - The function works for both positive and negative numbers by taking the absolute value.
        - For floating-point numbers, this only counts the digits in the integer part of the number.
    """
    if num == 0:
        return 1
    else:
        return int(math.log10(abs(num))) + 1


@dataclass
class Variable:
    """Class containing Dataframes, Lists, Dicts (JSON) - objects visible and possible to manipulate."""

    name: str
    value: VariableValueTypes
    type: Optional[str] = None
    size: Optional[int] = None
    is_result: bool = False
    pipeline_job_uid: str = "0"
    project_uid: str = "0"
    uid: Optional[str] = None

    def __post_init__(self) -> None:
        if self.type is None:
            self.type = type(self.value).__name__

        if self.size is None:
            try:
                self.size = len(self.value)
            except TypeError:
                self.size = 1

    def __str__(self) -> str:
        return f"{self.value}"

    # Misleading repr looking like a simple data type when debugging
    # retained as the Platform might depend on it
    def __repr__(self) -> str:
        return f"{self.value}"

    def __len__(self) -> int:
        return self.size

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if key in vars(self).keys():
                setattr(self, key, value)
            else:
                raise AttributeError(f"Attribute '{key}' cannot be updated, as it does not exist")
