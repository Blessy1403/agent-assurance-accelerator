from pydantic import BaseModel, Field, field_validator
from typing import Literal
from datetime import datetime

class Example(BaseModel):
    name: str
    count: int = Field(ge=0, le=100)
    status: Literal["open", "closed"]
    tags: list[str] = []
    note: str | None = None
    created_at: datetime

    @field_validator("name")
    @classmethod
    def name_not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("name must not be blank")
        return v

record = Example(
    name="Blessy",
    count=50,
    status="open",
    tags=["AAA", "Pydantic"],
    note="Day 2 Learning",
    created_at=datetime.now()
)

print(record)
print(record.model_dump())
print(record.model_dump_json())
