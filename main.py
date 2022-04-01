import os
import discord
from webserver import keep_alive


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))  
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="-help"))
@client.event
async def on_message(message):
    if message.content.startswith('-mon'):
          embedVar = discord.Embed(title="Day of the Week", description="MONDAY", color=0x94C973)
          embedVar.add_field(name="Advanced Systems Integration and Architecture", value="10:00 AM -12:00 PM", inline=False)
          embedVar.add_field(name="Gmeet Link ⬇", value="[Click Here](YOUR_LINK)", inline=False)
          embedVar.add_field(name="Analytics Techniques and Tools", value="1:00 PM - 3:00PM", inline=False)
          embedVar.add_field(name="Gmeet Link ⬇", value="[Click Here](YOUR_LINK)", inline=False)
          embedVar.set_thumbnail(url="https://media.discordapp.net/attachments/900360306310676540/939030971062313061/202-2022004_flexible-schedule-icon-v1-flexible-schedule-icon-hd-removebg-preview.png")
          embedVar.set_image(url="https://media.discordapp.net/attachments/900360306310676540/939366911773401118/1.png?width=991&height=701")
          await message.channel.send(embed=embedVar)
      
    elif message.content.startswith('-tue'):
          embedVar = discord.Embed(title="Day of the Week", description="TUESDAY", color=0x94C973)
          embedVar.add_field(name="Analytics Techniques and Tools", value="7:00 AM -10:00 AM", inline=False)
          embedVar.add_field(name="Gmeet Link ⬇", value="[Click Here](YOUR_LINK)", inline=False)
          embedVar.set_thumbnail(url="https://media.discordapp.net/attachments/900360306310676540/939030971062313061/202-2022004_flexible-schedule-icon-v1-flexible-schedule-icon-hd-removebg-preview.png")
          embedVar.set_image(url="https://media.discordapp.net/attachments/900360306310676540/939366912079568927/2.png?width=881&height=623")
          await message.channel.send(embed=embedVar)

    elif message.content.startswith('-wed'):
          embedVar = discord.Embed(title="Day of the Week", description="WEDNESDAY", color=0x94C973)
          embedVar.add_field(name="Information Assurance and Security", value="9:00 AM - 12:00PM", inline=False)
          embedVar.add_field(name="Gmeet Link ⬇", value="[Click Here](YOUR_LINK)", inline=False)
          embedVar.add_field(name="Capstone Project 1", value="3:00 PM - 6:00PM", inline=False)
          embedVar.add_field(name="Gmeet Link ⬇", value="[Click Here](YOUR_LINK)", inline=False)
          embedVar.set_thumbnail(url="https://media.discordapp.net/attachments/900360306310676540/939030971062313061/202-2022004_flexible-schedule-icon-v1-flexible-schedule-icon-hd-removebg-preview.png")
          embedVar.set_image(url="https://media.discordapp.net/attachments/900360306310676540/939366912394145812/3.png?width=881&height=623")
          await message.channel.send(embed=embedVar)

    elif message.content.startswith('-thu'):
          embedVar = discord.Embed(title="Day of the Week", description="THURSDAY", color=0x94C973)
          embedVar.add_field(name="Advanced Systems Integration and Architecture", value="10:00 AM - 1:00PM", inline=False)
          embedVar.add_field(name="Gmeet Link ⬇", value="[Click Here](YOUR_LINK)", inline=False)
          embedVar.set_thumbnail(url="https://media.discordapp.net/attachments/900360306310676540/939030971062313061/202-2022004_flexible-schedule-icon-v1-flexible-schedule-icon-hd-removebg-preview.png")
          embedVar.set_image(url="https://media.discordapp.net/attachments/900360306310676540/939366912683569212/4.png?width=881&height=623")
          await message.channel.send(embed=embedVar)

    elif message.content.startswith('-fri'):
          embedVar = discord.Embed(title="Day of the Week", description="FRIDAY", color=0x94C973)
          embedVar.add_field(name="	Information Assurance and Security", value="10:00 AM - 12:00 PM", inline=False)
          embedVar.add_field(name="Gmeet Link ⬇", value="[Click Here](YOUR_LINK)", inline=False)
          embedVar.add_field(name="Human-Computer Interaction", value="1:00 PM - 4:00 PM", inline=False)
          embedVar.add_field(name="Gmeet Link ⬇", value="[Click Here]()", inline=False)
          embedVar.set_thumbnail(url="https://media.discordapp.net/attachments/900360306310676540/939030971062313061/202-2022004_flexible-schedule-icon-v1-flexible-schedule-icon-hd-removebg-preview.png")
          embedVar.set_image(url="https://media.discordapp.net/attachments/900360306310676540/939368316248674304/2nd_Sem_Classes_1.png?width=991&height=701")
          await message.channel.send(embed=embedVar)

    elif message.content.startswith('-sat'):
          embedVar = discord.Embed(title="Day of the Week", description="SATURDAY", color=0x94C973)
          embedVar.add_field(name="Fundamentals of Enterprise Data Management", value="7:00 AM - 12:00PM", inline=False)
          embedVar.add_field(name="Gmeet Link ⬇", value="[Click Here](YOUR_LINK)", inline=False)
          embedVar.add_field(name="IT Project Management", value="2:00 AM - 5:00 PM", inline=False)
          embedVar.add_field(name="Gmeet Link ⬇", value="[Click Here](YOUR_LINK)", inline=False)
          embedVar.set_thumbnail(url="https://media.discordapp.net/attachments/900360306310676540/939030971062313061/202-2022004_flexible-schedule-icon-v1-flexible-schedule-icon-hd-removebg-preview.png")
          embedVar.set_image(url="https://media.discordapp.net/attachments/900360306310676540/939368799289868388/2nd_Sem_Classes_2.png?width=991&height=701")
          await message.channel.send(embed=embedVar)

    elif message.content.startswith('-sun'):
          embedVar = discord.Embed(title="Day of the Week", description="SUNDAY", color=0x94C973)
          embedVar.add_field(name="NO CLASSES AVAILABLE", value="❌", inline=False)
          embedVar.set_thumbnail(url="https://media.discordapp.net/attachments/900360306310676540/939030971062313061/202-2022004_flexible-schedule-icon-v1-flexible-schedule-icon-hd-removebg-preview.png")
          await message.channel.send(embed=embedVar)
    
    elif message.content.startswith('-gclass'):
          embedVar = discord.Embed(title="Google Classroom", description="", color=0x94C973)
          embedVar.add_field(name="Link Below", value="[Click Here](YOUR_LINK)", inline=False)
          embedVar.set_thumbnail(url="https://media.discordapp.net/attachments/900360306310676540/939030971062313061/202-2022004_flexible-schedule-icon-v1-flexible-schedule-icon-hd-removebg-preview.png")
          embedVar.set_image(url="https://logos-world.net/wp-content/uploads/2021/08/Google-Classroom-Logo-2014-2016.png")
          await message.channel.send(embed=embedVar)

 ###-------------------------------help------------------------------------------------------### 
    elif message.content.startswith('-help'):
          embedVar = discord.Embed(title="Commands:", description="", color=0x94C973)
      
          embedVar.add_field(name="ㅤ", value="SCHEDULE BOT", inline=False)
          embedVar.add_field(name="ㅤㅤ-mon to -sun", value="ㅤㅤDisplay class schedule from Monday to Sunday", inline=False)
          embedVar.add_field(name="ㅤㅤ-gclass", value="ㅤㅤDisplay google classroom ", inline=False)
      
          embedVar.add_field(name="ㅤ", value="CRYPTO BOT", inline=False)
          embedVar.add_field(name="ㅤㅤaxs", value="ㅤㅤDisplay the value of AXS", inline=False)
          embedVar.add_field(name="ㅤㅤslp", value="ㅤㅤDisplay the value of Smooth Love Potion", inline=False)
          embedVar.add_field(name="ㅤㅤeth", value="ㅤㅤDisplay the value of Ethereum", inline=False)
          embedVar.add_field(name="ㅤㅤbtc", value="ㅤㅤDisplay the value of Bitcoin", inline=False)
          embedVar.add_field(name="ㅤㅤbcoin", value="ㅤㅤDisplay the value of Bomber Coin", inline=False)
      
          embedVar.add_field(name="ㅤ", value="WEATHER BOT", inline=False)
          embedVar.add_field(name="ㅤㅤw.alitagtag", value="ㅤㅤDisplay the weather temperature of Alitagtag", inline=False)
          embedVar.add_field(name="ㅤㅤw.cuenca", value="ㅤㅤDisplay the weather temperature of Alitagtag", inline=False)
          embedVar.add_field(name="ㅤㅤw.lipa", value="ㅤㅤDisplay the weather temperature of Alitagtag", inline=False)
      
          embedVar.add_field(name="ㅤ", value="MUSIC BOT", inline=False)
          embedVar.add_field(name="ㅤㅤ!join", value="ㅤㅤJoins a voice channel", inline=False)
          embedVar.add_field(name="ㅤㅤ!play", value="ㅤㅤPlay a song", inline=False)
          embedVar.add_field(name="ㅤㅤ!stream", value="ㅤㅤSame as play(but doesn't pre-download)", inline=False)
          embedVar.add_field(name="ㅤㅤ!stop", value="ㅤㅤDisconnect the bot from voice channel", inline=False)

          embedVar.add_field(name="ㅤ", value="JOKES BOT", inline=False)
          embedVar.add_field(name="ㅤㅤjokes.pls", value="ㅤㅤDisplay random jokes", inline=False)
          embedVar.add_field(name="ㅤㅤdark.jokes", value="ㅤㅤDisplay random dark jokes", inline=False)
          embedVar.add_field(name="ㅤㅤinsult.me", value="ㅤㅤInsults you :D", inline=False)
      
          embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/877724467177062454/950019246447030334/Presentation2-removebg-preview.png")
          await message.channel.send(embed=embedVar)
 ###-------------------------------help------------------------------------------------------### 
    elif message.content.startswith('-lloyd'):
          embedVar = discord.Embed(title="", description="[ADD TO SERVER](YOUR_LINK)", color=0x94C973)
          embedVar.set_image(url="https://cdn.discordapp.com/attachments/877724467177062454/949460326045343815/unknown-removebg-preview.png")
          embedVar.set_author(name="Lloyd #8284", icon_url="https://cdn.discordapp.com/attachments/877724467177062454/949460326045343815/unknown-removebg-preview.png")
          await message.channel.send(embed=embedVar)
      
    elif message.content.startswith('-robolamb'):
          embedVar = discord.Embed(title="", description="[ADD TO SERVER](YOUR_LINK)", color=0x94C973)
          embedVar.set_author(name="Robolamb #8284", icon_url="https://cdn.discordapp.com/attachments/877724467177062454/949455991555113050/Presentation2-removebg-preview.png")
          embedVar.set_image(url="https://cdn.discordapp.com/attachments/877724467177062454/949455991555113050/Presentation2-removebg-preview.png")
          await message.channel.send(embed=embedVar)
    else:
      return

keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
