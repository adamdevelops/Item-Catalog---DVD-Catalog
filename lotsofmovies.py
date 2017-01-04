from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Movie

engine = create_engine('sqlite:///dvdcatalogue.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for UrbanBurger
category1 = Category(category="Action")

session.add(category1)
session.commit()

movie1 = Movie(name="Jason Bourne", description="Bourne is back.",
                     movie_poster="http://t3.gstatic.com/images?q=tbn:ANd9GcQ27a64TqUZLOU1QbJiBPhu4mBZMW50wFzR62ob5W9o9Mgx7blK", category="Action")

session.add(movie1)
session.commit()


print "added items!"