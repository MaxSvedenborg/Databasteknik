"""Create Sparepart Table

Revision ID: 7232330919f8
Revises: c37fa5ed6ad0
Create Date: 2020-11-18 17:25:07.361292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7232330919f8'
down_revision = 'c37fa5ed6ad0'
branch_labels = None
depends_on = None


def upgrade():
    op create_table(
        'spareparts',
        sa.Column('SparepartId', sa.Integer, primary_key=True, auto_increment=True),
        sa.Column('SparepartName', sa.String(45), nullable=False),
        sa.Column('ManufacturerId', sa.Integer, sa.ForeignKey('manufacturers.manufacturerId')),
        sa.Column('SupplierId', sa.Integer, sa.ForeignKey('suppliers.supplierId')),
        sa.Column('SparepartDescription', sa.String(10000), nullable=False),
    )

def downgrade():
    op.drop_table('spareparts')
