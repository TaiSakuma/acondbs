# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_success[updateMapFilePath] 1'] = {
    'data': {
        'updateMapFilePath': {
            'mapFilePath': {
                'path': 'nersc:/go/to/my/new_map_v2'
            }
        }
    }
}

snapshots['test_schema_success[updateMapFilePath] 2'] = {
    'data': {
        'map': {
            'beams': {
                'edges': [
                    {
                        'node': {
                            'name': '20200123'
                        }
                    }
                ]
            },
            'datePosted': '2020-01-20',
            'name': 'lat20200120',
            'note': '''- This is a dummy test with a lat map
- A beam depends on this map''',
            'paths': {
                'edges': [
                    {
                        'node': {
                            'note': '- Note 1 updated',
                            'path': 'nersc:/go/to/my/new_map_v2',
                            'product': {
                                'productId': '1012'
                            }
                        }
                    },
                    {
                        'node': {
                            'note': 'lat only',
                            'path': 'nersc:/go/to/my/maps_v2',
                            'product': {
                                'productId': '1012'
                            }
                        }
                    },
                    {
                        'node': {
                            'note': 'lat only',
                            'path': 'abcde:/path/to/the/maps_v2',
                            'product': {
                                'productId': '1012'
                            }
                        }
                    }
                ]
            },
            'producedBy': 'pwg-pmn'
        }
    }
}
