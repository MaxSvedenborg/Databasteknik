"""Create cars Table

Revision ID: f881f5c7db91
Revises: f8c6bfe5d361
Create Date: 2020-11-19 20:44:18.002046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f881f5c7db91'
down_revision = 'f8c6bfe5d361'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'cars',
        sa.Column('CarsId', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('CarsRegNo', sa.String(100), nullable=False),
        sa.Column('CarsManufacturer', sa.String(100), nullable=False),
        sa.Column('CarsModel', sa.String(100), nullable=False),
        sa.Column('CarsColor', sa.String(100), nullable=False),
        sa.Column('CustomerId', sa.Integer, sa.ForeignKey('customers.CustomerId')),
    )


def downgrade():
    op.drop_table('cars')