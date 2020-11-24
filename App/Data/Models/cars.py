from DB import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Car(Base):
    __tablename__ = 'cars'

    CarsId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    CarsRegNo = sa.Column(sa.String(100), nullable=False)
    CarsManufacturer = sa.Column(sa.String(100), nullable=False)
    CarsModel = sa.Column(sa.String(100), nullable=False)
    CarsColor = sa.Column(sa.String(100), nullable=False)
    CustomerId = sa.Column(sa.Integer, sa.ForeignKey('customers.CustomerId'), nullable=False)

    Customer = relationship("Customer", back_populates="Cars")
    CarSpareparts = relationship("CarSparepart")

    def __repr__(self):
        return f'{self.CarsManufacturer} ({self.CarsModel})'
