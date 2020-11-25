from DB import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Store(Base):
    __tablename__ = 'stores'

    StoreId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    StoreName = sa.Column(sa.String(100), nullable=False)
    StoreAddress = sa.Column(sa.String(100), nullable=False)
    StorePhone = sa.Column(sa.String(100), nullable=False)
    StoreEmail = sa.Column(sa.String(100), nullable=False)

    Inventories = relationship("Inventory", back_populates="Store")
    Orders = relationship("Order", back_populates="Store")
    Storeemployees = relationship("StoreEmployee", back_populates="Stores")

    def __repr__(self):
        return f'{self.StoreName}'
