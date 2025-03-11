from typing import List, Dict
from pydantic import BaseModel, Field
from langchain.agents import tool

from functions import get_playlist_videos

class GetPlaylistVideosInput(BaseModel):
    channel_id: str = Field(
        default="UCA_23dkEYToAc37hjSsCnXA",
        description="The YouTube channel ID to retrieve the latest videos from."
    )
    limit: int = Field(
        default=5,
        description="Number of videos to retrieve."
    )

@tool("get_latest_videos", return_direct=False)
def get_latest_videos(input_data: GetPlaylistVideosInput) -> List[Dict]:
    """
    Tool to fetch the latest videos from a given YouTube channel.
    Returns a list of dicts, each containing 'title', 'link', and 'view'.
    """
    return get_playlist_videos(channel_id=input_data.channel_id, limit=input_data.limit)
