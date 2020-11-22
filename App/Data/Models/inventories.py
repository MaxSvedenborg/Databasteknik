from DB import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Inventory(Base):
    __tablename__ = 'inventories'

    InventoryId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    InventoryLocation = sa.Column(sa.String(100), nullable=False)
    InventoryQTY = sa.Column(sa.Integer, nullable=False)
    InventoryCriticalLevel = sa.Column(sa.Integer, nullable=False)
    InventoryQTYAutomaticOrder = sa.Column(sa.Integer, nullable=False)
    InventoryETA = sa.Column(sa.String(100), nullable=False)
    SparepartId = sa.Column(sa.Integer, sa.ForeignKey('spareparts.SparepartId'), nullable=False),
    StoreId = sa.Column(sa.Integer, sa.ForeignKey('stores.StoreId'), nullable=False),

    Spareparts = relationship("Sparepart", back_populates="Inventories")
    Stores = relationship("Store", back_populates="Inventories")

    def __repr__(self):
        return f'{self.InventoryLocation}\nStore:\n\t{"".join(Store + ", " for Store in self.StoreId)}\nSparepart:\n\t{"".join(Sparepart.SparepartName + ", " for Sparepart in self.SparepartNameId)}'