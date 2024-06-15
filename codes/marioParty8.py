# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/21/2024
# License: MIT
# ============================================

def getBlueSpaceCodeEight(amount, amountDec):
    return f'''
MP8 - Blue Spaces Give {amountDec} Coins
2045ADE8 38A00003
0445ADE8 38A0{amount}
E0000000 80008000
2045ADEC 38C00003
0445ADEC 38C0{amount}
E0000000 80008000
20465EFC 38A00003
04465EFC 38A0{amount}
E0000000 80008000
20465F00 38C00003
04465F00 38C0{amount}
E0000000 80008000
2045F82C 38A00003
0445F82C 38A0{amount}
E0000000 80008000
2045F830 38C00003
0445F830 38C0{amount}
E0000000 80008000
20482308 38A00003
04482308 38A0{amount}
E0000000 80008000
204940AC 38C00003
044940AC 38C0{amount}
E0000000 80008000
2045D290 38A00003
0445D290 38A0{amount}
E0000000 80008000
2045D294 38C00003
0445D294 38C0{amount}
E0000000 80008000
20462BC4 38A00003
04462BC4 38A0{amount}
E0000000 80008000
20462BC8 38C00003
04462BC8 38C0{amount}
E0000000 80008000
'''

def getRedSpaceCodeEight(amount, amountDec):
    return f'''
MP8 - Red Spaces Take Away {amountDec} Coins
2045B124 38A0FFFD
0445B124 38A0{amount}
E0000000 80008000
2045B128 38C0FFFD
0445B128 38C0{amount}
E0000000 80008000
20466238 38A0FFFD
04466238 38A0{amount}
E0000000 80008000
2046623C 38C0FFFD
0446623C 38C0{amount}
E0000000 80008000
2045FB68 38A0FFFD
0445FB68 38A0{amount}
E0000000 80008000
2045FB6C 38C0FFFD
0445FB6C 38C0{amount}
E0000000 80008000
20482644 38A0FFFD
04482644 38A0{amount}
E0000000 80008000
20482648 38C0FFFD
04482648 38C0{amount}
E0000000 80008000
2045D5CC 38A0FFFD
0445D5CC 38A0{amount}
E0000000 80008000
2045D5D0 38C0FFFD
0445D5D0 38C0{amount}
E0000000 80008000
20462F00 38A0FFFD
04462F00 38A0{amount}
E0000000 80008000
20462F04 38C0FFFD
04462F04 38C0{amount}
E0000000 80008000
'''

def getMinigameCodeEight(amount, amountDec):
    return f'''
MP8 - Minigames Award {amountDec} Coins
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
2822832A FF00000A
0222832A 0000{amount}
E0000000 80008000
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
28228442 FF00000A
02228442 0000{amount}
E0000000 80008000
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
2822855A FF00000A
0222855A 0000{amount}
E0000000 80008000
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
28228672 FF00000A
02228672 0000{amount}
E0000000 80008000
'''

def getStarSpaceCodeEight(amount, negAmount, amountDec):
    return f'''
MP8 - Stars Cost {amountDec} Coins
203C5380 38600014
043C5380 3860{amount}
E0000000 80008000
203F2DB8 2C03000A
043F2DB8 2C03{amount}
E0000000 80008000
203F2EC4 38A0FFF6
043F2EC4 38A0{negAmount}
E0000000 80008000
203D146C 38A0FFEC
043D146C 38A0{negAmount}
E0000000 80008000
203D1470 38C0FFEC
043D1470 38C0{negAmount}
E0000000 80008000
203D1368 2C030014
043D1368 2C03{amount}
E0000000 80008000
48000000 800030C8
DE000000 80008180
30013078 9421F8B0
D2013078 00000009
8083000C 80840070
38A00067 3CC08023
1C840118 7CC62214
38C682F8 A8E60026
2C07{amount} 40800014
B0A60010 B0A60012
B0A60014 4E800020
38E7{negAmount} B0E60026
9421F8B0 00000000
E0000000 80008000
'''

