"""Create Customertyp Table

Revision ID: 56f3e40f635f
Revises: 20930bf422ac
Create Date: 2020-11-18 17:16:32.219186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56f3e40f635f'
down_revision = '20930bf422ac'
branch_labels = None
depends_on = None


def upgrade():
    op create_table(
        'customertypes',
        sa.Column('CustomerTypeId', sa.Integer, primary_key=True, auto_increment=True),
        sa.Column('CustomerType', sa.String(100), nullable=False)
    )

def downgrade():
    op.drop_table('customertypes')
