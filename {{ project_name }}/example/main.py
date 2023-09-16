# SPDX-License-Identifier: LGPL-3.0-only

import asyncio

from disnake.ext import commands


async def main() -> None:
    bot = commands.Bot()

    ...

    await bot.start("TOKEN")


asyncio.run(main())
