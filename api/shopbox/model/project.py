# -*- coding: utf-8 -*-

from shopbox.model import db


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=32), nullable=False, unique=True)
    display_name = db.Column(db.String(length=64), nullable=False, unique=True)
    short_description = db.Column(db.String(length=280), nullable=False)
    long_description = db.Column(db.Text)

    def __str__(self):
        return f"<Project name='{self.name}>"

    def __repr__(self):
        return self.__str__()
