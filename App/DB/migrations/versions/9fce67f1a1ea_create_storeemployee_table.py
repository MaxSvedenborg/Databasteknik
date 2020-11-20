"""Create storeemployee Table

Revision ID: 9fce67f1a1ea
Revises: e2a49eab9d62
Create Date: 2020-11-19 20:48:21.973902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fce67f1a1ea'
down_revision = 'e2a49eab9d62'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'storeemployees',
        sa.Column('StoreEmployeeId', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('StoreId', sa.Integer, sa.ForeignKey('stores.StoreId')),
        sa.Column('PersonalDataId', sa.Integer, sa.ForeignKey('personaldata.PersonalDataId')),
    )


def downgrade():
    op.drop_table('storeemployees')