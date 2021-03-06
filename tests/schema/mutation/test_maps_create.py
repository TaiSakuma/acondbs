import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          mutation m {
            createMap(input: {
              name: "map1",
              datePosted: "2020-02-20",
              mapper: "pwg-pmn",
              note: "- Item 1"
            }) { map { name } }
          }
        ''',
        '''
          {
            map(name: "map1") {
              name datePosted mapper note
              beams { edges { node { name } } }
              mapFilePaths { edges { node { path } } }
            }
          }
        ''',
        id='createMap-all-options'
    ),
    pytest.param(
        '''
          mutation m {
            createMap(input: {
              name: "map1",
              mapper: "pwg-pmn"
            }) { map { name } }
          }
        ''',
        '''
          {
            map(name: "map1") {
              name datePosted mapper note
              beams { edges { node { name } } }
              mapFilePaths { edges { node { path } } }
            }
          }
        ''',
        id='createMap-selective-options'
    ),
    pytest.param(
        '''
          mutation m {
            createMap(input: {
              mapper: "pwg-pmn"
            }) { map { name } }
          }
        ''',
        '''
          {
            map(name: "map1") {
              name datePosted mapper note
              beams { edges { node { name } } }
              mapFilePaths { edges { node { path } } }
            }
          }
        ''',
        id='createMap-error-no-name'
    ),
]

@pytest.mark.parametrize('mutation, query', params)
def test_schema(app, snapshot, mutation, query):
    client = Client(schema)
    with app.app_context():
        snapshot.assert_match(client.execute(mutation))
    with app.app_context():
        snapshot.assert_match(client.execute(query))

##__________________________________________________________________||
