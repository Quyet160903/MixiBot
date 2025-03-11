import requests
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_YOUTUBE_API_KEY = os.getenv("GOOGLE_YOUTUBE_API_KEY")

BASE_URL = "https://www.googleapis.com/youtube/v3"
MIXIGAMING_CHANNEL_ID = "UCA_23dkEYToAc37hjSsCnXA"

def get_uploads_playlist_id(channel_id):
    """
    Retrieves the uploads playlist ID for the given channel.
    """
    url = f"{BASE_URL}/channels?part=contentDetails&id={channel_id}&key={GOOGLE_YOUTUBE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if "items" in data and data["items"]:
        uploads_playlist_id = data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
        return uploads_playlist_id
    else:
        raise ValueError("No channel found with the provided channel ID.")

def get_playlist_video_ids(uploads_playlist_id, limit=5):
    """
    Retrieves video IDs from the uploads playlist with a specified limit.
    """
    url = (f"{BASE_URL}/playlistItems?part=snippet,contentDetails"
           f"&playlistId={uploads_playlist_id}&maxResults={limit}&key={GOOGLE_YOUTUBE_API_KEY}")
    response = requests.get(url)
    data = response.json()
    video_ids = [item["contentDetails"]["videoId"] for item in data.get("items", [])]
    return video_ids

def get_video_details(video_ids):
    """
    Retrieves video details (title, statistics) for a list of video IDs.
    """
    if not video_ids:
        return []
    ids_str = ",".join(video_ids)
    url = f"{BASE_URL}/videos?part=snippet,statistics&id={ids_str}&key={GOOGLE_YOUTUBE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    videos = []
    for item in data.get("items", []):
        title = item["snippet"]["title"]
        video_id = item["id"]
        view_count = item["statistics"].get("viewCount", "N/A")
        link = f"https://www.youtube.com/watch?v={video_id}"
        videos.append({"title": title, "link": link, "view": view_count})
    return videos

def get_playlist_videos(channel_id, limit=5):
    """
    Combines all steps to return a list of dictionaries with video details
    for the latest videos from a channel.
    """
    uploads_playlist_id = get_uploads_playlist_id(channel_id)
    video_ids = get_playlist_video_ids(uploads_playlist_id, limit)
    return get_video_details(video_ids)

# Example usage
if __name__ == "__main__":
    videos = get_playlist_videos(MIXIGAMING_CHANNEL_ID, limit=5)
    print(videos)