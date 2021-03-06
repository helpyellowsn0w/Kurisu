import discord
from discord.ext import commands
from sys import argv

class Memes:
    """
    Meme commands
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    async def _meme(self, ctx, msg):
        author = ctx.message.author
        if ctx.message.channel.name[0:5] == "help-" or "assistance" in ctx.message.channel.name or (self.bot.nomemes_role in author.roles):
            await self.bot.delete_message(ctx.message)
            try:
                await self.bot.send_message(author, "Meme commands are disabled in this channel, or your priviledges have been revoked.")
            except discord.errors.Forbidden:
                await self.bot.say(author.mention + " Meme commands are disabled in this channel, or your priviledges have been revoked.")
        else:
            await self.bot.say(self.bot.escape_name(ctx.message.author.display_name) + ": " + msg)

    # list import discord
from discord.ext import commands
from sys import argv

class Memes:
    """
    Meme commands
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    async def _meme(self, ctx, msg):
        author = ctx.message.author
        if ctx.message.channel.name[0:5] == "help-" or "assistance" in ctx.message.channel.name or (self.bot.nomemes_role in author.roles):
            await self.bot.delete_message(ctx.message)
            try:
                await self.bot.send_message(author, "Meme commands are disabled in this channel, or your priviledges have been revoked.")
            except discord.errors.Forbidden:
                await self.bot.say(author.mention + " Meme commands are disabled in this channel, or your priviledges have been revoked.")
        else:
            await self.bot.say(self.bot.escape_name(ctx.message.author.display_name) + ": " + msg)

    # list memes
    @commands.command(name="listmemes", pass_context=True)
    async def _listmemes(self, ctx):
        """List meme commands."""
        # this feels wrong...
        funcs = dir(self)
        msg = "```\n"
        msg += ", ".join(func for func in funcs if func != "bot" and func[0] != "_")
        msg += "```"
        await self._meme(ctx, msg)

    # 3dshacks memes (old)

    @commands.command()
    async def t(self):
        embed = discord.Embed(title="Nintendo Homebrew Mario Kart Tourney", description="**Nintendo Homebrew** is hosting a Mario Kart tournament and you are invited!", color=discord.Color.dark_blue())
        embed.set_image(url="http://art.gametdb.com/wii/cover/US/RMCE28.png?1431288336")
        embed.set_thumbnail(url="http://art.gametdb.com/wii/cover/US/RMCE28.png?1431288336")
        embed.set_author(name="author", url="https://google.com", icon_url="https://cdn.discordapp.com/avatars/78465448093417472/a06a07a9d8b5f75278281930c0cbe869.webp?size=64")
        embed.set_footer(text="footer", icon_url="https://cdn.discordapp.com/avatars/78465448093417472/a06a07a9d8b5f75278281930c0cbe869.webp?size=64")
        embed.add_field(name="When is this taking place?", value="We are currently not sure, but a date can be up for discussion in #meta.")
        embed.add_field(name="Will there be more?", value="That is the plan!")
        embed.add_field(name="Why this game?", value="This game was selected since there is online cheat code prevention, and its known for its fun multiplayer.  It also includes all the tracks you ever have wanted out of a Mario Kart Game.")
        embed.add_field(name="field1_noinline", value="field1_noinline")
#    embed.add_field(name="field2_noinline", value="field2_noinline", inline=False)
#    embed.add_field(name="field3_noinline", value="field3_noinline", inline=False)
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True, hidden=True)
    async def rip(self, ctx):
        """Memes."""
        await self._meme(ctx, "Press F to pay respects.")

    @commands.command(pass_context=True, hidden=True)
    async def bigsmoke(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/vo5l6Fo.jpg\nALL YOU HAD TO DO WAS FOLLOW THE DAMN GUIDE CJ!")

    @commands.command(pass_context=True, hidden=True)
    async def bigorder(self, ctx):
        """Memes."""
        await self._meme(ctx, "I’ll have two number 9s, a number 9 large, a number 6 with extra dip, a number 7, two number 45s, one with cheese, and a large soda.")

    # new memes
    @commands.command(pass_context=True, hidden=True)
    async def adrian1(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/j0Dkv2Z.png")

    @commands.command(pass_context=True, hidden=True)
    async def notmyb(self, ctx):
        """Memes."""
        await self._meme(ctx, "https://imgflip.com/s/meme/But-Thats-None-Of-My-Business.jpg")
        
# Load the extension
def setup(bot):
    bot.add_cog(Memes(bot))

    @commands.command(name="listmemes", pass_context=True)
    async def _listmemes(self, ctx):
        """List meme commands."""
        # this feels wrong...
        funcs = dir(self)
        msg = "```\n"
        msg += ", ".join(func for func in funcs if func != "bot" and func[0] != "_")
        msg += "```"
        await self._meme(ctx, msg)

    # 3dshacks memes (old)
    
    @commands.command(pass_context=True, hidden=True)
    async def lenny(self, ctx):
        """Memes."""
        await self._meme(ctx, "( ͡° ͜ʖ ͡°)")

    @commands.command(pass_context=True, hidden=True)
    async def rip(self, ctx):
        """Memes."""
        await self._meme(ctx, "Press F to pay respects.")

    @commands.command(pass_context=True, hidden=True)
    async def bigsmoke(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/vo5l6Fo.jpg\nALL YOU HAD TO DO WAS FOLLOW THE DAMN GUIDE CJ!")

    @commands.command(pass_context=True, hidden=True)
    async def bigorder(self, ctx):
        """Memes."""
        await self._meme(ctx, "I’ll have two number 9s, a number 9 large, a number 6 with extra dip, a number 7, two number 45s, one with cheese, and a large soda.")

    @commands.command(pass_context=True, hidden=True)
    async def adrian1(self, ctx):
        """Memes."""
        await self._meme(ctx, "http://i.imgur.com/j0Dkv2Z.png")
# Load the extension
def setup(bot):
    bot.add_cog(Memes(bot))
