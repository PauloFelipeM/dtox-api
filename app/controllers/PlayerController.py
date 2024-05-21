from fastapi import APIRouter

from ..services.GamersClubService import GamersClubService

router = APIRouter()


@router.get("/players/{player_id}/history", tags=["players-history"])
async def get_player_history(player_id: str):
    return GamersClubService.get_player_history(player_id)
