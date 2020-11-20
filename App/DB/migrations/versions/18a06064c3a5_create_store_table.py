"""Create store Table

Revision ID: 18a06064c3a5
Revises: c7ef87ce5116
Create Date: 2020-11-19 20:46:54.765808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18a06064c3a5'
down_revision = 'c7ef87ce5116'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stores',
        sa.Column('StoreId', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('StoreName', sa.String(100), nullable=False),
        sa.Column('StoreAddress', sa.String(100), nullable=False),
        sa.Column('StorePhone', sa.String(100), nullable=False),
        sa.Column('StoreEmail', sa.String(100), nullable=False),
    )


def downgrade():
    op.drop_table('stores')