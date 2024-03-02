
from sqlmodel import  Session, create_engine, select, SQLModel
from core.models.user import User
from core.models.trade import Trade
from core.models.pay_types import PayTypes

DATABASE_URL = "sqlite:///database.db"
    
class DatabaseHelper():
    engine = None

    @classmethod
    def get_engine(cls):
        if cls.engine is None:
            cls.engine = create_engine(DATABASE_URL)
        return cls.engine
    
    @classmethod
    def add(cls, DbObject):
        with Session(cls.get_engine()) as session:
            session.add(DbObject)
            session.commit()

    @classmethod
    def get_user(cls, user_id):
        with Session(cls.get_engine()) as session:
            statement = select(User).where(User.id == user_id)
            user = session.exec(statement).first()
            
        return user
    
    @classmethod
    def get_trade(cls, trade_id):
        with Session(cls.get_engine()) as session:
            statement = select(Trade).where(Trade.id == trade_id)
            trade = session.exec(statement).first()
        return trade

    
    @classmethod
    def update(cls, DbObject):
        print(DbObject, DbObject.name)
        with Session(cls.get_engine()) as session:
            statement = select(User).where(User.name == DbObject.name)
            db_object = session.exec(statement).first()
            print(db_object)
        
        #     object_class = DbObject.__class__
        #     print(DbObject.id)
        #     print(statement)
        #     db_object = statement.first()
            DatabaseHelper.copy_attributes(DbObject, db_object)
            session.add(db_object)
            session.commit()

    @staticmethod 
    def copy_attributes(source, destination):
        for attr in source.__fields_set__:
            setattr(destination, attr, getattr(source, attr))
