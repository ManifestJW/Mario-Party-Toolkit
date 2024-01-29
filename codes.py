# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 1/23/2024
# License: MIT
# ============================================

def getBlueSpaceCodeOne(amount, switch):
    return f'''
MP1 - Blue Spaces Give ONEBLUE Coins: ONEBLUESWITCH
81057D80 3408
81057D82 000{switch}
81057D84 1100
81057D86 0003
81057D88 3410
81057D8A {amount}
81057D8C 5440
81057D8E 0001
81057D90 0010
81057D92 8040
0407FBE0 3BC0
'''

def getRedSpaceCodeOne(amount, switch):
    return f'''
MP1 - Red Spaces Take Away ONEBLUE Coins: ONEREDSWITCH
81057DD8 3408
81057DDA 000{switch}
81057DDC 1100
81057DDE 0003
81057DE0 3410
81057DE2 {amount}
81057DE4 5440
81057DE6 0001
81057DE8 0010
81057DEA 8040
'''

def getBlueSpaceCodeTwo(amount, switch):
    return f'''
MP2 - Blue Spaces Give TWOBLUE Coins: TWOBLUESWITCH
81066300 3408
81066302 000{switch}
81066304 1100
81066306 0003
81066308 3410
8106630A {amount}
8106630C 5440
8106630E 0001
81066310 0010
81066312 8040
'''

def getRedSpaceCodeTwo(amount, switch):
    return f'''
MP2 - Blue Spaces Take Away TWOBLUE Coins: TWOREDSWITCH
8106634C 3408
8106634E 000{switch}
81066350 1100
81066352 0003
81066354 3410
81066356 {amount}
81066358 5440
8106635A 0001
8106635C 0010
8106635E 8040
'''

def getBlueSpaceCodeThree(amount, switch):
    return f'''
MP3 - Blue Spaces Give THREEBLUE Coins: THREEBLUESWITCH
810FE284 3408
810FE286 000{switch}
810FE288 1100
810FE28A 0003
810FE28C 3410
810FE28E {amount}
810FE290 5440
810FE292 0001
810FE294 0010
810FE296 8040
'''

def getRedSpaceCodeThree(amount, switch):
    return f'''
MP3 - Red Spaces Take Away THREEBLUE Coins: THREEREDSWITCH
810FE2C0 3408
810FE2C2 000{switch}
810FE2C4 1100
810FE2C6 0003
810FE2C8 3410
810FE2CA {amount}
810FE2CC 5440
810FE2CE 0001
810FE2D0 0010
810FE2D2 8040
'''

def getRedSpaceCodeFour(amount):
    return f'''
MP4 - Red Spaces Take Away FOURRED Coins
0407FD74 60000000
0407FD78 3BC0{amount}
'''


def getBlueSpaceCodeFour(amount):
    return f'''
MP4 - Blue Spaces Give FOURBLUE Coins
0407FBDC 60000000
0407FBE0 3BC0{amount}
'''

def getBooSpaceCodeFour(amount):
    return f'''
MP4 - Stars Cost FOURBOO Coins when stealing at the Boo House
040A5F30 2C1E{amount}
'''

def getStarSpaceCodeFour(amount):
    return f'''
MP4 - Stars Cost FOURSTAR Coins
040843CC 2C03{amount}
04084590 2C03{amount}
040845CC 2C03{amount}
0408473C 2C1C{amount}
'''

def getLotterySpaceCodeFour(amount):
    return f'''
MP4 - Lottery Costs FOURLOTTERY Coins
0407BD20 2C1E{amount}
'''

def getBlueSpaceCodeFive(amount):
    return f'''
MP5 - Blue Spaces Give FIVEBLUE Coins
040A9F5C 3880{amount}
'''

def getRedSpaceCodeFive(amount):
    return f'''
MP5 - Red Spaces Take Away FIVERED Coins
040AA160 3880{amount}
'''

def getStarSpaceCodeFive(amount, negAmount):
    return f'''
MP5 - Stars Cost FIVESTAR Coins
C20AFDB0 00000001
2C03{amount} 00000000
C20AFF9C 00000001
3880{negAmount} 00000000
'''


def getWigglerSpaceCodeFive(amount, negAmount):
    return f'''
MP5 - Stars Cost FIVEWIGGLER Coins from Wiggler
C20DB528 00000001
2C03{amount} 00000000
C20DBB40 00000001
3880{negAmount} 00000000
'''

