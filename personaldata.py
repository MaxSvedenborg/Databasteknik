from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class Personaldata(Base):
    __tablename__ = 'personaldata'
    PersonalDataId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    PersonalDataName = sa.Column(sa.Varchar(100), nullable=False)
    PersonalDataPhone = sa.Column(sa.Varchar(100), nullable=False)
    PersonalDataEmail = sa.Column(sa.Varchar(100), nullable=False)

    def __repr__(self):
        return f'{self.PersonalDataId}, {self.PersonalDataName}, {self.PersonalDataPhone}, {self.PersonalDataEmail}'