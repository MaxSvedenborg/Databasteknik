from DB import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class CarSparepart(Base):
    __tablename__ = 'carspareparts'

    CarId = sa.Column(sa.Integer, sa.ForeignKey('cars.CarsId'), primary_key=True),
    SparepartId = sa.Column(sa.Integer, sa.ForeignKey('spareparts.SparepartId'), primary_key=True),

    Cars = relationship("Car", back_populates="carspareparts")
    Spareparts = relationship("Sparepart", back_populates="carspareparts")


    def repr(self):
        return f'CarSparepart(CarId={self.CarId}, SparepartId={self.SparepartId})'
