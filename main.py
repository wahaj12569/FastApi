from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def index():
    return {'data':{'name':'wahaj'}}


@app.get('/about')
def about():
    return {'data':'this is about page'}

@app.get('/blog')
def index(limit,published:bool):
    return published
    if published:
        return {'data':f'{limit} published blogs from the DB'}
    else:
        return {'data':f'{limit} blogs from the DB'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'unpublished'}

@app.get('/blog/{id}') #It is dynamic routing and in dynamic routing the block of dynamic routing should be blow the others block!! 
def show(id : int):
    return {'data':id}
