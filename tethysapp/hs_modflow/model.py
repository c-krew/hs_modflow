import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import sessionmaker

from .app import HsModflow as app

Base = declarative_base()


# SQLAlchemy ORM definition for the models table
class Model(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'models'

    # Columns
    resourceid = Column(String, primary_key=True)
    displayname = Column(String)
    modeltype = Column(String)


def init_primary_db(engine, first_time):
    """
    Initializer for the primary database.
    """
    # Create all the tables
    Base.metadata.create_all(engine)

    # Add data
    if first_time:
        # Make session
        Session = sessionmaker(bind=engine)
        session = Session()

        session.commit()
        session.close()

def get_all_models():
    """
    Get all persisted dams.
    """
    # Get connection/session to database
    Session = app.get_persistent_store_database('primary_db', as_sessionmaker=True)
    session = Session()

    # Query for all model records
    models = session.query(Model).all()

    modellist = [(model.displayname, model.resourceid) for model in models]

    session.close()

    return modellist

def save_hs_to_favorites(resourceid, displayname, modeltype):

    Session = app.get_persistent_store_database('primary_db', as_sessionmaker=True)
    session = Session()

    fav = Model(
        resourceid=resourceid,
        displayname=displayname,
        modeltype=modeltype,
    )

    # Add the model to the session, commit, and close
    session.add(fav)

    session.commit()
    session.close()

    return
