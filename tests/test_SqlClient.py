import mysql.connector

import pytest
from organdonationwebapp.models.SqlClient import SqlClient


def test__init__(organdonationwebapp):
    with app.app_context():
        db = __init__()
        assert db is __init__()

    with pytest.raises(mysql.connector.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e)


def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('organdonationwebapp.models.SqlClient.init_db', fake__init__)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called