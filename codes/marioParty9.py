# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 7/3/2024
# License: MIT
# ============================================

def getMinigameReplacement9(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP9 - Minigame Replacement: {gameUno} -> {gameDos}
42000000 81000000
20758730 {hexUno}00
04758730 {hexDos}00
E0000000 80008000
'''