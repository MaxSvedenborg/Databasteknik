from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class OrderSparepart(Base):
    tablename = 'orderspareparts'

    OrderId = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    SparepartId = sa.Column(sa.String(100), nullable=False, autoincrement=True)
    OrderAmount = sa.Column(sa.String(100), nullable=False)

    def repr(self):
        return f'OrderSparepart(OrderId={self.OrderId}, SparepartId={self.SparepartId}, OrderAmount={self.OrderAmount})'
