from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


@app.get('/posts')
def get_posts():
    return {'data': 'My posts'}


@app.get('/')
def root():
    return {'message': 'Welcome to my first API'}


@app.post('/create-posts')
def create_post(new_post: Post):
    print(new_post)
    return {"data": "new post"}

