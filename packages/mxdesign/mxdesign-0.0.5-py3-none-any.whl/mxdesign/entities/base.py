"""Base"""
import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_base

__all__ = [
    'Base',
    'TimestampMixin',
]


class Base(object):
    """Base"""


class TimestampMixin(object):
    """TimestampMixin"""
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)


Base = declarative_base(cls=Base)
