import discord
from discord.ext import commands


class test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['Test'])
    async def test(self, ctx, member):
        if member[0] == '<' and member[1] == '@':
            converter = MemberConverter()
            member = await converter.convert(ctx, member)
        elif member.isnumeric():
            member = int(member)

        members = await ctx.guild.fetch_members().flatten()
        multiple_member_array = []
        try:
            if isinstance(member, discord.Member):
                for members_list in members:
                    if member.name.lower() in members_list.name.lower():
                        multiple_member_array.append(members_list)
                    else:
                        pass
            elif isinstance(member, int):
                for member_list in members:
                    if member_list.id == member:
                        multiple_member_array.append(member_list)
                    else:
                        pass


            else:
                for members_list in members:
                    if member.lower() in members_list.name.lower():
                        multiple_member_array.append(members_list)
                    else:
                        pass


            if len(multiple_member_array) == 1:

                await ctx.send('member exists!')

            elif len(multiple_member_array) > 1:

                multiple_member_array_duplicate_array = []
                for multiple_member_array_duplicate in multiple_member_array:
                    multiple_member_array_duplicate_array.append(multiple_member_array_duplicate.name)

                embed = discord.Embed(
                        title=f'Search for {member}\nFound multiple results',
                        description=f'\n'.join(multiple_member_array_duplicate_array),
                        colour=0x808080
                    )
                await ctx.send(embed=embed)

            else:
                await ctx.send(f'The member `{member}` does not exist!')
        except Exception as e:
        	await ctx.send(f'{e}')


def setup(bot):
    bot.add_cog(test(bot))
