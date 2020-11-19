"""Create Cars Table

Revision ID: 0440488bd91a
Revises: 56f3e40f635f
Create Date: 2020-11-18 17:20:46.485380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0440488bd91a'
down_revision = '56f3e40f635f'
branch_labels = None
depends_on = None


def upgrade():
    op create_table(
        'cars',
        sa.Column('CarsId', sa.Integer, primary_key=True, auto_increment=True),
        sa.Column('CarsRegNo', sa.String(100), nullable=False),
        sa.Column('CarsManufactor', sa.String(100), nullable=False),
        sa.Column('CarsModel', sa.String(100), nullable=False),
        sa.Column('CarsColor', sa.String(100), nullable=False),
        sa.Column('CustomerId', sa.Integer, sa.ForeignKey('customers.CustomerId')),
    )

def downgrade():
    op.drop_table('cars')
