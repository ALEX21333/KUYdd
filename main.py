import interactions
import os 
import platform
import random
import requests
from interactions import *
from keepAlive import keep_alive

token = os.environ['ICE_SHOP'] 

ICE_SHOP = interactions.Client(token=token, intents=Intents.ALL) # ห้ามแก้เด็ดขาด !!!

ch_id = "1230940770652127365" # ใส่ ID ช่องที่จะให้ซื้อยศ

phone = "0630102037" # ใส่เบอร์มือถือที่ใช้สมัครบัญชี ทรูมันนี่วอเลท

log_id = "1230940924624764948" # ใส่ไอดีช่องประวัติการซื้อ

# ห้ามนำไปแจกต่อ เจอปรับ 10 เท่าของราคา src ที่ขาย !!!

# ชื่อร้าน หรือชื่อ อื่นๆ...
m_title = "VIPTJ SHOP"

# ลิ้งค์รูปเล็ก By Ice Shop
m_tn = "https://media.discordapp.net/attachments/1230918596272590981/1230920080011952170/background_removed.png?ex=663512a8&is=66229da8&hm=1bab3b7e08a5b1cd554a2f9e82940e6352e5b14f98a6b706db5003bab0249d5e&=&format=webp&quality=lossless"

# ลิ้งค์รููปใหญ่ By Ice Shop
m_img = "https://media.discordapp.net/attachments/1026009843569528902/1026366243294416917/truemoney-wallet-768x426.png?ex=662f310d&is=661cbc0d&hm=6843d0395cf6bb125550050f0b17d633803e288bfea28a9088261958adc92d8e&=&format=webp&quality=lossless" 

role_01 = "1230885677802197093" # ใส่ไอดียศ By Ice Shop
role01_name = "VIPBOY" # ชื่อยศ By Ice Shop
role_01p = "70.00"  # ราคายศ By Ice Shop
 
role_02 = "1230885755006484601" # ใส่ไอดียศ By Ice Shop
role02_name = "VIPCUTE" # ชื่อยศ By Ice Shop
role_02p = "60.00" # ราคายศ By Ice Shop

role_03 = "1230885807393476729" # ใส่ไอดียศ By Ice Shop
role03_name = "Super VIP" # ชื่อยศ By Ice Shop
role_03p = "110.00" # ราคายศ By Ice Shop

