import os
import discord
from discord.ext import commands
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# --------------------- Event: On Ready ---------------------
@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.listening, name="ลองใช้คำสั่งต่าง ๆ ดูสิ (ทดสอบ)")
    await bot.change_presence(activity=activity)

    try:
        synced = await bot.tree.sync()  # Global sync
        print(f"✅ Synced {len(synced)} global commands")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

    print(f"บอท {bot.user} พร้อมใช้งานแล้ว!")

# --------------------- Slash Commands ---------------------

@bot.tree.command(name='ตอบกวนตีน', description="คำสั่งตอบกลับกวนตีน")
async def ตอบกวนตีน(interaction: discord.Interaction):
    responses = [
        "อะไรนะ? คุณพูดอะไรออกมา?",
        "ทำไมทำหน้าแบบนั้น? หัวเราะเหรอ?",
        "แหม สุดยอดไปเลยนะครับ!",
        "อ้าว! เป็นอะไรไปเนี่ย หัวเราะอะไรอยู่?",
        "นี่มันอะไรกัน คุณทำอะไรให้ขำได้ขนาดนี้?",
    ]
    await interaction.response.send_message(random.choice(responses))

@bot.tree.command(name='ตอบแบบสุภาพ', description="คำสั่งตอบกลับแบบสุภาพ")
async def ตอบแบบสุภาพ(interaction: discord.Interaction):
    responses = [
        "ขอบคุณมากครับ/ค่ะ สำหรับคำแนะนำที่ดี",
        "ขอโทษที่ทำให้คุณไม่สะดวกใจครับ/ค่ะ",
        "ยินดีที่ได้รู้จักนะครับ/ค่ะ",
        "ขอขอบพระคุณสำหรับการสนทนาครับ/ค่ะ",
        "ผม/ฉันจะพยายามทำให้ดีที่สุดครับ/ค่ะ",
    ]
    await interaction.response.send_message(random.choice(responses))

@bot.tree.command(name='แสดงอารมณ์ตอนนี้', description="คำสั่งแสดงอารมณ์ในตอนนี้")
async def แสดงอารมณ์(interaction: discord.Interaction):
    emotions = [
        "รู้สึกดีมากวันนี้! 😊",
        "อารมณ์แป๊บ ๆ นะ ยังไม่รู้จะบอกใครยังไงดี 😅",
        "รู้สึกสงบและเงียบสงบ",
        "รู้สึกคึกคักและพร้อมลุย!",
        "รู้สึกเหนื่อยและต้องการพักผ่อน 💤",
    ]
    await interaction.response.send_message(random.choice(emotions))

@bot.tree.command(name='คำด่าเจ็บๆ', description="คำสั่งด่าเจ็บๆ")
async def คำด่าเจ็บๆ(interaction: discord.Interaction):
    insults = [
        "ทำไมคุณยังหายใจอยู่ละ?",
        "บางทีก็อยากให้คุณหยุดคิดเลยนะ",
        "เก่งนัก ก็ลองทำดูสิ",
        "คุณรู้สึกตัวมั้ยว่าพูดอะไรออกมา?",
        "อย่าให้พูดเลย ถ้าไม่อยากร้องไห้",
    ]
    await interaction.response.send_message(random.choice(insults))

@bot.tree.command(name='คำชมปลอมๆ', description="คำสั่งชมปลอมๆ")
async def คำชมปลอมๆ(interaction: discord.Interaction):
    fake_compliments = [
        "อืม ดูเหมือนจะดี แต่ไม่แน่ใจนะ",
        "คุณเก่งนะ... ในเรื่องของความพยายาม",
        "คุณมีพรสวรรค์นะ... ถ้ามองข้ามหลาย ๆ อย่าง",
        "อืม ไม่รู้เหมือนกันว่ามันดีแค่ไหน แต่ก็ดูโอเค",
        "คุณทำได้ดีนะ... อาจจะไม่เก่งที่สุดแต่ก็ยังโอเค",
    ]
    await interaction.response.send_message(random.choice(fake_compliments))

@bot.tree.command(name='ให้กำลังใจ', description="คำสั่งให้กำลังใจ")
async def ให้กำลังใจ(interaction: discord.Interaction):
    encouragements = [
        "คุณทำได้ดีมากแล้ว อย่าหยุดพยายาม!",
        "เชื่อในตัวเอง สู้ไปเรื่อย ๆ นะ!",
        "คุณมีความสามารถในตัวเองมากกว่าที่คิด!",
        "ไม่มีอะไรที่คุณทำไม่ได้ ถ้าคุณเชื่อมั่นในตัวเอง!",
        "วันหนึ่งคุณจะเห็นผลของความพยายาม!",
    ]
    await interaction.response.send_message(random.choice(encouragements))

@bot.tree.command(name='แซะ', description="คำสั่งแซะ")
async def แซะ(interaction: discord.Interaction):
    teasing = [
        "ขอโทษนะ แต่ก็ไม่คิดว่าคุณจะทำได้ดีขนาดนี้",
        "หากคุณทำได้แบบนี้ จะเป็นความสำเร็จในชีวิตคุณเลยเหรอ?",
        "มีอะไรที่ทำได้ดีกว่านี้มั้ย?",
        "เฮ้! รู้มั้ยว่าฉันคิดว่าคุณน่าจะทำได้มากกว่านี้",
        "โอ้... ดีเลย ถ้าคิดว่าแค่พอใจแล้วก็โอเค",
    ]
    await interaction.response.send_message(random.choice(teasing))

@bot.tree.command(name='ตั้งชื่อ', description="คำสั่งตั้งชื่อแบบสุ่ม")
async def ตั้งชื่อ(interaction: discord.Interaction):
    names = [
        "วิเวียน", "มิวะ", "โคโค่", "นัตตี้", "บีบี", "ซาซ่า", "เอเรียล", "คีรา", "ลิซซี่", "บลูม",
        "ปอปี้", "แฟรงกี้", "โมจิ", "พุดดิ้ง", "พิงกี้", "มาม่า", "ฟุ้งฟิ้ง", "เจลลี่", "มากิ", "ยูยุ",
    ]
    await interaction.response.send_message(random.choice(names))

@bot.tree.command(name='เป่ายิงฉุบ', description="คำสั่งเล่นเป่ายิงฉุบ")
async def เป่ายิงฉุบ(interaction: discord.Interaction, choice: str):
    choice = choice.lower()
    options = ['ค้อน', 'กระดาษ', 'กรรไกร']

    if choice not in options:
        await interaction.response.send_message("❌ โปรดเลือก: ค้อน, กระดาษ หรือ กรรไกร")
        return

    bot_choice = random.choice(options)
    if choice == bot_choice:
        result = "เสมอ!"
    elif (choice == 'ค้อน' and bot_choice == 'กรรไกร') or \
         (choice == 'กระดาษ' and bot_choice == 'ค้อน') or \
         (choice == 'กรรไกร' and bot_choice == 'กระดาษ'):
        result = "คุณชนะ!"
    else:
        result = "คุณแพ้!"

    await interaction.response.send_message(f"บอทเลือก: {bot_choice} - {result}")

@bot.tree.command(name='ทายเหรียญ', description="สุ่มหัวหรือก้อย")
async def ทายเหรียญ(interaction: discord.Interaction):
    result = random.choice(["หัว", "ก้อย"])
    await interaction.response.send_message(f"ผลการทอยเหรียญคือ: {result} 🪙")

# --------------------- Run Bot ---------------------
bot.run(TOKEN)
