from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class Store(Base):
    tablename = 'stores'

    StoreId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    StoreName = sa.Column(sa.String(100), nullable=False)
    StoreAddress = sa.Column(sa.String(100), nullable=False)
    StorePhone = sa.Column(sa.String(100), nullable=False)
    StoreEmail = sa.Column(sa.String(100), nullable=False)

    def repr(self):
        return f'Store(StoreID={self.StoreId}, StoreName={self.StoreName}, StoreAddress={self.StoreAddress}' \
               f'StorePhone={self.StorePhone}, StoreEmail{self.StoreEmail})'
