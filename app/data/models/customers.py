from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = 'customers'

    CustomerId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    CustomerName = sa.Column(sa.String(100), nullable=False)
    CarsManufactor = sa.Column(sa.String(100), nullable=False)
    CustomerAddress = sa.Column(sa.String(100), nullable=False)
    CustomerPhone = sa.Column(sa.String(100), nullable=False)
    CustomerEmail = sa.Column(sa.String(100), nullable=False)
    CustomerTypeId = relationship("CustomerType", back_populates="customers")


    def __repr__(self):
        return f'{self.CustomerName}\nCustomerType:\n\t{"".join(CustomerType + ", " for CustomerType in self.CustomerTypeId)}'

