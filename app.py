import os
from flask import Flask
import threading
import discord
from discord.ext import commands

# เริ่มต้น Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Discord Bot is Running!"

# สร้างการทำงานของ Discord Bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# ฟังก์ชันที่รัน Discord Bot ใน background
def run_discord_bot():
    bot.run(os.getenv("TOKEN"))

# ฟังก์ชันที่จะรัน Flask และ Discord Bot พร้อมกัน
def run_flask():
    port = int(os.environ.get("PORT", 5000))  # พอร์ตที่ Render จะกำหนดให้
    app.run(host="0.0.0.0", port=port)

# ใช้ threading เพื่อให้ Flask กับ Discord Bot รันพร้อมกัน
if __name__ == "__main__":
    # เริ่มต้น Discord Bot ใน background
    discord_thread = threading.Thread(target=run_discord_bot)
    discord_thread.start()
    
    # เริ่มต้น Flask
    run_flask()
