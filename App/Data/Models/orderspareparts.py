from DB import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class OrderSparepart(Base):
    __tablename__ = 'orderspareparts'

    OrderId = sa.Column(sa.Integer, sa.ForeignKey('orders.OrderId'), primary_key=True)
    SparepartId = sa.Column(sa.String(100), sa.ForeignKey('spareparts.SparepartId'), primary_key=True)
    OrderAmount = sa.Column(sa.String(100), nullable=False)

    Orders = relationship("Order", back_populates="Orderspareparts")
    Spareparts = relationship("Sparepart", back_populates="Orderspareparts")

    def repr(self):
        return f'{self.OrderId},{self.SparepartId}'
