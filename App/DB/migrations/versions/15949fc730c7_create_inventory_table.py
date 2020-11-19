"""Create Inventory Table

Revision ID: 15949fc730c7
Revises: 59e18d0597fe
Create Date: 2020-11-18 17:29:29.287623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15949fc730c7'
down_revision = '59e18d0597fe'
branch_labels = None
depends_on = None


def upgrade():
    op create_table(
        'inventories',
        sa.Column('InventoryId', sa.Integer, primary_key=True, auto_increment=True),
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
