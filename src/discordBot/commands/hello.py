
def main(Bot):

  @Bot.slash_command(name="小幫手在不在", description="查看小幫手是否還在")
  async def ping(ctx):
    await ctx.respond("我還在~")
