# Authored By Certified Coders © 2025

import asyncio
import os
import re
from typing import Union

import aiohttp
import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message

from DestinyxMusic.utils.formatters import time_to_seconds
from DestinyxMusic import LOGGER

try:
    from py_yt import VideosSearch
except ImportError:
    from youtubesearchpython.__future__ import VideosSearch


# API Downloader (Shruti style)
API_URL = "https://shrutibots.site"

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


async def download_song(link: str):

    video_id = link.split("v=")[-1].split("&")[0] if "v=" in link else link

    if not video_id:
        return None

    file_path = f"{DOWNLOAD_DIR}/{video_id}.mp3"

    if os.path.exists(file_path):
        return file_path

    try:

        async with aiohttp.ClientSession() as session:

            params = {"url": video_id, "type": "audio"}

            async with session.get(
                f"{API_URL}/download",
                params=params,
                timeout=aiohttp.ClientTimeout(total=7),
            ) as response:

                if response.status != 200:
                    return None

                data = await response.json()
                token = data.get("download_token")

                if not token:
                    return None

                stream_url = f"{API_URL}/stream/{video_id}?type=audio&token={token}"

                async with session.get(stream_url) as file_response:

                    if file_response.status != 200:
                        return None

                    with open(file_path, "wb") as f:
                        async for chunk in file_response.content.iter_chunked(16384):
                            f.write(chunk)

        if os.path.exists(file_path):
            return file_path

    except Exception as e:
        LOGGER.error(f"Song download error: {e}")

    return None


async def download_video(link: str):

    video_id = link.split("v=")[-1].split("&")[0] if "v=" in link else link

    if not video_id:
        return None

    file_path = f"{DOWNLOAD_DIR}/{video_id}.mp4"

    if os.path.exists(file_path):
        return file_path

    try:

        async with aiohttp.ClientSession() as session:

            params = {"url": video_id, "type": "video"}

            async with session.get(
                f"{API_URL}/download",
                params=params,
                timeout=aiohttp.ClientTimeout(total=7),
            ) as response:

                if response.status != 200:
                    return None

                data = await response.json()
                token = data.get("download_token")

                if not token:
                    return None

                stream_url = f"{API_URL}/stream/{video_id}?type=video&token={token}"

                async with session.get(stream_url) as file_response:

                    if file_response.status != 200:
                        return None

                    with open(file_path, "wb") as f:
                        async for chunk in file_response.content.iter_chunked(16384):
                            f.write(chunk)

        if os.path.exists(file_path):
            return file_path

    except Exception as e:
        LOGGER.error(f"Video download error: {e}")

    return None


async def shell_cmd(cmd):

    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    out, err = await proc.communicate()

    if err:
        return err.decode()

    return out.decode()


class YouTubeAPI:

    def __init__(self):

        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.listbase = "https://youtube.com/playlist?list="

    async def exists(self, link: str, videoid: Union[bool, str] = None):

        if videoid:
            link = self.base + link

        return bool(re.search(self.regex, link))

    async def url(self, message: Message):

        messages = [message]

        if message.reply_to_message:
            messages.append(message.reply_to_message)

        for msg in messages:

            entities = msg.entities or msg.caption_entities
            text = msg.text or msg.caption

            if not entities:
                continue

            for entity in entities:

                if entity.type == MessageEntityType.URL:
                    return text[entity.offset: entity.offset + entity.length]

                if entity.type == MessageEntityType.TEXT_LINK:
                    return entity.url

        return None

    async def details(self, link, videoid=None):

        if videoid:
            link = self.base + link

        link = link.split("&")[0]

        results = VideosSearch(link, limit=1)

        result = (await results.next())["result"][0]

        title = result["title"]
        duration = result["duration"]
        thumb = result["thumbnails"][0]["url"].split("?")[0]
        vidid = result["id"]

        seconds = int(time_to_seconds(duration)) if duration else 0

        return title, duration, seconds, thumb, vidid

    async def track(self, link, videoid=None):

        if videoid:
            link = self.base + link

        link = link.split("&")[0]

        results = VideosSearch(link, limit=1)

        result = (await results.next())["result"][0]

        track_details = {
            "title": result["title"],
            "link": result["link"],
            "vidid": result["id"],
            "duration_min": result["duration"],
            "thumb": result["thumbnails"][0]["url"].split("?")[0],
        }

        return track_details, result["id"]

    async def playlist(self, link, limit, user_id, videoid=None):

        if videoid:
            link = self.listbase + link

        link = link.split("&")[0]

        data = await shell_cmd(
            f"yt-dlp -i --get-id --flat-playlist --playlist-end {limit} --skip-download {link}"
        )

        return [x for x in data.split("\n") if x]

    async def video(self, link, videoid=None):

        if videoid:
            link = self.base + link

        file = await download_video(link)

        if file:
            return 1, file

        return 0, "Video download failed"

    async def download(self, link, mystic, video=None, videoid=None):

        if videoid:
            link = self.base + link

        try:

            if video:
                file = await download_video(link)
            else:
                file = await download_song(link)

            if file:
                return file, True

            return None, False

        except Exception:
            return None, False
