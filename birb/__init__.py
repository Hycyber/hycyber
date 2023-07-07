from .birb import Birb


async def setup(bot):
    await bot.add_cog(Birb(bot))
