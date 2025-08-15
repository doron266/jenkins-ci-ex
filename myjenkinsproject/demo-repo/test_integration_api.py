
from app import app

def test_sum_endpoint():
    client = app.test_client()
    resp = client.post('/sum', json={'numbers':[2,3,5]})
    assert resp.status_code == 200
    assert resp.get_json()['sum'] == 10

def test_create_user_endpoint():
    client = app.test_client()
    resp = client.post('/users', json={'name':'  john DOE  '})
    assert resp.status_code == 201
    assert resp.get_json()['name'] == 'John Doe'
