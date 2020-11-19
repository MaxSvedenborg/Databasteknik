"""Create Supplier Table

Revision ID: 20930bf422ac
Revises: c3c7f4aa6b5a
Create Date: 2020-11-18 17:06:53.412828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20930bf422ac'
down_revision = 'c3c7f4aa6b5a'
branch_labels = None
depends_on = None


def upgrade():
    op create_table(
        'suppliers',
        sa.Column('SupplierId', sa.Integer, primary_key=True, auto_increment=True),
        sa.Column('SupplierName', sa.String(100), nullable=False),
        sa.Column('SupplierAddress', sa.String(100), nullable=False),
        sa.Column('SupplierPhone', sa.String(100), nullable=False),
        sa.Column('SupplierEmail', sa.String(100), nullable=False),
        sa.Column('PersonalDataId', sa.Integer, sa.ForeignKey('personaldata.PersonalDataId')),
    )

def downgrade():
    op.drop_table('suppliers')
