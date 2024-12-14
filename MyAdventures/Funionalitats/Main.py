from InsultBot import InsultBot
from TNTBot import TNTBot
from BotManager import BotManager
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import mcpi.minecraft as Minecraft
import mcpi.block as block



mc = Minecraft.Minecraft.create()

insult_bot  = InsultBot()
tnt_bot = TNTBot()
bot_manager = BotManager(insult_bot)

while True:
    chatEvent = mc.events.pollChatPosts()
    for mensaje in chatEvent:
        if mensaje.message == "change to insult bot":
            bot_manager.notify()
            bot_manager.set_bot_type(insult_bot)
        elif mensaje.message == "change to tnt bot":
            bot_manager.set_bot_type(tnt_bot)
        elif mensaje.message == "perform":
            bot_manager.perform()
        elif mensaje.message == "hola":
            mc.postToChat("hola que tal")
        
                

                