import tempfile
import os
from app import app,db
import pytest

import json

def test_base_route():
    client=app.test_client()
    url='get-all'


    response=client.get(url)
    assert response.status_code==200
    assert response.content_type == 'application/json'


def test_create():
    client=app.test_client()
    url='add_product'
    dataa={
    'description': "something new",
    
    "name": "lapto34 ",
    "price": 253.0,
    "qty": 5
}

#     response=client.post(url, data=json.dumps(dataa),headers={"Content-Type": "application/json"},)
   
    assert response.status_code==200

    




def test_details():
    client=app.test_client()
    url='get-details/1'


    response=client.get(url)
    assert response.status_code==200
    assert response.content_type == 'application/json'




def test_delete():
    client=app.test_client()
    url='delete-item/<put here id>'


    response=client.delete(url,follow_redirects=True)
    
    
    assert response.status_code==200 
    



def test_update():
    client=app.test_client()
    url='update-item/10'
    dataa=  {
        "description": "something new",
        "id": 10,
        "name": "laptopddd ",
        "price": 253.0,
        "qty": 5
    }

    response=client.put(url, data=json.dumps(dataa), headers={"Content-Type": "application/json"})
    
    
    assert response.status_code==200
    assert response.content_type == 'application/json'
