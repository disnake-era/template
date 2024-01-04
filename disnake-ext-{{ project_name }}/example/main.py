# SPDX-License-Identifier: {{ spdx_license }}

import asyncio

from disnake.ext import commands


async def main() -> None:
    bot = commands.Bot()

    await bot.start("TOKEN")


asyncio.run(main())
