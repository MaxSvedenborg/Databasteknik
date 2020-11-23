"""Create carssparepart Table

Revision ID: c7ef87ce5116
Revises: 6a422b8dbe6d
Create Date: 2020-11-19 20:46:35.101249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7ef87ce5116'
down_revision = '6a422b8dbe6d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'carspareparts',
        sa.Column('CarsId', sa.Integer, sa.ForeignKey('cars.CarsId'), primary_key=True),
        sa.Column('SparepartId', sa.Integer, sa.ForeignKey('spareparts.SparepartId'), primary_key=True),
    )


def downgrade():
    op.drop_table('carspareparts')