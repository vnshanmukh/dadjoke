from fastapi import FastAPI,Depends,status,HTTPException,APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session
import models,db,schemas,oauth
from typing import List
router = APIRouter(
    prefix="/jokes",
    tags=['Joke']
)

@router.get('/', response_model=List[schemas.Joke_out])
async def all_jokes(db: Session = Depends(db.get_db)):
    jokes = db.query(models.Joke).all()
    return jokes

@router.post('/post_joke')
async def post_joke(joke:schemas.Joke,db:Session = Depends(db.get_db),current_user : int = Depends(oauth.get_current_user)):
    new_joke = models.Joke(owner_id = current_user.id, **joke.dict())
    db.add(new_joke)
    db.commit()
    db.refresh(new_joke)
    return new_joke

@router.get('/{id}',response_model=schemas.Joke_out_id)
async def Joke_by_id(id:int,db:Session = Depends(db.get_db)):
    joke_query = db.query(models.Joke).filter(models.Joke.id == id)
    joke = joke_query.first()
    if joke is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Joke with id: {id} does not exist")
    return joke