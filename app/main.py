from fastapi import FastAPI,Depends,status,HTTPException
from sqlalchemy.orm import Session
import models,db,schema
app = FastAPI()
def create_tables():
    models.Base.metadata.create_all(bind=db.engine)
create_tables()
@app.get('/jokes', response_model=schema.Joke_out)
async def Job(db: Session = Depends(db.get_db)):
    jokes = db.query(models.Joke).all()
    return jokes

@app.post('/post_joke')
async def post_joke(joke:schema.Joke,db:Session = Depends(db.get_db)):
    new_joke = models.Joke( **joke.dict())
    db.add(new_joke)
    db.commit()
    db.refresh(new_joke)
    return new_joke

@app.get('/joke/{id}',response_model=schema.Joke_out)
async def Joke_by_id(id:int,db:Session = Depends(db.get_db)):
    joke_query = db.query(models.Joke).filter(models.Joke.id == id)
    joke = joke_query.first()
    if joke is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Joke with id: {id} does not exist")
    return joke
