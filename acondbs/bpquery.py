from flask import Blueprint, request, jsonify
import pandas as pd

from .db import get_db

##__________________________________________________________________||
bp = Blueprint('query', __name__)

##__________________________________________________________________||
@bp.route('/tables')
def tables():
    """returns all tables in HTML (to be deleted)
    """

    table_names = ['maps', 'beams', 'map_path']
    tables = { }
    for table_name in table_names:
        query_ = "SELECT * FROM {}".format(table_name)
        table_html = query_to_table_html(query_)
        tables[table_name] = table_html
    return jsonify(tables=tables)

##__________________________________________________________________||
@bp.route('/query', methods=['POST'])
def query():
    """returns the results of the query in HTML (to be deleted)
    """

    query = request.form['query']
    table_html = query_to_table_html(query)
    return jsonify(result=table_html)

##__________________________________________________________________||
@bp.route('/maps')
def maps():
    """returns the content of the table maps in JSON
    """

    query_ = "SELECT * FROM maps"
    return query_to_table_json(query_)

##__________________________________________________________________||
@bp.route('/paths', methods=['POST'])
def paths():
    map_id = request.form['map_id']
    query_ = "SELECT * FROM map_path WHERE map_id={}".format(map_id)
    return query_to_table_json(query_)

##__________________________________________________________________||
def query_to_dataframe(query):
    db = get_db()
    rows = db.execute(query)
    df = pd.DataFrame(rows, columns=rows.keys())
    return df

##__________________________________________________________________||
def query_to_table_html(query):
    df = query_to_dataframe(query)
    html = df.to_html()
    return html

##__________________________________________________________________||
def query_to_table_json(query):
    df = query_to_dataframe(query)

    json = df.to_json(orient='table', index=False)
    # Note: the orient 'table' option is described in
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html
    # e.g.,
    # >>> df = pd.DataFrame(dict(A=[10, 20], B=["abc", "def"]))
    # >>> df
    #     A    B
    # 0  10  abc
    # 1  20  def
    # >>> df.to_json(orient='table', index=False)
    # '{"schema":
    #    {"fields": [
    #         {"name":"A", "type":"integer"},
    #         {"name":"B", "type":"string"}
    #       ],
    #     "pandas_version":"0.20.0"},
    #     "data": [
    #         {"A":10, "B":"abc"},
    #         {"A":20, "B":"def"}
    #       ]
    # }'

    return json

##__________________________________________________________________||
