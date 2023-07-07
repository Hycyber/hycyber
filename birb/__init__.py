from .birb import Birb


async def setup(bot):
    cog = Birb(bot)
    await bot.add_cog(cog)
