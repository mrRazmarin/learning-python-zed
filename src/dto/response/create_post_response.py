from pydantic import BaseModel, Field


class CreatePostResponseDto(BaseModel):
    title: str
    body: str
    user_id: int = Field(alias="userId")
    id: int