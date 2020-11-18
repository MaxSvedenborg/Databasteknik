from DB import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = 'orders'

    OrdersId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    OrderDate = sa.Column(sa.Date, nullable=False)
    OrderTime = sa.Column(sa.Time, nullable=False)
    StoreId = relationship("Store", back_populates="orders")
    CustomerId = relationship("Customer", back_populates="orders")


    def __repr__(self):
        return f'{self.OrderDate}\nStore:\n\t{"".join(Store + ", " for Store in self.StoreId)}\nCustomer:\n\t{"".join(Customer.CustomerName + ", " for Customer in self.CustomerId)}'