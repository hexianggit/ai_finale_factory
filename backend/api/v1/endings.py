from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from core.auth import get_current_user
from schemas.ending import EndingCreate, EndingUpdate, EndingInDB
from schemas.user import UserInDB
from services import ending_service

router = APIRouter()

@router.post("/", response_model=EndingInDB)
async def create_ending(
    ending: EndingCreate,
    current_user: UserInDB = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await ending_service.create_ending(db, ending, current_user.id)

@router.get("/", response_model=List[EndingInDB])
async def list_endings(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    return await ending_service.get_endings(db, skip, limit)

@router.get("/{ending_id}", response_model=EndingInDB)
async def get_ending(
    ending_id: int,
    db: AsyncSession = Depends(get_db)
):
    ending = await ending_service.get_ending(db, ending_id)
    if not ending:
        raise HTTPException(status_code=404, detail="Ending not found")
    return ending

@router.put("/{ending_id}", response_model=EndingInDB)
async def update_ending(
    ending_id: int,
    ending: EndingUpdate,
    db: AsyncSession = Depends(get_db)
):
    updated_ending = await ending_service.update_ending(db, ending_id, ending)
    if not updated_ending:
        raise HTTPException(status_code=404, detail="Ending not found")
    return updated_ending 