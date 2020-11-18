from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class Sparepart(Base):
    tablename = 'spareparts'

    SparepartId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    SparepartName = sa.Column(sa.String(100), nullable=False)
    ManufacturerId = relationship("Manufacturer", back_populates="spareparts")
    SupplierId = relationship("Supplier", back_populates="spareparts")
    SparepartDescription = sa.Column(sa.String(10000), nullable=False)

    def __repr__(self):
        return f'{self.SparepartName}\nManufacturer:\n\t{"".join(Manufacturer.ManufacturerName + ", " for Manufacturer in self.ManufacturerId)}' \
               f'\nSupplier:\n\t{"".join(Supplier.SupplierName + ", " for Supplier in self.SupplierId)}'
