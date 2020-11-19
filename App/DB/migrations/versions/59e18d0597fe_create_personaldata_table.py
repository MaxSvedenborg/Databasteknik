"""Create Personaldata Table

Revision ID: 59e18d0597fe
Revises: 7754f4d2a18c
Create Date: 2020-11-18 17:28:42.371878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59e18d0597fe'
down_revision = '7754f4d2a18c'
branch_labels = None
depends_on = None


def upgrade():
    op create_table(
        'personaldata',
        sa.Column('PersonalDataId', sa.Integer, primary_key=True, auto_increment=True),
        sa.Column('PersonalDataName', sa.String(100), nullable=False),
        sa.Column('PersonalDataAddress', sa.String(100), nullable=False),
        sa.Column('PersonalDataPhone', sa.String(100), nullable=False)
    )

def downgrade():
    op.drop_table('personaldata')
