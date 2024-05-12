# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/9/2024
# License: MIT
# ============================================

def getRedSpaceCodeFour(amount, amountDec):
    return f'''
MP4 - Red Spaces Take Away {amountDec} Coins
C207FD5C 00000001
3BC0{amount} 00000000
'''

def getBlueSpaceCodeFour(amount, amountDec):
    return f'''
MP4 - Blue Spaces Give {amountDec} Coins
C207FBC4 00000001
3BC0{amount} 00000000
'''

def getMinigameCodeFour(amount, amountDec):
    return f'''
MP4 - Minigames Award {amountDec} Coins
2A18FD2C 00000003
2A18FD2C 00000007
2A18FD2C 00000015
2A18FD2C 0000001D
2A18FD2C 00000025
2A18FD2C 00000026
2A18FD2C 00000027
2A18FD2C 00000028
2A18FD2C 00000036
2818FC60 0000000A
0218FC60 0000{amount}
E0000000 80008000
2A18FD2C 00000003
2A18FD2C 00000007
2A18FD2C 00000015
2A18FD2C 0000001D
2A18FD2C 00000025
2A18FD2C 00000026
2A18FD2C 00000027
2A18FD2C 00000028
2A18FD2C 00000036
2818FC90 0000000A
0218FC90 0000{amount}
E0000000 80008000
2A18FD2C 00000003
2A18FD2C 00000007
2A18FD2C 00000015
2A18FD2C 0000001D
2A18FD2C 00000025
2A18FD2C 00000026
2A18FD2C 00000027
2A18FD2C 00000028
2A18FD2C 00000036
2818FCC0 0000000A
0218FCC0 0000{amount}
E0000000 80008000
2A18FD2C 00000003
2A18FD2C 00000007
2A18FD2C 00000015
2A18FD2C 0000001D
2A18FD2C 00000025
2A18FD2C 00000026
2A18FD2C 00000027
2A18FD2C 00000028
2A18FD2C 00000036
2818FCF0 0000000A
0218FCF0 0000{amount}
E0000000 80008000
'''

def getBooSpaceStarFour(amount, amountDec):
    return f'''
MP4 - Stars Cost {amountDec} Coins when stealing at the Boo House
040A5F30 2C1E{amount}
'''

def getBooSpaceCoinsFour(amount, amountDec):
    return f'''
MP4 - Coins Cost {amountDec} Coins when stealing at the Boo House
040A61DC 2C1E{amount}
040A517C 2C03{amount}
'''

def getStarSpaceCodeFour(amount, amountDec):
    return f'''
MP4 - Stars Cost {amountDec} Coins
040843CC 2C03{amount}
04084590 2C03{amount}
040845CC 2C03{amount}
0408473C 2C1C{amount}
'''

def getSquishCodeFour(amount, amountDec):
    return f'''
MP4 - Mega Mushroom Steals {amountDec} Coins
0406BE90 3800{amountDec}
'''

def getLotterySpaceCodeFour(amount, amountDec):
    return f'''
MP4 - Lottery Costs {amountDec} Coins
0407BD20 2C1E{amount}
'''

