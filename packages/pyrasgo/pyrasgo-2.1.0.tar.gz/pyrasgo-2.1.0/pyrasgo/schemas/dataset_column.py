from typing import Optional, List, Dict

from pydantic import BaseModel, Field


class DatasetColumn(BaseModel):
    """
    Contract to return from get by id endpoints
    """

    id: Optional[int]
    name: Optional[str] = Field(alias='columnName')
    display_name: Optional[str] = Field(alias='displayName')
    data_type: Optional[str] = Field(alias='dataType')
    description: Optional[str]
    attributes: Optional[Dict[str, str]]

    class Config:
        allow_population_by_field_name = True


class DatasetColumnUpdate(BaseModel):
    """
    Contract to send to put endpoints
    """

    display_name: Optional[str] = Field(alias='displayName')
    description: Optional[str]
    attributes: Optional[Dict[str, str]]

    class Config:
        allow_population_by_field_name = True
