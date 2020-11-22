from DB import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class StoreEmployee(Base):
    __tablename__ = 'storeemployees'

    StoreEmployeeId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    StoreId = sa.Column(sa.Integer, sa.ForeignKey('stores.StoreId'), nullable=False)
    PersonalDataId = sa.Column(sa.Integer, sa.ForeignKey('personaldata.PersonalDataId'), nullable=False)

    Stores = relationship("Store", back_populates="Storeemployees")
    Personalata = relationship("Personaldata")


    def __repr__(self):
        return f'{self.StoreEmployeeId}'
