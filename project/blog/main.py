from fastapi import FastAPI, Depends
from . import schemas
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post('/blog')
def create(request: schemas.Blog, db: Session = Depends(get_db)): #request is a type of pydantic field Blog
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}')
def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    return blog

#stopped at 1:43:29