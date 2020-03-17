from queue import Queue
import enum
import uuid
import threading
import os
import json
from typing import Dict, Any


store = {}


def save_request(request: Dict[str, Any]) -> str:
    id = str(uuid.uuid4())
    store[id] = request
    return id


def remove_request(id: str):
    try:
        del store[str(id)]
    except KeyError:
        pass


def clear_request():
    for key in store:
        del key
