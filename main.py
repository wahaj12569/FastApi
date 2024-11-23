from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
@app.get('/')
def index():
    return {'data':{'name':'wahaj'}}


@app.get('/about')
def about():
    return {'data':'this is about page'}

@app.get('/blog')
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    # return published
    if published:
        return {'data':f'{limit} published blogs from the DB'}
    else:
        return {'data':f'{limit} blogs from the DB'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'unpublished'}

@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    # return limit 
    return {'data':{'1','2'}}

@app.get('/blog/{id}') #It is dynamic routing and in dynamic routing the block of dynamic routing should be blow the others block!! 
def show(id : int):
    return {'data':id}

class Blog(BaseModel):
    title: str
    body : str
    p_published: Optional[bool] 


@app.post('/blog')
def create_blog(request:Blog):
    # return request
    return {'data':f'the post is created as title {request.title}'}
