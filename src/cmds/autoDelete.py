from discord.ext import commands, tasks

@commands.command()


async def setup(bot):
    bot.add_command(say)