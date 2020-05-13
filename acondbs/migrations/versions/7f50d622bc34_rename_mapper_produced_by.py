"""rename mapper produced_by

Revision ID: 7f50d622bc34
Revises: d06579a3102e
Create Date: 2020-05-12 19:23:11.877667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f50d622bc34'
down_revision = 'd06579a3102e'
branch_labels = None
depends_on = None

# Alembic document alter_column()
# https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.alter_column


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('simulations', 'mapper', new_column_name='produced_by')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('simulations', 'produced_by', new_column_name='mapper')
    # ### end Alembic commands ###
