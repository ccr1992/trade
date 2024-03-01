
from sqlmodel import  Session, create_engine, select, SQLModel
from core.models.user import User
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
    def get_user(user_id):
        #TODO 
        return User(id=user_id, pay_type=PayTypes.type_A)