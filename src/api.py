import logging

from fastapi import APIRouter

logger = logging.getLogger('backend')

SERVICE_STATUS_PATH = "/status"

router = APIRouter()


@router.get(SERVICE_STATUS_PATH)
async def status():
    return {"message": "Backend service is available"}
