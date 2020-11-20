"""Create orderssparepart Table

Revision ID: e2a49eab9d62
Revises: 823e9f46499a
Create Date: 2020-11-19 20:48:01.094380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2a49eab9d62'
down_revision = '823e9f46499a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orderspareparts',
        sa.Column('OrderId', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('SparepartId', sa.Integer, primary_key=True, auto_increment=True),
        sa.Column('OrdersAmount', sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table('orderspareparts')