def getChompSpaceCodeFive(amount, negAmount):
    return f'''
MP5 - Stars Cost FIVECHOMP Coins when stealing with Chain Chomp
C20F5F34 00000001
2C03{amount} 00000000
C20F630C 00000001
3880{negAmount} 00000000
'''

def getBlueSpaceCodeSix(amount):
    return f'''
MP6 - Blue Spaces Give SIXBLUE Coins
0415F1E8 3880{amount}
'''

def getRedSpaceCodeSix(amount):
    return f'''
MP6 - Red Spaces Take Away SIXRED Coins
0415F278 3880{amount}
'''

def getCharacterSpaceCodeSix(amount):
    return f'''
MP6 - Character Spaces Give SIXCHARACTER Coins
0415F230 3880{amount}
'''

def getStarSpaceCodeSix(amount, negAmount):
    return f'''
MP6 - Stars Cost SIXSTAR Coins
0418333C 2C03{amount}
0418342C 2C03{amount}
041834C4 2C03{amount}
044F0E28 2C03{amount}
0415F668 2C03{amount}
0415FA18 2C03{negAmount}
C2183590 00000002
3880{amount} 7C8400D0
60000000 00000000
28265B8A 00000014
00265B8B 0000{amount}
E2000001 80008000
'''


def getFaireSquareStarCodeSix(one, two, three, four):
    return f'''
MP6 - Stars Can Cost SIXONE, SIXTWO, SIXTHREE, or SIXFOUR During Faire Square's Nightime
04248064 0000{one}
04248068 0000{two}
04248070 0000{three}
04248074 0000{four}
04248D3C 0000{one}
04248D40 0000{two}
04248D48 0000{three}
04248D4C 0000{four}
204DDF60 465F6C00
044DDF74 0000{one}
044DDF78 0000{two}
044DDF80 0000{three}
044DDF84 0000{four}
E2000001 80008000
'''

def getPinkBooSpaceCodeSix(amount, negAmount):
    return f'''
MP6 - Stars Cost SIXBOO Coins when stealing with Pink Boo
C21B1FB4 00000001
2C04{amount} 00000000
C21B2634 00000001
3880{negAmount} 00000000
'''

def getBlueSpaceCodeSeven(amount):
    return f'''
MP7 - Blue Spaces Give SEVENBLUE Coins
04168578 60000000
0416857C 3880{amount}
'''

def getRedSpaceCodeSeven(amount):
    return f'''
MP7 - Red Spaces Take Away SEVENRED Coins
04168600 60000000
04168604 3880{amount}
'''

def getCharacterSpaceCodeSeven(amount):
    return f'''
MP7 - Character Spaces Give SEVENCHARACTER Coins
041685BC 60000000
041685C0 3880{amount}
'''

def getStarSpaceCodeSeven(amount):
    return f'''
MP7 - Stars Cost SEVENSTAR Coins
04188774 3B80{amount}
'''

def getStarSpaceCodeSevenLastFive(amount):
    return f'''
MP7 - Stars Cost SEVENSTLASTFIVE Coins During the Last 5 Turns Event
0418876C 3B80{amount}
'''

def getHammerBroSpaceCodeSeven(amount, negAmount, halfAmount):
    return f'''
MP7 - Hammer Bro Takes SEVENHAMMERBRO Coins
041A902C 3AC0{amount}
041A9A28 38A0{negAmount}
041A973C 38000000
041A9744 3800{halfAmount}
041A974C 38000000
041A9754 3800{halfAmount}
'''

def getZapSpaceCodeSeven(amount):
    return f'''
MP7 - Zap Takes SEVENZAP Coins
C21B652C 00000001
3880{amount} 00000000
'''

def getBlueSpaceCodeEight(amount):
    return f'''
MP8 - Blue Spaces Give EIGHTBLUE Coins
2046CB88 38A00003
0446CB88 38A0{amount}
E0000000 80008000
2046CB8C 38C00003
0446CB8C 38C0{amount}
E0000000 80008000
20477C9C 38A00003
04477C9C 38A0{amount}
E0000000 80008000
20477CA0 38C00003
04477CA0 38C0{amount}
E0000000 80008000
204715CC 38A00003
044715CC 38A0{amount}
E0000000 80008000
204715D0 38C00003
044715D0 38C0{amount}
E0000000 80008000
204940A8 38A00003
044940A8 38A0{amount}
E0000000 80008000
204940AC 38C00003
044940AC 38C0{amount}
E0000000 80008000
2046F030 38A00003
0446F030 38A0{amount}
E0000000 80008000
2046F034 38C00003
0446F034 38C0{amount}
E0000000 80008000
20474964 38A00003
04474964 38A0{amount}
E0000000 80008000
20474968 38C00003
04474968 38C0{amount}
E0000000 80008000
'''

