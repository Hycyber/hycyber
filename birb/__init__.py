from .birb import Birb


def setup(bot):
    bot.add_cog(Birb(bot))
