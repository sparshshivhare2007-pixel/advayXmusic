# Authored By Certified Coders © 2025
import asyncio
import shlex
from typing import Tuple
from ..logging import LOGGER

# Bypass the Git Update logic to prevent Heroku/VPS Authentication Crashes
def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())

def git():
    # Humne saara crash hone wala code hata diya hai.
    # Ab bot bina kisi error ke start ho jayega.
    LOGGER(__name__).info(f"Git Update Check Bypassed. Bot is starting...")
    return
