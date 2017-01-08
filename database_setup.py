import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, desc
from sqlalchemy import types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Category(Base):
    __tablename__ = 'dvdcategory'

    id = Column(Integer, primary_key=True)
    category = Column(String(80), nullable=False)
    #created = Column(DateTime)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'category': self.category,
            'id': self.id,
        }


class Movie(Base):
    __tablename__ = 'movie'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(Text)
    movie_poster = Column(Text)
    category = Column(String(80), ForeignKey('dvdcategory.category'))
    dvdcategory = relationship(Category)
    #created = Column(DateTime)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'movie_poster': self.movie_poster,
            'category': self.category
        }


engine = create_engine('sqlite:///dvdcatalogue.db')


Base.metadata.create_all(engine)
