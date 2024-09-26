import math
from dataclasses import dataclass
from numbers import Number
from typing import Optional, Union

import numpy as np
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
class BaseVariable:
    """
    Base class for variable and initial_variable objects with common initialization logic and
    dunder methods.
    """

    name: str
    value: VariableValueTypes
    type: Optional[str] = None
    size: Optional[int] = None
    is_result: bool = False
    project_uid: str = "0"
    uid: Optional[str] = None

    def __post_init__(self) -> None:
        if self.type is None:
            self.type = type(self.value).__name__

        if self.size is None:
            if self.value is None:
                self.size = 0
            elif isinstance(self.value, Number):
                self.size = get_digits(self.value)
            elif isinstance(self.value, (pd.DataFrame, pd.Series, np.ndarray)):
                self.size = self.value.size
            else:
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
                raise AttributeError(
                    f"Attribute '{key}' cannot be updated, as it does not exist"
                )


@dataclass
class Variable(BaseVariable):
    """
    Class containing Dataframes, Lists, Dicts (JSON) - objects visible and possible to manipulate.
    """

    pipeline_job_uid: str = "0"


@dataclass
class InitialVariable(BaseVariable):
    """
    Class containing Dataframes, Lists, Dicts (JSON) - objects visible and possible to manipulate.
    """

    pipeline_uid: str = "0"
