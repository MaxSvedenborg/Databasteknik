"""Create manufactor Table

Revision ID: d47d7b14ca1d
Revises: 75fb44cfc147
Create Date: 2020-11-19 20:45:26.058003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd47d7b14ca1d'
down_revision = '75fb44cfc147'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'manufacturers',
        sa.Column('ManufacturerId', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('ManufacturerName', sa.String(100), nullable=False),
        sa.Column('ManufacturerAddressHQ', sa.String(100), nullable=False),
        sa.Column('ManufacturerPhoneHQ', sa.String(100), nullable=False),
        sa.Column('PersonalDataId', sa.Integer, sa.ForeignKey('personaldata.PersonalDataId'), nullable=False),
    )


def downgrade():
    op.drop_table('manufacturers')