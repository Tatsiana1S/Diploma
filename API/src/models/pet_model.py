from typing import List
from pydantic import BaseModel
from API.src.models.category_model import Category
from API.src.models.tag_model import Tag


class PetModel(BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: List[str]
    tags: List[Tag]
    status: str
