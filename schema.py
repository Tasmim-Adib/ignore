from typing import List
from pydantic import BaseModel

class Products(BaseModel):
    c : str
    l : List[str] = []
    ia : List[str] = []
    ir : List[str] = []
    
