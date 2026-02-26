from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return 'Hello'



@app.get('/blog')
def blog(limit = 10, published:bool = True, sort: Optional[str] = None):
    # return published
    if published:
        return {'data':f'Total {limit} published blogs'}
    else:
        return {'data':f'Total {limit} blogs'}



@app.get('/blog/unpublished') 
def unpublished():
    return {'data':'Unpublished Blog'}

@app.get('/blog/{id}')
def blog_page(id:int):
    # DO: Fetch the blog page here
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id:int):
    # TODO: Fetch comments of blog by ID
    return {'data':{'1', '2', '3'}}