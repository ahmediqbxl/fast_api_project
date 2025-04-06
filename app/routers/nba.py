from fastapi import APIRouter, HTTPException
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from typing import List, Optional

router = APIRouter(
    prefix="/nba",
    tags=["NBA"],
    responses={404: {"description": "Not found"}},
)

@router.get("/players")
async def get_all_players():
    """Get all NBA players"""
    try:
        all_players = players.get_players()
        return {"players": all_players}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/teams")
async def get_all_teams():
    """Get all NBA teams"""
    try:
        all_teams = teams.get_teams()
        return {"teams": all_teams}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/player/{player_id}/career")
async def get_player_career_stats(player_id: str):
    """Get career stats for a specific player"""
    try:
        career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
        return career_stats.get_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/player/{player_id}/info")
async def get_player_info(player_id: str):
    """Get basic information for a specific player"""
    try:
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
        return player_info.get_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 