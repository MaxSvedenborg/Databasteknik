from DB import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Supplier(Base):
    __tablename__ = 'suppliers'

    SupplierId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    SupplierName = sa.Column(sa.String(100), nullable=False)
    SupplierAddress = sa.Column(sa.String(100), nullable=False)
    CarsModel = sa.Column(sa.String(100), nullable=False)
    SupplierPhone = sa.Column(sa.String(100), nullable=False)
    SupplierEmail = sa.Column(sa.String(100), nullable=False)
    PersonalDataId = relationship("PersonalData", back_populates="suppliers")



    def __repr__(self):
        return f'{self.SupplierName}\nPersonaldata:\n\t{"".join(Personaldata.PersonalDataName + ", " for Personaldata in self.PersonalDataId)}'