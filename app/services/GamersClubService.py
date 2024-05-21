import requests
from ..shared.config import config


class GamersClubService:

    @staticmethod
    def get_player_history(player_id: str):
        url = f"{config['SERVICES_URLS']['GAMERS_CLUB']}/box/history/{player_id}"
        headers = {
            'Authorization': 'Basic ' + config['KEYS']['GAMERS_CLUB_AUTH_KEY'],
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
