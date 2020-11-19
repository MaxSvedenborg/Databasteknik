"""Create Customer Table

Revision ID: c3c7f4aa6b5a
Revises: 
Create Date: 2020-11-18 17:06:22.370825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3c7f4aa6b5a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op create_table(
        'customers',
        sa.Column('CustomerId', sa.Integer, primary_key=True, auto_increment=True),
        sa.Column('CustomerName', sa.String(100), nullable=False),
        sa.Column('CustomerAddress', sa.String(100), nullable=False),
        sa.Column('CustomerPhone', sa.String(100), nullable=False),
        sa.Column('CustomerEmail', sa.String(100), nullable=False),
        sa.Column('CustomerTypeId', sa.Integer, sa.ForeignKey('customertypes.CustomerTypeId')),
    )

def downgrade():
    op.drop_table('customers')
