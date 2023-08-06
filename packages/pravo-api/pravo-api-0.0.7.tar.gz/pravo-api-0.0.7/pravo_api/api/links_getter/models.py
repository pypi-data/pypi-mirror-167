import json
from pydantic import BaseModel, Field, validator
from pathlib import Path
from typing import List



class DocInfo(BaseModel):
    doc_id:str
    tags: List[str] = None
    author: str = None
    date: str = None
    url: str = None
    region: str = None