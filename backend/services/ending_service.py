from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.ending import Ending
from schemas.ending import EndingCreate, EndingUpdate
from services.dify_service import generate_ending

async def create_ending(db: AsyncSession, ending: EndingCreate, user_id: int) -> Ending:
    # 调用 Dify API 生成结局内容
    generated_content = await generate_ending(ending.query)
    
    db_ending = Ending(
        work=ending.work,
        query=ending.query,
        user_id=user_id,
        content=generated_content
    )
    db.add(db_ending)
    await db.commit()
    await db.refresh(db_ending)
    return db_ending

async def get_ending(db: AsyncSession, ending_id: int) -> Optional[Ending]:
    result = await db.execute(select(Ending).filter(Ending.id == ending_id))
    return result.scalar_one_or_none()

async def get_endings(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 10
) -> List[Ending]:
    result = await db.execute(
        select(Ending).offset(skip).limit(limit)
    )
    return result.scalars().all()

async def update_ending(
    db: AsyncSession,
    ending_id: int,
    ending: EndingUpdate
) -> Optional[Ending]:
    db_ending = await get_ending(db, ending_id)
    if not db_ending:
        return None
        
    update_data = ending.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_ending, field, value)
        
    await db.commit()
    await db.refresh(db_ending)
    return db_ending 