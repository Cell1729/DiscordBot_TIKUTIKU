from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


Base = declarative_base()

engine = create_engine('sqlite:///db.sqlite3')
Base.metadata.create_all(engine)
