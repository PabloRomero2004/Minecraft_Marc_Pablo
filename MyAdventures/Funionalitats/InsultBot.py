import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import mcpi.minecraft as Minecraft
import mcpi.block as block

# Connect to the Minecraft game  
mc = Minecraft.Minecraft.create()

insults=["saboc", "no vals un fuckin duro", "Algun dia jugaras en los ulls oberts", "tens menos habilitat que nepe, i es dir molt...",
         "vaia ascla", "Osti xec, no val ni un duro lo paio...", "Onso", "Sol de veuret jugar he agafat clamidia"]

class InsultBot(Bot):
    def perform(self):
        count=0
        while True:
            chatEvent = mc.events.pollChatPosts()
            for mensaje in chatEvent:
                if mensaje.message == "insultam":
                    mc.postToChat(insults[count])

                    count += 1
                    count = count % len(insults)


         
    