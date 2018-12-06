import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

from hs_restclient import HydroShare

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
    modelfiles = Column(String)


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

    hs = HydroShare()

    app_dir = app.get_app_workspace().path
    resourcelist = hs.getResourceFileList(resourceid)

    filelist = []

    conn_engine = app.get_persistent_store_database('primary_db', as_url=True)
    engine = create_engine(conn_engine)
    meta = MetaData()
    conn = engine.connect()

    for resource in resourcelist:
        url = resource['url'].split("/")
        fname = url[-1]
        ext = url[-1].split(".")[1]
        hs.getResourceFile('21c38e32c8f34de1a3073e738e7726bc', fname, destination=app_dir)
        filelist.append(fname)
        with open(
                '/Users/student/tethysdev/tethysapp-hs_modflow/tethysapp/hs_modflow/workspaces/app_workspace/etsdrt.dis',
                'r'
        ) as myfile:
            data = myfile.read()
            json.dumps(data)

        table = Table(ext, meta,
                          Column('resourceid', String, primary_key=True),
                          Column('data', String)
                          )
        table.create(engine, checkfirst=True)

        ins = table.insert().values(
            resourceid=resourceid,
            data=data)
        conn.execute(ins)

    conn.close()
    json.dumps(filelist)

    fav = Model(
        resourceid=resourceid,
        displayname=displayname,
        modeltype=modeltype,
        modelfiles=filelist
    )

    # Add the model to the session, commit, and close
    session.add(fav)

    session.commit()
    session.close()

    return
