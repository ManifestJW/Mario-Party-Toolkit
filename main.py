# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 1/23/2024
# License: MIT
# ============================================


import tkinter
import tkinter.messagebox
import customtkinter
import version
import tkinter as tk
import pyperclip

from CTkToolTip import *

from functions import *
from credits import *
from codes import *

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Mario Party: Toolkit")
        self.geometry(f"{1330}x{780}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Mario Party Toolkit", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.mario_party_1_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 1", command=self.mp1ButtonEvent)
        self.mario_party_1_button.grid(row=1, column=0, padx=20, pady=10)

        self.mario_party_2_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 2", command=self.mp2ButtonEvent)
        self.mario_party_2_button.grid(row=2, column=0, padx=20, pady=10)

        self.mario_party_3_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 3", command=self.mp3ButtonEvent)
        self.mario_party_3_button.grid(row=3, column=0, padx=20, pady=10)

        self.mario_party_4_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 4", command=self.mp4ButtonEvent)
        self.mario_party_4_button.grid(row=4, column=0, padx=20, pady=10)

        self.mario_party_5_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 5", command=self.mp5ButtonEvent)
        self.mario_party_5_button.grid(row=5, column=0, padx=20, pady=10)
        
        self.mario_party_6_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 6", command=self.mp6ButtonEvent)
        self.mario_party_6_button.grid(row=6, column=0, padx=20, pady=10)

        self.mario_party_7_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 7", command=self.mp7ButtonEvent)
        self.mario_party_7_button.grid(row=7, column=0, padx=20, pady=10)

        self.mario_party_8_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 8 (Rev. 1)", command=self.mp8ButtonEvent)
        self.mario_party_8_button.grid(row=8, column=0, padx=20, pady=10)

        self.mario_party_82_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 8 (Rev. 2)", command=self.mp82ButtonEvent)
        self.mario_party_82_button.grid(row=9, column=0, padx=20, pady=10)

        self.credits_button = customtkinter.CTkButton(self.sidebar_frame, text="Credits", command=self.creditsButtonEvent)
        self.credits_button.grid(row=11, column=0, padx=20, pady=10)
        
        self.version_label = customtkinter.CTkLabel(self.sidebar_frame, text=f"Version: {version.appVersion}", anchor="w", font=("Arial", 14, "bold"))
        self.version_label.grid(row=13, column=0, padx=20, pady=(10, 0))

        self.current_game_frame = None  # To keep track of the currently displayed game frame
    
        # set default values
        self.mario_party_1_button.configure(state="disabled")

    def reset_game_frames(self):
        # Reset the main frame to remove any existing game-specific widgets
        if self.current_game_frame:
            self.current_game_frame.destroy()

    def create_game_frame(self, game_name):
        # Create a new game frame based on the selected game_name
        self.reset_game_frames()

        if game_name == "Mario Party 1":
            self.current_game_frame = self.create_mp1_frame()
        elif game_name == "Mario Party 2":
            self.current_game_frame = self.create_mp2_frame()
        elif game_name == "Mario Party 3":
            self.current_game_frame = self.create_mp3_frame()
        elif game_name == "Mario Party 4":
            self.current_game_frame = self.create_mp4_frame()
        elif game_name == "Mario Party 5":
            self.current_game_frame = self.create_mp5_frame()
        elif game_name == "Mario Party 6":
            self.current_game_frame = self.create_mp6_frame()
        elif game_name == "Mario Party 7":
            self.current_game_frame = self.create_mp7_frame()
        elif game_name == "Mario Party 8 (Rev. 1)":
            self.current_game_frame = self.create_mp8_frame()
        elif game_name == "Mario Party 8 (Rev. 2)":
            self.current_game_frame = self.create_mp82_frame()
        elif game_name == "Credits":
            self.current_game_frame = self.create_credits_frame()
        self.current_game_frame.grid(row=0, column=1, padx=(0, 0), pady=(0, 0), rowspan=3, sticky="nsew")

    def create_mp1_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry, and tickbox
        blueSpaceIconOne = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Give  ", font=("Arial", 16))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountOne = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountOne.grid(row=1, column=3)
        blueSpaceLabel1 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Blue Space.", font=("Arial", 16))
        blueSpaceLabel1.grid(row=1, column=4)
        self.blueSpaceTickboxOne = ctk.CTkCheckBox(master=tabview.tab("Space Modifiers"), text="Double the coins on Last 5", width=16, checkbox_width=16, checkbox_height=16)
        self.blueSpaceTickboxOne.grid(row=1, column=5, padx=10, pady=10)
        
        # Create red space icon and entry, and tickbox
        redSpaceIconOne = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountOne = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountOne.grid(row=2, column=3)
        redSpaceLabel1 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel1.grid(row=2, column=4)
        self.redSpaceTickboxOne = ctk.CTkCheckBox(master=tabview.tab("Space Modifiers"), text="Double the coins on Last 5", width=16, checkbox_width=16, checkbox_height=16)
        self.redSpaceTickboxOne.grid(row=2, column=5, padx=10, pady=10)

        parseButtonOne = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonOne, text="Generate Codes")
        parseButtonOne.place(x=390, y=660)

        return frame

    def create_mp2_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry, and tickbox
        blueSpaceIconTwo = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Give  ", font=("Arial", 16))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountTwo = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountTwo.grid(row=1, column=3)
        blueSpaceLabel2 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Blue Space.", font=("Arial", 16))
        blueSpaceLabel2.grid(row=1, column=4)
        self.blueSpaceTickboxTwo = ctk.CTkCheckBox(master=tabview.tab("Space Modifiers"), text="Double the coins on Last 5", width=16, checkbox_width=16, checkbox_height=16)
        self.blueSpaceTickboxTwo.grid(row=1, column=5, padx=10, pady=10)

        # Create red space icon and entry, and tickbox
        redSpaceIconTwo = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountTwo = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountTwo.grid(row=2, column=3)
        redSpaceLabel2 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel2.grid(row=2, column=4)
        self.redSpaceTickboxTwo = ctk.CTkCheckBox(master=tabview.tab("Space Modifiers"), text="Double the coins on Last 5", width=16, checkbox_width=16, checkbox_height=16)
        self.redSpaceTickboxTwo.grid(row=2, column=5, padx=10, pady=10)

        parseButtonTwo = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonTwo, text="Generate Codes")
        parseButtonTwo.place(x=390, y=660)

        return frame

    def create_mp3_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry, and tickbox
        blueSpaceIconThree = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Give  ", font=("Arial", 16))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountThree = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountThree.grid(row=1, column=3)
        blueSpaceLabel3 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Blue Space.", font=("Arial", 16))
        blueSpaceLabel3.grid(row=1, column=4)
        self.blueSpaceTickboxThree = ctk.CTkCheckBox(master=tabview.tab("Space Modifiers"), text="Double the coins on Last 5", width=16, checkbox_width=16, checkbox_height=16)
        self.blueSpaceTickboxThree.grid(row=1, column=5, padx=10, pady=10)

        # Create red space icon and entry, and tickbox
        redSpaceIconThree = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountThree = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountThree.grid(row=2, column=3)
        redSpaceLabel3 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel3.grid(row=2, column=4)
        self.redSpaceTickboxThree = ctk.CTkCheckBox(master=tabview.tab("Space Modifiers"), text="Double the coins on Last 5", width=16, checkbox_width=16, checkbox_height=16)
        self.redSpaceTickboxThree.grid(row=2, column=5, padx=10, pady=10)
        parseButtonThree = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonThree, text="Generate Codes")
        parseButtonThree.place(x=390, y=660)
        return frame


    def create_mp4_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry
        blueSpaceIconFour = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Give  ", font=("Arial", 16))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountFour = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountFour.grid(row=1, column=3)
        blueSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Blue Space.", font=("Arial", 16))
        blueSpaceLabel4.grid(row=1, column=4, sticky="w")

        # Create red space icon and entry
        redSpaceIconFour = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountFour = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountFour.grid(row=2, column=3)
        redSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel4.grid(row=2, column=4, sticky="w")

        # Create star space icon and entry
        starSpaceIconFour = create_image_icon(tabview.tab("Space Modifiers"), "assets/starSpace.png", 3, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=3, column=2)
        self.starSpaceAmountFour = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.starSpaceAmountFour.grid(row=3, column=3)
        starSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins when passing and using a Magic Lamp.", font=("Arial", 16))
        starSpaceLabel4.grid(row=3, column=4, sticky="w")

        parseButtonFour = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonFour, text="Generate Codes")
        parseButtonFour.place(x=390, y=660)
        return frame

    def create_mp5_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry
        blueSpaceIconFive = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gain  ", font=("Arial", 16))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountFive = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountFive.grid(row=1, column=3)
        blueSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Blue Space.", font=("Arial", 16))
        blueSpaceLabel4.grid(row=1, column=4, sticky="w")

        # Create red space icon and entry
        redSpaceIconFive = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountFive = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountFive.grid(row=2, column=3)
        redSpaceLabel5 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel5.grid(row=2, column=4, sticky="w")

        # Create star space icon and entry
        starSpaceIconFive = create_image_icon(tabview.tab("Space Modifiers"), "assets/starSpace.png", 3, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=3, column=2)
        self.starSpaceAmountFive = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.starSpaceAmountFive.grid(row=3, column=3)
        starSpaceLabel5 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins when passing a Star Space.", font=("Arial", 16))
        starSpaceLabel5.grid(row=3, column=4, sticky="w")

        # Create wiggler space icon and entry
        wigglerSpaceIconFive = create_image_icon(tabview.tab("Space Modifiers"), "assets/wigglerCapsule.png", 4, 1)
        wigglerSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Cost  ", font=("Arial", 16))
        wigglerSpaceLabel.grid(row=4, column=2)
        self.wigglerSpaceAmountFive = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.wigglerSpaceAmountFive.grid(row=4, column=3)
        wigglerSpaceLabel5 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins to use Wiggler.", font=("Arial", 16))
        wigglerSpaceLabel5.grid(row=4, column=4, sticky="w")

        # Create chain chomp space icon and entry
        chompSpaceIconFive = create_image_icon(tabview.tab("Space Modifiers"), "assets/chainChomp.png", 5, 1)
        chompSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Cost  ", font=("Arial", 16))
        chompSpaceLabel.grid(row=5, column=2)
        self.chompSpaceAmountFive = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.chompSpaceAmountFive.grid(row=5, column=3)
        chompSpaceLabel5 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins to steal a Star.", font=("Arial", 16))
        chompSpaceLabel5.grid(row=5, column=4, sticky="w")

        parseButtonFive = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonFive, text="Generate Codes")
        parseButtonFive.place(x=390, y=660)
        return frame

    def create_mp6_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry
        blueSpaceIconSix = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Give  ", font=("Arial", 16))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountSix = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountSix.grid(row=1, column=3)
        blueSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Blue Space.", font=("Arial", 16))
        blueSpaceLabel4.grid(row=1, column=4, sticky="w")

        # Create red space icon and entry
        redSpaceIconSix = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountSix = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountSix.grid(row=2, column=3)
        redSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel6.grid(row=2, column=4, sticky="w")

        # Create star space icon and entry
        starSpaceIconSix = create_image_icon(tabview.tab("Space Modifiers"), "assets/starSpace.png", 3, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=3, column=2)
        self.starSpaceAmountSix = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.starSpaceAmountSix.grid(row=3, column=3)
        starSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins when passing and using a Flutter.", font=("Arial", 16))
        starSpaceLabel6.grid(row=3, column=4, sticky="w")

        # Create boo space icon and entry
        pinkBooSpaceIconSix = create_image_icon(tabview.tab("Space Modifiers"), "assets/pinkBoo.png", 4, 1)
        pinkBooSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Cost  ", font=("Arial", 16))
        pinkBooSpaceLabel.grid(row=4, column=2)
        self.pinkBooSpaceAmountSix = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.pinkBooSpaceAmountSix.grid(row=4, column=3)
        pinkBooSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins when stealing a Star.", font=("Arial", 16))
        pinkBooSpaceLabel6.grid(row=4, column=4, sticky="w")
        
        parseButtonSix = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonSix, text="Generate Codes")
        parseButtonSix.place(x=390, y=660)
        return frame

    def create_mp7_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=750, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.add("Orb Modifiers")
        tabview.set("Space Modifiers")

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/mushroomCapsule.png", 2, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=2, column=2)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" 5  ", font=("Arial", 24, "bold"))
        label.grid(row=2, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=2, column=4)
        self.mushroomCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.mushroomCapsuleWeight7.grid(row=2, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.   ", font=("Arial", 16))
        label.grid(row=2, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/goldenMushroomCapsule.png", 3, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=3, column=2)
        self.goldenMushroomCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.goldenMushroomCapsulePrice7.grid(row=3, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=3, column=4)
        self.goldenMushroomCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.goldenMushroomCapsuleWeight7.grid(row=3, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=3, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/slowMushroomCapsule.png", 4, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=4, column=2)
        self.slowMushroomCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.slowMushroomCapsulePrice7.grid(row=4, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=4, column=4)
        self.slowMushroomCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.slowMushroomCapsuleWeight7.grid(row=4, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=4, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/metalMushroomCapsule.png", 5, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=5, column=2)
        self.metalMushroomCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.metalMushroomCapsulePrice7.grid(row=5, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=5, column=4)
        self.metalMushroomCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.metalMushroomCapsuleWeight7.grid(row=5, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=5, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/wigglerCapsule.png", 6, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=6, column=2)
        self.flutterCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.flutterCapsulePrice7.grid(row=6, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=6, column=4)
        self.flutterCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.flutterCapsuleWeight7.grid(row=6, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=6, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/cannonCapsule.png", 7, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=7, column=2)
        self.cannonCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.cannonCapsulePrice7.grid(row=7, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=7, column=4)
        self.cannonCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.cannonCapsuleWeight7.grid(row=7, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=7, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/snackCapsule.png", 8, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=8, column=2)
        self.snackCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.snackCapsulePrice7.grid(row=8, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=8, column=4)
        self.snackCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.snackCapsuleWeight7.grid(row=8, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=8, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/lakituCapsule.png", 9, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=9, column=2)
        self.lakituCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.lakituCapsulePrice7.grid(row=9, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=9, column=4)
        self.lakituCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.lakituCapsuleWeight7.grid(row=9, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=9, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/hammerBroCapsule.png", 10, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=10, column=2)
        self.hammerBroCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.hammerBroCapsulePrice7.grid(row=10, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=10, column=4)
        self.hammerBroCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.hammerBroCapsuleWeight7.grid(row=10, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=10, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/spearCapsule.png", 11, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=11, column=2)
        self.spearCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.spearCapsulePrice7.grid(row=11, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=11, column=4)
        self.spearCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.spearCapsuleWeight7.grid(row=11, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=11, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/plantCapsule.png", 12, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=12, column=2)
        self.plantCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.plantCapsulePrice7.grid(row=12, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=12, column=4)
        self.plantCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.plantCapsuleWeight7.grid(row=12, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.  ", font=("Arial", 16))
        label.grid(row=12, column=6)

        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text="", font=("Arial", 16))
        label.grid(row=2, column=7)
        

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/kamekCapsule.png", 2, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=2, column=9)
        self.kamekCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.kamekCapsulePrice7.grid(row=2, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=2, column=11)
        self.kamekCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.kamekCapsuleWeight7.grid(row=2, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.  ", font=("Arial", 16))
        label.grid(row=2, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/toadyCapsule.png", 3, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=3, column=9)
        self.toadyCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.toadyCapsulePrice7.grid(row=3, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=3, column=11)
        self.toadyCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.toadyCapsuleWeight7.grid(row=3, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=3, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/blizzardCapsule.png", 4, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=4, column=9)
        self.blizzardCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.blizzardCapsulePrice7.grid(row=4, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=4, column=11)
        self.blizzardCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.blizzardCapsuleWeight7.grid(row=4, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=4, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/banditCapsule.png", 5, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=5, column=9)
        self.banditCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.banditCapsulePrice7.grid(row=5, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=5, column=11)
        self.banditCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.banditCapsuleWeight7.grid(row=5, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=5, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/pinkBooCapsule.png", 6, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=6, column=9)
        self.pinkBooCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.pinkBooCapsulePrice7.grid(row=6, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=6, column=11)
        self.pinkBooCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.pinkBooCapsuleWeight7.grid(row=6, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=6, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/spinyCapsule.png", 7, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=7, column=9)
        self.spinyCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.spinyCapsulePrice7.grid(row=7, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=7, column=11)
        self.spinyCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.spinyCapsuleWeight7.grid(row=7, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=7, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/zapCapsule.png", 8, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=8, column=9)
        self.zapCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.zapCapsulePrice7.grid(row=8, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=8, column=11)
        self.zapCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.zapCapsuleWeight7.grid(row=8, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=8, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/tweesterCapsule.png", 9, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=9, column=9)
        self.tweesterCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.tweesterCapsulePrice7.grid(row=9, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=9, column=11)
        self.tweesterCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.tweesterCapsuleWeight7.grid(row=9, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=9, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/thwompCapsule.png", 10, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=10, column=9)
        self.thwompCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.thwompCapsulePrice7.grid(row=10, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=10, column=11)
        self.thwompCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.thwompCapsuleWeight7.grid(row=10, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=10, column=13)
    
        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/warpCapsule.png", 11, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=11, column=9)
        self.warpCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.warpCapsulePrice7.grid(row=11, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=11, column=11)
        self.warpCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.warpCapsuleWeight7.grid(row=11, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=11, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/bombCapsule.png", 12, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=12, column=9)
        self.bombCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.bombCapsulePrice7.grid(row=12, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=12, column=11)
        self.bombCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.bombCapsuleWeight7.grid(row=12, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.  ", font=("Arial", 16))
        label.grid(row=12, column=13)

        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text="", font=("Arial", 16))
        label.grid(row=2, column=14)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/fireballCapsule.png", 2, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=2, column=16)
        self.fireballCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.fireballCapsulePrice7.grid(row=2, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=2, column=18)
        self.fireballCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.fireballCapsuleWeight7.grid(row=2, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=2, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/flowerCapsule.png", 3, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=3, column=16)
        self.flowerCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.flowerCapsulePrice7.grid(row=3, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=3, column=18)
        self.flowerCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.flowerCapsuleWeight7.grid(row=3, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=3, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/eggCapsule.png", 4, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=4, column=16)
        self.eggCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.eggCapsulePrice7.grid(row=4, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=4, column=18)
        self.eggCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.eggCapsuleWeight7.grid(row=4, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=4, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/vacuumCapsule.png", 5, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=5, column=16)
        self.vacuumCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.vacuumCapsulePrice7.grid(row=5, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=5, column=18)
        self.vacuumCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.vacuumCapsuleWeight7.grid(row=5, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=5, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/magicCapsule.png", 6, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=6, column=16)
        self.magicCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.magicCapsulePrice7.grid(row=6, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=6, column=18)
        self.magicCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.magicCapsuleWeight7.grid(row=6, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=6, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/tripleCapsule.png", 7, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=7, column=16)
        self.tripleCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.tripleCapsulePrice7.grid(row=7, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=7, column=18)
        self.tripleCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.tripleCapsuleWeight7.grid(row=7, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=7, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Modifiers"), "assets/koopaCapsule.png", 8, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=8, column=16)
        self.koopaCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.koopaCapsulePrice7.grid(row=8, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" and is ", font=("Arial", 16))
        label.grid(row=8, column=18)
        self.koopaCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.koopaCapsuleWeight7.grid(row=8, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Modifiers"), text=" % common.", font=("Arial", 16))
        label.grid(row=8, column=20)

        # Create blue space icon and entry
        blueSpaceIconSeven = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Give  ", font=("Arial", 16))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountSeven = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountSeven.grid(row=1, column=3)
        blueSpaceLabel7 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Blue Space.", font=("Arial", 16))
        blueSpaceLabel7.grid(row=1, column=4, sticky="w")

        # Create red space icon and entry
        redSpaceIconSeven = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountSeven = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountSeven.grid(row=2, column=3)
        redSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel6.grid(row=2, column=4, sticky="w")

        # Create star space icon and entry
        starSpaceIconSeven= create_image_icon(tabview.tab("Space Modifiers"), "assets/starSpace.png", 3, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=3, column=2)
        self.starSpaceAmountSeven = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.starSpaceAmountSeven.grid(row=3, column=3)
        starSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins when passing or when using a Flutter.", font=("Arial", 16))
        starSpaceLabel6.grid(row=3, column=4, sticky="w")

        # Create star space last five icon and entry
        starSpaceIconSeven= create_image_icon(tabview.tab("Space Modifiers"), "assets/starSpaceLastFive.png", 4, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=4, column=2)
        self.starSpaceAmountSevenLastFive = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.starSpaceAmountSevenLastFive.grid(row=4, column=3)
        starSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins during the Last 5 Turns Event (only if wheel lands on it).", font=("Arial", 16))
        starSpaceLabel6.grid(row=4, column=4, sticky="w")

        parseButtonSeven = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonSeven, text="Generate Codes")
        parseButtonSeven.place(x=390, y=660)

        parseButtonSevenOrbs = ctk.CTkButton(master=tabview.tab("Orb Modifiers"), command=self.actionSpaceButtonSevenOrb, text="Generate Codes")
        parseButtonSevenOrbs.place(x=390, y=660)
        return frame
    
    def create_credits_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Credits")
        tabview.add("About")
        tabview.add("License")
        tabview.set("About")
        mit_license_widget = customtkinter.CTkLabel(tabview.tab("License"), width=80, height=20, text=(get_mit_license_text()))
        mit_license_widget.pack(padx=10, pady=10)
        credits_widget = customtkinter.CTkLabel(tabview.tab("Credits"), width=80, height=20, text=(get_credits_text()))
        credits_widget.pack(padx=10, pady=10)
        about_widget = customtkinter.CTkLabel(tabview.tab("About"), width=80, height=20, text=(get_about_text()))
        about_widget.pack(padx=10, pady=10)
        return frame

    def create_mp82_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry
        blueSpaceIconEight2 = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Give  ", font=("Arial", 16))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountEight2 = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountEight2.grid(row=1, column=3)
        blueSpaceLabel28 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Blue Space.", font=("Arial", 16))
        blueSpaceLabel28.grid(row=1, column=4, sticky="w")

        # Create red space icon and entry
        redSpaceIconEight2 = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountEight2 = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountEight2.grid(row=2, column=3)
        redSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel6.grid(row=2, column=4, sticky="w")

        # Create star space icon and entry
        starSpaceIconEight2= create_image_icon(tabview.tab("Space Modifiers"), "assets/starSpace.png", 3, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=3, column=2)
        self.starSpaceAmountEight2 = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.starSpaceAmountEight2.grid(row=3, column=3)
        starSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins when passing.", font=("Arial", 16))
        starSpaceLabel6.grid(row=3, column=4, sticky="w")

        parseButtonEight2 = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonEight2, text="Generate Codes")
        parseButtonEight2.place(x=390, y=660)
        return frame
        
    def create_mp8_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry
        blueSpaceIconEight = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Give  ", font=("Arial", 16))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountEight = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountEight.grid(row=1, column=3)
        blueSpaceLabel8 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Blue Space.", font=("Arial", 16))
        blueSpaceLabel8.grid(row=1, column=4, sticky="w")

        # Create red space icon and entry
        redSpaceIconEight = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountEight = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountEight.grid(row=2, column=3)
        redSpaceLabel8 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel8.grid(row=2, column=4, sticky="w")

        # Create star space icon and entry
        starSpaceIconEight= create_image_icon(tabview.tab("Space Modifiers"), "assets/starSpace.png", 3, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=3, column=2)
        self.starSpaceAmountEight = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 16, "bold"))
        self.starSpaceAmountEight.grid(row=3, column=3)
        starSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins when passing.", font=("Arial", 16))
        starSpaceLabel6.grid(row=3, column=4, sticky="w")

        parseButtonEight = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonEight, text="Generate Codes")
        parseButtonEight.place(x=390, y=660)
        return frame

    def actionSpaceButtonOne(self):
        if not self.blueSpaceAmountOne.get() and not self.redSpaceAmountOne.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseOne = self.blueSpaceAmountOne.get()
        try:
            blueSpaceAmountOne = hex(int(blueSpaceAmountBaseOne))
            if len(blueSpaceAmountOne) == 5:
                blueSpaceAmountOne = "0" + blueSpaceAmountOne[2:]
            elif len(blueSpaceAmountOne) == 4:
                blueSpaceAmountOne = "00" + blueSpaceAmountOne[2:]
            elif len(blueSpaceAmountOne) == 3:
                blueSpaceAmountOne = "000" + blueSpaceAmountOne[2:]
        except:
            blueSpaceAmountOne = "DUMMY"
    
        blueSpaceSwitchOne = self.blueSpaceTickboxOne.get()
        if blueSpaceSwitchOne:
            blueSpaceSwitchOne = "1"
        else:
            blueSpaceSwitchOne = "0"

    
        redSpaceAmountBaseOne = self.redSpaceAmountOne.get()
        try:
            redSpaceAmountOne = hex(int(self.redSpaceAmountOne.get()))
            if len(redSpaceAmountOne) == 5:
                redSpaceAmountOne = "0" + redSpaceAmountOne[2:]
            elif len(redSpaceAmountOne) == 4:
                redSpaceAmountOne = "00" + redSpaceAmountOne[2:]
            elif len(redSpaceAmountOne) == 3:
                redSpaceAmountOne = "000" + redSpaceAmountOne[2:]
        except:
            redSpaceAmountOne = "DUMMY"
    
    
        redSpaceSwitchOne = self.redSpaceTickboxOne.get()
        if redSpaceSwitchOne == True:
            redSpaceSwitchOne = "1"
        elif redSpaceSwitchOne == False:
            redSpaceSwitchOne = "0"
    
        marioPartyOneBlueSpace = getBlueSpaceCodeOne(blueSpaceAmountOne, blueSpaceSwitchOne)
        marioPartyOneRedSpace = getRedSpaceCodeOne(redSpaceAmountOne, redSpaceSwitchOne)
    
        if redSpaceAmountOne == "DUMMY":
            marioPartyOneRedSpace = ""
        if blueSpaceAmountOne == "DUMMY":
            marioPartyOneBlueSpace = ""
    
        generatedCode = marioPartyOneRedSpace + marioPartyOneBlueSpace
        generatedCode = generatedCode.replace("ONEBLUESWITCH", "Doesn't Double on Last 5")
        generatedCode = generatedCode.replace("ONEREDSWITCH", "Doubles on Last 5")
        generatedCode = generatedCode.replace("ONERED", redSpaceAmountBaseOne)
        generatedCode = generatedCode.replace("ONEBLUE", blueSpaceAmountBaseOne)
    
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)

    def actionSpaceButtonTwo(self):
        if not self.blueSpaceAmountTwo.get() and not self.redSpaceAmountTwo.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseTwo = self.blueSpaceAmountTwo.get()
        try:
            blueSpaceAmountTwo = hex(int(blueSpaceAmountBaseTwo))
            if len(blueSpaceAmountTwo) == 5:
                blueSpaceAmountTwo = "0" + blueSpaceAmountTwo[2:]
            elif len(blueSpaceAmountTwo) == 4:
                blueSpaceAmountTwo = "00" + blueSpaceAmountTwo[2:]
            elif len(blueSpaceAmountTwo) == 3:
                blueSpaceAmountTwo = "000" + blueSpaceAmountTwo[2:]
        except:
            blueSpaceAmountTwo = "DUMMY"
    
        blueSpaceSwitchTwo = self.blueSpaceTickboxTwo.get()
        if blueSpaceSwitchTwo:
            blueSpaceSwitchTwo = "1"
        else:
            blueSpaceSwitchTwo = "0"

    
        redSpaceAmountBaseTwo = self.redSpaceAmountTwo.get()
        try:
            redSpaceAmountTwo = hex(int(self.redSpaceAmountTwo.get()))
            if len(redSpaceAmountTwo) == 5:
                redSpaceAmountTwo = "0" + redSpaceAmountTwo[2:]
            elif len(redSpaceAmountTwo) == 4:
                redSpaceAmountTwo = "00" + redSpaceAmountTwo[2:]
            elif len(redSpaceAmountTwo) == 3:
                redSpaceAmountTwo = "000" + redSpaceAmountTwo[2:]
        except:
            redSpaceAmountTwo = "DUMMY"
    
    
        redSpaceSwitchTwo = self.redSpaceTickboxTwo.get()
        if redSpaceSwitchTwo == True:
            redSpaceSwitchTwo = "1"
        elif redSpaceSwitchTwo == False:
            redSpaceSwitchTwo = "0"
    
        marioPartyTwoBlueSpace = getBlueSpaceCodeTwo(blueSpaceAmountTwo, blueSpaceSwitchTwo)
        marioPartyTwoRedSpace = getRedSpaceCodeTwo(redSpaceAmountTwo, redSpaceSwitchTwo)
    
        if redSpaceAmountTwo == "DUMMY":
            marioPartyTwoRedSpace = ""
        if blueSpaceAmountTwo == "DUMMY":
            marioPartyTwoBlueSpace = ""
    
        generatedCode = marioPartyTwoRedSpace + marioPartyTwoBlueSpace
        generatedCode = generatedCode.replace("TWOBLUESWITCH", "Doesn't Double on Last 5")
        generatedCode = generatedCode.replace("TWOREDSWITCH", "Doubles on Last 5")
        generatedCode = generatedCode.replace("TWORED", redSpaceAmountBaseTwo)
        generatedCode = generatedCode.replace("TWOBLUE", blueSpaceAmountBaseTwo)
    
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)
    def actionSpaceButtonThree(self):
        if not self.blueSpaceAmountThree.get() and not self.redSpaceAmountThree.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseThree = self.blueSpaceAmountThree.get()
        try:
            blueSpaceAmountThree = hex(int(blueSpaceAmountBaseThree))
            if len(blueSpaceAmountThree) == 5:
                blueSpaceAmountThree = "0" + blueSpaceAmountThree[2:]
            elif len(blueSpaceAmountThree) == 4:
                blueSpaceAmountThree = "00" + blueSpaceAmountThree[2:]
            elif len(blueSpaceAmountThree) == 3:
                blueSpaceAmountThree = "000" + blueSpaceAmountThree[2:]
        except:
            blueSpaceAmountThree = "DUMMY"
    
        blueSpaceSwitchThree = self.blueSpaceTickboxThree.get()
        if blueSpaceSwitchThree:
            blueSpaceSwitchThree = "1"
        else:
            blueSpaceSwitchThree = "0"

    
        redSpaceAmountBaseThree = self.redSpaceAmountThree.get()
        try:
            redSpaceAmountThree = hex(int(self.redSpaceAmountThree.get()))
            if len(redSpaceAmountThree) == 5:
                redSpaceAmountThree = "0" + redSpaceAmountThree[2:]
            elif len(redSpaceAmountThree) == 4:
                redSpaceAmountThree = "00" + redSpaceAmountThree[2:]
            elif len(redSpaceAmountThree) == 3:
                redSpaceAmountThree = "000" + redSpaceAmountThree[2:]
        except:
            redSpaceAmountThree = "DUMMY"
    
    
        redSpaceSwitchThree = self.redSpaceTickboxThree.get()
        if redSpaceSwitchThree == True:
            redSpaceSwitchThree = "1"
        elif redSpaceSwitchThree == False:
            redSpaceSwitchThree = "0"
    
        marioPartyThreeBlueSpace = getBlueSpaceCodeThree(blueSpaceAmountThree, blueSpaceSwitchThree)
        marioPartyThreeRedSpace = getRedSpaceCodeThree(redSpaceAmountThree, redSpaceSwitchThree)
    
        if redSpaceAmountThree == "DUMMY":
            marioPartyThreeRedSpace = ""
        if blueSpaceAmountThree == "DUMMY":
            marioPartyThreeBlueSpace = ""
    
        generatedCode = marioPartyThreeRedSpace + marioPartyThreeBlueSpace
        generatedCode = generatedCode.replace("THREEBLUESWITCH", "Doesn't Double on Last 5")
        generatedCode = generatedCode.replace("THREEREDSWITCH", "Doubles on Last 5")
        generatedCode = generatedCode.replace("THREERED", redSpaceAmountBaseThree)
        generatedCode = generatedCode.replace("THREEBLUE", blueSpaceAmountBaseThree)
    
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)
    def actionSpaceButtonFour(self):    
        if not self.blueSpaceAmountFour.get() and not self.redSpaceAmountFour.get() and not self.starSpaceAmountFour.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseFour = self.blueSpaceAmountFour.get()
        try:
            blueSpaceAmountFour = hex(int(self.blueSpaceAmountFour.get()))
            if len(blueSpaceAmountFour) == 5:
                blueSpaceAmountFour = "0" + blueSpaceAmountFour[2:]
            elif len(blueSpaceAmountFour) == 4:
                blueSpaceAmountFour = "00" + blueSpaceAmountFour[2:]
            elif len(blueSpaceAmountFour) == 3:
                blueSpaceAmountFour = "000" + blueSpaceAmountFour[2:]
        except:
            blueSpaceAmountFour = "DUMMY"

        redSpaceAmountBaseFour = self.redSpaceAmountFour.get()
        try:
            redSpaceAmountFour = hex(int(self.redSpaceAmountFour.get()))
            if len(redSpaceAmountFour) == 5:
                redSpaceAmountFour = "0" + redSpaceAmountFour[2:]
            elif len(redSpaceAmountFour) == 4:
                redSpaceAmountFour = "00" + redSpaceAmountFour[2:]
            elif len(redSpaceAmountFour) == 3:
                redSpaceAmountFour = "000" + redSpaceAmountFour[2:]
        except:
            redSpaceAmountFour = "DUMMY"

        starSpaceAmountFourBase = self.starSpaceAmountFour.get()

        try:
            starSpaceAmountFour = hex(int(self.starSpaceAmountFour.get()))
            if len(starSpaceAmountFour) == 4:
                starSpaceAmountFour = "00" + starSpaceAmountFour[2:]
            elif len(starSpaceAmountFour) == 3:
                starSpaceAmountFour = "000" + starSpaceAmountFour[2:]
        except:
            starSpaceAmountFour = "DUMMY"


        marioPartyFourBlueSpace = getBlueSpaceCodeFour(blueSpaceAmountFour)
        marioPartyFourRedSpace = getRedSpaceCodeFour(redSpaceAmountFour)
        marioPartyFourStarSpace = getStarSpaceCodeFour(starSpaceAmountFour)

        if redSpaceAmountFour == "DUMMY":
            marioPartyFourRedSpace = ""
        if blueSpaceAmountFour == "DUMMY":
            marioPartyFourBlueSpace = ""
        if starSpaceAmountFour == "DUMMY":
            marioPartyFourStarSpace = ""

        generatedCode = marioPartyFourRedSpace + marioPartyFourBlueSpace + marioPartyFourStarSpace
        generatedCode = generatedCode.replace("FOURRED", redSpaceAmountBaseFour)
        generatedCode = generatedCode.replace("FOURBLUE", blueSpaceAmountBaseFour)
        generatedCode = generatedCode.replace("FOURSTAR", starSpaceAmountFourBase)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)

    def actionSpaceButtonFive(self):
        if not self.blueSpaceAmountFive.get() and not self.redSpaceAmountFive.get() and not self.starSpaceAmountFive.get() and not self.wigglerSpaceAmountFive.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseFive = self.blueSpaceAmountFive.get()
        try:
            blueSpaceAmountFive = hex(int(self.blueSpaceAmountFive.get()))
            if len(blueSpaceAmountFive) == 5:
                blueSpaceAmountFive = "0" + blueSpaceAmountFive[2:]
            elif len(blueSpaceAmountFive) == 4:
                blueSpaceAmountFive = "00" + blueSpaceAmountFive[2:]
            elif len(blueSpaceAmountFive) == 3:
                blueSpaceAmountFive = "000" + blueSpaceAmountFive[2:]
        except:
            blueSpaceAmountFive = "DUMMY"

        redSpaceAmountBaseFive = self.redSpaceAmountFive.get()
        try:
            redSpaceAmountFive = int(redSpaceAmountBaseFive, 16)
            negativeRedSpaceAmountBaseFive = -int(redSpaceAmountBaseFive)
            redSpaceAmountFive = format(negativeRedSpaceAmountBaseFive & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            redSpaceAmountFive = "DUMMY"

        starSpaceAmountFiveBase = self.starSpaceAmountFive.get()

        try:
            starSpaceAmountFive = hex(int(self.starSpaceAmountFive.get()))
            if len(starSpaceAmountFive) == 4:
                starSpaceAmountFive = "00" + starSpaceAmountFive[2:]
            elif len(starSpaceAmountFive) == 3:
                starSpaceAmountFive = "000" + starSpaceAmountFive[2:]

            negativeRedSpaceAmountBaseFive = -int(starSpaceAmountFiveBase)
            starSpaceAmountNegativeFive = format(negativeRedSpaceAmountBaseFive & 0xFFFFFFFFFFFFFFFF, 'X')[12:]

        except:
            starSpaceAmountFive = "DUMMY"
            starSpaceAmountNegativeFive = "DUMMY"

        wigglerSpaceAmountFiveBase = self.wigglerSpaceAmountFive.get()

        chompSpaceAmountFiveBase = self.chompSpaceAmountFive.get()

        try:
            chompSpaceAmountFive = hex(int(self.chompSpaceAmountFive.get()))
            if len(chompSpaceAmountFive) == 4:
                chompSpaceAmountFive = "00" + chompSpaceAmountFive[2:]
            elif len(chompSpaceAmountFive) == 3:
                chompSpaceAmountFive = "000" + chompSpaceAmountFive[2:]

            negativeChompSpaceAmountBaseFive = -int(chompSpaceAmountFiveBase)
            chompSpaceAmountNegativeFive = format(negativeChompSpaceAmountBaseFive & 0xFFFFFFFFFFFFFFFF, 'X')[12:]

        except:
            chompSpaceAmountFive = "DUMMY"
            chompSpaceAmountNegativeFive = "DUMMY"

        try:
            wigglerSpaceAmountFive = hex(int(self.wigglerSpaceAmountFive.get()))
            if len(wigglerSpaceAmountFive) == 4:
                wigglerSpaceAmountFive = "00" + wigglerSpaceAmountFive[2:]
            elif len(wigglerSpaceAmountFive) == 3:
                wigglerSpaceAmountFive = "000" + wigglerSpaceAmountFive[2:]

            negativeWigglerSpaceAmountBaseFive = -int(wigglerSpaceAmountFiveBase)
            wigglerSpaceAmountNegativeFive = format(negativeWigglerSpaceAmountBaseFive & 0xFFFFFFFFFFFFFFFF, 'X')[12:]

        except:
            wigglerSpaceAmountFive = "DUMMY"
            wigglerSpaceAmountNegativeFive = "DUMMY"

        marioPartyFiveStarSpace = getStarSpaceCodeFive(starSpaceAmountFive, starSpaceAmountNegativeFive)
        marioPartyFiveWigglerSpace = getWigglerSpaceCodeFive(wigglerSpaceAmountFive, wigglerSpaceAmountNegativeFive)
        marioPartyFiveChompSpace = getChompSpaceCodeFive(chompSpaceAmountFive, chompSpaceAmountNegativeFive)
        marioPartyFiveBlueSpace = getBlueSpaceCodeFive(blueSpaceAmountFive)
        marioPartyFiveRedSpace = getRedSpaceCodeFive(redSpaceAmountFive)

        if redSpaceAmountFive == "DUMMY":
            marioPartyFiveRedSpace = ""
        if blueSpaceAmountFive == "DUMMY":
            marioPartyFiveBlueSpace = ""
        if starSpaceAmountFive == "DUMMY":
            marioPartyFiveStarSpace = ""
        if starSpaceAmountNegativeFive == "DUMMY":
            marioPartyFiveStarSpace = ""
        if wigglerSpaceAmountFive == "DUMMY":
            marioPartyFiveWigglerSpace = ""
        if wigglerSpaceAmountNegativeFive == "DUMMY":
            marioPartyFiveWigglerSpace = ""
        if chompSpaceAmountFive == "DUMMY":
            marioPartyFiveChompSpace = ""
        if chompSpaceAmountNegativeFive == "DUMMY":
            marioPartyFiveChompSpace = ""

        generatedCode = marioPartyFiveRedSpace + marioPartyFiveBlueSpace + marioPartyFiveStarSpace + marioPartyFiveWigglerSpace + marioPartyFiveChompSpace
        generatedCode = generatedCode.replace("FIVERED", redSpaceAmountBaseFive)
        generatedCode = generatedCode.replace("FIVEBLUE", blueSpaceAmountBaseFive)
        generatedCode = generatedCode.replace("FIVESTAR", starSpaceAmountFiveBase)
        generatedCode = generatedCode.replace("FIVEWIGGLER", wigglerSpaceAmountFiveBase)
        generatedCode = generatedCode.replace("FIVECHOMP", chompSpaceAmountFiveBase)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)

    def actionSpaceButtonSix(self):
        if not self.blueSpaceAmountSix.get() and not self.redSpaceAmountSix.get() and not self.starSpaceAmountSix.get() and not self.pinkBooSpaceAmountSix.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseSix = self.blueSpaceAmountSix.get()
        try:
            blueSpaceAmountSix = hex(int(self.blueSpaceAmountSix.get()))
            if len(blueSpaceAmountSix) == 5:
                blueSpaceAmountSix = "0" + blueSpaceAmountSix[2:]
            elif len(blueSpaceAmountSix) == 4:
                blueSpaceAmountSix = "00" + blueSpaceAmountSix[2:]
            elif len(blueSpaceAmountSix) == 3:
                blueSpaceAmountSix = "000" + blueSpaceAmountSix[2:]
        except:
            blueSpaceAmountSix = "DUMMY"

        redSpaceAmountBaseSix = self.redSpaceAmountSix.get()
        try:
            redSpaceAmountSix = int(redSpaceAmountBaseSix, 16)
            negativeRedSpaceAmountBaseSix = -int(redSpaceAmountBaseSix)
            redSpaceAmountSix = format(negativeRedSpaceAmountBaseSix & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            redSpaceAmountSix = "DUMMY"

        starSpaceAmountSixBase = self.starSpaceAmountSix.get()
        try:
            starSpaceAmountSix = hex(int(self.starSpaceAmountSix.get()))
            if len(starSpaceAmountSix) == 4:
                starSpaceAmountSix = "00" + starSpaceAmountSix[2:]
            elif len(starSpaceAmountSix) == 3:
                starSpaceAmountSix = "000" + starSpaceAmountSix[2:]

            negativeRedSpaceAmountBaseSix = -int(starSpaceAmountSixBase)
            starSpaceAmountNegativeSix = format(negativeRedSpaceAmountBaseSix & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            starSpaceAmountSix = "DUMMY"
            starSpaceAmountNegativeSix = "DUMMY"

        pinkBooSpaceAmountSixBase = self.pinkBooSpaceAmountSix.get()
        try:
            pinkBooSpaceAmountSix = hex(int(self.pinkBooSpaceAmountSix.get()))
            if len(pinkBooSpaceAmountSix) == 4:
                pinkBooSpaceAmountSix = "00" + pinkBooSpaceAmountSix[2:]
            elif len(pinkBooSpaceAmountSix) == 3:
                pinkBooSpaceAmountSix = "000" + pinkBooSpaceAmountSix[2:]

            pinkBooSpaceAmountBaseNegativeSix = -int(pinkBooSpaceAmountSixBase)
            pinkBooSpaceAmountNegativeSix = format(pinkBooSpaceAmountBaseNegativeSix & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            pinkBooSpaceAmountSix = "DUMMY"
            pinkBooSpaceAmountNegativeSix = "DUMMY"

        marioPartySixBlueSpace = getBlueSpaceCodeSix(blueSpaceAmountSix)
        marioPartySixRedSpace = getRedSpaceCodeSix(redSpaceAmountSix)
        marioPartySixStarSpace = getStarSpaceCodeSix(starSpaceAmountSix, starSpaceAmountNegativeSix)
        marioPartySixPinkBooSpace = getPinkBooSpaceCodeSix(pinkBooSpaceAmountSix, pinkBooSpaceAmountNegativeSix)

        if redSpaceAmountSix == "DUMMY":
            marioPartySixRedSpace = ""
        if blueSpaceAmountSix == "DUMMY":
            marioPartySixBlueSpace = ""
        if starSpaceAmountSix == "DUMMY":
            marioPartySixStarSpace = ""
        if starSpaceAmountNegativeSix == "DUMMY":
            marioPartySixStarSpace = ""
        if pinkBooSpaceAmountSix == "DUMMY":
            marioPartySixPinkBooSpace = ""
        if pinkBooSpaceAmountNegativeSix == "DUMMY":
            marioPartySixPinkBooSpace = ""
        
        generatedCode = marioPartySixRedSpace + marioPartySixBlueSpace + marioPartySixStarSpace + marioPartySixPinkBooSpace
        generatedCode = generatedCode.replace("SIXRED", redSpaceAmountBaseSix)
        generatedCode = generatedCode.replace("SIXBLUE", blueSpaceAmountBaseSix)
        generatedCode = generatedCode.replace("SIXSTAR", starSpaceAmountSixBase)
        generatedCode = generatedCode.replace("SIXBOO", pinkBooSpaceAmountSixBase)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)

    def actionSpaceButtonSeven(self):
        if not self.blueSpaceAmountSeven.get() and not self.redSpaceAmountSeven.get() and not self.starSpaceAmountSeven.get() and not self.starSpaceAmountSevenLastFive.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseSeven = self.blueSpaceAmountSeven.get()
        try:
            blueSpaceAmountSeven = hex(int(self.blueSpaceAmountSeven.get()))
            if len(blueSpaceAmountSeven) == 5:
                blueSpaceAmountSeven = "0" + blueSpaceAmountSeven[2:]
            elif len(blueSpaceAmountSeven) == 4:
                blueSpaceAmountSeven = "00" + blueSpaceAmountSeven[2:]
            elif len(blueSpaceAmountSeven) == 3:
                blueSpaceAmountSeven = "000" + blueSpaceAmountSeven[2:]
        except:
            blueSpaceAmountSeven = "DUMMY"

        redSpaceAmountBaseSeven = self.redSpaceAmountSeven.get()
        try:
            redSpaceAmountSeven = int(redSpaceAmountBaseSeven, 16)
            negativeRedSpaceAmountBaseSeven = -int(redSpaceAmountBaseSeven)
            redSpaceAmountSeven = format(negativeRedSpaceAmountBaseSeven & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            redSpaceAmountSeven = "DUMMY"

        starSpaceAmountSevenBase = self.starSpaceAmountSeven.get()
        starSpaceAmountSevenLastFiveBase = self.starSpaceAmountSevenLastFive.get()

        try:
            starSpaceAmountSeven = hex(int(self.starSpaceAmountSeven.get()))
            if len(starSpaceAmountSeven) == 4:
                starSpaceAmountSeven = "00" + starSpaceAmountSeven[2:]
            elif len(starSpaceAmountSeven) == 3:
                starSpaceAmountSeven = "000" + starSpaceAmountSeven[2:]
        except:
            starSpaceAmountSeven = "DUMMY"

        try:
            starSpaceAmountSevenLastFive = hex(int(self.starSpaceAmountSevenLastFive.get()))
            if len(starSpaceAmountSevenLastFive) == 4:
                starSpaceAmountSevenLastFive = "00" + starSpaceAmountSevenLastFive[2:]
            elif len(starSpaceAmountSevenLastFive) == 3:
                starSpaceAmountSevenLastFive = "000" + starSpaceAmountSevenLastFive[2:]
        except:
            starSpaceAmountSevenLastFive = "DUMMY"

        marioPartySevenBlueSpace = getBlueSpaceCodeSeven(blueSpaceAmountSeven)
        marioPartySevenRedSpace = getRedSpaceCodeSeven(redSpaceAmountSeven)
        marioPartySevenStarSpace = getStarSpaceCodeSeven(starSpaceAmountSeven)
        marioPartySevenStarSpaceLastFive = getStarSpaceCodeSevenLastFive(starSpaceAmountSevenLastFive)

        if redSpaceAmountSeven == "DUMMY":
            marioPartySevenRedSpace = ""
        if blueSpaceAmountSeven == "DUMMY":
            marioPartySevenBlueSpace = ""
        if starSpaceAmountSeven == "DUMMY":
            marioPartySevenStarSpace = ""
        if starSpaceAmountSevenLastFive == "DUMMY":
            marioPartySevenStarSpaceLastFive = ""

        generatedCode = marioPartySevenRedSpace + marioPartySevenBlueSpace + marioPartySevenStarSpace + marioPartySevenStarSpaceLastFive
        generatedCode = generatedCode.replace("SEVENRED", redSpaceAmountBaseSeven)
        generatedCode = generatedCode.replace("SEVENBLUE", blueSpaceAmountBaseSeven)
        generatedCode = generatedCode.replace("SEVENSTAR", starSpaceAmountSevenBase)
        generatedCode = generatedCode.replace("SEVENSTLASTFIVE", starSpaceAmountSevenLastFiveBase)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)

    def actionSpaceButtonEight(self):
        if not self.blueSpaceAmountEight.get() and not self.redSpaceAmountEight.get() and not self.starSpaceAmountEight.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseEight = self.blueSpaceAmountEight.get()
        try:
            blueSpaceAmountEight = hex(int(self.blueSpaceAmountEight.get()))
            if len(blueSpaceAmountEight) == 5:
                blueSpaceAmountEight = "0" + blueSpaceAmountEight[2:]
            elif len(blueSpaceAmountEight) == 4:
                blueSpaceAmountEight = "00" + blueSpaceAmountEight[2:]
            elif len(blueSpaceAmountEight) == 3:
                blueSpaceAmountEight = "000" + blueSpaceAmountEight[2:]
        except:
            blueSpaceAmountEight = "DUMMY"

        redSpaceAmountBaseEight = self.redSpaceAmountEight.get()
        try:
            redSpaceAmountEight = int(redSpaceAmountBaseEight, 16)
            negativeRedSpaceAmountBaseEight = -int(redSpaceAmountBaseEight)
            redSpaceAmountEight = format(negativeRedSpaceAmountBaseEight & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            redSpaceAmountEight = "DUMMY"

        starSpaceAmountEightBase = self.starSpaceAmountEight.get()

        try:
            starSpaceAmountEight = hex(int(self.starSpaceAmountEight.get()))

            if len(starSpaceAmountEight) == 4:
                starSpaceAmountEight = "00" + starSpaceAmountEight[2:]
            elif len(starSpaceAmountEight) == 3:
                starSpaceAmountEight = "000" + starSpaceAmountEight[2:]

            negativeRedSpaceAmountBaseEight = -int(starSpaceAmountEightBase)
            starSpaceAmountNegativeEight = format(negativeRedSpaceAmountBaseEight & 0xFFFFFFFFFFFFFFFF, 'X')[12:]

        except:
            starSpaceAmountEight = "DUMMY"
            starSpaceAmountNegativeEight = "DUMMY"

        marioPartyEightStarSpace = getStarSpaceCodeEight(starSpaceAmountEight, starSpaceAmountNegativeEight)
        marioPartyEightBlueSpace = getBlueSpaceCodeEight(blueSpaceAmountEight)
        marioPartyEightRedSpace = getRedSpaceCodeEight(redSpaceAmountEight)

        if redSpaceAmountEight == "DUMMY":
            marioPartyEightRedSpace = ""
        if blueSpaceAmountEight == "DUMMY":
            marioPartyEightBlueSpace = ""
        if starSpaceAmountEight == "DUMMY":
            marioPartyFiveStarSpace = ""
        if starSpaceAmountNegativeEight == "DUMMY":
            marioPartyEightStarSpace = ""

        generatedCode = marioPartyEightRedSpace + marioPartyEightBlueSpace + marioPartyEightStarSpace
        generatedCode = generatedCode.replace("EIGHTRED", redSpaceAmountBaseEight)
        generatedCode = generatedCode.replace("EIGHTBLUE", blueSpaceAmountBaseEight)
        generatedCode = generatedCode.replace("EIGHTSTAR", starSpaceAmountEightBase)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)

    def actionSpaceButtonEight2(self):
        if not self.blueSpaceAmountEight2.get() and not self.redSpaceAmountEight2.get() and not self.starSpaceAmountEight2.get():
            createDialog("Error", "error", "No information provided.", None)
            return
        blueSpaceAmountBaseEight2 = self.blueSpaceAmountEight2.get()

        try:
            blueSpaceAmountEight2 = hex(int(self.blueSpaceAmountEight2.get()))
            if len(blueSpaceAmountEight2) == 5:
                blueSpaceAmountEight2 = "0" + blueSpaceAmountEight2[2:]
            elif len(blueSpaceAmountEight2) == 4:
                blueSpaceAmountEight2 = "00" + blueSpaceAmountEight2[2:]
            elif len(blueSpaceAmountEight2) == 3:
                blueSpaceAmountEight2 = "000" + blueSpaceAmountEight2[2:]
        except:
            blueSpaceAmountEight2 = "DUMMY"

        redSpaceAmountBaseEight2 = self.redSpaceAmountEight2.get()
        try:
            redSpaceAmountEight2 = int(redSpaceAmountBaseEight2, 16)
            negativeRedSpaceAmountBaseEight2 = -int(redSpaceAmountBaseEight2)
            redSpaceAmountEight2 = format(negativeRedSpaceAmountBaseEight2 & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            redSpaceAmountEight2 = "DUMMY"

        starSpaceAmountEight2Base = self.starSpaceAmountEight2.get()
        try:
            starSpaceAmountEight2 = hex(int(self.starSpaceAmountEight2.get()))
            if len(starSpaceAmountEight2) == 4:
                starSpaceAmountEight2 = "00" + starSpaceAmountEight2[2:]
            elif len(starSpaceAmountEight2) == 3:
                starSpaceAmountEight2 = "000" + starSpaceAmountEight2[2:]
            negativeRedSpaceAmountBaseEight2 = -int(starSpaceAmountEight2Base)
            starSpaceAmountNegativeEight2 = format(negativeRedSpaceAmountBaseEight2 & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            starSpaceAmountEight2 = "DUMMY"
            starSpaceAmountNegativeEight2 = "DUMMY"

        marioPartyEight2StarSpace = getStarSpaceCodeEightGC(starSpaceAmountEight2, starSpaceAmountNegativeEight2)
        marioPartyEight2BlueSpace = getBlueSpaceCodeEightGC(blueSpaceAmountEight2)
        marioPartyEight2RedSpace = getRedSpaceCodeEightGC(redSpaceAmountEight2)

        if redSpaceAmountEight2 == "DUMMY":
            marioPartyEight2RedSpace = ""
        if blueSpaceAmountEight2 == "DUMMY":
            marioPartyEight2BlueSpace = ""
        if starSpaceAmountEight2 == "DUMMY":
            marioPartyFiveStarSpace = ""
        if starSpaceAmountNegativeEight2 == "DUMMY":
            marioPartyEight2StarSpace = ""

        generatedCode = marioPartyEight2RedSpace + marioPartyEight2BlueSpace + marioPartyEight2StarSpace
        generatedCode = generatedCode.replace("EIGHTREDGC", redSpaceAmountBaseEight2)
        generatedCode = generatedCode.replace("EIGHTBLUEGC", blueSpaceAmountBaseEight2)
        generatedCode = generatedCode.replace("EIGHTSTARGC", starSpaceAmountEight2Base)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)

        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)

    def actionSpaceButtonSevenOrb(self):
        if not self.mushroomCapsuleWeight7.get() or not self.goldenMushroomCapsulePrice7.get() or not self.goldenMushroomCapsuleWeight7.get() or not self.slowMushroomCapsulePrice7.get() or not self.slowMushroomCapsuleWeight7.get() or not self.metalMushroomCapsulePrice7.get() or not self.metalMushroomCapsuleWeight7.get() or not self.flutterCapsulePrice7.get() or not self.flutterCapsuleWeight7.get() or not self.cannonCapsulePrice7.get() or not self.cannonCapsuleWeight7.get() or not self.snackCapsulePrice7.get() or not self.snackCapsuleWeight7.get() or not self.lakituCapsulePrice7.get() or not self.lakituCapsuleWeight7.get() or not self.hammerBroCapsuleWeight7.get() or not self.hammerBroCapsulePrice7.get() or not self.plantCapsulePrice7.get() or not self.plantCapsuleWeight7.get() or not self.spearCapsuleWeight7.get() or not self.spearCapsulePrice7.get() or not self.kamekCapsuleWeight7.get() or not self.kamekCapsulePrice7.get() or not self.toadyCapsuleWeight7.get() or not self.toadyCapsulePrice7.get() or not self.blizzardCapsuleWeight7.get() or not self.blizzardCapsulePrice7.get():
            createDialog("Error", "error", "Please fill out all the boxes.", None)
            return
        
        mushroomCapsuleWeight7 = self.mushroomCapsuleWeight7.get()
        
        goldenMushroomCapsulePrice7 = self.goldenMushroomCapsulePrice7.get()
        goldenMushroomCapsuleWeight7 = self.goldenMushroomCapsuleWeight7.get()

        slowMushroomCapsulePrice7 = self.slowMushroomCapsulePrice7.get()
        slowMushroomCapsuleWeight7 = self.slowMushroomCapsuleWeight7.get()

        metalMushroomCapsulePrice7 = self.metalMushroomCapsulePrice7.get()
        metalMushroomCapsuleWeight7 = self.metalMushroomCapsuleWeight7.get()

        flutterCapsulePrice7 = self.flutterCapsulePrice7.get()
        flutterCapsuleWeight7 = self.flutterCapsuleWeight7.get()

        cannonCapsulePrice7 = self.cannonCapsulePrice7.get()
        cannonCapsuleWeight7 = self.cannonCapsuleWeight7.get()

        snackCapsulePrice7 = self.snackCapsulePrice7.get()
        snackCapsuleWeight7 = self.snackCapsuleWeight7.get()

        lakituCapsulePrice7 = self.lakituCapsulePrice7.get()
        lakituCapsuleWeight7 = self.lakituCapsuleWeight7.get()

        hammerBroCapsulePrice7 = self.hammerBroCapsulePrice7.get()
        hammerBroCapsuleWeight7 = self.hammerBroCapsuleWeight7.get()

        plantCapsulePrice7 = self.plantCapsulePrice7.get()
        plantCapsuleWeight7 = self.plantCapsuleWeight7.get()

        spearCapsulePrice7 = self.spearCapsulePrice7.get()
        spearCapsuleWeight7 = self.spearCapsuleWeight7.get()

        kamekCapsulePrice7 = self.kamekCapsulePrice7.get()
        kamekCapsuleWeight7 = self.kamekCapsuleWeight7.get()

        toadyCapsulePrice7 = self.toadyCapsulePrice7.get()
        toadyCapsuleWeight7 = self.toadyCapsuleWeight7.get()

        blizzardCapsulePrice7 = self.blizzardCapsulePrice7.get()
        blizzardCapsuleWeight7 = self.blizzardCapsuleWeight7.get()

        banditCapsulePrice7 = self.banditCapsulePrice7.get()
        banditCapsuleWeight7 = self.banditCapsuleWeight7.get()

        pinkBooCapsulePrice7 = self.pinkBooCapsulePrice7.get()
        pinkBooCapsuleWeight7 = self.pinkBooCapsuleWeight7.get()

        spinyCapsulePrice7 = self.spinyCapsulePrice7.get()
        spinyCapsuleWeight7 = self.spinyCapsuleWeight7.get()

        zapCapsulePrice7 = self.zapCapsulePrice7.get()
        zapCapsuleWeight7 = self.zapCapsuleWeight7.get()

        tweesterCapsulePrice7 = self.tweesterCapsulePrice7.get()
        tweesterCapsuleWeight7 = self.tweesterCapsuleWeight7.get()

        thwompCapsulePrice7 = self.thwompCapsulePrice7.get()
        thwompCapsuleWeight7 = self.thwompCapsuleWeight7.get()

        warpCapsulePrice7 = self.warpCapsulePrice7.get()
        warpCapsuleWeight7 = self.warpCapsuleWeight7.get()

        bombCapsulePrice7 = self.bombCapsulePrice7.get()
        bombCapsuleWeight7 = self.bombCapsuleWeight7.get()

        fireballCapsulePrice7 = self.fireballCapsulePrice7.get()
        fireballCapsuleWeight7 = self.fireballCapsuleWeight7.get()

        flowerCapsulePrice7 = self.flowerCapsulePrice7.get()
        flowerCapsuleWeight7 = self.flowerCapsuleWeight7.get()

        eggCapsulePrice7 = self.eggCapsulePrice7.get()
        eggCapsuleWeight7 = self.eggCapsuleWeight7.get()

        vacuumCapsulePrice7 = self.vacuumCapsulePrice7.get()
        vacuumCapsuleWeight7 = self.vacuumCapsuleWeight7.get()

        magicCapsulePrice7 = self.magicCapsulePrice7.get()
        magicCapsuleWeight7 = self.magicCapsuleWeight7.get()

        tripleCapsulePrice7 = self.tripleCapsulePrice7.get()
        tripleCapsuleWeight7 = self.tripleCapsuleWeight7.get()

        koopaCapsulePrice7 = self.koopaCapsulePrice7.get()
        koopaCapsuleWeight7 = self.koopaCapsuleWeight7.get()

        orbWeightTotal = int(mushroomCapsuleWeight7) + int(goldenMushroomCapsuleWeight7) + int(metalMushroomCapsuleWeight7) + int(slowMushroomCapsuleWeight7) + int(flutterCapsuleWeight7) + int(cannonCapsuleWeight7) + int(snackCapsuleWeight7) + int(lakituCapsuleWeight7) + int(hammerBroCapsuleWeight7) + int(plantCapsuleWeight7) + int(spearCapsuleWeight7) + int(kamekCapsuleWeight7) + int(toadyCapsuleWeight7) + int(blizzardCapsuleWeight7) + int(banditCapsuleWeight7) + int(pinkBooCapsuleWeight7) + int(spinyCapsuleWeight7) + int(zapCapsuleWeight7) + int(tweesterCapsuleWeight7) + int(thwompCapsuleWeight7) + int(warpCapsuleWeight7) + int(bombCapsuleWeight7) + int(fireballCapsuleWeight7) + int(flowerCapsulePrice7) + int(eggCapsuleWeight7) + int(vacuumCapsuleWeight7) + int(magicCapsuleWeight7) + int(tripleCapsuleWeight7) + int(koopaCapsuleWeight7)

        mushroomCapsuleWeight7 = (int(mushroomCapsuleWeight7) / orbWeightTotal) * 100
        goldenMushroomCapsuleWeight7 = (int(goldenMushroomCapsuleWeight7) / orbWeightTotal) * 100
        metalMushroomCapsuleWeight7 = (int(metalMushroomCapsuleWeight7) / orbWeightTotal) * 100
        slowMushroomCapsuleWeight7 = (int(slowMushroomCapsuleWeight7) / orbWeightTotal) * 100
        flutterCapsuleWeight7 = (int(flutterCapsuleWeight7) / orbWeightTotal) * 100
        cannonCapsuleWeight7 = (int(cannonCapsuleWeight7) / orbWeightTotal) * 100
        snackCapsuleWeight7 = (int(snackCapsuleWeight7) / orbWeightTotal) * 100
        lakituCapsuleWeight7 = (int(lakituCapsuleWeight7) / orbWeightTotal) * 100
        hammerBroCapsuleWeight7 = (int(hammerBroCapsuleWeight7) / orbWeightTotal) * 100
        plantCapsuleWeight7 = (int(plantCapsuleWeight7) / orbWeightTotal) * 100
        spearCapsuleWeight7 = (int(spearCapsuleWeight7) / orbWeightTotal) * 100
        kamekCapsuleWeight7 = (int(kamekCapsuleWeight7) / orbWeightTotal) * 100
        toadyCapsuleWeight7 = (int(toadyCapsuleWeight7) / orbWeightTotal) * 100
        blizzardCapsuleWeight7 = (int(blizzardCapsuleWeight7) / orbWeightTotal) * 100
        banditCapsuleWeight7 = (int(banditCapsuleWeight7) / orbWeightTotal) * 100
        pinkBooCapsuleWeight7 = (int(pinkBooCapsuleWeight7) / orbWeightTotal) * 100
        spinyCapsuleWeight7 = (int(spinyCapsuleWeight7) / orbWeightTotal) * 100
        zapCapsuleWeight7 = (int(zapCapsuleWeight7) / orbWeightTotal) * 100
        tweesterCapsuleWeight7 = (int(tweesterCapsuleWeight7) / orbWeightTotal) * 100
        thwompCapsuleWeight7 = (int(thwompCapsuleWeight7) / orbWeightTotal) * 100
        warpCapsuleWeight7 = (int(warpCapsuleWeight7) / orbWeightTotal) * 100
        bombCapsuleWeight7 = (int(bombCapsuleWeight7) / orbWeightTotal) * 100
        fireballCapsuleWeight7 = (int(fireballCapsuleWeight7) / orbWeightTotal) * 100
        flowerCapsuleWeight7 = (int(flowerCapsuleWeight7) / orbWeightTotal) * 100
        eggCapsuleWeight7 = (int(eggCapsuleWeight7) / orbWeightTotal) * 100
        vacuumCapsuleWeight7 = (int(vacuumCapsuleWeight7) / orbWeightTotal) * 100
        magicCapsuleWeight7 = (int(magicCapsuleWeight7) / orbWeightTotal) * 100
        tripleCapsuleWeight7 = (int(tripleCapsuleWeight7) / orbWeightTotal) * 100
        koopaCapsuleWeight7 = (int(koopaCapsuleWeight7) / orbWeightTotal) * 100
        try:
            mushroomCapsuleWeight7 = hex(int(mushroomCapsuleWeight7))
            if len(mushroomCapsuleWeight7) == 4:
                mushroomCapsuleWeight7 = mushroomCapsuleWeight7[2:]
            elif len(mushroomCapsuleWeight7) == 3:
                mushroomCapsuleWeight7 = "0" + mushroomCapsuleWeight7[2:]
        except:
            mushroomCapsuleWeight7 = "00"

        try:
            goldenMushroomCapsuleWeight7 = hex(int(goldenMushroomCapsuleWeight7))
            if len(goldenMushroomCapsuleWeight7) == 4:
                goldenMushroomCapsuleWeight7 = goldenMushroomCapsuleWeight7[2:]
            elif len(goldenMushroomCapsuleWeight7) == 3:
                goldenMushroomCapsuleWeight7 = "0" + goldenMushroomCapsuleWeight7[2:]
        except:
            goldenMushroomCapsuleWeight7 = "00"

        try:
            goldenMushroomCapsulePrice7 = hex(int(goldenMushroomCapsulePrice7))
            if len(goldenMushroomCapsulePrice7) == 4:
                goldenMushroomCapsulePrice7 = goldenMushroomCapsulePrice7[2:]
            elif len(goldenMushroomCapsulePrice7) == 3:
                goldenMushroomCapsulePrice7 = "0" + goldenMushroomCapsulePrice7[2:]
        except:
            goldenMushroomCapsulePrice7 = "00"
       
        try:
            slowMushroomCapsuleWeight7 = hex(int(slowMushroomCapsuleWeight7))
            if len(slowMushroomCapsuleWeight7) == 4:
                slowMushroomCapsuleWeight7 = slowMushroomCapsuleWeight7[2:]
            elif len(slowMushroomCapsuleWeight7) == 3:
                slowMushroomCapsuleWeight7 = "0" + slowMushroomCapsuleWeight7[2:]
        except:
            slowMushroomCapsuleWeight7 = "00"

        try:
            slowMushroomCapsulePrice7 = hex(int(slowMushroomCapsulePrice7))
            if len(slowMushroomCapsulePrice7) == 4:
                slowMushroomCapsulePrice7 = slowMushroomCapsulePrice7[2:]
            elif len(slowMushroomCapsulePrice7) == 3:
                slowMushroomCapsulePrice7 = "0" + slowMushroomCapsulePrice7[2:]
        except:
            slowMushroomCapsulePrice7 = "00"

        try:
            metalMushroomCapsuleWeight7 = hex(int(metalMushroomCapsuleWeight7))
            if len(metalMushroomCapsuleWeight7) == 4:
                metalMushroomCapsuleWeight7 = metalMushroomCapsuleWeight7[2:]
            elif len(metalMushroomCapsuleWeight7) == 3:
                metalMushroomCapsuleWeight7 = "0" + metalMushroomCapsuleWeight7[2:]
        except:
            metalMushroomCapsuleWeight7 = "00"

        try:
            metalMushroomCapsulePrice7 = hex(int(metalMushroomCapsulePrice7))
            if len(metalMushroomCapsulePrice7) == 4:
                metalMushroomCapsulePrice7 = metalMushroomCapsulePrice7[2:]
            elif len(metalMushroomCapsulePrice7) == 3:
                metalMushroomCapsulePrice7 = "0" + metalMushroomCapsulePrice7[2:]
        except:
            metalMushroomCapsulePrice7 = "00"

        try:
            flutterCapsuleWeight7 = hex(int(flutterCapsuleWeight7))
            if len(flutterCapsuleWeight7) == 4:
                flutterCapsuleWeight7 = flutterCapsuleWeight7[2:]
            elif len(flutterCapsuleWeight7) == 3:
                flutterCapsuleWeight7 = "0" + flutterCapsuleWeight7[2:]
        except:
            flutterCapsuleWeight7 = "00"

        try:
            flutterCapsulePrice7 = hex(int(flutterCapsulePrice7))
            if len(flutterCapsulePrice7) == 4:
                flutterCapsulePrice7 = flutterCapsulePrice7[2:]
            elif len(flutterCapsulePrice7) == 3:
                flutterCapsulePrice7 = "0" + flutterCapsulePrice7[2:]
        except:
            flutterCapsulePrice7 = "00"

        try:
            cannonCapsuleWeight7 = hex(int(cannonCapsuleWeight7))
            if len(cannonCapsuleWeight7) == 4:
                cannonCapsuleWeight7 = cannonCapsuleWeight7[2:]
            elif len(cannonCapsuleWeight7) == 3:
                cannonCapsuleWeight7 = "0" + cannonCapsuleWeight7[2:]
        except:
            cannonCapsuleWeight7 = "00"

        try:
            cannonCapsulePrice7 = hex(int(cannonCapsulePrice7))
            if len(cannonCapsulePrice7) == 4:
                cannonCapsulePrice7 = cannonCapsulePrice7[2:]
            elif len(cannonCapsulePrice7) == 3:
                cannonCapsulePrice7 = "0" + cannonCapsulePrice7[2:]
        except:
            cannonCapsulePrice7 = "00"

        try:
            snackCapsuleWeight7 = hex(int(snackCapsuleWeight7))
            if len(snackCapsuleWeight7) == 4:
                snackCapsuleWeight7 = snackCapsuleWeight7[2:]
            elif len(snackCapsuleWeight7) == 3:
                snackCapsuleWeight7 = "0" + snackCapsuleWeight7[2:]
        except:
            snackCapsuleWeight7 = "00"

        try:
            snackCapsulePrice7 = hex(int(snackCapsulePrice7))
            if len(snackCapsulePrice7) == 4:
                snackCapsulePrice7 = snackCapsulePrice7[2:]
            elif len(snackCapsulePrice7) == 3:
                snackCapsulePrice7 = "0" + snackCapsulePrice7[2:]
        except:
            snackCapsulePrice7 = "00"

        try:
            lakituCapsuleWeight7 = hex(int(lakituCapsuleWeight7))
            if len(lakituCapsuleWeight7) == 4:
                lakituCapsuleWeight7 = lakituCapsuleWeight7[2:]
            elif len(lakituCapsuleWeight7) == 3:
                lakituCapsuleWeight7 = "0" + lakituCapsuleWeight7[2:]
        except:
            lakituCapsuleWeight7 = "00"

        try:
            lakituCapsulePrice7 = hex(int(lakituCapsulePrice7))
            if len(lakituCapsulePrice7) == 4:
                lakituCapsulePrice7 = lakituCapsulePrice7[2:]
            elif len(lakituCapsulePrice7) == 3:
                lakituCapsulePrice7 = "0" + lakituCapsulePrice7[2:]
        except:
            lakituCapsulePrice7 = "00"

        try:
            hammerBroCapsuleWeight7 = hex(int(hammerBroCapsuleWeight7))
            if len(hammerBroCapsuleWeight7) == 4:
                hammerBroCapsuleWeight7 = hammerBroCapsuleWeight7[2:]
            elif len(hammerBroCapsuleWeight7) == 3:
                hammerBroCapsuleWeight7 = "0" + hammerBroCapsuleWeight7[2:]
        except:
            hammerBroCapsuleWeight7 = "00"

        try:
            hammerBroCapsulePrice7 = hex(int(hammerBroCapsulePrice7))
            if len(hammerBroCapsulePrice7) == 4:
                hammerBroCapsulePrice7 = hammerBroCapsulePrice7[2:]
            elif len(hammerBroCapsulePrice7) == 3:
                hammerBroCapsulePrice7 = "0" + hammerBroCapsulePrice7[2:]
        except:
            hammerBroCapsulePrice7 = "00"

        try:
            plantCapsuleWeight7 = hex(int(plantCapsuleWeight7))
            if len(plantCapsuleWeight7) == 4:
                plantCapsuleWeight7 = plantCapsuleWeight7[2:]
            elif len(plantCapsuleWeight7) == 3:
                plantCapsuleWeight7 = "0" + plantCapsuleWeight7[2:]
        except:
            plantCapsuleWeight7 = "00"

        try:
            plantCapsulePrice7 = hex(int(plantCapsulePrice7))
            if len(plantCapsulePrice7) == 4:
                plantCapsulePrice7 = plantCapsulePrice7[2:]
            elif len(plantCapsulePrice7) == 3:
                plantCapsulePrice7 = "0" + plantCapsulePrice7[2:]
        except:
            plantCapsulePrice7 = "00"

        try:
            spearCapsuleWeight7 = hex(int(spearCapsuleWeight7))
            if len(spearCapsuleWeight7) == 4:
                spearCapsuleWeight7 = spearCapsuleWeight7[2:]
            elif len(spearCapsuleWeight7) == 3:
                spearCapsuleWeight7 = "0" + spearCapsuleWeight7[2:]
        except:
            spearCapsuleWeight7 = "00"

        try:
            spearCapsulePrice7 = hex(int(spearCapsulePrice7))
            if len(spearCapsulePrice7) == 4:
                spearCapsulePrice7 = spearCapsulePrice7[2:]
            elif len(spearCapsulePrice7) == 3:
                spearCapsulePrice7 = "0" + spearCapsulePrice7[2:]
        except:
            spearCapsulePrice7 = "00"

        try:
            kamekCapsuleWeight7 = hex(int(kamekCapsuleWeight7))
            if len(kamekCapsuleWeight7) == 4:
                kamekCapsuleWeight7 = kamekCapsuleWeight7[2:]
            elif len(kamekCapsuleWeight7) == 3:
                kamekCapsuleWeight7 = "0" + kamekCapsuleWeight7[2:]
        except:
            kamekCapsuleWeight7 = "00"

        try:
            kamekCapsulePrice7 = hex(int(kamekCapsulePrice7))
            if len(kamekCapsulePrice7) == 4:
                kamekCapsulePrice7 = kamekCapsulePrice7[2:]
            elif len(kamekCapsulePrice7) == 3:
                kamekCapsulePrice7 = "0" + kamekCapsulePrice7[2:]
        except:
            kamekCapsulePrice7 = "00"

        try:
            toadyCapsuleWeight7 = hex(int(toadyCapsuleWeight7))
            if len(toadyCapsuleWeight7) == 4:
                toadyCapsuleWeight7 = toadyCapsuleWeight7[2:]
            elif len(toadyCapsuleWeight7) == 3:
                toadyCapsuleWeight7 = "0" + toadyCapsuleWeight7[2:]
        except:
            toadyCapsuleWeight7 = "00"

        try:
            toadyCapsulePrice7 = hex(int(toadyCapsulePrice7))
            if len(toadyCapsulePrice7) == 4:
                toadyCapsulePrice7 = toadyCapsulePrice7[2:]
            elif len(toadyCapsulePrice7) == 3:
                toadyCapsulePrice7 = "0" + toadyCapsulePrice7[2:]
        except:
            toadyCapsulePrice7 = "00"

        try:
            blizzardCapsuleWeight7 = hex(int(blizzardCapsuleWeight7))
            if len(blizzardCapsuleWeight7) == 4:
                blizzardCapsuleWeight7 = blizzardCapsuleWeight7[2:]
            elif len(blizzardCapsuleWeight7) == 3:
                blizzardCapsuleWeight7 = "0" + blizzardCapsuleWeight7[2:]
        except:
            blizzardCapsuleWeight7 = "00"

        try:
            blizzardCapsulePrice7 = hex(int(blizzardCapsulePrice7))
            if len(blizzardCapsulePrice7) == 4:
                blizzardCapsulePrice7 = blizzardCapsulePrice7[2:]
            elif len(blizzardCapsulePrice7) == 3:
                blizzardCapsulePrice7 = "0" + blizzardCapsulePrice7[2:]
        except:
            blizzardCapsulePrice7 = "00"

        try:
            banditCapsuleWeight7 = hex(int(banditCapsuleWeight7))
            if len(banditCapsuleWeight7) == 4:
                banditCapsuleWeight7 = banditCapsuleWeight7[2:]
            elif len(banditCapsuleWeight7) == 3:
                banditCapsuleWeight7 = "0" + banditCapsuleWeight7[2:]
        except:
            banditCapsuleWeight7 = "00"

        try:
            banditCapsulePrice7 = hex(int(banditCapsulePrice7))
            if len(banditCapsulePrice7) == 4:
                banditCapsulePrice7 = banditCapsulePrice7[2:]
            elif len(banditCapsulePrice7) == 3:
                banditCapsulePrice7 = "0" + banditCapsulePrice7[2:]
        except:
            banditCapsulePrice7 = "00"

        try:
            pinkBooCapsuleWeight7 = hex(int(pinkBooCapsuleWeight7))
            if len(pinkBooCapsuleWeight7) == 4:
                pinkBooCapsuleWeight7 = pinkBooCapsuleWeight7[2:]
            elif len(pinkBooCapsuleWeight7) == 3:
                pinkBooCapsuleWeight7 = "0" + pinkBooCapsuleWeight7[2:]
        except:
            pinkBooCapsuleWeight7 = "00"

        try:
            pinkBooCapsulePrice7 = hex(int(pinkBooCapsulePrice7))
            if len(pinkBooCapsulePrice7) == 4:
                pinkBooCapsulePrice7 = pinkBooCapsulePrice7[2:]
            elif len(pinkBooCapsulePrice7) == 3:
                pinkBooCapsulePrice7 = "0" + pinkBooCapsulePrice7[2:]
        except:
            pinkBooCapsulePrice7 = "00"

        try:
            spinyCapsuleWeight7 = hex(int(spinyCapsuleWeight7))
            if len(spinyCapsuleWeight7) == 4:
                spinyCapsuleWeight7 = spinyCapsuleWeight7[2:]
            elif len(spinyCapsuleWeight7) == 3:
                spinyCapsuleWeight7 = "0" + spinyCapsuleWeight7[2:]
        except:
            spinyCapsuleWeight7 = "00"

        try:
            spinyCapsulePrice7 = hex(int(spinyCapsulePrice7))
            if len(spinyCapsulePrice7) == 4:
                spinyCapsulePrice7 = spinyCapsulePrice7[2:]
            elif len(spinyCapsulePrice7) == 3:
                spinyCapsulePrice7 = "0" + spinyCapsulePrice7[2:]
        except:
            spinyCapsulePrice7 = "00"

        try:
            zapCapsuleWeight7 = hex(int(zapCapsuleWeight7))
            if len(zapCapsuleWeight7) == 4:
                zapCapsuleWeight7 = zapCapsuleWeight7[2:]
            elif len(zapCapsuleWeight7) == 3:
                zapCapsuleWeight7 = "0" + zapCapsuleWeight7[2:]
        except:
            zapCapsuleWeight7 = "00"

        try:
            zapCapsulePrice7 = hex(int(zapCapsulePrice7))
            if len(zapCapsulePrice7) == 4:
                zapCapsulePrice7 = zapCapsulePrice7[2:]
            elif len(zapCapsulePrice7) == 3:
                zapCapsulePrice7 = "0" + zapCapsulePrice7[2:]
        except:
            zapCapsulePrice7 = "00"

        try:
            tweesterCapsuleWeight7 = hex(int(tweesterCapsuleWeight7))
            if len(tweesterCapsuleWeight7) == 4:
                tweesterCapsuleWeight7 = tweesterCapsuleWeight7[2:]
            elif len(tweesterCapsuleWeight7) == 3:
                tweesterCapsuleWeight7 = "0" + tweesterCapsuleWeight7[2:]
        except:
            tweesterCapsuleWeight7 = "00"

        try:
            tweesterCapsulePrice7 = hex(int(tweesterCapsulePrice7))
            if len(tweesterCapsulePrice7) == 4:
                tweesterCapsulePrice7 = tweesterCapsulePrice7[2:]
            elif len(tweesterCapsulePrice7) == 3:
                tweesterCapsulePrice7 = "0" + tweesterCapsulePrice7[2:]
        except:
            tweesterCapsulePrice7 = "00"

        try:
            thwompCapsuleWeight7 = hex(int(thwompCapsuleWeight7))
            if len(thwompCapsuleWeight7) == 4:
                thwompCapsuleWeight7 = thwompCapsuleWeight7[2:]
            elif len(thwompCapsuleWeight7) == 3:
                thwompCapsuleWeight7 = "0" + thwompCapsuleWeight7[2:]
        except:
            thwompCapsuleWeight7 = "00"

        try:
            thwompCapsulePrice7 = hex(int(thwompCapsulePrice7))
            if len(thwompCapsulePrice7) == 4:
                thwompCapsulePrice7 = thwompCapsulePrice7[2:]
            elif len(thwompCapsulePrice7) == 3:
                thwompCapsulePrice7 = "0" + thwompCapsulePrice7[2:]
        except:
            thwompCapsulePrice7 = "00"


        try:
            warpCapsuleWeight7 = hex(int(warpCapsuleWeight7))
            if len(warpCapsuleWeight7) == 4:
                warpCapsuleWeight7 = warpCapsuleWeight7[2:]
            elif len(warpCapsuleWeight7) == 3:
                warpCapsuleWeight7 = "0" + warpCapsuleWeight7[2:]
        except:
            warpCapsuleWeight7 = "00"

        try:
            warpCapsulePrice7 = hex(int(warpCapsulePrice7))
            if len(warpCapsulePrice7) == 4:
                warpCapsulePrice7 = warpCapsulePrice7[2:]
            elif len(warpCapsulePrice7) == 3:
                warpCapsulePrice7 = "0" + warpCapsulePrice7[2:]
        except:
            warpCapsulePrice7 = "00"

        try:
            bombCapsuleWeight7 = hex(int(bombCapsuleWeight7))
            if len(bombCapsuleWeight7) == 4:
                bombCapsuleWeight7 = bombCapsuleWeight7[2:]
            elif len(bombCapsuleWeight7) == 3:
                bombCapsuleWeight7 = "0" + bombCapsuleWeight7[2:]
        except:
            bombCapsuleWeight7 = "00"

        try:
            bombCapsulePrice7 = hex(int(bombCapsulePrice7))
            if len(bombCapsulePrice7) == 4:
                bombCapsulePrice7 = bombCapsulePrice7[2:]
            elif len(bombCapsulePrice7) == 3:
                bombCapsulePrice7 = "0" + bombCapsulePrice7[2:]
        except:
            bombCapsulePrice7 = "00"

        try:
            fireballCapsuleWeight7 = hex(int(fireballCapsuleWeight7))
            if len(fireballCapsuleWeight7) == 4:
                fireballCapsuleWeight7 = fireballCapsuleWeight7[2:]
            elif len(fireballCapsuleWeight7) == 3:
                fireballCapsuleWeight7 = "0" + fireballCapsuleWeight7[2:]
        except:
            fireballCapsuleWeight7 = "00"

        try:
            fireballCapsulePrice7 = hex(int(fireballCapsulePrice7))
            if len(fireballCapsulePrice7) == 4:
                fireballCapsulePrice7 = fireballCapsulePrice7[2:]
            elif len(fireballCapsulePrice7) == 3:
                fireballCapsulePrice7 = "0" + fireballCapsulePrice7[2:]
        except:
            fireballCapsulePrice7 = "00"

        try:
            flowerCapsuleWeight7 = hex(int(flowerCapsuleWeight7))
            if len(flowerCapsuleWeight7) == 4:
                flowerCapsuleWeight7 = flowerCapsuleWeight7[2:]
            elif len(flowerCapsuleWeight7) == 3:
                flowerCapsuleWeight7 = "0" + flowerCapsuleWeight7[2:]
        except:
            flowerCapsuleWeight7 = "00"

        try:
            flowerCapsulePrice7 = hex(int(flowerCapsulePrice7))
            if len(flowerCapsulePrice7) == 4:
                flowerCapsulePrice7 = flowerCapsulePrice7[2:]
            elif len(flowerCapsulePrice7) == 3:
                flowerCapsulePrice7 = "0" + flowerCapsulePrice7[2:]
        except:
            flowerCapsulePrice7 = "00"

        try:
            eggCapsuleWeight7 = hex(int(eggCapsuleWeight7))
            if len(eggCapsuleWeight7) == 4:
                eggCapsuleWeight7 = eggCapsuleWeight7[2:]
            elif len(eggCapsuleWeight7) == 3:
                eggCapsuleWeight7 = "0" + eggCapsuleWeight7[2:]
        except:
            eggCapsuleWeight7 = "00"

        try:
            eggCapsulePrice7 = hex(int(eggCapsulePrice7))
            if len(eggCapsulePrice7) == 4:
                eggCapsulePrice7 = eggCapsulePrice7[2:]
            elif len(eggCapsulePrice7) == 3:
                eggCapsulePrice7 = "0" + eggCapsulePrice7[2:]
        except:
            eggCapsulePrice7 = "00"

        try:
            vacuumCapsuleWeight7 = hex(int(vacuumCapsuleWeight7))
            if len(vacuumCapsuleWeight7) == 4:
                vacuumCapsuleWeight7 = vacuumCapsuleWeight7[2:]
            elif len(vacuumCapsuleWeight7) == 3:
                vacuumCapsuleWeight7 = "0" + vacuumCapsuleWeight7[2:]
        except:
            vacuumCapsuleWeight7 = "00"

        try:
            vacuumCapsulePrice7 = hex(int(vacuumCapsulePrice7))
            if len(vacuumCapsulePrice7) == 4:
                vacuumCapsulePrice7 = vacuumCapsulePrice7[2:]
            elif len(vacuumCapsulePrice7) == 3:
                vacuumCapsulePrice7 = "0" + vacuumCapsulePrice7[2:]
        except:
            vacuumCapsulePrice7 = "00"

        try:
            magicCapsuleWeight7 = hex(int(magicCapsuleWeight7))
            if len(magicCapsuleWeight7) == 4:
                magicCapsuleWeight7 = magicCapsuleWeight7[2:]
            elif len(magicCapsuleWeight7) == 3:
                magicCapsuleWeight7 = "0" + magicCapsuleWeight7[2:]
        except:
            magicCapsuleWeight7 = "00"

        try:
            magicCapsulePrice7 = hex(int(magicCapsulePrice7))
            if len(magicCapsulePrice7) == 4:
                magicCapsulePrice7 = magicCapsulePrice7[2:]
            elif len(magicCapsulePrice7) == 3:
                magicCapsulePrice7 = "0" + magicCapsulePrice7[2:]
        except:
            magicCapsulePrice7 = "00"
        
        try:
            tripleCapsuleWeight7 = hex(int(tripleCapsuleWeight7))
            if len(tripleCapsuleWeight7) == 4:
                tripleCapsuleWeight7 = tripleCapsuleWeight7[2:]
            elif len(tripleCapsuleWeight7) == 3:
                tripleCapsuleWeight7 = "0" + tripleCapsuleWeight7[2:]
        except:
            tripleCapsuleWeight7 = "00"

        try:
            tripleCapsulePrice7 = hex(int(tripleCapsulePrice7))
            if len(tripleCapsulePrice7) == 4:
                tripleCapsulePrice7 = tripleCapsulePrice7[2:]
            elif len(tripleCapsulePrice7) == 3:
                tripleCapsulePrice7 = "0" + tripleCapsulePrice7[2:]
        except:
            tripleCapsulePrice7 = "00"

        try:
            koopaCapsuleWeight7 = hex(int(koopaCapsuleWeight7))
            if len(koopaCapsuleWeight7) == 4:
                koopaCapsuleWeight7 = koopaCapsuleWeight7[2:]
            elif len(koopaCapsuleWeight7) == 3:
                koopaCapsuleWeight7 = "0" + koopaCapsuleWeight7[2:]
        except:
            koopaCapsuleWeight7 = "00"

        try:
            koopaCapsulePrice7 = hex(int(koopaCapsulePrice7))
            if len(koopaCapsulePrice7) == 4:
                koopaCapsulePrice7 = koopaCapsulePrice7[2:]
            elif len(koopaCapsulePrice7) == 3:
                koopaCapsulePrice7 = "0" + koopaCapsulePrice7[2:]
        except:
            koopaCapsulePrice7 = "00"

        generatedCode = getOrbModsSeven(mushroomCapsuleWeight7, goldenMushroomCapsulePrice7, goldenMushroomCapsuleWeight7, slowMushroomCapsulePrice7, slowMushroomCapsuleWeight7, metalMushroomCapsulePrice7, metalMushroomCapsuleWeight7, flutterCapsulePrice7, flutterCapsuleWeight7, cannonCapsulePrice7, cannonCapsuleWeight7, snackCapsulePrice7, snackCapsuleWeight7, lakituCapsulePrice7, lakituCapsuleWeight7, hammerBroCapsulePrice7, hammerBroCapsuleWeight7, plantCapsulePrice7, plantCapsuleWeight7, spearCapsulePrice7, spearCapsuleWeight7, kamekCapsulePrice7, kamekCapsuleWeight7, toadyCapsulePrice7, toadyCapsuleWeight7, blizzardCapsulePrice7, blizzardCapsuleWeight7, banditCapsulePrice7, banditCapsuleWeight7, pinkBooCapsulePrice7, pinkBooCapsuleWeight7, spinyCapsulePrice7, spinyCapsuleWeight7, zapCapsulePrice7, zapCapsuleWeight7, tweesterCapsulePrice7, tweesterCapsuleWeight7, thwompCapsulePrice7, thwompCapsuleWeight7, warpCapsulePrice7, warpCapsuleWeight7, bombCapsulePrice7, bombCapsuleWeight7, fireballCapsulePrice7, fireballCapsuleWeight7, flowerCapsulePrice7, flowerCapsuleWeight7, eggCapsulePrice7, eggCapsuleWeight7, vacuumCapsulePrice7, vacuumCapsuleWeight7, magicCapsulePrice7, magicCapsuleWeight7, tripleCapsulePrice7, tripleCapsuleWeight7, koopaCapsulePrice7, koopaCapsuleWeight7)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)

        print("Generated code copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)

    def mp1ButtonEvent(self):
        self.mario_party_1_button.configure(state="disabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 1")

    def mp2ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="disabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 2")

    def mp3ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="disabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 3")

    def mp4ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="disabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 4")

    def mp5ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="disabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 5")

    def mp6ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="disabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 6")

    def mp7ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="disabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 7")

    def mp8ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="disabled")
        self.mario_party_82_button.configure(state="enabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 8 (Rev. 1)")

    def mp82ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="disabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 8 (Rev. 2)")

    def creditsButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.credits_button.configure(state="disabled")
        self.reset_game_frames()
        self.create_game_frame("Credits")

if __name__ == "__main__":
    app = App()
    app.mainloop()