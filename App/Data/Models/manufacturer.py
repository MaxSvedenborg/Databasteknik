from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class Manufacturer(Base):
    tablename = 'manufacturers'

    ManufacturerId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    ManufacturerName = sa.Column(sa.String(100), nullable=False)
    ManufacturerAddressHQ = sa.Column(sa.String(100), nullable=False)
    ManufacturerPhoneHQ = sa.Column(sa.String(100), nullable=False)
    PersonalDataId = relationship("PersonalData", back_populates="manufacturers")

    def __repr__(self):
        return f'{self.ManufacturerName}\nPersonalData:\n\t{"".join(PersonalData.PersonalDataName + ", " for PersonalData in self.PersonalDataId)}'
