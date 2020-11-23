"""Create orders Table

Revision ID: 823e9f46499a
Revises: 936f5737eaa2
Create Date: 2020-11-19 20:47:40.968016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '823e9f46499a'
down_revision = '936f5737eaa2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orders',
        sa.Column('OrderId', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('OrderDate', sa.Date, nullable=False),
        sa.Column('OrderTime', sa.Time, nullable=False),
        sa.Column('StoreId', sa.Integer, sa.ForeignKey('stores.StoreId'), nullable=False),
        sa.Column('CustomerId', sa.Integer, sa.ForeignKey('customers.CustomerId'), nullable=False),
    )


def downgrade():
    op.drop_table('orders')