"""Create personaldata Table

Revision ID: 75fb44cfc147
Revises: f881f5c7db91
Create Date: 2020-11-19 20:44:51.516993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75fb44cfc147'
down_revision = 'f881f5c7db91'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'personaldata',
        sa.Column('PersonalDataId', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('PersonalDataName', sa.String(100), nullable=False),
        sa.Column('PersonalDataAddress', sa.String(100), nullable=False),
        sa.Column('PersonalDataPhone', sa.String(100), nullable=False),
    )


def downgrade():
    op.drop_table('personaldata')
