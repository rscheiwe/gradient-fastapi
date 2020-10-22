from fastapi import APIRouter

from gradient.models.heartbeat import HeartbeatResult

router = APIRouter()


@router.get('/heartbeat', response_model=HeartbeatResult, name='heartbeat')
def get_heartbeat() -> HeartbeatResult:
    """Utility endpoint for health check

    :return: (bool) True if app alive
    """
    heartbeat = HeartbeatResult(is_alive=True)
    return heartbeat
