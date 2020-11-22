from DB import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class CustomerType(Base):
    __tablename__ = 'customertypes'

    CustomerTypeId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    CustomerType = sa.Column(sa.String(100), nullable=False)

    Customers = relationship("Customer", back_populates="Customertypes")


    def __repr__(self):
        return f'CustomerTypes(CustomerTypeId={self.CustomerTypeId}, CustomerTypes={self.CustomerType})'