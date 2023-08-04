from fastapi import FastAPI, Body, UploadFile, Depends, Request
from fastapi.exceptions import HTTPException
from datetime import datetime
from typing import Annotated

from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

import os
from os import environ

from collections import defaultdict, OrderedDict
import traceback



app = FastAPI(root_path=os.getenv('ROOT_PATH', '/'))

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/", tags=["Admin"])
async def root(request: Request):
    return {"message": "Hello World", "root_path": os.getenv('ROOT_PATH', '/')}