def getMinigameReplacement82(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP8 - Minigame Replacement: {gameUno} ➜ {gameDos}
282287CC 000000{hexUno}
022287CC 000000{hexDos}
E0000000 80008000
'''

def getBitsizeCode8(value, amountDec):
    return f'''
MP8 - Bitsize Candy Gives {amountDec} Coins per Space
2052B658 38A00003
0452B658 38A0{value}
E0000000 80008000
2052B65C 38C00003
0452B65C 38C0{value}
E0000000 80008000
205367B4 38A00003
045367B4 38A0{value}
E0000000 80008000
205367B8 38C00003
045367B8 38C0{value}
E0000000 80008000
2055245C 38A00003
0455245C 38A0{value}
E0000000 80008000
20552460 38C00003
04552460 38C0{value}
E0000000 80008000
20530070 38A00003
04530070 38A0{value}
E0000000 80008000
20530074 38C00003
04530074 38C0{value}
E0000000 80008000
2052DA34 38A00003
0452DA34 38A0{value}
E0000000 80008000
2052DA38 38C00003
0452DA38 38C0{value}
E0000000 80008000
20532E2C 38A00003
04532E2C 38A0{value}
E0000000 80008000
20532E30 38C00003
04532E30 38C0{value}
E0000000 80008000
'''

def hotelMaxInvest(value, valueDec):
    return f'''
MP8 - Invest Up To {valueDec} in Hotels
203CB930 2C000064
043CB930 2C00{value}
043CB950 2C00{value}
043CBBE4 2C00{value}
043CBD6C 2C00{value}
043CE480 2C00{value}
043CE52C 2C00{value}
043CE564 2C00{value}
043CE5B0 2C00{value}
043CE9F8 2C00{value}
043CEAB0 2C00{value}
043D2F7C 2C00{value}
043D34B4 2C00{value}
043D254C 2C1D{value}
E2000001 80008000
'''

def getBowloCode8(value, amountDec):
    return f'''
MP8 - Bowlo Candy Gives {amountDec} Coins Per Player Bowled
205173E4 3800000A
205173E4 3800{value}
E0000000 80008000
20522540 3800000A
20522540 3800{value}
E0000000 80008000
2053E1E8 3800000A
2053E1E8 3800{value}
E0000000 80008000
2051BDFC 3800000A
2051BDFC 3800{value}
E0000000 80008000
205197BC 3800000A
205197BC 3800{value}
E0000000 80008000
2051EBB4 3800000A
2051EBB4 3800{value}
E0000000 80008000
'''

def getVampireCode8(value, amountDec):
    return f'''
MP8 - Vampire Candy Gives {amountDec} Despite Roulette
282CD222 00000010
C24C4028 00000002
3880{value} 909F052C
60000000 00000000
E0000000 80008000
282CD222 00000011
C24CF170 00000002
3880{value} 909F052C
60000000 00000000
E0000000 80008000
282CD222 00000012
C24EAEEC 00000002
3880{value} 909F052C
60000000 00000000
E0000000 80008000
282CD222 00000013
C24CF170 00000002
3880{value} 909F052C
60000000 00000000
E0000000 80008000
282CD222 00000014
C24C8ADC 00000002
3880{value} 909F052C
60000000 00000000
E0000000 80008000
282CD222 00000015
C24CB7E0 00000002
3880{value} 909F052C
60000000 00000000
E0000000 80008000
'''

def getCandyCodeDK(oneW, twoP, twoW, threeP, threeW, fourP, fourW, fiveP, fiveW, sixP, sixW, sevenP, sevenW, eightP, eightW, nineP, nineW, tenP, tenW, elevenP, elevenW, twelveP, twelveW, thirteenP, thirteenW, fourteenP, fourteenW):
    return f'''
202CD220 00000010
42000000 90000000
20725868 0000000F
4A000000 90000080
66000008 00000000
E2000001 80008000
20725828 0000000F
4A000000 90000040
66000004 00000000
E2000001 80008000
42000000 90000000
207257E8 0000000F
4A000000 90000000
147257E8 000000{twoP}
147209E8 000000{twoP}
147251E8 000000{threeP}
147252A8 000000{threeP}
147227E8 000000{fourP}
147228A8 000000{fourP}
147221E8 000000{fiveP}
147221E8 000000{fiveP}
147222A8 000000{sixP}
14724BE8 000000{sixP}
14721BE8 000000{sevenP}
14721CA8 000000{sevenP}
14722EA8 000000{eightP}
14722DE8 000000{eightP}
147240A8 000000{nineP}
14723FE8 000000{nineP}
147216A8 000000{tenP}
147215E8 000000{tenP}
147245E8 000000{elevenP}
147246A8 000000{elevenP}
14723AA8 000000{thirteenP}
147239E8 000000{thirteenP}
147234A8 000000{fourteenP}
147210A8 000000{twelveP}
E0000000 80008000
42000000 90000000
20710C14 0000001E
4A000000 90000080
66000008 00000000
E2000001 80008000
20710BD4 0000001E
4A000000 90000040
66000004 00000000
E2000001 80008000
42000000 90000000
20710B94 0000001E
4A000000 90000000
14710B94 000000{twoW}
14710B98 000000{twoW}
14710BA4 000000{threeW}
14710BA8 000000{threeW}
14710BB4 000000{sevenW}
14710BB8 000000{sevenW}
14710BC4 000000{nineW}
14710BC8 000000{nineW}
14710BD4 000000{tenW}
14710BD8 000000{tenW}
14710BE4 000000{elevenW}
14710BE8 000000{elevenW}
14710BF4 000000{fourteenW}
14710BF8 000000{fourteenW}
14710C04 000000{sixW}
14710C08 000000{sixW}
14710C14 000000{fourW}
14710C18 000000{fourW}
14710C24 000000{fiveW}
14710C28 000000{fiveW}
14710C34 000000{eightW}
14710C38 000000{eightW}
14710C44 000000{thirteenW}
14710C48 000000{thirteenW}
14710C54 000000{twelveW}
14710C58 000000{twelveW}
E0000000 80008000
42000000 90000000
20720704 0000000A
4A000000 90000080
66000008 00000000
E2000001 80008000
207206C4 0000000A
4A000000 90000040
66000004 00000000
E2000001 80008000
42000000 90000000
20720684 0000000A
4A000000 90000000
14720684 000000{oneW}
14720688 000000{oneW}
1472068C 000000{oneW}
14720690 000000{oneW}
1472069C 000000{twoW}
147206A0 000000{twoW}
147206A4 000000{twoW}
147206A8 000000{twoW}
147206B4 000000{threeW}
147206B8 000000{threeW}
147206BC 000000{threeW}
147206C0 000000{threeW}
147206CC 000000{sevenW}
147206D0 000000{sevenW}
147206D4 000000{sevenW}
147206D8 000000{sevenW}
147206E4 000000{nineW}
147206E8 000000{nineW}
147206EC 000000{nineW}
147206F0 000000{nineW}
147206FC 000000{tenW}
14720700 000000{tenW}
14720704 000000{tenW}
14720708 000000{tenW}
14720714 000000{elevenW}
14720718 000000{elevenW}
1472071C 000000{elevenW}
14720720 000000{elevenW}
1472072C 000000{fourteenW}
14720730 000000{fourteenW}
14720734 000000{fourteenW}
14720738 000000{fourteenW}
14720744 000000{sixW}
14720748 000000{sixW}
1472074C 000000{sixW}
14720750 000000{sixW}
1472075C 000000{fourW}
14720760 000000{fourW}
14720764 000000{fourW}
14720768 000000{fourW}
14720774 000000{fiveW}
14720778 000000{fiveW}
1472077C 000000{fiveW}
14720780 000000{fiveW}
1472078C 000000{eightW}
14720790 000000{eightW}
14720794 000000{eightW}
14720798 000000{eightW}
147207A4 000000{thirteenW}
147207A8 000000{thirteenW}
147207AC 000000{thirteenW}
147207B0 000000{thirteenW}
147207BC 000000{twelveW}
147207C0 000000{twelveW}
147207C4 000000{twelveW}
147207C8 000000{twelveW}
E0000000 80008000
'''

def getCandyCodeShyGuy(oneW, twoP, twoW, threeP, threeW, fourP, fourW, fiveP, fiveW, sixP, sixW, sevenP, sevenW, eightP, eightW, nineP, nineW, tenP, tenW, elevenP, elevenW, twelveP, twelveW, thirteenP, thirteenW, fourteenP, fourteenW):
    return f'''
202CD220 00000013
42000000 90000000
20726008 00000014
4A000000 90000080
66000008 00000000
E2000001 80008000
42000000 90000000
20725FC8 00000014
4A000000 90000040
66000004 00000000
E2000001 80008000
42000000 90000000
4A000000 90000000
20725F88 00000014
14725F88 000000{twoP}
14725EC8 000000{twoP}
14725808 000000{threeP}
147258C8 000000{threeP}
14722F88 000000{fourP}
14722EC8 000000{fourP}
14722988 000000{fiveP}
147228C8 000000{fiveP}
14723588 000000{sixP}
147234C8 000000{sixP}
147252C8 000000{sevenP}
14721608 000000{sevenP}
14722388 000000{eightP}
14722208 000000{eightP}
14724C08 000000{nineP}
14724B48 000000{nineP}
14724848 000000{tenP}
14724608 000000{tenP}
14723F48 000000{elevenP}
14723AC8 000000{elevenP}
14721D88 000000{thirteenP}
14721CC8 000000{thirteenP}
14723B88 000000{fourteenP}
14723AC8 000000{fourteenP}
14721788 000000{twelveP}
147216C8 000000{twelveP}
E0000000 80008000
42000000 90000000
20710B94 0000001E
4A000000 90000080
66000008 00000000
E2000001 80008000
20710B54 0000001E
4A000000 90000040
66000004 00000000
E2000001 80008000
42000000 90000000
20710B14 0000001E
4A000000 90000000
14710B04 000000{oneW}
14710B08 000000{oneW}
14710B14 000000{twoW}
14710B18 000000{twoW}
14710B24 000000{threeW}
14710B28 000000{threeW}
14710B34 000000{sevenW}
14710B38 000000{sevenW}
14710B44 000000{nineW}
14710B48 000000{nineW}
14710B54 000000{tenW}
14710B58 000000{tenW}
14710B64 000000{elevenW}
14710B68 000000{elevenW}
14710B74 000000{fourteenW}
14710B78 000000{fourteenW}
14710B84 000000{sixW}
14710B88 000000{sixW}
14710B94 000000{fourW}
14710B98 000000{fourW}
14710BA4 000000{fiveW}
14710BA8 000000{fiveW}
14710BB4 000000{eightW}
14710BB8 000000{eightW}
14710BC4 000000{thirteenW}
14710BC8 000000{thirteenW}
14710BD4 000000{twelveW}
14710BD8 000000{twelveW}
E0000000 80008000
42000000 90000000
20720DE4 00000014
4A000000 90000080
66000008 00000000
E2000001 80008000
20720DA4 00000014
4A000000 90000040
66000004 00000000
E2000001 80008000
42000000 90000000
20720D64 00000014
4A000000 90000000
14720D64 000000{oneW}
14720D68 000000{oneW}
14720D6C 000000{oneW}
14720D70 000000{oneW}
14720D7C 000000{twoW}
14720D80 000000{twoW}
14720D84 000000{twoW}
14720D88 000000{twoW}
14720D94 000000{threeW}
14720D98 000000{threeW}
14720D9C 000000{threeW}
14720DA0 000000{threeW}
14720DAC 000000{sevenW}
14720DB0 000000{sevenW}
14720DB4 000000{sevenW}
14720DB8 000000{sevenW}
14720DC4 000000{nineW}
14720DC8 000000{nineW}
14720DCC 000000{nineW}
14720DD0 000000{nineW}
14720DDC 000000{tenW}
14720DE0 000000{tenW}
14720DE4 000000{tenW}
14720DE8 000000{tenW}
14720DF4 000000{elevenW}
14720DF8 000000{elevenW}
14720DFC 000000{elevenW}
14720E00 000000{elevenW}
14720E0C 000000{fourteenW}
14720E10 000000{fourteenW}
14720E14 000000{fourteenW}
14720E18 000000{fourteenW}
14720E24 000000{sixW}
14720E28 000000{sixW}
14720E2C 000000{sixW}
14720E30 000000{sixW}
14720E3C 000000{fourW}
14720E40 000000{fourW}
14720E44 000000{fourW}
14720E48 000000{fourW}
14720E54 000000{fiveW}
14720E58 000000{fiveW}
14720E5C 000000{fiveW}
14720E60 000000{fiveW}
14720E6C 000000{eightW}
14720E70 000000{eightW}
14720E74 000000{eightW}
14720E78 000000{eightW}
14720E84 000000{thirteenW}
14720E88 000000{thirteenW}
14720E8C 000000{thirteenW}
14720E90 000000{thirteenW}
14720E9C 000000{twelveW}
14720EA0 000000{twelveW}
14720EA4 000000{twelveW}
14720EA8 000000{twelveW}
E0000000 80008000
'''