from pydantic import BaseModel, Field


class SinglePostResponseDto(BaseModel):
    user_id: int = Field(alias="userId")
    id: int
    title: str
    body: str