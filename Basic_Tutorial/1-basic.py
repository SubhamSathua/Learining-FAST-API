from fastapi import FastAPI

"""This is also works `app2` """
# app2 = FastAPI()

# @app2.get('/')
# def index():
#     return "Heyy!"
""" uvicorn main:app2 --reload """

app = FastAPI()

@app.get('/')
def index():
    return "Heyy!"

@app.get('/json')
def json_output():
    return {'data':{'name':'Subham', 'age':'12'}}

@app.get('/data')
def data_info():
    return {'data':'Subham'}


# @app.get('/data/{id}')
# def data_info():
#     return {'data':{id}}