"""Create Orders Table

Revision ID: 6553feae01d8
Revises: 0440488bd91a
Create Date: 2020-11-18 17:22:39.073108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6553feae01d8'
down_revision = '0440488bd91a'
branch_labels = None
depends_on = None


def upgrade():
    op create_table(
        'orders',
        sa.Column('OrderId', sa.Integer, primary_key=True, auto_increment=True),
        sa.Column('OrderDate', sa.Date, nullable=False),
        sa.Column('OrderTime', sa.Time, nullable=False),
        sa.Column('StoreId', sa.Integer, sa.ForeignKey('stores.StoreId')),
        sa.Column('CustomerId', sa.Integer, sa.ForeignKey('customers.CustomerId'))
    )

def downgrade():
    op.drop_table('orders')
