from DB import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = 'orders'

    OrderId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    OrderDate = sa.Column(sa.Date, nullable=False)
    OrderTime = sa.Column(sa.Time, nullable=False)
    StoreId = sa.Column(sa.Integer, sa.ForeignKey('stores.StoreId'), nullable=False)
    CustomerId = sa.Column(sa.Integer, sa.ForeignKey('customers.CustomerId'), nullable=False)

    Store = relationship("Store", back_populates="Orders")
    Customer = relationship("Customer", back_populates="Orders")


    def __repr__(self):
        return f'{self.OrdersId}'