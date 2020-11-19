"""Create Storeemployee Table

Revision ID: 004508175b9e
Revises: 2ebac545fd00
Create Date: 2020-11-18 17:31:15.523794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '004508175b9e'
down_revision = '2ebac545fd00'
branch_labels = None
depends_on = None


def upgrade():
    op create_table(
        'storeemployees',
        sa.Column('StoreEmployeeId', sa.Integer, primary_key=True, auto_increment=True),
        sa.Column('StoreId', sa.Integer, sa.ForeignKey('stores.StoreId')),
        sa.Column('PersonalDataId', sa.Integer, sa.ForeignKey('personaldata.PersonalDataId'))
    )

def downgrade():
    op.drop_table('storeemployees')