def getRedSpaceCodeEight(amount):
    return f'''
MP8 - Red Spaces Take Away EIGHTRED Coins
2046CEC4 38A0FFFD
0446CEC4 38A0{amount}
E0000000 80008000
2046CEC8 38C0FFFD
0446CEC8 38C0{amount}
E0000000 80008000
20477FD8 38A0FFFD
04477FD8 38A0{amount}
E0000000 80008000
20477FDC 38C0FFFD
04477FDC 38C0{amount}
E0000000 80008000
20471908 38A0FFFD
04471908 38A0{amount}
E0000000 80008000
2047190C 38C0FFFD
0447190C 38C0{amount}
E0000000 80008000
204943E4 38A0FFFD
044943E4 38A0{amount}
E0000000 80008000
204943E8 38C0FFFD
044943E8 38C0{amount}
E0000000 80008000
2046F36C 38A0FFFD
0446F36C 38A0{amount}
E0000000 80008000
2046F370 38C0FFFD
0446F370 38C0{amount}
E0000000 80008000
20474CA0 38A0FFFD
04474CA0 38A0{amount}
E0000000 80008000
20474CA4 38C0FFFD
04474CA4 38C0{amount}
E0000000 80008000
'''

def getBlueSpaceCodeEightGC(amount):
    return f'''
MP8GC - Blue Spaces Give EIGHTBLUEGC Coins
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

def getRedSpaceCodeEightGC(amount):
    return f'''
MP8GC - Red Spaces Take Away EIGHTREDGC Coins
2045B124 38A0FFFD
0445B124 38A0{amount}
E0000000 80008000
2045B128 38C0FFFD
0445B128 38C0{amount}
E0000000 80008000
20477FD8 38A0FFFD
04477FD8 38A0{amount}
E0000000 80008000
20477FDC 38C0FFFD
04477FDC 38C0{amount}
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

def getStarSpaceCodeEight(amount, negAmount):
    return f'''
MP8 - Stars Cost EIGHTSTAR Coins
203D7120 38600014
043D7120 3860{amount}
E0000000 80008000
20404B58 2C03000A
04404B58 2C03{amount}
E0000000 80008000
20404C64 38A0FFF6
04404C64 38A0{negAmount}
E0000000 80008000
203E320C 38A0FFEC
043E320C 38A0{negAmount}
E0000000 80008000
203E3210 38C0FFEC
043E3210 38C0{negAmount}
E0000000 80008000
203E3108 2C030014
043E3108 2C03{amount}
E0000000 80008000
'''

def getStarSpaceCodeEightGC(amount, negAmount):
    return f'''
MP8 - Stars Cost EIGHTSTARGC Coins
203C5380 38600014
043C5380 3860{amount}
E0000000 80008000
203FFFAC 2C03000A
043FFFAC 2C03{amount}
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
'''

def getItemModsFour(oneP, oneW, twoP, twoW, threeP, threeW, fourP, fourW, fiveP, fiveW, sixP, sixW, sevenP, sevenW, eightP, eightW, nineP, nineW, tenP, tenW, elevenP, elevenW, twelveP, twelveW, thirteenP, thirteenW, fourteenP, fourteenW):
    return f'''
MP4 - Item Modifer
C2083724 0000001E
48000041 60000000
00{oneW}0000 {twoW}0001  
00{threeW}0002 {fourW}0003
00{fiveW}0004 {sixW}0005
00{sevenW}0006 {eightW}0007
00{nineW}0008 {tenW}0009
00{elevenW}000A {twelveW}000B
00{thirteenW}000C {fourteenW}000D
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
'''

