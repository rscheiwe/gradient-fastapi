from fastapi import APIRouter
from typing import List

from gradient.models.content import ContentResult

from gradient.services.content_db_service import ContentDBService

import json


router = APIRouter()

@router.get('/unfamiliar-wow', response_model=List[ContentResult], name='unfamiliar-wow')
def get_unfamiliar_wow() -> List[ContentResult]:
    """Endpoint for Unfamiliar Content WoW Results

    :return: (dict) results structured per ContentResult model
    """
    response_class = ContentDBService('vertica', 'unfamiliar query')
    response = response_class._wow_aggregate()
    unfamiliar_response: List[ContentResult] = response
    return unfamiliar_response