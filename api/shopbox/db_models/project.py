# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String

from shopbox.db.base_class import Base


class Project(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True, nullable=False)
    display_name = Column(String, nullable=False)
    short_description = Column(String(280), nullable=False)
    long_description = Column(String, nullable=False)
