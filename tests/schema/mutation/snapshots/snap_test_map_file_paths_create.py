# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[createMapFilePath] 1'] = {
    'data': {
        'createMapFilePath': {
            'mapFilePath': {
                'path': 'nersc:/go/to/my/new_map_v1'
            }
        }
    }
}

snapshots['test_schema_success[createMapFilePath] 2'] = {
    'data': {
        'map': {
            'beams': {
                'edges': [
                ]
            },
            'datePosted': '2019-02-13',
            'name': 'lat20190213',
            'note': '''- This is a dummy test with a lat map
- This should not depend on any beam''',
            'paths': {
                'edges': [
                    {
                        'node': {
                            'note': '',
                            'path': 'nersc:/go/to/my/maps',
                            'product': {
                                'productId': '1001'
                            }
                        }
                    },
                    {
                        'node': {
                            'note': '- Note 1',
                            'path': 'nersc:/go/to/my/new_map_v1',
                            'product': {
                                'productId': '1001'
                            }
                        }
                    }
                ]
            },
            'producedBy': 'pwg-pmn'
        }
    }
}
