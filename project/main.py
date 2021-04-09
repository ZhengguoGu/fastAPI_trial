from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog') #? onwards 
def index(limit=10, published: bool = True, sort: Optional[str]=None):
    if published:
        return {'data': f'{limit} blogs'}
    else:
        return {'data': 'no blogs'}

@app.get('/blog/unpublished') 
def unpublished():
    return {'data': 'all unpublished blog'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}

# @app.get('/blog/unpublished') #this will cause problem, because of the dynamic routing above. 
# def unpublished():
#     return {'data': 'all unpublished blog'}

@app.get('/blog/{id}/comments')
def comment(id):
    return{'data': {'1', '2'}}

class Blog(BaseModel):
    title: int
    body: str 
    published_at: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is created with {request.title} title.'}

#to run: uvicorn main:app --reload