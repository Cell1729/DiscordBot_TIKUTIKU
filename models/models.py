from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Quotes(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True)
    quote = Column(String)
    url = Column(String)

class ServerSettings(Base):
    __tablename__ = 'server_settings'

    id = Column(Integer, primary_key=True)
    server_id = Column(String, unique=True)
    reminder_time = Column(String)
    reminder_channel = Column(Integer)
    reminder_channel_name = Column(String)
    reminder_enabled = Column(Integer)  # 0 or 1 for boolean


if __name__ == '__main__':
    # 初期化処理
    engine = create_engine('sqlite:///db.sqlite3')
    Base.metadata.create_all(engine)
    print('Database initialized')