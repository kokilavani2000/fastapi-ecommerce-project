from app.modules.users.model import User
from sqlalchemy import statement, select, scalars
from sqlalchemy.orm import Session

class UserReository:

    def __init__(self, db):
        self.db = db


    def get_all(self)-> list:
        return self.db.scalars(statement).all()


    def get_by_id(self, user_id:int) -> User|None:
        return self.db.get(User, user_id)

    def get_by_email(self, email:str) ->User|None:
        statement = select(User).where(User.email == email)
        return self.db.scalars(statement).one_or_none()

    def create(self, user:User)-> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update(self, user:User)-> User:
        self.db.commit()
        self.db.refresh(user)
        return user


    def delete(self, user:User)-> None:
        self.db.delete(user)
        self.db.commit()