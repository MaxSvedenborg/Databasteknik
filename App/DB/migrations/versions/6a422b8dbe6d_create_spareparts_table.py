"""Create sparepart Table

Revision ID: 6a422b8dbe6d
Revises: fc7604bb2fa1
Create Date: 2020-11-19 20:46:06.121389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a422b8dbe6d'
down_revision = 'fc7604bb2fa1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'spareparts',
        sa.Column('SparepartId', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('SparepartName', sa.String(100), nullable=False),
        sa.Column('ManufacturerId', sa.Integer, sa.ForeignKey('manufacturers.ManufacturerId'), nullable=False),
        sa.Column('SupplierId', sa.Integer, sa.ForeignKey('suppliers.SupplierId'), nullable=False),
        sa.Column('SparepartDescription', sa.String(10000), nullable=False),
    )


def downgrade():
    op.drop_table('spareparts')