#!/usr/bin/python3
"""write a class BaseModel that defines all common
attributes/methos for other classes"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "created_at" in kwargs:
                self.created_at = kwargs["created_at"]
            if "updated_at" in kwargs:
                self.updated_at = kwargs["updated_at"]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dic = self.__dict__.copy()
        dic.update(
            {"created_at": self.created_at.isoformat(),
             "updated_at": self.updated_at.isoformat(),
             "__class__": __class__.__name__})
        return dic
