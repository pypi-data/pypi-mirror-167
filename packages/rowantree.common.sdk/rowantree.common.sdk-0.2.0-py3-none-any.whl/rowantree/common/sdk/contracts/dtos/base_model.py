""" Base Model (Pydantic) Over-Ride """

from pydantic import BaseModel as PydanticBaseModel


def to_camel(string: str) -> str:
    """
    Alias Generator Definition
    Used for external came based consumption.

    Parameters
    ----------
    string: str
        The input string to change casing of.

    Returns
    -------
    new_string: str
        A new string which has been camel cased.
    """

    return "".join(word.capitalize() for word in string.split("_"))


class BaseModel(PydanticBaseModel):
    """BaseModel [Pydantic] Over-Ride"""

    # https://pydantic-docs.helpmanual.io/usage/model_config/#options
    class Config:
        """Pydantic Config Over-Ride"""

        alias_generator = to_camel
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        use_enum_values = True
