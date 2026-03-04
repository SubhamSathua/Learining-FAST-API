from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return 'Hello'


class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/blog')
def create_blog(any_name:Blog):
    return {'data' : {
        'title of blog':f'{any_name.title}',
        'body' : f'{any_name.body}'
    }}



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


# if __name__ == "__main__":
#     uvicorn.run('app', host="127.0.0.1", port=9000)