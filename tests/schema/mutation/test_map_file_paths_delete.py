import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            deleteMapFilePath(mapFilePathId: 1) { ok }
          }
        ''',
        '''
          {
            map(mapId: 1001 ) {
              name datePosted producedBy note
              beams { edges { node { name } } }
              mapFilePaths { edges { node { path note map { mapId } } } }
            }
          }
        ''',
        id='deleteMapFilePath'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema_success(app, snapshot, mutation, query, mock_request_backup_db):
    client = Client(schema)
    with app.app_context():
        snapshot.assert_match(client.execute(mutation))
    with app.app_context():
        snapshot.assert_match(client.execute(query))
    assert 1 == mock_request_backup_db.call_count

##__________________________________________________________________||
