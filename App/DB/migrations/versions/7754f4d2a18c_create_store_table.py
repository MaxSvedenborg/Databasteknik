"""Create Store Table

Revision ID: 7754f4d2a18c
Revises: 7232330919f8
Create Date: 2020-11-18 17:25:54.818366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7754f4d2a18c'
down_revision = '7232330919f8'
branch_labels = None
depends_on = None


def upgrade():
    op create_table(
        'stores',
        sa.Column('StoreId', sa.Integer, primary_key=True, auto_increment=True),
        sa.Column('StoreName', sa.String(100), nullable=False),
        sa.Column('StoreAddress', sa.String(100), nullable=False),
        sa.Column('StorePhone', sa.String(100), nullable=False),
        sa.Column('StoreEmail', sa.String(100), nullable=False),
    )

def downgrade():
    op.drop_table('stores')
