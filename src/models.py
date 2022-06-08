import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()




class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username_id = Column(Integer)
    planets_id = Column(Integer)
    characters_id = Column(Integer)

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(Favorites.username_id))
    username = Column(String(250), nullable=False)
    password = Column(String(250))

class Planets(Base):
    __tablename__ = "Planets"
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey(Favorites.planets_id))
    name = Column(String)
    population = Column(Integer)
    terrain = Column(String)

class Characters(Base):
    __tablename__ = "Characters"
    id = Column(Integer, primary_key=True)
    char_id = Column(Integer, ForeignKey(Favorites.characters_id))
    name = Column(String)
    birth_year = Column(Integer)
    eye_color = Column(String)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')