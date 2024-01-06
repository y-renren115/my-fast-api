from fastapi import APIRouter
from .models import TodoItem

router = APIRouter()
todo_items = []

@router.post("/items/")
def create_item(item: TodoItem):
    todo_items.append(item)
    return item

@router.get("/items/")
def read_items():
    return todo_items