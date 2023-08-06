Imports = """from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from sqlalchemy.orm import Session
from core.providers.database import get_db\n
router = APIRouter()\n\n"""

ImportsController = """from http.client import HTTPException
from sqlalchemy.orm import Session
"""
ImportsListroutes = """

from fastapi import APIRouter
"""

ImportsSchemas = """
from pydantic import BaseModel
from typing import Optional

"""