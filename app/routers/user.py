import models,schemas,utils,db
from fastapi import Depends,HTTPException,status, APIRouter
from sqlalchemy.orm import Session
router = APIRouter(
    prefix= "/users",
    tags=['users']
)
@router.post("/", response_model=schemas.UserOut)
async def create_user(user:schemas.UserCreate,db: Session = Depends(db.get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
