"""Create supplier Table

Revision ID: fc7604bb2fa1
Revises: d47d7b14ca1d
Create Date: 2020-11-19 20:45:44.811769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc7604bb2fa1'
down_revision = 'd47d7b14ca1d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'suppliers',
        sa.Column('SupplierId', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('SupplierName', sa.String(100), nullable=False),
        sa.Column('SupplierAddress', sa.String(100), nullable=False),
        sa.Column('SupplierPhone', sa.String(100), nullable=False),
        sa.Column('SupplierEmail', sa.String(100), nullable=False),
        sa.Column('PersonalDataId', sa.Integer, sa.ForeignKey('personaldata.PersonalDataId')),
    )


def downgrade():
    op.drop_table('suppliers')