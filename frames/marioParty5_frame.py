# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/12/2024
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioParty5_coins import *
from events.marioParty5_mgreplace import *
from events.marioParty5_modselect import *
from events.marioParty5_items import *

# Import custom tkinter module as ctk
import customtkinter as ctk

# Function to create the main interface for Mario Party 1
def create_mario_party_5_interface(frame):
    # Create a tabbed interface
    tabview = ctk.CTkTabview(frame, width=1110, height=752, fg_color=("#fcfcfc", "#323232"))
    tabview.grid(padx=10, pady=10)
    tabview.add("Mod Selection")
    tabview.add("Coins Mods")
    tabview.add("Minigame Replacement")
    tabview.add("Capsule Mods")
    tabview.set("Mod Selection")

    # Function to create an entry field and checkbox
    def create_entry(tab, row, icon_path, label_text, color):
        create_image_icon(tab, icon_path, row, 1)
        label = ctk.CTkLabel(master=tab, text=label_text, font=("Arial", 16))
        label.grid(row=row, column=2, sticky="w", pady=15)
        entry = ctk.CTkEntry(master=tab, width=48, font=("Arial", 16, "bold"))
        entry.grid(row=row, column=3)
        label1 = ctk.CTkLabel(master=tab, text=color, font=("Arial", 16))
        label1.grid(row=row, column=4, sticky="w")
        return entry

    # Create entry fields and checkboxes for Coins Mods tab
    blue_entry = create_entry(tabview.tab("Coins Mods"), 1, "assets/eventTags/blueSpace.png", " Gain  ", " Coins on a Blue Space.")
    red_entry = create_entry(tabview.tab("Coins Mods"), 2, "assets/eventTags/redSpace.png", " Lose  ", " Coins on a Red Space.")
    mgWin_entry = create_entry(tabview.tab("Coins Mods"), 3, "assets/eventTags/miniGame.png", " Gain  ", " Coins when winning a Minigame.")
    star_entry = create_entry(tabview.tab("Coins Mods"), 4, "assets/eventTags/starSpace.png", " Costs ", " Coins to buy a Star at a Star Space.")
    wiggler_entry = create_entry(tabview.tab("Coins Mods"), 5, "assets/eventTags/wigglerCapsule.png", " Costs ", " Coins to buy a Star with Wiggler.")
    chompCost_entry = create_entry(tabview.tab("Coins Mods"), 6, "assets/eventTags/chainChomp.png", " Costs ", " Coins to Steal a Star.")
    chompMin_entry = create_entry(tabview.tab("Coins Mods"), 7, "assets/eventTags/chainChomp.png", " Steal ", " mininum when stealing Coins.")

    # Create button to generate coins modification codes
    parse_coins_button = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=lambda: coinsEvent_mp5(blue_entry, red_entry, mgWin_entry, star_entry, wiggler_entry, chompCost_entry, chompMin_entry), text="Generate Codes")
    parse_coins_button.place(x=10, y=640)

    # List of minigame names
    minigames_list = ["Coney Island", "Ground Pound Down", "Chimp Chase", "Chomp Romp", "Pushy Penguins", "Leaf Leap", "Night Light Fright", "Pop-Star Piranhas", "Mazed & Confused", "Dinger Derby", "Hydrostars", "Later Skater", "Will Flower", "Triple Jump", "Hotel Goomba", "Coin Cache", "Flatiator", "Squared Away", "Mario Mechs", "Revolving Fire", "Clock Stoppers", "Heat Stroke", "Beam Team", "Vicious Vending", "Big Top Drop", "Defuse or Lose", "ID UFO", "Mario Can-Can", "Handy Hoppers", "Berry Basket", "Bus Buffer", "Rumble Ready", "Submarathon", "Manic Mallets", "Astro-Logical", "Bill Blasters", "Tug-o-Dorrie", "Twist 'n' Out", "Lucky Lineup", "Random Ride", "Shock Absorbers", "Countdown Pound", "Whomp Maze", "Shy Guy Showdown", "Button Mashers", "Get a Rope", "Pump 'n' Jump", "Head Waiter", "Blown Away", "Merry Poppings", "Pound Peril", "Piece Out", "Bound of Music", "Wind Wavers", "Sky Survivor", "Cage-in Cookin'", "Rain of Fire", "Scaldin' Cauldron", "Frightmare", "Flower Shower", "Dodge Bomb", "Fish Upon a Star", "Rumble Fumble", "Quilt for Speed", "Tube It or Lose It", "Mathletes", "Fight Cards", "Banana Punch", "Da Vine Climb", "Mass A-peel", "Panic Pinball", "Banking Coins", "Frozen Frenzy", "Curvy Curbs", "Beach Volleyball", "Fish Sticks", "Ice Hockey"]   
    # Create labels, comboboxes, and button for Minigame Replacement tab
    replace_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
    replace_label.grid(row=0, column=0)
    combobox_mingames_1 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_1.grid(row=0, column=1)
    with_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
    with_label.grid(row=0, column=2)
    combobox_mingames_2 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_2.grid(row=0, column=3)
    parse_minigame_button = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=lambda: mgReplaceEvent_mp5(combobox_mingames_1, combobox_mingames_2, minigames_list), text="Generate Codes")
    parse_minigame_button.place(x=10, y=640)

    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/mushroomCapsule.png", 2, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=2)
    mushroomCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    mushroomCapsulePrice5.grid(row=2, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=4)
    mushroomCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    mushroomCapsuleWeight5.grid(row=2, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.   ", font=("Arial", 16))
    label.grid(row=2, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/goldenMushroomCapsule.png", 3, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=2)
    goldenMushroomCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsulePrice5.grid(row=3, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=4)
    goldenMushroomCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsuleWeight5.grid(row=3, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/cursedMushroomCapsule.png", 4, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=2)
    cursedMushroomCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    cursedMushroomCapsulePrice5.grid(row=4, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=4)
    cursedMushroomCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    cursedMushroomCapsuleWeight5.grid(row=4, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/warpCapsule.png", 5, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=2)
    warpPipeCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    warpPipeCapsulePrice5.grid(row=5, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=4)
    warpPipeCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    warpPipeCapsuleWeight5.grid(row=5, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/kleptoCapsule.png", 6, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=2)
    kleptoCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    kleptoCapsulePrice5.grid(row=6, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=4)
    kleptoCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    kleptoCapsuleWeight5.grid(row=6, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/wigglerCapsule.png", 8, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=8, column=2)
    flutterCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    flutterCapsulePrice5.grid(row=8, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=8, column=4)
    flutterCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    flutterCapsuleWeight5.grid(row=8, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=8, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/podobooCapsule.png", 9, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=9, column=2)
    podobooCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    podobooCapsulePrice5.grid(row=9, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=9, column=4)
    podobooCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    podobooCapsuleWeight5.grid(row=9, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=9, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/spinyCapsule.png", 10, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=10, column=2)
    spinyCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    spinyCapsulePrice5.grid(row=10, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=10, column=4)
    spinyCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    spinyCapsuleWeight5.grid(row=10, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=10, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/coinBlockCapsule.png", 11, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=11, column=2)
    coinBlockCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    coinBlockCapsulePrice5.grid(row=11, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=11, column=4)
    coinBlockCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    coinBlockCapsuleWeight5.grid(row=11, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=11, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/hammerBroCapsule.png", 12, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=12, column=2)
    hammerBroCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    hammerBroCapsulePrice5.grid(row=12, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=12, column=4)
    hammerBroCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    hammerBroCapsuleWeight5.grid(row=12, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.  ", font=("Arial", 16))
    label.grid(row=12, column=6)

    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text="", font=("Arial", 16))
    label.grid(row=2, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/paraTroopaCapsule.png", 2, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=9)
    paraTroopaCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    paraTroopaCapsulePrice5.grid(row=2, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=11)
    paraTroopaCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    paraTroopaCapsuleWeight5.grid(row=2, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.  ", font=("Arial", 16))
    label.grid(row=2, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/bulletBillCapsule.png", 3, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=9)
    bulletBillCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    bulletBillCapsulePrice5.grid(row=3, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=11)
    bulletBillCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    bulletBillCapsuleWeight5.grid(row=3, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/blizzardCapsule.png", 4, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=9)
    blizzardCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    blizzardCapsulePrice5.grid(row=4, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=11)
    blizzardCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    blizzardCapsuleWeight5.grid(row=4, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/kamekCapsule.png", 5, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=9)
    kamekCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    kamekCapsulePrice5.grid(row=5, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=11)
    kamekCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    kamekCapsuleWeight5.grid(row=5, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/koopaBankCapsule.png", 6, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=9)
    koopaBankCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    koopaBankCapsulePrice5.grid(row=6, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=11)
    koopaBankCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    koopaBankCapsuleWeight5.grid(row=6, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/goombaCapsule.png", 8, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=8, column=9)
    goombaCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    goombaCapsulePrice5.grid(row=8, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=8, column=11)
    goombaCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    goombaCapsuleWeight5.grid(row=8, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=8, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/bombCapsule.png", 9, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=9, column=9)
    bombCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    bombCapsulePrice5.grid(row=9, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=9, column=11)
    bombCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    bombCapsuleWeight5.grid(row=9, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=9, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/tweesterCapsule.png", 10, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=10, column=9)
    tweesterCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    tweesterCapsulePrice5.grid(row=10, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=10, column=11)
    tweesterCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    tweesterCapsuleWeight5.grid(row=10, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=10, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/lakituCapsule.png", 11, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=11, column=9)
    lakituCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    lakituCapsulePrice5.grid(row=11, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=11, column=11)
    lakituCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    lakituCapsuleWeight5.grid(row=11, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=11, column=13)
    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/ukikiCapsule.png", 12, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=12, column=9)
    ukikiCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    ukikiCapsulePrice5.grid(row=12, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=12, column=11)
    ukikiCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    ukikiCapsuleWeight5.grid(row=12, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=12, column=13)

    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text="", font=("Arial", 16))
    label.grid(row=2, column=14)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/miracleCapsule.png", 2, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=16)
    miracleCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    miracleCapsulePrice5.grid(row=2, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=18)
    miracleCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    miracleCapsuleWeight5.grid(row=2, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=2, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/snackCapsule.png", 3, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=16)
    boneCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    boneCapsulePrice5.grid(row=3, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=18)
    boneCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    boneCapsuleWeight5.grid(row=3, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/plantCapsule.png", 4, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=16)
    plantCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    plantCapsulePrice5.grid(row=4, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=18)
    plantCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    plantCapsuleWeight5.grid(row=4, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/chainChompCapsule.png", 5, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=16)
    chainChompCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    chainChompCapsulePrice5.grid(row=5, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=18)
    chainChompCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    chainChompCapsuleWeight5.grid(row=5, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/chanceCapsule.png", 6, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=16)
    chanceCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    chanceCapsulePrice5.grid(row=6, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=18)
    chanceCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    chanceCapsuleWeight5.grid(row=6, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/dkCapsule.png", 8, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=8, column=16)
    dkCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    dkCapsulePrice5.grid(row=8, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=8, column=18)
    dkCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    dkCapsuleWeight5.grid(row=8, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=8, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/bowserCapsule.png", 9, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=9, column=16)
    bowserCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    bowserCapsulePrice5.grid(row=9, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=9, column=18)
    bowserCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    bowserCapsuleWeight5.grid(row=9, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=9, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/duelCapsule.png", 10, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=10, column=16)
    duelCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    duelCapsulePrice5.grid(row=10, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=10, column=18)
    duelCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    duelCapsuleWeight5.grid(row=10, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=10, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/toadyCapsule.png", 11, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=11, column=16)
    magiKoopaCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    magiKoopaCapsulePrice5.grid(row=11, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=11, column=18)
    magiKoopaCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    magiKoopaCapsuleWeight5.grid(row=11, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=11, column=20)

    parseButtonFiveItems = ctk.CTkButton(master=tabview.tab("Capsule Mods"), command=lambda: itemsEvent_mp5(bombCapsulePrice5, bombCapsuleWeight5, koopaBankCapsulePrice5, koopaBankCapsuleWeight5, bulletBillCapsulePrice5, bulletBillCapsuleWeight5, hammerBroCapsulePrice5, hammerBroCapsuleWeight5, coinBlockCapsulePrice5, coinBlockCapsuleWeight5, duelCapsulePrice5, duelCapsuleWeight5, mushroomCapsulePrice5, mushroomCapsuleWeight5, goldenMushroomCapsulePrice5, goldenMushroomCapsuleWeight5, cursedMushroomCapsulePrice5, cursedMushroomCapsuleWeight5, flutterCapsulePrice5, flutterCapsuleWeight5, spinyCapsulePrice5, spinyCapsuleWeight5, goombaCapsuleWeight5, goombaCapsulePrice5, plantCapsulePrice5, plantCapsuleWeight5, kleptoCapsuleWeight5, kleptoCapsulePrice5, kamekCapsuleWeight5, kamekCapsulePrice5, magiKoopaCapsuleWeight5, magiKoopaCapsulePrice5, blizzardCapsuleWeight5, blizzardCapsulePrice5, podobooCapsulePrice5, podobooCapsuleWeight5, paraTroopaCapsuleWeight5, paraTroopaCapsulePrice5, ukikiCapsulePrice5, ukikiCapsuleWeight5, tweesterCapsulePrice5, tweesterCapsuleWeight5, lakituCapsulePrice5, lakituCapsuleWeight5, warpPipeCapsulePrice5, warpPipeCapsuleWeight5, miracleCapsulePrice5, miracleCapsuleWeight5, boneCapsulePrice5, boneCapsuleWeight5, chanceCapsulePrice5, chanceCapsuleWeight5, chainChompCapsulePrice5, chainChompCapsuleWeight5, bowserCapsulePrice5, bowserCapsuleWeight5, dkCapsulePrice5, dkCapsuleWeight5), text="Generate Codes", )
    parseButtonFiveItems.place(x=10, y=640)

    parseButtonFive = ctk.CTkButton(master=tabview.tab("Capsule Mods"), command=lambda: savePresetItems5(bombCapsulePrice5, bombCapsuleWeight5, koopaBankCapsulePrice5, koopaBankCapsuleWeight5, bulletBillCapsulePrice5, bulletBillCapsuleWeight5, hammerBroCapsulePrice5, hammerBroCapsuleWeight5, coinBlockCapsulePrice5, coinBlockCapsuleWeight5, duelCapsulePrice5, duelCapsuleWeight5, mushroomCapsulePrice5, mushroomCapsuleWeight5, goldenMushroomCapsulePrice5, goldenMushroomCapsuleWeight5, cursedMushroomCapsulePrice5, cursedMushroomCapsuleWeight5, flutterCapsulePrice5, flutterCapsuleWeight5, spinyCapsulePrice5, spinyCapsuleWeight5, goombaCapsuleWeight5, goombaCapsulePrice5, plantCapsulePrice5, plantCapsuleWeight5, kleptoCapsuleWeight5, kleptoCapsulePrice5, kamekCapsuleWeight5, kamekCapsulePrice5, magiKoopaCapsuleWeight5, magiKoopaCapsulePrice5, blizzardCapsuleWeight5, blizzardCapsulePrice5, podobooCapsulePrice5, podobooCapsuleWeight5, paraTroopaCapsuleWeight5, paraTroopaCapsulePrice5, ukikiCapsulePrice5, ukikiCapsuleWeight5, tweesterCapsulePrice5, tweesterCapsuleWeight5, lakituCapsulePrice5, lakituCapsuleWeight5, warpPipeCapsulePrice5, warpPipeCapsuleWeight5, miracleCapsulePrice5, miracleCapsuleWeight5, boneCapsulePrice5, boneCapsuleWeight5, chanceCapsulePrice5, chanceCapsuleWeight5, chainChompCapsulePrice5, chainChompCapsuleWeight5, bowserCapsulePrice5, bowserCapsuleWeight5, dkCapsulePrice5, dkCapsuleWeight5), text="Save Preset", )
    parseButtonFive.place(x=160, y=640)

    parseButtonFive = ctk.CTkButton(master=tabview.tab("Capsule Mods"), command=lambda: loadPresetItems5(bombCapsulePrice5, bombCapsuleWeight5, koopaBankCapsulePrice5, koopaBankCapsuleWeight5, bulletBillCapsulePrice5, bulletBillCapsuleWeight5, hammerBroCapsulePrice5, hammerBroCapsuleWeight5, coinBlockCapsulePrice5, coinBlockCapsuleWeight5, duelCapsulePrice5, duelCapsuleWeight5, mushroomCapsulePrice5, mushroomCapsuleWeight5, goldenMushroomCapsulePrice5, goldenMushroomCapsuleWeight5, cursedMushroomCapsulePrice5, cursedMushroomCapsuleWeight5, flutterCapsulePrice5, flutterCapsuleWeight5, spinyCapsulePrice5, spinyCapsuleWeight5, goombaCapsuleWeight5, goombaCapsulePrice5, plantCapsulePrice5, plantCapsuleWeight5, kleptoCapsuleWeight5, kleptoCapsulePrice5, kamekCapsuleWeight5, kamekCapsulePrice5, magiKoopaCapsuleWeight5, magiKoopaCapsulePrice5, blizzardCapsuleWeight5, blizzardCapsulePrice5, podobooCapsulePrice5, podobooCapsuleWeight5, paraTroopaCapsuleWeight5, paraTroopaCapsulePrice5, ukikiCapsulePrice5, ukikiCapsuleWeight5, tweesterCapsulePrice5, tweesterCapsuleWeight5, lakituCapsulePrice5, lakituCapsuleWeight5, warpPipeCapsulePrice5, warpPipeCapsuleWeight5, miracleCapsulePrice5, miracleCapsuleWeight5, boneCapsulePrice5, boneCapsuleWeight5, chanceCapsulePrice5, chanceCapsuleWeight5, chainChompCapsulePrice5, chainChompCapsuleWeight5, bowserCapsulePrice5, bowserCapsuleWeight5, dkCapsulePrice5, dkCapsuleWeight5), text="Load Preset", )
    parseButtonFive.place(x=310, y=640)

    # Create Code Checkboxes
    checkboxAdvTxt = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Automatically Advance Text Boxes", font=("Arial", 13))
    checkboxAdvTxt.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxBattleNoStar = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Battle Minigames Don't Affect Mini-Game Star   ", font=("Arial", 13))
    checkboxBattleNoStar.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxDisableAdv = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Disable Advance on Results", font=("Arial", 13))
    checkboxDisableAdv.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxDisableMus = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Disable In-game Music", font=("Arial", 13))
    checkboxDisableMus.grid(row=3, column=0, sticky="w", padx=5, pady=5)

    # Create Code Checkboxes
    checkboxBoot = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Faster Boot Time", font=("Arial", 13))
    checkboxBoot.grid(row=4, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxBSpeed = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Increased Board Speed", font=("Arial", 13))
    checkboxBSpeed.grid(row=5, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxCSpeed = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Increased Capsule Throwing Speed", font=("Arial", 13))
    checkboxCSpeed.grid(row=6, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxTaunt = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Increased Taunt Capabilities", font=("Arial", 13))
    checkboxTaunt.grid(row=7, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxTxtDisplay = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Instant Text Display", font=("Arial", 13))
    checkboxTxtDisplay.grid(row=8, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxShowCtrl = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Show Player Who Paused", font=("Arial", 13))
    checkboxShowCtrl.grid(row=9, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxUnlockAll = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Unlock Everything", font=("Arial", 13))
    checkboxUnlockAll.grid(row=10, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxBowserNoStealCoins = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Bowser Nightmare - Bowser does not Steal Coins", font=("Arial", 13))
    checkboxBowserNoStealCoins.grid(row=11, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkbox60RocketShip = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Future Dream - 60 Seconds in Rocket Ship Game", font=("Arial", 13))
    checkbox60RocketShip.grid(row=12, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxFreeTaxi = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Future Dream - Free Taxi Ride", font=("Arial", 13))
    checkboxFreeTaxi.grid(row=13, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxFreeThwmopWhomp = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Pirate Dream - Free Thwomps & Whomps", font=("Arial", 13))
    checkboxFreeThwmopWhomp.grid(row=14, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxFreeBridge = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Rainbow Dream - Free Bridge Crossings", font=("Arial", 13))
    checkboxFreeBridge.grid(row=15, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxDisableHappening = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Sweet Dream - Disable Topmost Happening Space", font=("Arial", 13))
    checkboxDisableHappening.grid(row=16, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxAllDK = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="All DK Spaces are Active", font=("Arial", 13))
    checkboxAllDK.grid(row=0, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxCapsulesAny= ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Capsules Can Be Thrown Everywhere", font=("Arial", 13))
    checkboxCapsulesAny.grid(row=1, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxDoubleTurns = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Double the Amount of Turns", font=("Arial", 13))
    checkboxDoubleTurns.grid(row=2, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxForceLast5 = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Last 5 Turns Event - First Turn", font=("Arial", 13))
    checkboxForceLast5.grid(row=3, column=1, sticky="w", padx=5, pady=5)

    # Create Code Checkboxes
    checkboxCapsulesFinal = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Obtain Capsules on Final Turn", font=("Arial", 13))
    checkboxCapsulesFinal.grid(row=4, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxsameSpaceAlways = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Same Space Duels Always Happen", font=("Arial", 13))
    checkboxsameSpaceAlways.grid(row=5, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxsameSpaceNever = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Same Space Duels Never Happen", font=("Arial", 13))
    checkboxsameSpaceNever.grid(row=6, column=1, sticky="w", padx=5, pady=5)

    def checkbox_callback_SameSpace():
        if checkboxsameSpaceNever.get() == 1:
            checkboxsameSpaceAlways.configure(state="disabled")
        else:
            checkboxsameSpaceAlways.configure(state="normal")

        if checkboxsameSpaceAlways.get() == 1:
            checkboxsameSpaceNever.configure(state="disabled")
        else:
            checkboxsameSpaceNever.configure(state="normal")

    # Attach the callback function to the checkboxes
    checkboxsameSpaceNever.configure(command=checkbox_callback_SameSpace)
    checkboxsameSpaceAlways.configure(command=checkbox_callback_SameSpace)
    
    # Create Code Checkboxes
    checkbox20Sec = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Beam Team - 20 Second Timer", font=("Arial", 13))
    checkbox20Sec.grid(row=7, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxNoBrick = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Bound of Music - No Bricks", font=("Arial", 13))
    checkboxNoBrick.grid(row=8, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkbox1Slow = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Curvy Curves - 1 Player is Slower", font=("Arial", 13))
    checkbox1Slow.grid(row=9, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxNoSlow = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Coney Island - No Slow Down", font=("Arial", 13))
    checkboxNoSlow.grid(row=10, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxFlowers3 = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Flower Shower - All Flowers Worth 3pts", font=("Arial", 13))
    checkboxFlowers3.grid(row=11, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxNoRocks = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Ground Pound Down - No Rocks Until End", font=("Arial", 13))
    checkboxNoRocks.grid(row=12, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxLeafDisplay = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Leaf Leap - Leaves Display Quicker", font=("Arial", 13))
    checkboxLeafDisplay.grid(row=13, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxHalvedTime = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Pop Star Piranhas - Halved Time to Pick", font=("Arial", 13))
    checkboxHalvedTime.grid(row=14, column=1, sticky="w", padx=5, pady=5)

    # Create Code Comboboxes
    label = ctk.CTkLabel(master=tabview.tab("Mod Selection"), text="Last 5 Turns Events", font=("Arial", 17, "bold"))
    label.grid(row=0, column=2, sticky="w", padx=5, pady=5)
    comboboxLast5Event = ctk.CTkComboBox(master=tabview.tab("Mod Selection"), values=["Random", "Disabled", "x3 Coins", "5 Star Spaces", "Capsule Sapces on Every Space", "Red Spaces are Bowser Spaces"], font=("Arial", 13), width=300)
    comboboxLast5Event.grid(row=1, column=2, sticky="w", padx=5, pady=5)

    def checkbox_callback_Last5():
        if checkboxDisableLast5.get() == 1:
            checkboxForceLast5.configure(state="disabled")
            comboboxLast5Event.configure(state="disabled")
        else:
            checkboxForceLast5.configure(state="normal")
            comboboxLast5Event.configure(state="normal")
        if checkboxForceLast5.get() == 1:
            checkboxDisableLast5.configure(state="disabled")
            
    def combobox_callback_Last5(choice):  
        if comboboxLast5Event.get() == "Disabled":
            checkboxForceLast5.configure(state="disabled")

    # Attach the callback function to the checkboxes
    checkboxForceLast5.configure(command=checkbox_callback_Last5)
    comboboxLast5Event.configure(command=combobox_callback_Last5)

    # Default Check Boxes
    checkboxDisableAdv.select()
    checkboxBoot.select()
    checkboxBSpeed.select()
    checkboxCSpeed.select()
    checkboxTaunt.select()
    checkboxTxtDisplay.select()
    checkboxShowCtrl.select()
    checkboxUnlockAll.select()
    checkboxBattleNoStar.select()

    parseButtonFiveOther = ctk.CTkButton(master=tabview.tab("Mod Selection"), command=lambda: modSelect_mp5(checkboxDisableAdv, checkboxDisableMus, checkboxBoot, checkboxBSpeed, checkboxCSpeed, checkboxTaunt, checkboxTxtDisplay, checkboxShowCtrl, checkboxUnlockAll, checkboxBowserNoStealCoins, checkbox60RocketShip, checkboxFreeTaxi, checkboxFreeThwmopWhomp, checkboxFreeBridge, checkboxDisableHappening, checkboxAdvTxt, checkboxAllDK, checkboxBattleNoStar, checkboxCapsulesAny, checkboxDoubleTurns, checkboxCapsulesFinal, checkboxsameSpaceAlways, checkboxsameSpaceNever, checkbox20Sec, checkboxNoBrick, checkbox1Slow, checkboxNoSlow, checkboxFlowers3, checkboxNoRocks, checkboxLeafDisplay, checkboxHalvedTime, checkboxDisableLast5, checkboxForceLast5, comboboxLast5Event), text="Generate Codes", )
    parseButtonFiveOther.place(x=10, y=640)

    return frame
    