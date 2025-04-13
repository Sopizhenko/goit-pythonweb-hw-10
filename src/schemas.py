from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict


class ContactBase(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: str = Field(max_length=100)
    phone: str = Field(max_length=20)
    birthdate: Optional[datetime] = None
    additional_info: Optional[str] = Field(None, max_length=255)

    model_config = ConfigDict(from_attributes=True)


class ContactCreate(ContactBase):
    pass


class ContactUpdate(ContactBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    birthdate: Optional[datetime] = None
    additional_info: Optional[str] = None


class ContactUpdateBirthdate(BaseModel):
    birthdate: datetime


class ContactModel(ContactBase):
    id: int

    class Config:
        orm_mode = True
