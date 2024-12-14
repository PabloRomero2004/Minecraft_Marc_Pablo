import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import mcpi.minecraft as Minecraft
import mcpi.block as block

class Bot:
    def _init_(self, name):
        self.name = name

    def perform(self):
        return "Parent class does not implement this method"
    
    