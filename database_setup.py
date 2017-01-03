import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Category(Base):
    __tablename__ = 'dvdcategory'

    id = Column(Integer, primary_key=True)
    category = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Movie(Base):
    __tablename__ = 'movie'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    movie_poster = Column(String(250))
    category_id = Column(Integer, ForeignKey('dvdcategory.id'))
    category = Column(String(250), ForeignKey('dvdcategory.category'))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'category_id': self.category_id,
            'category': self.category,
        }


engine = create_engine('sqlite:///dvdcatalogue.db')


Base.metadata.create_all(engine)
