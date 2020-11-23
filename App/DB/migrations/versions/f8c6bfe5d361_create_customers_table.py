"""Create customer Table

Revision ID: f8c6bfe5d361
Revises: 834fdd749c1b
Create Date: 2020-11-19 20:43:43.425087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8c6bfe5d361'
down_revision = '834fdd749c1b'
branch_labels = None
depends_on = None



def upgrade():
    op.create_table(
        'customers',
        sa.Column('CustomerId', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('CustomerName', sa.String(100), nullable=False),
        sa.Column('CustomerAddress', sa.String(100), nullable=False),
        sa.Column('CustomerPhone', sa.String(100), nullable=False),
        sa.Column('CustomerEmail', sa.String(100), nullable=False),
        sa.Column('CustomerTypeId', sa.Integer, sa.ForeignKey('customertypes.CustomerTypeId'), nullable=False),
    )


def downgrade():
    op.drop_table('customers')