from DB import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Inventory(Base):
    __tablename__ = 'inventories'

    InventoryId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    StoreId = relationship("Store", back_populates="inventories")
    InventoryLocation = sa.Column(sa.String(100), nullable=False)
    InventoryQTY = sa.Column(sa.Integer, nullable=False)
    InventoryCriticalLevel = sa.Column(sa.Integer, nullable=False)
    InventoryQTYAutomaticOrder = sa.Column(sa.Integer, nullable=False)
    InventoryETA = sa.Column(sa.String(100, nullable=False)
    SparepartId = relationship("Sparepart", back_populates="inventories")


    def __repr__(self):
        return f'{self.InventoryLocation}\nStore:\n\t{"".join(Store + ", " for Store in self.StoreId)}\nSparepart:\n\t{"".join(Sparepart.SparepartName + ", " for Sparepart in self.SparepartNameId)}'