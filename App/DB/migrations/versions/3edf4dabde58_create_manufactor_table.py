"""Create Manufactor Table

Revision ID: 3edf4dabde58
Revises: 6553feae01d8
Create Date: 2020-11-18 17:23:23.317931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3edf4dabde58'
down_revision = '6553feae01d8'
branch_labels = None
depends_on = None


def upgrade():
    op create_table(
        'manufacturers',
        sa.Column('ManufacturerId', sa.Integer, primary_key=True, auto_increment=True),
        sa.Column('ManufacturerName', sa.String(100), nullable=False),
        sa.Column('ManufacturerAddressHQ', sa.String(100), nullable=False),
        sa.Column('ManufacturerPhoneHQ', sa.String(100), nullable=False),
        sa.Column('PersonalDataId', sa.Integer, sa.ForeignKey('personaldata.PersonalDataId'))
    )

def downgrade():
    op.drop_table('manufacturers')
