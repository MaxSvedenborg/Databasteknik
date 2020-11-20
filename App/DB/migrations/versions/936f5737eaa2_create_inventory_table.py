"""Create inventory Table

Revision ID: 936f5737eaa2
Revises: 18a06064c3a5
Create Date: 2020-11-19 20:47:19.726795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '936f5737eaa2'
down_revision = '18a06064c3a5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'inventories',
        sa.Column('InventoryId', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('StoreId', sa.Integer, sa.ForeignKey('stores.StoreId')),
        sa.Column('InventoryLocation', sa.String(100), nullable=False),
        sa.Column('InventoryQTY', sa.Integer, nullable=False),
        sa.Column('InventoryCriticalLevel', sa.Integer, nullable=False),
        sa.Column('InventoryQTYAutomaticOrder', sa.Integer, nullable=False),
        sa.Column('InventoryETA', sa.String(100), nullable=False),
        sa.Column('SparepartId', sa.Integer, sa.ForeignKey('spareparts.SparepartId')),
    )


def downgrade():
    op.drop_table('inventories')