@interactions.listen()
async def on_ready():

    ch = await ICE_SHOP.fetch_channel(channel_id=ch_id)
    main_embed = interactions.Embed(title=f"**{m_title} ซื้อยศผ่านบอทอัตโนมัติ**", description="", color=0x7300ff)
    main_embed.set_image(m_img)
    main_embed.set_footer("© 2023 ICE SHOP All rights reserved", 'https://cdn.discordapp.com/attachments/1101236843900588043/1107341553971769415/IMG_1032.jpg')



    components: list[ActionRow] = [
        ActionRow(
            Button(
                style=ButtonStyle.GREEN,
                custom_id="price_cb",
                label="ดูราคายศ", emoji="<a:7y4badgesrole:1135479816280358984>"
            ),
            Button(
                style=ButtonStyle.BLUE,
                custom_id="all_cb",
                label="ดูวิธีใช้", emoji="<a:Book_rules:1135484365372149810>"
            )
        ),
        ActionRow(
            StringSelectMenu(
                [
                    interactions.StringSelectOption(emoji="", label="VIPBOY", description="70 BAHT", value="70"),
                    interactions.StringSelectOption(emoji="", label="VIPCUTE", description="60 BAHT", value="0"),
                    interactions.StringSelectOption(emoji="", label="Super VIP", description="110 BAHT", value="110"),
                ],
                custom_id="buy_cb",
                placeholder="🛒 ซื้อยศกดตรงนี้",
                min_values=1,
                max_values=1,
        )

        )
    ]


    await ch.send(embeds=main_embed, components=components)# ห้ามนำไปแจกต่อ เจอปรับ 10 เท่าของราคา src ที่ขาย !!!


    if platform.system() == 'Windows':

        os.system(f'cls & title สำเร็จ {m_title} กำลังออนไลน์ | บอทขายยศ By Ice Shop')
        
        print(" ")

        print(f'''\x1b[38;5;92m
  ██ ▄████▄ ▓█████      ██████   ██░ ██  ▒█████   ██▓███  
▒▓██▒██▀ ▀█ ▓█   ▀    ▒██    ▒ ▒▓██░ ██ ▒██▒  ██▒▓██░  ██ 
░▒██▒▓█    ▄▒███      ░ ▓██▄   ░▒██▀▀██ ▒██░  ██▒▓██░ ██▓▒
 ░██▒▓▓▄ ▄██▒▓█  ▄      ▒   ██▒ ░▓█ ░██ ▒██   ██░▒██▄█▓▒ ▒
 ░██▒ ▓███▀ ░▒████    ▒██████▒▒ ░▓█▒░██▓░ ████▓▒░▒██▒ ░  ░
 ░▓ ░ ░▒ ▒  ░░ ▒░     ▒ ▒▓▒ ▒ ░  ▒ ░░▒░▒░ ▒░▒░▒░ ▒▓▒░ ░  ░
  ▒   ░  ▒   ░ ░      ░ ░▒  ░    ▒ ░▒░ ░  ░ ▒ ▒░ ░▒ ░     
  ▒ ░          ░      ░  ░  ░    ░  ░░ ░░ ░ ░ ▒  ░░       
  ░ ░ ░        ░            ░    ░  ░  ░    ░ ░           
  
\x1b[38;5;21mสำเร็จ {m_title} กำลังออนไลน์ | บอทขายยศ By Ice Shop

\x1b[38;5;10m.gg/pyKyCxc2cM

© 2023 Zxaicas_ice All rights reserved

ห้ามนำไปแจกต่อ เจอปรับ 10 เท่าของราคา src ที่ขาย !!!


''')

        print(" ")
    
    else:

        os.system("clear")

        print(" ")

        print(f'''\x1b[38;5;92m     
  ██ ▄████▄ ▓█████      ██████   ██░ ██  ▒█████   ██▓███  
▒▓██▒██▀ ▀█ ▓█   ▀    ▒██    ▒ ▒▓██░ ██ ▒██▒  ██▒▓██░  ██ 
░▒██▒▓█    ▄▒███      ░ ▓██▄   ░▒██▀▀██ ▒██░  ██▒▓██░ ██▓▒
 ░██▒▓▓▄ ▄██▒▓█  ▄      ▒   ██▒ ░▓█ ░██ ▒██   ██░▒██▄█▓▒ ▒
 ░██▒ ▓███▀ ░▒████    ▒██████▒▒ ░▓█▒░██▓░ ████▓▒░▒██▒ ░  ░
 ░▓ ░ ░▒ ▒  ░░ ▒░     ▒ ▒▓▒ ▒ ░  ▒ ░░▒░▒░ ▒░▒░▒░ ▒▓▒░ ░  ░
  ▒   ░  ▒   ░ ░      ░ ░▒  ░    ▒ ░▒░ ░  ░ ▒ ▒░ ░▒ ░     
  ▒ ░          ░      ░  ░  ░    ░  ░░ ░░ ░ ░ ▒  ░░       
  ░ ░ ░        ░            ░    ░  ░  ░    ░ ░           
  
\x1b[38;5;27mสำเร็จ {m_title} กำลังออนไลน์ | บอทขายยศ By Ice Shop

\x1b[38;5;10m.gg/pyKyCxc2cM

© 2023 Zxaicas_ice All rights reserved

ห้ามนำไปแจกต่อ เจอปรับ 10 เท่าของราคา src ที่ขาย !!!''')




        print(" ")
      
