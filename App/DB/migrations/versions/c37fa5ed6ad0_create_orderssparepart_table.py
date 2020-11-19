"""Create Orderssparepart Table

Revision ID: c37fa5ed6ad0
Revises: 3edf4dabde58
Create Date: 2020-11-18 17:24:21.970261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c37fa5ed6ad0'
down_revision = '3edf4dabde58'
branch_labels = None
depends_on = None


def upgrade():
    op create_table(
        'orderspareparts',
        sa.Column('OrderId', sa.Integer, primary_key=True, auto_increment=True),
        sa.Column('SparepartId', sa.Integer, primary_key=True, auto_increment=True),
        sa.Column('OrdersAmount', sa.Integer, nullable=False)
    )

def downgrade():
    op.drop_table('orderspareparts')
