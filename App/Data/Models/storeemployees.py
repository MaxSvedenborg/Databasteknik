from DB import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class StoreEmployee(Base):
    __tablename__ = 'storeemployees'

    StoreEmployeeId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    StoreId = sa.Column(sa.Integer, sa.ForeignKey('stores.StoreId'), nullable=False)
    PersonalDataId = sa.Column(sa.Integer, sa.ForeignKey('personaldata.PersonalDataId'), nullable=False)

    Stores = relationship("Store", back_populates="Storeemployees")
    PersonalData = relationship("PersonalData", back_populates="Storeemployees")


    def __repr__(self):
        return f'{self.StoreEmployeeId}\nStore:\n\t{"".join(Store + ", " for Store in self.StoreId)}\nPersonalData:\n\t{"".join(PersonalData.PersonalDataName + ", " for PersonalData in self.PersonalDataId)}'