def getOrbModsSeven(oneW, twoP, twoW, threeP, threeW, fourP, fourW, fiveP, fiveW, sixP, sixW, sevenP, sevenW, eightP, eightW, nineP, nineW, tenP, tenW, elevenP, elevenW, twelveP, twelveW, thirteenP, thirteenW, fourteenP, fourteenW, fifteenP, fifteenW, sixteenP, sixteenW, seventeenP, seventeenW, eighteenP, eighteenW, ninteenP, ninteenW, twentyP, twentyW, twentyOneP, twentyOneW, twentyTwoP, twentyTwoW, twentyThreeP, twentyThreeW, twentyFourP, twentyFourW, twentyFiveP, twentyFiveW, twentySixP, twentySixW, twentySevenP, twentySevenW, twentyEightP, twentyEightW, twentyNineP, twentyNineW):
    return f'''
MP7 - Orb Modifer
042EF588 00050505
042EF58C 05{oneW}{oneW}{oneW}
042EF590 {oneW}{oneW}{oneW}{oneW}
042EF594 {oneW}{oneW}0000
042EF598 01{twoP}{twoP}{twoP}
042EF59C {twoP}{twoW}{twoW}{twoW}
042EF5A0 {twoW}{twoW}{twoW}{twoW}
042EF5A4 {twoW}{twoW}0000
042EF5A8 02{threeP}{threeP}{threeP}
042EF5AC {threeP}{threeW}{threeW}{threeW}
042EF5B0 {threeW}{threeW}{threeW}{threeW}
042EF5B4 {threeW}{threeW}0000
042EF5B8 03{fourP}{fourP}{fourP}
042EF5BC {fourP}{fourW}{fourW}{fourW}
042EF5C0 {fourW}{fourW}{fourW}{fourW}
042EF5C4 {fourW}{fourW}0000
042EF5C8 04{fiveP}{fiveP}{fiveP}
042EF5CC {fiveP}{fiveW}{fiveW}{fiveW}
042EF5D0 {fiveW}{fiveW}{fiveW}{fiveW}
042EF5D4 {fiveW}{fiveW}0000
042EF5D8 05{sixP}{sixP}{sixP}
042EF5DC {sixP}{sixW}{sixW}{sixW}
042EF5E0 {sixW}{sixW}{sixW}{sixW}
042EF5E4 {sixW}{sixW}0000
042EF5E8 06{sevenP}{sevenP}{sevenP}
042EF5EC {sevenP}{sevenW}{sevenW}{sevenW}
042EF5F0 {sevenW}{sevenW}{sevenW}{sevenW}
042EF5F4 {sevenW}{sevenW}0000
042EF5F8 07{eightP}{eightP}{eightP}
042EF5FC {eightP}{eightW}{eightW}{eightW}
042EF600 {eightW}{eightW}{eightW}{eightW}
042EF604 {eightW}{eightW}0000
042EF608 0A{nineP}{nineP}{nineP}
042EF60C {nineP}{nineW}{nineW}{nineW}
042EF610 {nineW}{nineW}{nineW}{nineW}
042EF614 {nineW}{nineW}0000
042EF618 0B{tenP}{tenP}{tenP}
042EF61C {tenP}{tenW}{tenW}{tenW}
042EF620 {tenW}{tenW}{tenW}{tenW}
042EF624 {tenW}{tenW}0000
042EF628 0C{elevenP}{elevenP}{elevenP}
042EF62C {elevenP}{elevenW}{elevenW}{elevenW}
042EF630 {elevenW}{elevenW}{elevenW}{elevenW}
042EF634 {elevenW}{elevenW}0000
042EF638 0D{twelveP}{twelveP}{twelveP}
042EF63C {twelveP}{twelveW}{twelveW}{twelveW}
042EF640 {twelveW}{twelveW}{twelveW}{twelveW}
042EF644 {twelveW}{twelveW}0000
042EF648 0E{thirteenP}{thirteenP}{thirteenP}
042EF64C {thirteenP}{thirteenW}{thirteenW}{thirteenW}
042EF650 {thirteenW}{thirteenW}{thirteenW}{thirteenW}
042EF654 {thirteenW}{thirteenW}0000
042EF658 0F{fourteenP}{fourteenP}{fourteenP}
042EF65C {fourteenP}{fourteenW}{fourteenW}{fourteenW}
042EF660 {fourteenW}{fourteenW}{fourteenW}{fourteenW}
042EF664 {fourteenW}{fourteenW}0000
042EF668 10{fifteenP}{fifteenP}{fifteenP}
042EF66C {fifteenP}{fifteenW}{fifteenW}{fifteenW}
042EF670 {fifteenW}{fifteenW}{fifteenW}{fifteenW}
042EF674 {fifteenW}{fifteenW}0000
042EF678 11{sixteenP}{sixteenP}{sixteenP}
042EF67C {sixteenP}{sixteenW}{sixteenW}{sixteenW}
042EF680 {sixteenW}{sixteenW}{sixteenW}{sixteenW}
042EF684 {sixteenW}{sixteenW}0000
042EF688 14{seventeenP}{seventeenP}{seventeenP}
042EF68C {seventeenP}{seventeenW}{seventeenW}{seventeenW}
042EF690 {seventeenW}{seventeenW}{seventeenW}{seventeenW}
042EF694 {seventeenW}{seventeenW}0000
042EF698 15{eighteenP}{eighteenP}{eighteenP}
042EF69C {eighteenP}{eighteenW}{eighteenW}{eighteenW}
042EF6A0 {eighteenW}{eighteenW}{eighteenW}{eighteenW}
042EF6A4 {eighteenW}{eighteenW}0000
042EF6A8 16{ninteenP}{ninteenP}{ninteenP}
042EF6AC {ninteenP}{ninteenW}{ninteenW}{ninteenW}
042EF6B0 {ninteenW}{ninteenW}{ninteenW}{ninteenW}
042EF6B4 {ninteenW}{ninteenW}0000
042EF6B8 17{twentyP}{twentyP}{twentyP}
042EF6BC {twentyP}{twentyW}{twentyW}{twentyW}
042EF6C0 {twentyW}{twentyW}{twentyW}{twentyW}
042EF6C4 {twentyW}{twentyW}0000
042EF6C8 18{twentyOneP}{twentyOneP}{twentyOneP}
042EF6CC {twentyOneP}{twentyOneW}{twentyOneW}{twentyOneW}
042EF6D0 {twentyOneW}{twentyOneW}{twentyOneW}{twentyOneW}
042EF6D4 {twentyOneW}{twentyOneW}0000
042EF6D8 19{twentyTwoP}{twentyTwoP}{twentyTwoP}
042EF6DC {twentyTwoP}{twentyTwoW}{twentyTwoW}{twentyTwoW}
042EF6E0 {twentyTwoW}{twentyTwoW}{twentyTwoW}{twentyTwoW}
042EF6E4 {twentyTwoW}{twentyTwoW}0000
042EF6E8 1E{twentyThreeP}{twentyThreeP}{twentyThreeP}
042EF6EC {twentyThreeP}{twentyThreeW}{twentyThreeW}{twentyThreeW}
042EF6F0 {twentyThreeW}{twentyThreeW}{twentyThreeW}{twentyThreeW}
042EF6F4 {twentyThreeW}{twentyThreeW}0000
042EF6F8 1F{twentyFourP}{twentyFourP}{twentyFourP}
042EF6FC {twentyFourP}{twentyFourW}{twentyFourW}{twentyFourW}
042EF700 {twentyFourW}{twentyFourW}{twentyFourW}{twentyFourW}
042EF704 {twentyFourW}{twentyFourW}0000
042EF708 20{twentyFiveP}{twentyFiveP}{twentyFiveP}
042EF70C {twentyFiveP}{twentyFiveW}{twentyFiveW}{twentyFiveW}
042EF710 {twentyFiveW}{twentyFiveW}{twentyFiveW}{twentyFiveW}
042EF714 {twentyFiveW}{twentyFiveW}0000
042EF718 21{twentySixP}{twentySixP}{twentySixP}
042EF71C {twentySixP}{twentySixW}{twentySixW}{twentySixW}
042EF720 {twentySixW}{twentySixW}{twentySixW}{twentySixW}
042EF724 {twentySixW}{twentySixW}0000
042EF728 22{twentySevenP}{twentySevenP}{twentySevenP}
042EF72C {twentySevenP}{twentySevenW}{twentySevenW}{twentySevenW}
042EF730 {twentySevenW}{twentySevenW}{twentySevenW}{twentySevenW}
042EF734 {twentySevenW}{twentySevenW}0000
042EF738 23{twentyEightP}{twentyEightP}{twentyEightP}
042EF73C {twentyEightP}{twentyEightW}{twentyEightW}{twentyEightW}
042EF740 {twentyEightW}{twentyEightW}{twentyEightW}{twentyEightW}
042EF744 {twentyEightW}{twentyEightW}0000
042EF748 28{twentyNineP}{twentyNineP}{twentyNineP}
042EF74C {twentyNineP}{twentyNineW}{twentyNineW}{twentyNineW}
042EF750 {twentyNineW}{twentyNineW}{twentyNineW}{twentyNineW}
042EF754 {twentyNineW}{twentyNineW}0000
042EF758 32000000
042EF75C 00000000
042EF760 00000000
042EF764 00000000
042EF768 33000000
042EF76C 00000000
042EF770 00000000
042EF774 00000000
042EF778 34000000
042EF77C 00000000
042EF780 00000000
042EF784 00000000
042EF788 35000000
042EF78C 00000000
042EF790 00000000
042EF794 00000000
042EF798 FF000000
042EF79C 00000000
042EF7A0 00000000
042EF7A4 00000000
'''