@component_callback("buy_cb")
async def buy_cb(ctx: ComponentContext):
    rolebuy = ctx.values[0]

    topup_modal = Modal(
        ShortText(
            label='''ซื้อยศอัตโนมัติ 24h ซื้อแล้วได้ยศ 100%''',
            custom_id="giftLink",
            required=True,
            placeholder="🧧 ใส่ลิ้งค์ซองอั่งเปา",
            max_length=80,
        ),
        title="🧧 ใส่จำนวนเงินในซองตามราคาของยศ",
    )
    await ctx.send_modal(modal=topup_modal)

    modal_ctx: ModalContext = await ctx.bot.wait_for_modal(topup_modal)

    giftLink = modal_ctx.responses['giftLink']

    print("YEAH")

    auth = requests.get(f"https://zamex-hub.000webhostapp.com/index.php?phone={phone}&link={giftLink}")

    gotji = auth.json()# ห้ามนำไปแจกต่อ เจอปรับ 10 เท่าของราคา src ที่ขาย !!!

    if gotji["status"] == "SUCCESS":

        if gotji["amount"] == role_01p:

            role_01s = interactions.Embed(title=f"**{m_title} ประวัติการทำรายการ**", description="_ _", color=0x33FF99)

            role_01s.add_field(name="ข้อมูลถูกต้อง", value=f"_ _\n> <a:7y4badgesrole:1135479816280358984> **ยศที่ซื้อ <@&{role_01}> **")

            await modal_ctx.send(embeds=role_01s, ephemeral=True)

            log_01 = await ICE_SHOP.fetch_channel(channel_id=log_id)

            log_01eb = interactions.Embed(title=f"**{m_title} ประวัติการทำรายการ**", description="_ _", color=0x33FF99)

            log_01eb.add_field(name="ข้อมูลถูกต้อง", value=f"_ _\n> <a:7y4badgesrole:1135479816280358984> **ยศที่ซื้อ <@&{role_01}> **")

            await log_01.send(f"<@{ctx.author.id}>", embeds=log_01eb)

        elif gotji["amount"] == role_02p:

            role_02s = interactions.Embed(title=f"**{m_title} ประวัติการทำรายการ**", description="_ _", color=0x33FF99)

            role_02s.add_field(name="ข้อมูลถูกต้อง", value=f"_ _\n> <a:7y4badgesrole:1135479816280358984> **ยศที่ซื้อ <@&{role_02}> **")

            await modal_ctx.send(embeds=role_02s, ephemeral=True)

            log_02 = await ICE_SHOP.fetch_channel(channel_id=log_id)

            log_02eb = interactions.Embed(title=f"**{m_title} ประวัติการทำรายการ**", description="_ _", color=0x33FF99)

            log_02eb.add_field(name="ข้อมูลถูกต้อง", value=f"_ _\n> <a:7y4badgesrole:1135479816280358984> **ยศที่ซื้อ <@&{role_02}> **")

            await log_02.send(f"<@{ctx.author.id}>", embeds=log_02eb)

        elif gotji["amount"] == role_03p:

            role_03s = interactions.Embed(title=f"**{m_title} ประวัติการทำรายการ**", description="_ _", color=0x33FF99)

            role_03s.add_field(name="ข้อมูลถูกต้อง", value=f"_ _\n> <a:7y4badgesrole:1135479816280358984> **ยศที่ซื้อ <@&{role_03}> **")

            await modal_ctx.send(embeds=role_03s, ephemeral=True)

            log_03 = await ICE_SHOP.fetch_channel(channel_id=log_id)

            log_03eb = interactions.Embed(title=f"**{m_title} ประวัติการทำรายการ**", description="_ _", color=0x33FF99)

            log_03eb.add_field(name="ข้อมูลถูกต้อง", value=f"_ _\n> <a:7y4badgesrole:1135479816280358984> **ยศที่ซื้อ <@&{role_03}> **")

            await log_03.send(f"<@{ctx.author.id}>", embeds=log_03eb)

        elif gotji["amount"] == role_04p:

            role_04s = interactions.Embed(title=f"**{m_title} ประวัติการทำรายการ**", description="_ _", color=0x33FF99)

            role_04s.add_field(name="ข้อมูลถูกต้อง", value=f"_ _\n> <a:7y4badgesrole:1135479816280358984> **ยศที่ซื้อ <@&{role_04}> **")

            await modal_ctx.send(embeds=role_04s, ephemeral=True)

            log_04 = await ICE_SHOP.fetch_channel(channel_id=log_id)

            log_04eb = interactions.Embed(title=f"**{m_title} ประวัติการทำรายการ**", description="_ _", color=0x33FF99)

            log_04eb.add_field(name="ข้อมูลถูกต้อง", value=f"_ _\n> <a:7y4badgesrole:1135479816280358984> **ยศที่ซื้อ <@&{role_04}> **")

            await log_04.send(f"<@{ctx.author.id}>", embeds=log_04eb)

    else:

        print("Fail")

        fail = interactions.Embed(title=f"**{m_title} ประวัติการทำรายการ**", description="_ _", color=0xFF0033)

        fail.add_field(name="ข้อมูลผิดผลาด", value="_ _\n> **<a:50_:1135481101914214431>  ซื้อยศไม่สำเร็จโปรดลองอีกครั้ง**")

        await modal_ctx.send(embeds=fail, ephemeral=True)

        fail_x = await ICE_SHOP.fetch_channel(channel_id=log_id)

        faileb = interactions.Embed(title=f"**{m_title} ประวัติการทำรายการ**", description="_ _", color=0xFF0033)

        faileb.add_field(name="ข้อมูลผิดผลาด", value="_ _\n> **<a:50_:1135481101914214431>  ซื้อยศไม่สำเร็จโปรดลองอีกครั้ง**")

        await fail_x.send(f"<@{ctx.author.id}>", embeds=faileb)

