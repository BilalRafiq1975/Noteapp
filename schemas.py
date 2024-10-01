from pydantic import BaseModel, EmailStr, Fieldfrom typing import Optional# User registration schemaclass UserRegister(BaseModel):    username: str = Field(..., min_length=3, max_length=30)    email: EmailStr    password: str = Field(..., min_length=8)  # Enforcing a minimum length for password# Note schemaclass NoteBase(BaseModel):    title: str = Field(..., min_length=1)  # Ensuring title is at least 1 character    desc: str = Field(..., min_length=1)   # Ensuring description is at least 1 character    important: bool = Field(default=False)    pinned: bool = Field(default=False)class NoteCreate(NoteBase):    passclass NoteUpdate(NoteBase):    passclass NoteResponse(NoteBase):    id: str# Convert a single note from the database to a NoteResponsedef noteEntity(item) -> NoteResponse:    return NoteResponse(        id=str(item["_id"]),        title=item["title"],        desc=item["desc"],        important=item["important"],        pinned=item["pinned"]    )# Convert a list of notes from the database to a list of NoteResponsedef notesEntity(items) -> list:    return [noteEntity(item) for item in items]