from sqlalchemy.ext.declarative import declarative_base
from models import tickit


Base = declarative_base(metadata=tickit.metadata)


class Category(Base):
    __table__ = tickit.t_category


class Date(Base):
    __table__ = tickit.t_date


class Event(Base):
    __table__ = tickit.t_event


class Listing(Base):
    __table__ = tickit.t_listing


class Sales(Base):
    __table__ = tickit.t_sales


class User(Base):
    __table__ = tickit.t_users


class Venue(Base):
    __table__ = tickit.t_venue