@component_callback("price_cb")
async def price_cb(ctx: ComponentContext):
    role_all = interactions.Embed(title=f"**{m_title} ยศทั้งหมด**", description=" ", color=0x7300ff)
    role_all.set_image ("https://cdn.discordapp.com/attachments/1101236843900588043/1112192033189265498/1ADF94D2-6F6D-44FD-B1D0-9C208ECA113A.gif") # ลิ้งค์รููปใหญ่ By Ice Shop
    role_all.add_field(name="•• ━━━━━ ••●•• ━━━━━ ••", value=" ")
    role_all.add_field(name=f"> ยศ {role01_name}", value=f"_ _\n<@&{role_01}> **\n_ _\n`🛒` : `{role_01p}` ฿**")
    role_all.add_field(name="•• ━━━━━ ••●•• ━━━━━ ••", value=" ")
    role_all.add_field(name=f"> ยศ {role02_name}", value=f"_ _\n<@&{role_02}> **\n_ _\n`🛒` : `{role_02p}` ฿**")
    role_all.add_field(name="•• ━━━━━ ••●•• ━━━━━ ••", value=" ")
    role_all.add_field(name=f"> ยศ {role03_name}", value=f"_ _\n<@&{role_03}> **\n_ _\n`🛒` : `{role_03p}` ฿**")
    role_all.add_field(name="•• ━━━━━ ••●•• ━━━━━ ••", value=" ")
    role_all.set_footer("© 2023 ICE SHOP All rights reserved", 'https://cdn.discordapp.com/attachments/1101236843900588043/1107341553971769415/IMG_1032.jpg')

    await ctx.send(embeds=role_all, ephemeral=True)# ห้ามนำไปแจกต่อ เจอปรับ 10 เท่าของราคา src ที่ขาย !!!

@component_callback("all_cb")
async def all_cb(ctx: ComponentContext):
    role_all = interactions.Embed(title=f'''**{m_title} วิธีใช้ <:truewallet_new:1135481231056838686>**''', description=" ", color=0x7300ff)
    role_all.set_image ("https://cdn.discordapp.com/attachments/1101114027951788063/1130552015966187621/aungpao_truewallet_01.jpg")
    role_all.add_field(name="**•• ━━━━━ ••●•• ━━━━━ ••**", value=" ")
    role_all.add_field(name="> **วิธีซื้อยศ**", value='''
    \n**กดไปที่คำว่า ซื้อยศกดตรงนี้ เลือกยศที่จะซื้อ แล้วนำลิ้งค์ซองอั่งเปาไปวางในช่องแล้วกดส่ง
    \n•• ━━━━━ ••●•• ━━━━━ •• \n**''')
    role_all.add_field(name="> **คำเตือน! <a:50_:1135481101914214431> **", value='''
    \n**ใส่จำนวนเงินให้ตรงกับราคายศที่จะซื้อ
    \n•• ━━━━━ ••●•• ━━━━━ •• **\n''')

    role_all.set_footer("© 2023 ICE SHOP All rights reserved", 'https://cdn.discordapp.com/attachments/1101236843900588043/1107341553971769415/IMG_1032.jpg')

    await ctx.send(embeds=role_all, ephemeral=True) # ห้ามนำไปแจกต่อ เจอปรับ 10 เท่าของราคา src ที่ขาย !!!


keep_alive()

ICE_SHOP.start(token)

# By Ice Shop 

# ใช้ไม่ได้เปิด Tickets มาเลยคับ 

# .gg/pyKyCxc2cM

# © 2023 Zxaicas_ice All rights reserved

# ห้ามนำไปแจกต่อ เจอปรับ 10 เท่าของราคา src ที่ขาย !!!