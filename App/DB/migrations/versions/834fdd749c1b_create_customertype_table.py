"""Create customertype Table

Revision ID: 834fdd749c1b
Revises: 
Create Date: 2020-11-19 20:43:07.530790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '834fdd749c1b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customertypes',
        sa.Column('CustomerTypeId', sa.Integer, Primary_key=True, autoincrement=True),
        sa.Column('CustomerType', sa.String(100), nullable=False),
    )


def downgrade():
    op.drop_table('customertypes')