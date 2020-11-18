from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class StoreEmployee(Base):
    __tablename__ = 'storeemployees'

    StoreEmployeeId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    StoreId = relationship("Store", back_populates="storeemployees")
    PersonalDataId = relationship("PersonalData", back_populates="storeemployees")

    def __repr__(self):
        return f'{self.StoreEmployeeId}\nStore:\n\t{"".join(Store + ", " for Store in self.StoreId)}\nPersonalData:\n\t{"".join(PersonalData.PersonalDataName + ", " for PersonalData in self.PersonalDataId)}'
