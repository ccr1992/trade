from core.models.fiat_payment import FiatPayment
from core.models.user import User, PayTypes
from sqlmodel import  Session, create_engine, select, SQLModel, delete



User_1 = User(id=1, pay_type=PayTypes.type_A, name="user_1")
User_2 = User(id=2, pay_type=PayTypes.type_A, name="user_2")
User_3 = User(id=3, pay_type=PayTypes.type_B, name="user_3")

Payment_1 = FiatPayment(value= 100, full_paid=False, user_id=1)
Payment_2 = FiatPayment(value= 100, full_paid=False, user_id=2)
Payment_3 = FiatPayment(value= 100, full_paid=False, user_id=45)
#TODO USUARIO NO EXISTE


CLEAN_DB = True


engine = create_engine("sqlite:///database.db")
if CLEAN_DB:
    SQLModel.metadata.drop_all(engine)
    # with Session(engine) as session:
    #   statement = delete(User)
    #   _ = session.exec(statement)
    #   statement = delete(FiatPayment)
    #   _ = session.exec(statement)
    #   session.commit()
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(User_1)
    session.add(User_2)
    session.add(User_3)
    session.commit()
    

with Session(engine) as session:
    statement = select(User).where(User.name == "user_1")
    User = session.exec(statement).first()
    print(User)



with Session(engine) as session:
    session.add(Payment_1)
    session.add(Payment_2)
    session.add(Payment_3)
    session.commit()
    

with Session(engine) as session:
    statement = select(FiatPayment).where(FiatPayment.user_id == 1)
    Payment = session.exec(statement).first()
    print(Payment)
