from DB import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Supplier(Base):
    __tablename__ = 'suppliers'

    SupplierId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    SupplierName = sa.Column(sa.String(100), nullable=False)
    SupplierAddress = sa.Column(sa.String(100), nullable=False)
    SupplierPhone = sa.Column(sa.String(100), nullable=False)
    SupplierEmail = sa.Column(sa.String(100), nullable=False)
    PersonalDataId = sa.Column(sa.Integer, sa.ForeignKey('personaldata.PersonalDataId'), nullable=False)

    PersonalData = relationship("Personaldata")
    Spareparts = relationship("Sparepart", back_populates="Supplier")


    def __repr__(self):
        return f'{self.SupplierId}'