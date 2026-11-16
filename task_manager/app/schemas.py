
from pydantic import BaseModel, Field, field_validator


# Schema for creating a task
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Title cannot be empty")

        return value



# Schema for updating a task
class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    completed: bool | None = None

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if value is not None:
            value = value.strip()

            if not value:
                raise ValueError("Title cannot be empty")

        return value


# Schema for displaying a task
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool

    class Config:
        from_attributes = True