def getMinigameReplacement4(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP4 - Minigame Replacement: {gameUno} ➜ {gameDos}
2818FD2C 000000{hexUno}
0218FD2C 000000{hexDos}
E2000001 80008000
'''

def getItemModsFour(oneP, oneW, twoP, twoW, threeP, threeW, fourP, fourW, fiveP, fiveW, sixP, sixW, sevenP, sevenW, eightP, eightW, nineP, nineW, tenP, tenW, elevenP, elevenW, twelveP, twelveW, thirteenP, thirteenW, fourteenP, fourteenW, minCoins):
    return f'''
MP4 - Item Modifer
C2083878 0000001E
48000045 60000000
00{oneW}0000 00{twoW}0001  
00{threeW}0002 00{fourW}0003
00{fiveW}0004 00{sixW}0005
00{sevenW}0006 00{eightW}0007
00{nineW}0008 00{tenW}0009
00{elevenW}000A 00{twelveW}000B
00{thirteenW}000C 00{fourteenW}000D
00000000 7CE802A6
38E70004 38600000
38800000 2C030038
41820014 7CA71A2E
7C842A14 38630004
4BFFFFEC 3CA08005
60A5FB40 7CA903A6
7C832378 4E800421
38800000 38A00000
2C050034 41820024
7CC72A2E 7C661850
2C030000 40A00008
48000010 38840001
38A50004 4BFFFFDC
1C840004 38840002
7C87222E 3CA0817F
60A5FFF0 90850000
2C040008 41800008
38840001 3CA00007
60A5006D 7C642A14
38800000 38A00000
38A00000 00000000
C2083028 00000041
480001B1 0B596F75
10676F74 1061101E
054D696E 69104D75
7368726F 6F6D1E08
85FF000B 596F7510
676F7410 61101E05
4D656761 104D7573
68726F6F 6D1E0885
FF000B59 6F751067
6F741061 101E0553
75706572 104D696E
69104D75 7368726F
6F6D1E08 85FF000B
596F7510 676F7410
61101E05 53757065
72104D65 6761104D
75736872 6F6F6D1E
0885FF00 0B596F75
10676F74 1061101E
054D696E 69104D65
67611048 616D6D65
721E0885 FF000B59
6F751067 6F741061
101E0557 61727010
50697065 1E0885FF
000B596F 7510676F
74106110 1E055377
61701043 6172641E
0885FF00 0B596F75
10676F74 1061101E
05537061 726B7910
53746963 6B65721E
0885FF00 0B596F75
10676F74 1061101E
05476164 646C6967
68741E08 85FF000B
596F7510 676F7410
61101E05 43686F6D
70104361 6C6C1E08
85FF000B 596F7510
676F7410 61101E05
426F7773 65721053
7569741E 0885FF00
0B596F75 10676F74
1061101E 04437279
7374616C 1042616C
6C1E0885 FF000B59
6F751067 6F741061
101E074D 61676963
104C616D 701E0885
FF000B59 6F751067
6F741061 6E101E07
4974656D 10426167
1E0885FF 00000000
7C6802A6 3C80817F
6084FFF0 80840000
38A00000 38C00000
7CE518AE 2C070000
40A20020 7C062000
41820020 7C632A14
38630001 38C60001
38A00000 4BFFFFDC
38A50001 4BFFFFD4
7C641B78 38600000
60000000 00000000
C2083CF0 00000002
3C80817F 6084FFF0
80840000 00000000
00139D2C 000000{oneP} 
00139D2D 000000{twoP} 
00139D2E 000000{threeP} 
00139D2F 000000{fourP}
00139D30 000000{fiveP} 
00139D31 000000{sixP} 
00139D32 000000{sevenP} 
00139D33 000000{eightP} 
00139D34 000000{nineP} 
00139D35 000000{tenP} 
00139D36 000000{elevenP} 
00139D37 000000{twelveP} 
00139D38 000000{thirteenP}
00139D39 000000{fourteenP}
02139DB2 0000{oneW}{twoW}
02139DB4 0000{threeW}{fourW}
02139DB6 0000{fiveW}{sixW}
02139DB8 0000{sevenW}{eightW}
02139DBA 0000{nineW}{tenW}
02139DBC 0000{elevenW}{twelveW}
02139DBE 0000{thirteenW}{fourteenW}
02139DC0 0000{oneW}{twoW}
02139DC2 0000{threeW}{fourW}
02139DC4 0000{fiveW}{sixW}
02139DC6 0000{sevenW}{eightW}
02139DC8 0000{nineW}{tenW}
02139DCA 0000{elevenW}{twelveW}
02139DCC 0000{thirteenW}{fourteenW}
02139DCE 0000{oneW}{twoW}
02139DD0 0000{threeW}{fourW}
02139DD2 0000{fiveW}{sixW}
02139DD4 0000{sevenW}{eightW}
02139DD6 0000{nineW}{tenW}
02139DD8 0000{elevenW}{twelveW}
02139DDA 0000{thirteenW}{fourteenW}
02139DDC 0000{oneW}{twoW}
02139DDE 0000{threeW}{fourW} 
02139DE0 0000{fiveW}{sixW}
02139DE2 0000{sevenW}{eightW} 
02139DE4 0000{nineW}{tenW}
02139DE6 0000{elevenW}{twelveW}
02139DE8 0000{thirteenW}{fourteenW}
02139DEA 0000{oneW}{twoW}
02139DEC 0000{threeW}{fourW}
02139DEE 0000{fiveW}{sixW} 
02139DF0 0000{sevenW}{eightW}
02139DF2 0000{nineW}{tenW}
02139DF4 0000{elevenW}{twelveW}
02139DF6 0000{thirteenW}{fourteenW}
02139DF8 0000{oneW}{twoW}
02139DFA 0000{threeW}{fourW}
02139DFC 0000{fiveW}{sixW}
02139DFE 0000{sevenW}{eightW}
02139E00 0000{nineW}{tenW}
02139E02 0000{elevenW}{twelveW}
02139E04 0000{thirteenW}{fourteenW}
02139E06 0000{oneW}{twoW}
02139E08 0000{threeW}{fourW}
02139E0A 0000{fiveW}{sixW}
02139E0c 0000{sevenW}{eightW}
02139E0E 0000{nineW}{tenW}
02139E10 0000{elevenW}{twelveW}
02139E12 0000{thirteenW}{fourteenW}
02139E14 0000{oneW}{twoW}
02139E16 0000{threeW}{fourW}
02139E18 0000{fiveW}{sixW}
02139E1A 0000{sevenW}{eightW}
02139E1C 0000{nineW}{tenW}
02139E1E 0000{elevenW}{twelveW}
02139E20 0000{thirteenW}{fourteenW}
02139E22 0000{oneW}{twoW}
02139E24 0000{threeW}{fourW}
02139E26 0000{fiveW}{sixW}
02139E28 0000{sevenW}{eightW}
02139E2A 0000{nineW}{tenW}
02139E2C 0000{elevenW}{twelveW}
02139E2E 0000{thirteenW}{fourteenW}
02139E30 0000{oneW}{twoW}
02139E32 0000{threeW}{fourW}
02139E34 0000{fiveW}{sixW}
02139E36 0000{sevenW}{eightW}
02139E38 0000{nineW}{tenW}
02139E3A 0000{elevenW}{twelveW}
02139E3C 0000{thirteenW}{fourteenW}
C2077D84 00000001
2C03{minCoins} 00000000
'''

def getInitialItemsFour(one, two, three, oneItem, twoItem, threeItem):
    return f'''
MP4 - Start with {oneItem}, {twoItem}, and {threeItem}
C2063AE0 00000013
7C83032E 2C040007
40820080 3DC08018
61CEFCFC 89CE0000
2C0E0001 4082006C
3DC08018 61CEFC3D
39E000{one} 99EE0000
39E000{two} 99EE0001
39E000{three} 99EE0002
39E000{one} 99EE0030
39E000{two} 99EE0031
39E000{three} 99EE0032
39E000{one} 99EE0060
39E000{two} 99EE0061
39E000{three} 99EE0062
39E000{one} 99EE0090
39E000{two} 99EE0091
39E000{three} 99EE0092
39C00000 39E00000
60000000 00000000
'''

def getSpaceReplaceFour1(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP4 - Replace {spaceName} with {spaceName2} (Slot A)
C2076A08 00000003
A01F0028 280000{spaceHex1}
4082000C 380000{spaceHex2}
B01F0028 00000000
'''

def getSpaceReplaceFour2(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP4 - Replace {spaceName} with {spaceName2} (Slot B)
C2076A0C 00000003
280000{spaceHex1} 4082000C
380000{spaceHex2} B01F0028
28000000 00000000
'''

def getLotteryRewards4(lotteryPrizeA, lotteryPrizeB, lotteryPrizeC, lotteryPrizeD, lotteryPrizeALabel, lotteryPrizeBLabel, lotteryPrizeCLabel, lotteryPrizeDLabel):
    return f'''
MP4 - Lottery 1st is {lotteryPrizeALabel} - 2nd is {lotteryPrizeBLabel} - 3rd is {lotteryPrizeCLabel} or {lotteryPrizeDLabel}
0407EA58 3B80{lotteryPrizeA}
0407EA60 3B80{lotteryPrizeB}
021D5678 0000{lotteryPrizeC}{lotteryPrizeD}
'''

def getOtherCodesFour(code):
    if code == "30Hz":
        return '''
041D3B00 40000000
041D3B04 00000002
04035480 38600001
C200592C 00000009
3C808000 6084D01C
7C8903A6 4E800421
3C808000 60845B4C
7C8903A6 4E800421
38800000 908D8688
908D868C 38600001
3C808000 6084D01C
7C8903A6 4E800421
60000000 00000000'''
    if code == "DigtPress":
        return '''
c2086774 00000002
70000020 2c000020
60000000 00000000
c2073c7c 00000002
735a0020 281a0020
60000000 00000000'''
    if code == "AdvanceText":
        return '''
04044A90 60000000'''
    if code == "CPUItems":
        return '''
C20719F0 00000004
7C000774 2C1F000D
40800008 4800000C
3800FFF3 7C00FA14
60000000 00000000
C2071A10 00000001
2C1F001B 00000000
C2071A4C 00000004
7FBD0774 2C1F000D
40800008 4800000C
3BA0FFF3 7FBDFA14
60000000 00000000
04139B88 80071CBC
04139B94 80071CBC'''
    if code == "DisableAdv":
        return '''
20446468 4182FF60
04446468 4BFFFF60
E2000001 80008000'''
    if code == "TxtDisplay":
        return '''
0404a560 38000000'''
    if code == "Boot":
        return '''
04056168 38607FFF'''
    if code == "BSpeed":
        return '''
04066dd8 38c0000d
20432574 2c1c002d
04432570 3b9c0002
e2000001 80008000
040786a0 c02281f0
0406e314 c02281f0
0408FB64 3860001E
0408FC08 3860001E
0408FCAC 3860001E
0408FD50 3860001E
0408FA78 3BDE0002
20432574 2C1C002D
04432570 3B9C0002
E2000001 80008000
0408F4D4 38600005
0408F53C 3860000F
0408F0E4 3BFF0002
0408F154 3BFF0002'''
    if code == "TSpam":
        return '''
04061d5c 60000000
04061eb8 60000000'''
    if code == "TxtDisplay":
        return '''
04044808 38600000'''
    if code == "ShowCtrl":
        return '''
C203e9b4 00000002
807f0050 906d0000
38600000 00000000
c2031b88 0000000c
3860012c 3880000a
38a0002d 38c00028
38e000ff 90ed0004
38ed0004 3d008000
6108b150 7d0903a6
4e800421 3860012c
3880000a 3ca08013
38a5db52 80cd0000
38c60001 c02283c0
3ce08000 60e7aff4
7ce903a6 4e800421
57a0083c 00000000
C20B1184 00000007
88CD8488 38C60001
C02281F0 38600138
38800010 3CA08012
60A5DB53 3CE08000
60E7AFF4 7CE903A6
4E800421 880D8488
60000000 00000000'''
    if code == "UnlockAll":
        return '''
040310BC 3880FFFF
20446064 4082002C
04445FA4 38000001
0444605C 38000001
E2000001 80008000
2044E6DC 40820028
0444E578 38000001
0444E6D4 38A00001
E2000001 80008000
2044D25C 5400E7FE
0444D258 380000FF
0444D198 380000FF
E2000001 80008000
2043EDF8 4082002C
0443EDE8 38A000FF
0443ED28 380000FF
E2000001 80008000
20449684 4082002C
04449674 38A000FF
044495B4 380000FF
E2000001 80008000
20441D98 2C000001
04441D94 38000001
044396FC 38000001
E2000001 80008000'''
    if code == "BooRed":
        return '''
0018fd08 00000000'''
    if code == "BridgeGnarly":
        return '''
2043801c 4182004c
04438294 38000002
e2000001 80008000'''
    if code == "FreeTaxi":
        return '''
2046DA84 386002F6
0446DA80 48000038
0446E414 2C070000
0446E4A4 2C050000
0446E4C4 38800000
E2000001 80008000'''
    if code == "NeverBack":
        return '''
20432D5C 3860000A
04432D60 38600009
E2000001 80008000'''
    if code == "BananaJct":
        return '''
2043030c 48000088
044326fc 4e800020
e2000001 80008000'''
    if code == "TeacupJct":
        return '''
20435308 80010008
044352f4 4e800020
e2000001 80008000'''
    if code == "BowserBag":
        return '''
C208B1EC 00000001
2C1E000E 00000000'''
    if code == "DoubleDice":
        return '''
C2085CEC 00000005
3DC0801D 61CE3F44
89CE0000 38000001
2C0E000A 41820008
48000008 38000002
39C00000 00000000'''
    if code == "DoubleTurns":
        return '''
C205BEF8 00000004
2C000032 4182000C
7C000214 48000008
38000063 98030005
60000000 00000000'''
    if code == "AlwaysKK":
        return '''
04097784 38600028'''
    if code == "AlwaysBowser":
        return '''
04097784 38600014'''
    if code == "DoubleTurns":
        return '''
C208DA0C 00000004
2C000032 4182000C
7C000214 48000008
38000063 98030005
60000000 00000000'''
    if code == "EventAcc":
        return '''
04075ff0 38600000
040a50a4 38600000
04077c50 38600000
0407a868 38600000
04083fe4 60000000
04076148 60000000
204302f8 2c030002
044302fc 60000000
04434aa4 60000000
e2000001 80008000
204302e0 2c030002
044302e4 4800000c
e2000001 80008000
204303f0 2c030002
044303f4 60000000
0443049c 60000000
e2000001 80008000
204302a8 2c030002
044302ac 4800000c
e2000001 80008000
20430338 2c030002
0443033c 4800000c
e2000001 80008000
C2076014 00000002
38000000 28000000
60000000 00000000'''
    if code == "ItemDeletion":
        return '''
c208d424 00000002
987d0001 3c608000
93a30010 00000000
c208a07c 0000001f
9421ffe0 7c0802a6
9001001c 90a10018
3c608018 6063fcf8
8883000a 1c840030
3c608018 6063fc38
7c632214 88830004
5485083c 3c80801d
60843ad0 7c842a14
88840000 80a10018
2c040020 41820008
48000090 3ca08000
60a50010 80a50000
88a50001 2c050000
41820018 2c050001
41820038 2c050002
41820050 48000064
3ca00000 60a500ff
88c30006 88e30007
98c30005 98e30006
98a30007 3ca00000
60a50200 4800003c
88c30007 98c30006
3cc00000 60c600ff
98c30007 3ca00000
60a50200 4800001c
3cc00000 60c600ff
98c30007 3ca00000
60a50200 48000004
8001001c 94210020
7c0803a6 7cbd2b78
60000000 00000000'''
    if code == "ForceL5":
        return '''
0405C180 60000000
0405C2C8 60000000
'''
    if code == "Mini2Dice":
        return '''
00085D33 00000002'''
    if code == "MiniPipeSize":
        return '''
04066348 60000000
04064ed0 60000000
04065114 60000000'''
    if code == "MiniRoll":
        return '''
04085D74 3800000A'''
    if code == "SMiniRoll":
        return '''
00085D3F 00000003'''
    if code == "AfterBag":
        return '''
201D3F44 0D000001
001D3F44 000000FF
E2000001 80008000'''
    if code == "AfterItems":
        return '''
001D3F44 000000FF'''
    if code == "x2 Coins":
        return '''
040FB87C 38A00000
040FB8EC 3A600000'''
    if code == "Free Stars":
        return '''
040AD074 38600003
040AD078 987E0001'''
    if code == "Red Spaces are Fortune Spaces":
        return '''
040ACDC0 3BA00003
040AD074 38600002
040AD078 987E0001'''
    if code == "Red Spaces are Bowser Spaces":
        return '''
040AD074 38600001
040AD078 987E0001'''
    if code == "Disabled":
        return '''
0405C180 48000048
0405C2C8 48000020'''
    if code == "Domination":
        return '''
C203220C 0000001F
A0610008 2C03000F
408200E8 807F0004
4800002D 7C8802A6
A0A40000 7CA00734
2C00FFFF 41820054
80C40002 7CA32A14
90C50000 38840006
4BFFFFE0 4E800021
00200000 4C60016C
38600528 24BC281F
04B0393C 280004B0
27C0281F 012C2608
281F04B4 2664281F
04B42850 380304B0
29A83804 04B0FFFF
807F0004 48000031
7C8802A6 A0A40000
38840002 A0C40000
7CC00734 2C00FFFF
41820058 7CC33214
90A60000 38840002
4BFFFFE4 4E800021
39908490 849884A0
84A884B0 84B884E0
84E884F0 84F88500
85088530 85388550
85588560 856885E0
85E88630 86388640
864886F0 86F88730
87388B10 8B18FFFF
38600000 00000000'''
    if code == "HoopsE":
        return '''
20434274 3800000A
04434260 38800000
0443427C 38A00000
0443425C 60000000
E2000001 80008000'''