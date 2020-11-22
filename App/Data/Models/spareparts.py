from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Sparepart(Base):
    __tablename__ = 'spareparts'

    SparepartId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    SparepartName = sa.Column(sa.String(100), nullable=False)
    SparepartDescription = sa.Column(sa.String(10000), nullable=False)
    ManufacturerId = sa.Column(sa.Integer, sa.ForeignKey('manufacturers.ManufacturerId'), nullable=False)
    SupplierId = sa.Column(sa.Integer, sa.ForeignKey('suppliers.SupplierId'), nullable=False)

    Manufacturers = relationship("Manufacturer", back_populates="Spareparts")
    Suppliers = relationship("Supplier", back_populates="Spareparts")
    Carspareparts = relationship("Carsparepart", back_populates="Spareparts")
    Inventories = relationship("Inventory", back_populates="Spareparts")

    def __repr__(self):
        return f'{self.SparepartName}\nManufacturer:\n\t{"".join(Manufacturer.ManufacturerName + ", " for Manufacturer in self.ManufacturerId)}' \
               f'\nSupplier:\n\t{"".join(Supplier.SupplierName + ", " for Supplier in self.SupplierId)}'
