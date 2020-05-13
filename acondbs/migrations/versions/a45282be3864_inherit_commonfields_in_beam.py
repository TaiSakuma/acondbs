"""inherit CommonFields in Beam

Revision ID: a45282be3864
Revises: d164761c73d2
Create Date: 2020-05-12 21:00:07.225074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a45282be3864'
down_revision = 'd164761c73d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('beams', sa.Column('contact', sa.Text(), nullable=True))
    op.add_column('beams', sa.Column('date_posted', sa.Date(), nullable=True))
    op.add_column('beams', sa.Column('date_produced', sa.Date(), nullable=True))
    op.add_column('beams', sa.Column('date_updated', sa.Date(), nullable=True))
    op.add_column('beams', sa.Column('note', sa.Text(), nullable=True))
    op.add_column('beams', sa.Column('posted_by', sa.Text(), nullable=True))
    op.add_column('beams', sa.Column('produced_by', sa.Text(), nullable=True))
    op.add_column('beams', sa.Column('updated_by', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('beams', 'updated_by')
    op.drop_column('beams', 'produced_by')
    op.drop_column('beams', 'posted_by')
    op.drop_column('beams', 'note')
    op.drop_column('beams', 'date_updated')
    op.drop_column('beams', 'date_produced')
    op.drop_column('beams', 'date_posted')
    op.drop_column('beams', 'contact')
    # ### end Alembic commands ###