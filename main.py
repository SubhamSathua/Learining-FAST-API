from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return "Welcome! To The Blog"

@app.get('/blog')
def blog_home():
    return 'NEWS | Technology'

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