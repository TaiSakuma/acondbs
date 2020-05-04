"""Initial migration.

Revision ID: ef4e36b7f296
Revises: 
Create Date: 2020-05-04 13:59:03.745738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef4e36b7f296'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('maps',
    sa.Column('map_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('date_posted', sa.Date(), nullable=True),
    sa.Column('mapper', sa.Text(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('map_id')
    )
    op.create_index(op.f('ix_maps_name'), 'maps', ['name'], unique=True)
    op.create_table('simulations',
    sa.Column('simulation_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('date_posted', sa.Date(), nullable=True),
    sa.Column('mapper', sa.Text(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('simulation_id')
    )
    op.create_index(op.f('ix_simulations_name'), 'simulations', ['name'], unique=True)
    op.create_table('beams',
    sa.Column('beam_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('input_map_id', sa.Integer(), nullable=True),
    sa.Column('input_beam_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['input_beam_id'], ['beams.beam_id'], ),
    sa.ForeignKeyConstraint(['input_map_id'], ['maps.map_id'], ),
    sa.PrimaryKeyConstraint('beam_id')
    )
    op.create_index(op.f('ix_beams_name'), 'beams', ['name'], unique=True)
    op.create_table('map_file_paths',
    sa.Column('map_file_path_id', sa.Integer(), nullable=False),
    sa.Column('map_id', sa.Integer(), nullable=True),
    sa.Column('path', sa.Text(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['map_id'], ['maps.map_id'], ),
    sa.PrimaryKeyConstraint('map_file_path_id')
    )
    op.create_table('simulation_file_paths',
    sa.Column('simulation_file_path_id', sa.Integer(), nullable=False),
    sa.Column('simulation_id', sa.Integer(), nullable=True),
    sa.Column('path', sa.Text(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['simulation_id'], ['simulations.simulation_id'], ),
    sa.PrimaryKeyConstraint('simulation_file_path_id')
    )
    op.create_table('beam_file_paths',
    sa.Column('beam_file_path_id', sa.Integer(), nullable=False),
    sa.Column('beam_id', sa.Integer(), nullable=True),
    sa.Column('path', sa.Text(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['beam_id'], ['beams.beam_id'], ),
    sa.PrimaryKeyConstraint('beam_file_path_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('beam_file_paths')
    op.drop_table('simulation_file_paths')
    op.drop_table('map_file_paths')
    op.drop_index(op.f('ix_beams_name'), table_name='beams')
    op.drop_table('beams')
    op.drop_index(op.f('ix_simulations_name'), table_name='simulations')
    op.drop_table('simulations')
    op.drop_index(op.f('ix_maps_name'), table_name='maps')
    op.drop_table('maps')
    # ### end Alembic commands ###
