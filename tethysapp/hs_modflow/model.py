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
    id = Column(Integer, primary_key=True)
    resourceid = Column(String)
    displayname = Column(String)
    modeltype = Column(String)
    modelfiles = Column(String)
    zoneid = Column(Integer, ForeignKey("zone.id"), nullable=True)
    multid = Column(Integer, ForeignKey("mult.id"), nullable=True)
    pvalid = Column(Integer, ForeignKey("pval.id"), nullable=True)
    bas6id = Column(Integer, ForeignKey("bas6.id"), nullable=True)
    disid = Column(Integer, ForeignKey("dis.id"), nullable=True)
    disuid = Column(Integer, ForeignKey("disu.id"), nullable=True)
    bcf6id = Column(Integer, ForeignKey("bcf6.id"), nullable=True)
    lpfid = Column(Integer, ForeignKey("lpf.id"), nullable=True)
    hfb6id = Column(Integer, ForeignKey("hfb6.id"), nullable=True)
    chdid = Column(Integer, ForeignKey("chd.id"), nullable=True)
    fhbid = Column(Integer, ForeignKey("fhb.id"), nullable=True)
    welid = Column(Integer, ForeignKey("wel.id"), nullable=True)
    mnw1id = Column(Integer, ForeignKey("mnw1.id"), nullable=True)
    mnw2id = Column(Integer, ForeignKey("mnw2.id"), nullable=True)
    mnwiid = Column(Integer, ForeignKey("mnwi.id"), nullable=True)
    drnid = Column(Integer, ForeignKey("drn.id"), nullable=True)
    rchid = Column(Integer, ForeignKey("rch.id"), nullable=True)
    evtid = Column(Integer, ForeignKey("evt.id"), nullable=True)
    ghbid = Column(Integer, ForeignKey("ghb.id"), nullable=True)
    gmgid = Column(Integer, ForeignKey("gmg.id"), nullable=True)
    lmt6id = Column(Integer, ForeignKey("lmt6.id"), nullable=True)
    lmt7id = Column(Integer, ForeignKey("lmt7.id"), nullable=True)
    rivid = Column(Integer, ForeignKey("riv.id"), nullable=True)
    strid = Column(Integer, ForeignKey("str.id"), nullable=True)
    swi2id = Column(Integer, ForeignKey("swi2.id"), nullable=True)
    pcgid = Column(Integer, ForeignKey("pcg.id"), nullable=True)
    pcgnid = Column(Integer, ForeignKey("pcgn.id"), nullable=True)
    nwtid = Column(Integer, ForeignKey("nwt.id"), nullable=True)
    pksid = Column(Integer, ForeignKey("pks.id"), nullable=True)
    smsid = Column(Integer, ForeignKey("sms.id"), nullable=True)
    sfrid = Column(Integer, ForeignKey("sfr.id"), nullable=True)
    lakid = Column(Integer, ForeignKey("lak.id"), nullable=True)
    gageid = Column(Integer, ForeignKey("gage.id"), nullable=True)
    sipid = Column(Integer, ForeignKey("sip.id"), nullable=True)
    sorid = Column(Integer, ForeignKey("sor.id"), nullable=True)
    de4id = Column(Integer, ForeignKey("de4.id"), nullable=True)
    ocid = Column(Integer, ForeignKey("oc.id"), nullable=True)
    uzfid = Column(Integer, ForeignKey("uzf.id"), nullable=True)
    upwid = Column(Integer, ForeignKey("upw.id"), nullable=True)
    subid = Column(Integer, ForeignKey("sub.id"), nullable=True)
    swtid = Column(Integer, ForeignKey("swt.id"), nullable=True)
    hydid = Column(Integer, ForeignKey("hyd.id"), nullable=True)
    hobid = Column(Integer, ForeignKey("hob.id"), nullable=True)
    vdfid = Column(Integer, ForeignKey("vdf.id"), nullable=True)
    vscid = Column(Integer, ForeignKey("vsc.id"), nullable=True)

class zone(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'zone'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)

class mult(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'mult'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)

class pval(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'pval'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class bas6(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'bas6'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class dis(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'dis'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class disu(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'disu'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class bcf6(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'bcf6'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class lpf(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'lpf'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class hfb6(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'hfb6'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class chd(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'chd'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class fhb(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'fhb'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class wel(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'wel'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class mnw1(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'mnw1'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class mnw2(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'mnw2'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class mnwi(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'mnwi'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class drn(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'drn'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class rch(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'rch'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class evt(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'evt'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class ghb(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'ghb'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class gmg(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'gmg'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class lmt6(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'lmt6'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class lmt7(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'lmt7'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class riv(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'riv'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class str(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'str'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class swi2(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'swi2'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class pcg(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'pcg'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class pcgn(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'pcgn'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)

class nwt(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'nwt'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)

class pks(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'pks'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class sms(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'sms'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class sfr(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'sfr'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class lak(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'lak'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class gage(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'gage'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class sip(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'sip'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class sor(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'sor'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class de4(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'de4'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class oc(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'oc'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class uzf(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'uzf'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class upw(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'upw'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class sub(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'sub'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class swt(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'swt'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class hyd(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'hyd'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)


class hob(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'hob'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)

class vdf(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'vdf'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)

class vsc(Base):
    """
    SQLAlchemy Model DB Model
    """
    __tablename__ = 'vsc'

    # Columns
    id = Column(Integer, primary_key=True)
    data = Column(String)

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
        hs.getResourceFile('21c38e32c8f34de1a3073e738e7726bc', fname, destination=app_dir)
        filelist.append(fname)

    json.dumps(filelist)

    fav = Model(
        resourceid=resourceid,
        displayname=displayname,
        modeltype=modeltype,
        modelfiles=filelist
    )

    # Add the model to the session, commit, and close
    session.add(fav)

    model = session.query(Model).filter(Model.resourceid==resourceid).first()
    mainid = model.id

    for fi in filelist:
        ext = fi.split(".")[1]
        setattr(model, ext + 'id', mainid)
        with open(
                '/Users/student/tethysdev/tethysapp-hs_modflow/tethysapp/hs_modflow/workspaces/app_workspace/' + fi,
                'r'
        ) as myfile:
            data = myfile.read()
            json.dumps(data)

        table = Table(ext, meta,
                          Column('id', String, primary_key=True),
                          Column('data', String)
                          )
        table.create(engine, checkfirst=True)

        ins = table.insert().values(
            id=mainid,
            data=data)
        conn.execute(ins)

    conn.close()
    session.commit()
    session.close()

    return
