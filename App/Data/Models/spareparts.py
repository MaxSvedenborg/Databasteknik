from DB import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Sparepart(Base):
    __tablename__ = 'spareparts'

    SparepartId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    SparepartName = sa.Column(sa.String(100), nullable=False)
    SparepartDescription = sa.Column(sa.String(10000), nullable=False)
    ManufacturerId = sa.Column(sa.Integer, sa.ForeignKey('manufacturers.ManufacturerId'), nullable=False)
    SupplierId = sa.Column(sa.Integer, sa.ForeignKey('suppliers.SupplierId'), nullable=False)

    Manufacturer = relationship("Manufacturer")
    Supplier = relationship("Supplier")

    Carspareparts = relationship("CarSparepart", back_populates="Sparepart")
    Inventories = relationship("Inventory", back_populates="Sparepart")

    def __repr__(self):
        return f'{self.SparepartId}'
