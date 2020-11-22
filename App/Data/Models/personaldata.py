from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Personaldata(Base):
    __tablename__ = 'personaldata'

    PersonalDataId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    PersonalDataName = sa.Column(sa.String(100), nullable=False)
    PersonalDataPhone = sa.Column(sa.String(100), nullable=False)
    PersonalDataEmail = sa.Column(sa.String(100), nullable=False)

    Manufacturers = relationship("PersonalData", back_populates="PersonalData")
    Storeemployees = relationship("PersonalData", back_populates="PersonalData")

    def repr(self):
        return f'Personaldata(PersonalDataID={self.PersonalDataId}, PersonalDataName={self.PersonalDataName}, ' \
               f'PersonalDataPhone={self.PersonalDataPhone}, PersonalDataEmail{self.PersonalDataEmail})'
