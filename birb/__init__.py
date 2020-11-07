from .birb import birb


def setup(bot):
    bot.add_cog(birb(bot))
