# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_define_tables_start_with_empty_db 1'] = {
    'beam_file_paths': GenericRepr("Table('beam_file_paths', MetaData(bind=None), Column('path_id', INTEGER(), table=<beam_file_paths>, primary_key=True, nullable=False), Column('path', TEXT(), table=<beam_file_paths>), Column('note', TEXT(), table=<beam_file_paths>), Column('product_id', INTEGER(), ForeignKey('beams.product_id'), table=<beam_file_paths>), schema=None)"),
    'beams': GenericRepr("Table('beams', MetaData(bind=None), Column('product_id', INTEGER(), table=<beams>, primary_key=True, nullable=False), Column('name', TEXT(), table=<beams>, nullable=False), Column('contact', TEXT(), table=<beams>), Column('date_produced', DATE(), table=<beams>), Column('produced_by', TEXT(), table=<beams>), Column('date_posted', DATE(), table=<beams>), Column('posted_by', TEXT(), table=<beams>), Column('date_updated', DATE(), table=<beams>), Column('updated_by', TEXT(), table=<beams>), Column('note', TEXT(), table=<beams>), Column('input_map_product_id', INTEGER(), ForeignKey('maps.product_id'), table=<beams>), Column('input_beam_product_id', INTEGER(), ForeignKey('beams.product_id'), table=<beams>), schema=None)"),
    'map_file_paths': GenericRepr("Table('map_file_paths', MetaData(bind=None), Column('path_id', INTEGER(), table=<map_file_paths>, primary_key=True, nullable=False), Column('path', TEXT(), table=<map_file_paths>), Column('note', TEXT(), table=<map_file_paths>), Column('product_id', INTEGER(), ForeignKey('maps.product_id'), table=<map_file_paths>), schema=None)"),
    'maps': GenericRepr("Table('maps', MetaData(bind=None), Column('product_id', INTEGER(), table=<maps>, primary_key=True, nullable=False), Column('name', TEXT(), table=<maps>, nullable=False), Column('contact', TEXT(), table=<maps>), Column('date_produced', DATE(), table=<maps>), Column('produced_by', TEXT(), table=<maps>), Column('date_posted', DATE(), table=<maps>), Column('posted_by', TEXT(), table=<maps>), Column('date_updated', DATE(), table=<maps>), Column('updated_by', TEXT(), table=<maps>), Column('note', TEXT(), table=<maps>), schema=None)"),
    'simulation_file_paths': GenericRepr("Table('simulation_file_paths', MetaData(bind=None), Column('path_id', INTEGER(), table=<simulation_file_paths>, primary_key=True, nullable=False), Column('path', TEXT(), table=<simulation_file_paths>), Column('note', TEXT(), table=<simulation_file_paths>), Column('product_id', INTEGER(), ForeignKey('simulations.product_id'), table=<simulation_file_paths>), schema=None)"),
    'simulations': GenericRepr("Table('simulations', MetaData(bind=None), Column('product_id', INTEGER(), table=<simulations>, primary_key=True, nullable=False), Column('name', TEXT(), table=<simulations>, nullable=False), Column('contact', TEXT(), table=<simulations>), Column('date_produced', DATE(), table=<simulations>), Column('produced_by', TEXT(), table=<simulations>), Column('date_posted', DATE(), table=<simulations>), Column('posted_by', TEXT(), table=<simulations>), Column('date_updated', DATE(), table=<simulations>), Column('updated_by', TEXT(), table=<simulations>), Column('note', TEXT(), table=<simulations>), schema=None)")
}

snapshots['test_define_tables_start_with_nonempty_db 1'] = {
    'beam_file_paths': GenericRepr("Table('beam_file_paths', MetaData(bind=None), Column('path_id', INTEGER(), table=<beam_file_paths>, primary_key=True, nullable=False), Column('path', TEXT(), table=<beam_file_paths>), Column('note', TEXT(), table=<beam_file_paths>), Column('product_id', INTEGER(), ForeignKey('beams.product_id'), table=<beam_file_paths>), schema=None)"),
    'beams': GenericRepr("Table('beams', MetaData(bind=None), Column('product_id', INTEGER(), table=<beams>, primary_key=True, nullable=False), Column('name', TEXT(), table=<beams>, nullable=False), Column('contact', TEXT(), table=<beams>), Column('date_produced', DATE(), table=<beams>), Column('produced_by', TEXT(), table=<beams>), Column('date_posted', DATE(), table=<beams>), Column('posted_by', TEXT(), table=<beams>), Column('date_updated', DATE(), table=<beams>), Column('updated_by', TEXT(), table=<beams>), Column('note', TEXT(), table=<beams>), Column('input_map_product_id', INTEGER(), ForeignKey('maps.product_id'), table=<beams>), Column('input_beam_product_id', INTEGER(), ForeignKey('beams.product_id'), table=<beams>), schema=None)"),
    'map_file_paths': GenericRepr("Table('map_file_paths', MetaData(bind=None), Column('path_id', INTEGER(), table=<map_file_paths>, primary_key=True, nullable=False), Column('path', TEXT(), table=<map_file_paths>), Column('note', TEXT(), table=<map_file_paths>), Column('product_id', INTEGER(), ForeignKey('maps.product_id'), table=<map_file_paths>), schema=None)"),
    'maps': GenericRepr("Table('maps', MetaData(bind=None), Column('product_id', INTEGER(), table=<maps>, primary_key=True, nullable=False), Column('name', TEXT(), table=<maps>, nullable=False), Column('contact', TEXT(), table=<maps>), Column('date_produced', DATE(), table=<maps>), Column('produced_by', TEXT(), table=<maps>), Column('date_posted', DATE(), table=<maps>), Column('posted_by', TEXT(), table=<maps>), Column('date_updated', DATE(), table=<maps>), Column('updated_by', TEXT(), table=<maps>), Column('note', TEXT(), table=<maps>), schema=None)"),
    'simulation_file_paths': GenericRepr("Table('simulation_file_paths', MetaData(bind=None), Column('path_id', INTEGER(), table=<simulation_file_paths>, primary_key=True, nullable=False), Column('path', TEXT(), table=<simulation_file_paths>), Column('note', TEXT(), table=<simulation_file_paths>), Column('product_id', INTEGER(), ForeignKey('simulations.product_id'), table=<simulation_file_paths>), schema=None)"),
    'simulations': GenericRepr("Table('simulations', MetaData(bind=None), Column('product_id', INTEGER(), table=<simulations>, primary_key=True, nullable=False), Column('name', TEXT(), table=<simulations>, nullable=False), Column('contact', TEXT(), table=<simulations>), Column('date_produced', DATE(), table=<simulations>), Column('produced_by', TEXT(), table=<simulations>), Column('date_posted', DATE(), table=<simulations>), Column('posted_by', TEXT(), table=<simulations>), Column('date_updated', DATE(), table=<simulations>), Column('updated_by', TEXT(), table=<simulations>), Column('note', TEXT(), table=<simulations>), schema=None)")
}
