from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class CarSparepart(Base):
    tablename = 'carspareparts'

    CarId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    SparepartId = sa.Column(sa.String(100), nullable=False, autoincrement=True)

    def repr(self):
        return f'CarSparepart(CarId={self.CarId}, SparepartId={self.SparepartId})'
