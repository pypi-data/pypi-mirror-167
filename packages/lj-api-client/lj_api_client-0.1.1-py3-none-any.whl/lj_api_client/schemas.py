from typing import Optional, List
from enum import Enum

from pydantic import BaseModel

class CardPermissionEnum(str, Enum):
    private = 'private'
    public = 'public'

class CardLogoEnum(str, Enum):
    person = 'person'
    memory = 'memory'
    smiley = 'smiley'
    car = 'car'
    flag = 'flag'
    subway = 'subway'
    tag = 'tag'
    medic = 'medic'
    card = 'card'

class CardKeyMappingModel(BaseModel):
    unit_key: str
    event_keys: List[str]
    date_keys: List[str]
    date_format: str

class CardFrontData(BaseModel):
    color: Optional[str]
    logo: Optional[CardLogoEnum]

class CardCreationModel(BaseModel):
    name: str
    permission: CardPermissionEnum
    unit_name: str
    key_mapping: CardKeyMappingModel
    front_data: Optional[CardFrontData]
    currency: Optional[str]
    currency_filters: Optional[List[str]]
    qualitative_filters: Optional[List[str]]
    quantitative_filters: Optional[List[str]]
    verbatim_filters: Optional[List[str]]

class CardUpdateModel(BaseModel):
    name: Optional[str]
    permission: Optional[CardPermissionEnum]    
    unit_name: Optional[str]
    front_data: Optional[CardFrontData]