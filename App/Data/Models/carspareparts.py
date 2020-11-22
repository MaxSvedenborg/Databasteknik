from DB import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class CarSparepart(Base):
    __tablename__ = 'carspareparts'

    CarsId = sa.Column(sa.Integer, sa.ForeignKey('cars.CarsId'), primary_key=True)
    SparepartId = sa.Column(sa.Integer, sa.ForeignKey('spareparts.SparepartId'), primary_key=True)

    Car = relationship("Car")
    Sparepart = relationship("Sparepart")


    def repr(self):
        return f'{self.CarId},{self.SparepartId}'
