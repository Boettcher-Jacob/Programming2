import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("BlackJack2.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._Player1 = System.Windows.Forms.PictureBox()
		self._Player2 = System.Windows.Forms.PictureBox()
		self._Player3 = System.Windows.Forms.PictureBox()
		self._Player4 = System.Windows.Forms.PictureBox()
		self._Player5 = System.Windows.Forms.PictureBox()
		self._Gambler5 = System.Windows.Forms.PictureBox()
		self._Gambler4 = System.Windows.Forms.PictureBox()
		self._Gambler3 = System.Windows.Forms.PictureBox()
		self._Gambler2 = System.Windows.Forms.PictureBox()
		self._Gambler1 = System.Windows.Forms.PictureBox()
		self._PlayerLabel = System.Windows.Forms.Label()
		self._GamblerLabel = System.Windows.Forms.Label()
		self._House1 = System.Windows.Forms.PictureBox()
		self._House2 = System.Windows.Forms.PictureBox()
		self._CardAce = System.Windows.Forms.PictureBox()
		self._CardTwo = System.Windows.Forms.PictureBox()
		self._CardThree = System.Windows.Forms.PictureBox()
		self._CardSix = System.Windows.Forms.PictureBox()
		self._CardFive = System.Windows.Forms.PictureBox()
		self._CardFour = System.Windows.Forms.PictureBox()
		self._CardNine = System.Windows.Forms.PictureBox()
		self._CardEight = System.Windows.Forms.PictureBox()
		self._CardSeven = System.Windows.Forms.PictureBox()
		self._CardBack = System.Windows.Forms.PictureBox()
		self._CardTEn = System.Windows.Forms.PictureBox()
		self._BetButton = System.Windows.Forms.Button()
		self._TakeButton = System.Windows.Forms.Button()
		self._StayButton = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._HousePot = System.Windows.Forms.Label()
		self._label = System.Windows.Forms.Label()
		self._Gambler6 = System.Windows.Forms.PictureBox()
		self._Gambler7 = System.Windows.Forms.PictureBox()
		self._Player6 = System.Windows.Forms.PictureBox()
		self._Player7 = System.Windows.Forms.PictureBox()
		self._PlayerPot = System.Windows.Forms.Label()
		self._PlayerBet = System.Windows.Forms.TextBox()
		self._GamblerSecret = System.Windows.Forms.PictureBox()
		self._Player1.BeginInit()
		self._Player2.BeginInit()
		self._Player3.BeginInit()
		self._Player4.BeginInit()
		self._Player5.BeginInit()
		self._Gambler5.BeginInit()
		self._Gambler4.BeginInit()
		self._Gambler3.BeginInit()
		self._Gambler2.BeginInit()
		self._Gambler1.BeginInit()
		self._House1.BeginInit()
		self._House2.BeginInit()
		self._CardAce.BeginInit()
		self._CardTwo.BeginInit()
		self._CardThree.BeginInit()
		self._CardSix.BeginInit()
		self._CardFive.BeginInit()
		self._CardFour.BeginInit()
		self._CardNine.BeginInit()
		self._CardEight.BeginInit()
		self._CardSeven.BeginInit()
		self._CardBack.BeginInit()
		self._CardTEn.BeginInit()
		self._Gambler6.BeginInit()
		self._Gambler7.BeginInit()
		self._Player6.BeginInit()
		self._Player7.BeginInit()
		self._GamblerSecret.BeginInit()
		self.SuspendLayout()
		# 
		# Player1
		# 
		self._Player1.BackColor = System.Drawing.Color.Transparent
		self._Player1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._Player1.Location = System.Drawing.Point(12, 380)
		self._Player1.Name = "Player1"
		self._Player1.Size = System.Drawing.Size(109, 180)
		self._Player1.TabIndex = 0
		self._Player1.TabStop = False
		# 
		# Player2
		# 
		self._Player2.BackColor = System.Drawing.Color.DimGray
		self._Player2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._Player2.Location = System.Drawing.Point(52, 380)
		self._Player2.Name = "Player2"
		self._Player2.Size = System.Drawing.Size(109, 180)
		self._Player2.TabIndex = 1
		self._Player2.TabStop = False
		# 
		# Player3
		# 
		self._Player3.BackColor = System.Drawing.Color.Transparent
		self._Player3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._Player3.Location = System.Drawing.Point(92, 380)
		self._Player3.Name = "Player3"
		self._Player3.Size = System.Drawing.Size(109, 180)
		self._Player3.TabIndex = 2
		self._Player3.TabStop = False
		# 
		# Player4
		# 
		self._Player4.BackColor = System.Drawing.Color.DimGray
		self._Player4.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._Player4.Location = System.Drawing.Point(127, 380)
		self._Player4.Name = "Player4"
		self._Player4.Size = System.Drawing.Size(109, 180)
		self._Player4.TabIndex = 3
		self._Player4.TabStop = False
		# 
		# Player5
		# 
		self._Player5.BackColor = System.Drawing.Color.Transparent
		self._Player5.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._Player5.Location = System.Drawing.Point(167, 380)
		self._Player5.Name = "Player5"
		self._Player5.Size = System.Drawing.Size(109, 180)
		self._Player5.TabIndex = 4
		self._Player5.TabStop = False
		# 
		# Gambler5
		# 
		self._Gambler5.BackColor = System.Drawing.Color.Transparent
		self._Gambler5.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._Gambler5.Location = System.Drawing.Point(167, 12)
		self._Gambler5.Name = "Gambler5"
		self._Gambler5.Size = System.Drawing.Size(109, 180)
		self._Gambler5.TabIndex = 11
		self._Gambler5.TabStop = False
		# 
		# Gambler4
		# 
		self._Gambler4.BackColor = System.Drawing.Color.Transparent
		self._Gambler4.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._Gambler4.Location = System.Drawing.Point(127, 12)
		self._Gambler4.Name = "Gambler4"
		self._Gambler4.Size = System.Drawing.Size(109, 180)
		self._Gambler4.TabIndex = 10
		self._Gambler4.TabStop = False
		# 
		# Gambler3
		# 
		self._Gambler3.BackColor = System.Drawing.Color.Transparent
		self._Gambler3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._Gambler3.Location = System.Drawing.Point(92, 12)
		self._Gambler3.Name = "Gambler3"
		self._Gambler3.Size = System.Drawing.Size(109, 180)
		self._Gambler3.TabIndex = 9
		self._Gambler3.TabStop = False
		# 
		# Gambler2
		# 
		self._Gambler2.BackColor = System.Drawing.Color.Transparent
		self._Gambler2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._Gambler2.Location = System.Drawing.Point(52, 12)
		self._Gambler2.Name = "Gambler2"
		self._Gambler2.Size = System.Drawing.Size(109, 180)
		self._Gambler2.TabIndex = 8
		self._Gambler2.TabStop = False
		# 
		# Gambler1
		# 
		self._Gambler1.BackColor = System.Drawing.Color.Transparent
		self._Gambler1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._Gambler1.Location = System.Drawing.Point(12, 12)
		self._Gambler1.Name = "Gambler1"
		self._Gambler1.Size = System.Drawing.Size(109, 180)
		self._Gambler1.TabIndex = 7
		self._Gambler1.TabStop = False
		# 
		# PlayerLabel
		# 
		self._PlayerLabel.BackColor = System.Drawing.SystemColors.ControlLight
		self._PlayerLabel.Font = System.Drawing.Font("Microsoft Sans Serif", 24)
		self._PlayerLabel.Location = System.Drawing.Point(12, 314)
		self._PlayerLabel.Name = "PlayerLabel"
		self._PlayerLabel.Size = System.Drawing.Size(353, 63)
		self._PlayerLabel.TabIndex = 14
		self._PlayerLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._PlayerLabel.Click += self.PStateLabelClick
		# 
		# GamblerLabel
		# 
		self._GamblerLabel.BackColor = System.Drawing.SystemColors.ControlLight
		self._GamblerLabel.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._GamblerLabel.Location = System.Drawing.Point(12, 195)
		self._GamblerLabel.Name = "GamblerLabel"
		self._GamblerLabel.Size = System.Drawing.Size(353, 63)
		self._GamblerLabel.TabIndex = 15
		self._GamblerLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# House1
		# 
		self._House1.BackColor = System.Drawing.Color.Gold
		self._House1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._House1.Location = System.Drawing.Point(556, 170)
		self._House1.Name = "House1"
		self._House1.Size = System.Drawing.Size(109, 180)
		self._House1.TabIndex = 16
		self._House1.TabStop = False
		# 
		# House2
		# 
		self._House2.BackColor = System.Drawing.Color.Gold
		self._House2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._House2.Location = System.Drawing.Point(627, 195)
		self._House2.Name = "House2"
		self._House2.Size = System.Drawing.Size(109, 180)
		self._House2.TabIndex = 17
		self._House2.TabStop = False
		# 
		# CardAce
		# 
		self._CardAce.BackgroundImage = resources.GetObject("CardAce.BackgroundImage")
		self._CardAce.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom
		self._CardAce.Location = System.Drawing.Point(769, 523)
		self._CardAce.Name = "CardAce"
		self._CardAce.Size = System.Drawing.Size(21, 37)
		self._CardAce.TabIndex = 18
		self._CardAce.TabStop = False
		# 
		# CardTwo
		# 
		self._CardTwo.BackgroundImage = resources.GetObject("CardTwo.BackgroundImage")
		self._CardTwo.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom
		self._CardTwo.Location = System.Drawing.Point(742, 523)
		self._CardTwo.Name = "CardTwo"
		self._CardTwo.Size = System.Drawing.Size(21, 37)
		self._CardTwo.TabIndex = 19
		self._CardTwo.TabStop = False
		# 
		# CardThree
		# 
		self._CardThree.BackgroundImage = resources.GetObject("CardThree.BackgroundImage")
		self._CardThree.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom
		self._CardThree.Location = System.Drawing.Point(715, 523)
		self._CardThree.Name = "CardThree"
		self._CardThree.Size = System.Drawing.Size(21, 37)
		self._CardThree.TabIndex = 20
		self._CardThree.TabStop = False
		# 
		# CardSix
		# 
		self._CardSix.BackgroundImage = resources.GetObject("CardSix.BackgroundImage")
		self._CardSix.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom
		self._CardSix.Location = System.Drawing.Point(715, 480)
		self._CardSix.Name = "CardSix"
		self._CardSix.Size = System.Drawing.Size(21, 37)
		self._CardSix.TabIndex = 23
		self._CardSix.TabStop = False
		# 
		# CardFive
		# 
		self._CardFive.BackgroundImage = resources.GetObject("CardFive.BackgroundImage")
		self._CardFive.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom
		self._CardFive.Location = System.Drawing.Point(742, 480)
		self._CardFive.Name = "CardFive"
		self._CardFive.Size = System.Drawing.Size(21, 37)
		self._CardFive.TabIndex = 22
		self._CardFive.TabStop = False
		# 
		# CardFour
		# 
		self._CardFour.BackgroundImage = resources.GetObject("CardFour.BackgroundImage")
		self._CardFour.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom
		self._CardFour.Location = System.Drawing.Point(769, 480)
		self._CardFour.Name = "CardFour"
		self._CardFour.Size = System.Drawing.Size(21, 37)
		self._CardFour.TabIndex = 21
		self._CardFour.TabStop = False
		# 
		# CardNine
		# 
		self._CardNine.BackgroundImage = resources.GetObject("CardNine.BackgroundImage")
		self._CardNine.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom
		self._CardNine.Location = System.Drawing.Point(715, 437)
		self._CardNine.Name = "CardNine"
		self._CardNine.Size = System.Drawing.Size(21, 37)
		self._CardNine.TabIndex = 26
		self._CardNine.TabStop = False
		# 
		# CardEight
		# 
		self._CardEight.BackgroundImage = resources.GetObject("CardEight.BackgroundImage")
		self._CardEight.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom
		self._CardEight.Location = System.Drawing.Point(742, 437)
		self._CardEight.Name = "CardEight"
		self._CardEight.Size = System.Drawing.Size(21, 37)
		self._CardEight.TabIndex = 25
		self._CardEight.TabStop = False
		# 
		# CardSeven
		# 
		self._CardSeven.BackgroundImage = resources.GetObject("CardSeven.BackgroundImage")
		self._CardSeven.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom
		self._CardSeven.Location = System.Drawing.Point(769, 437)
		self._CardSeven.Name = "CardSeven"
		self._CardSeven.Size = System.Drawing.Size(21, 37)
		self._CardSeven.TabIndex = 24
		self._CardSeven.TabStop = False
		# 
		# CardBack
		# 
		self._CardBack.BackgroundImage = resources.GetObject("CardBack.BackgroundImage")
		self._CardBack.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._CardBack.Location = System.Drawing.Point(742, 394)
		self._CardBack.Name = "CardBack"
		self._CardBack.Size = System.Drawing.Size(21, 37)
		self._CardBack.TabIndex = 28
		self._CardBack.TabStop = False
		# 
		# CardTEn
		# 
		self._CardTEn.BackgroundImage = resources.GetObject("CardTEn.BackgroundImage")
		self._CardTEn.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom
		self._CardTEn.Location = System.Drawing.Point(769, 394)
		self._CardTEn.Name = "CardTEn"
		self._CardTEn.Size = System.Drawing.Size(21, 37)
		self._CardTEn.TabIndex = 27
		self._CardTEn.TabStop = False
		# 
		# BetButton
		# 
		self._BetButton.Location = System.Drawing.Point(371, 437)
		self._BetButton.Name = "BetButton"
		self._BetButton.Size = System.Drawing.Size(99, 32)
		self._BetButton.TabIndex = 29
		self._BetButton.Text = "Place Bet"
		self._BetButton.UseVisualStyleBackColor = True
		self._BetButton.Click += self.Button1Click
		# 
		# TakeButton
		# 
		self._TakeButton.Location = System.Drawing.Point(483, 420)
		self._TakeButton.Name = "TakeButton"
		self._TakeButton.Size = System.Drawing.Size(99, 32)
		self._TakeButton.TabIndex = 30
		self._TakeButton.Text = "Take Card"
		self._TakeButton.UseVisualStyleBackColor = True
		self._TakeButton.Click += self.TakeButtonClick
		# 
		# StayButton
		# 
		self._StayButton.Location = System.Drawing.Point(483, 458)
		self._StayButton.Name = "StayButton"
		self._StayButton.Size = System.Drawing.Size(99, 32)
		self._StayButton.TabIndex = 31
		self._StayButton.Text = "Stay "
		self._StayButton.UseVisualStyleBackColor = True
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(371, 480)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(99, 32)
		self._button4.TabIndex = 32
		self._button4.Text = "Attempt Steal"
		self._button4.UseVisualStyleBackColor = True
		# 
		# button5
		# 
		self._button5.Location = System.Drawing.Point(371, 523)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(99, 32)
		self._button5.TabIndex = 33
		self._button5.Text = "Attempt Peak"
		self._button5.UseVisualStyleBackColor = True
		# 
		# HousePot
		# 
		self._HousePot.BackColor = System.Drawing.SystemColors.ControlLight
		self._HousePot.Location = System.Drawing.Point(399, 278)
		self._HousePot.Name = "HousePot"
		self._HousePot.Size = System.Drawing.Size(100, 56)
		self._HousePot.TabIndex = 34
		self._HousePot.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label
		# 
		self._label.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label.Font = System.Drawing.Font("Microsoft YaHei UI", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label.Location = System.Drawing.Point(399, 229)
		self._label.Name = "label"
		self._label.Size = System.Drawing.Size(100, 38)
		self._label.TabIndex = 35
		self._label.Text = "HousePot"
		self._label.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# Gambler6
		# 
		self._Gambler6.BackColor = System.Drawing.Color.Transparent
		self._Gambler6.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._Gambler6.Location = System.Drawing.Point(207, 12)
		self._Gambler6.Name = "Gambler6"
		self._Gambler6.Size = System.Drawing.Size(109, 180)
		self._Gambler6.TabIndex = 12
		self._Gambler6.TabStop = False
		# 
		# Gambler7
		# 
		self._Gambler7.BackColor = System.Drawing.Color.Transparent
		self._Gambler7.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._Gambler7.Location = System.Drawing.Point(256, 12)
		self._Gambler7.Name = "Gambler7"
		self._Gambler7.Size = System.Drawing.Size(109, 180)
		self._Gambler7.TabIndex = 13
		self._Gambler7.TabStop = False
		# 
		# Player6
		# 
		self._Player6.BackColor = System.Drawing.Color.DimGray
		self._Player6.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._Player6.Location = System.Drawing.Point(207, 380)
		self._Player6.Name = "Player6"
		self._Player6.Size = System.Drawing.Size(109, 180)
		self._Player6.TabIndex = 5
		self._Player6.TabStop = False
		# 
		# Player7
		# 
		self._Player7.BackColor = System.Drawing.Color.Transparent
		self._Player7.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._Player7.Location = System.Drawing.Point(256, 380)
		self._Player7.Name = "Player7"
		self._Player7.Size = System.Drawing.Size(109, 180)
		self._Player7.TabIndex = 6
		self._Player7.TabStop = False
		# 
		# PlayerPot
		# 
		self._PlayerPot.BackColor = System.Drawing.SystemColors.ControlLight
		self._PlayerPot.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._PlayerPot.Location = System.Drawing.Point(483, 499)
		self._PlayerPot.Name = "PlayerPot"
		self._PlayerPot.Size = System.Drawing.Size(100, 28)
		self._PlayerPot.TabIndex = 36
		self._PlayerPot.Text = "200"
		self._PlayerPot.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# PlayerBet
		# 
		self._PlayerBet.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._PlayerBet.Location = System.Drawing.Point(482, 530)
		self._PlayerBet.Name = "PlayerBet"
		self._PlayerBet.Size = System.Drawing.Size(100, 31)
		self._PlayerBet.TabIndex = 37
		# 
		# GamblerSecret
		# 
		self._GamblerSecret.BackColor = System.Drawing.Color.Transparent
		self._GamblerSecret.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._GamblerSecret.Location = System.Drawing.Point(371, 12)
		self._GamblerSecret.Name = "GamblerSecret"
		self._GamblerSecret.Size = System.Drawing.Size(109, 180)
		self._GamblerSecret.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
		self._GamblerSecret.TabIndex = 38
		self._GamblerSecret.TabStop = False
		self._GamblerSecret.Visible = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(802, 572)
		self.Controls.Add(self._GamblerSecret)
		self.Controls.Add(self._Gambler1)
		self.Controls.Add(self._Gambler2)
		self.Controls.Add(self._Gambler3)
		self.Controls.Add(self._Gambler4)
		self.Controls.Add(self._Gambler5)
		self.Controls.Add(self._Player1)
		self.Controls.Add(self._Player2)
		self.Controls.Add(self._Player3)
		self.Controls.Add(self._Player4)
		self.Controls.Add(self._Player5)
		self.Controls.Add(self._PlayerBet)
		self.Controls.Add(self._PlayerPot)
		self.Controls.Add(self._label)
		self.Controls.Add(self._HousePot)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._StayButton)
		self.Controls.Add(self._TakeButton)
		self.Controls.Add(self._BetButton)
		self.Controls.Add(self._CardBack)
		self.Controls.Add(self._CardTEn)
		self.Controls.Add(self._CardNine)
		self.Controls.Add(self._CardEight)
		self.Controls.Add(self._CardSeven)
		self.Controls.Add(self._CardSix)
		self.Controls.Add(self._CardFive)
		self.Controls.Add(self._CardFour)
		self.Controls.Add(self._CardThree)
		self.Controls.Add(self._CardTwo)
		self.Controls.Add(self._CardAce)
		self.Controls.Add(self._House2)
		self.Controls.Add(self._House1)
		self.Controls.Add(self._GamblerLabel)
		self.Controls.Add(self._PlayerLabel)
		self.Controls.Add(self._Gambler6)
		self.Controls.Add(self._Player6)
		self.Controls.Add(self._Player7)
		self.Controls.Add(self._Gambler7)
		self.Name = "MainForm"
		self._Player1.EndInit()
		self._Player2.EndInit()
		self._Player3.EndInit()
		self._Player4.EndInit()
		self._Player5.EndInit()
		self._Gambler5.EndInit()
		self._Gambler4.EndInit()
		self._Gambler3.EndInit()
		self._Gambler2.EndInit()
		self._Gambler1.EndInit()
		self._House1.EndInit()
		self._House2.EndInit()
		self._CardAce.EndInit()
		self._CardTwo.EndInit()
		self._CardThree.EndInit()
		self._CardSix.EndInit()
		self._CardFive.EndInit()
		self._CardFour.EndInit()
		self._CardNine.EndInit()
		self._CardEight.EndInit()
		self._CardSeven.EndInit()
		self._CardBack.EndInit()
		self._CardTEn.EndInit()
		self._Gambler6.EndInit()
		self._Gambler7.EndInit()
		self._Player6.EndInit()
		self._Player7.EndInit()
		self._GamblerSecret.EndInit()
		self.ResumeLayout(False)
		self.PerformLayout()


	def PStateLabelClick(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		
		wallet = float(self._PlayerPot.Text)
		bet = float(self._PlayerBet.Text)
		rnd = System.Random()
		
		Back = self._CardBack.BackgroundImage
		Ace = self._CardAce.BackgroundImage
		Two = self._CardTwo.BackgroundImage
		Three = self._CardThree.BackgroundImage
		Four = self._CardFour.BackgroundImage
		Five = self._CardFive.BackgroundImage
		Six = self._CardSix.BackgroundImage
		Seven = self._CardSeven.BackgroundImage
		Eight = self._CardEight.BackgroundImage
		Nine = self._CardNine.BackgroundImage
		Ten = self._CardTEn.BackgroundImage
		
		self._GamblerSecret.BackgroundImage == Back
		
		if bet < 1:
			MessageBox.Show("You must bet atleast 1 dollar.")
		elif bet > wallet:
			MessageBox.Show("You don't have the funds for that bet")
		elif wallet >= bet:
			self._PlayerPot.Text = str(wallet - bet)
			self._HousePot.Text = str(bet)
			
		#Player's Deck
		
			P1 = rnd.Next(1,11)
			P2 = rnd.Next(1,11)
			G2 = rnd.Next(1,11)
		
			if P1 == 1:
				self._Player1.BackgroundImage = Ace
			if P1 == 2:
				self._Player1.BackgroundImage = Two
			if P1 == 3:
				self._Player1.BackgroundImage = Three
			if P1 == 4:
				self._Player1.BackgroundImage = Four
			if P1 == 5:
				self._Player1.BackgroundImage = Five
			if P1 == 6:
				self._Player1.BackgroundImage = Six
			if P1 == 7:
				self._Player1.BackgroundImage = Seven
			if P1 == 8:
				self._Player1.BackgroundImage = Eight
			if P1 == 9:
				self._Player1.BackgroundImage = Nine
			if P1 == 10:
				self._Player1.BackgroundImage = Ten
				
			if P2 == 1:
				self._Player2.BackgroundImage = Ace
			if P2 == 2:
				self._Player2.BackgroundImage = Two
			if P2 == 3:
				self._Player2.BackgroundImage = Three
			if P2 == 4:
				self._Player2.BackgroundImage = Four
			if P2 == 5:
				self._Player2.BackgroundImage = Five
			if P2 == 6:
				self._Player2.BackgroundImage = Six
			if P2 == 7:
				self._Player2.BackgroundImage = Seven
			if P2 == 8:
				self._Player2.BackgroundImage = Eight
			if P2 == 9:
				self._Player2.BackgroundImage = Nine
			if P2 == 10:
				self._Player2.BackgroundImage = Ten

			self._Player3.BackgroundImage = Back
			self._Player4.BackgroundImage = Back
			self._Player5.BackgroundImage = Back
			self._Player6.BackgroundImage = Back
			self._Player7.BackgroundImage = Back
			
			self._Gambler1.BackgroundImage = Back
			self._Gambler3.BackgroundImage = Back
			self._Gambler4.BackgroundImage = Back
			self._Gambler5.BackgroundImage = Back
			self._Gambler6.BackgroundImage = Back
			self._Gambler7.BackgroundImage = Back
			
			if G2 == 1:
				self._Gambler2.BackgroundImage = Ace
			if G2 == 2:
				self._Gambler2.BackgroundImage = Two
			if G2 == 3:
				self._Gambler2.BackgroundImage= Three
			if G2 == 4:
				self._Gambler2.BackgroundImage= Four
			if G2 == 5:
				self._Gambler2.BackgroundImage= Five
			if G2 == 6:
				self._Gambler2.BackgroundImage= Six
			if G2 == 7:
				self._Gambler2.BackgroundImage= Seven
			if G2 == 8:
				self._Gambler2.BackgroundImage = Eight
			if G2 == 9:
				self._Gambler2.BackgroundImage = Nine
			if G2 == 10:
				self._Gambler2.BackgroundImage = Ten
				
			H2 = rnd.Next(1,11)
				
			self._House1.BackgroundImage = Back
			
			if H2 == 1:
				self._House2.BackgroundImage = Ace
			if H2 == 2:
				self._House2.BackgroundImage = Two
			if H2 == 3:
				self._House2.BackgroundImage= Three
			if H2 == 4:
				self._House2.BackgroundImage= Four
			if H2 == 5:
				self._House2.BackgroundImage= Five
			if H2 == 6:
				self._House2.BackgroundImage= Six
			if H2 == 7:
				self._House2.BackgroundImage= Seven
			if H2 == 8:
				self._House2.BackgroundImage = Eight
			if H2 == 9:
				self._House2.BackgroundImage = Nine
			if H2 == 10:
				self._House2.BackgroundImage = Ten
			
				
				
			self._BetButton.Visible = False
			self._TakeButton.Visible = True
			self._StayButton.Visible = True

	def TakeButtonClick(self, sender, e):
		rnd = System.Random()
		PC1 = 0
		PC2 = 0
		PC3 = 0 
		PC4 = 0
		PC5 = 0 
		PC6 = 0
		PC7 = 0
		
		GC1 = 0
		GC2 = 0
		GC3 = 0
		GC4 = 0
		GC5 = 0
		GC6 = 0
		GC7 = 0
	
		self._PlayerLabel.Text = "Hit Me"
		
		Back = self._CardBack.BackgroundImage
		Ace = self._CardAce.BackgroundImage
		Two = self._CardTwo.BackgroundImage
		Three = self._CardThree.BackgroundImage
		Four = self._CardFour.BackgroundImage
		Five = self._CardFive.BackgroundImage
		Six = self._CardSix.BackgroundImage
		Seven = self._CardSeven.BackgroundImage
		Eight = self._CardEight.BackgroundImage
		Nine = self._CardNine.BackgroundImage
		Ten = self._CardTEn.BackgroundImage
		
		
		if self._Player3.BackgroundImage == Back:
			P3 = rnd.Next(1,11)
			if P3 == 1:
				self._Player3.BackgroundImage = Ace
			if P3 == 2:
				self._Player3.BackgroundImage = Two
			if P3 == 3:
				self._Player3.BackgroundImage = Three
			if P3 == 4:
				self._Player3.BackgroundImage = Four
			if P3 == 5:
				self._Player3.BackgroundImage = Five
			if P3 == 6:
				self._Player3.BackgroundImage = Six
			if P3 == 7:
				self._Player3.BackgroundImage = Seven
			if P3 == 8:
				self._Player3.BackgroundImage = Eight
			if P3 == 9:
				self._Player3.BackgroundImage = Nine
			if P3 == 10:
				self._Player3.BackgroundImage = Ten
				
		elif self._Player4.BackgroundImage == Back:
			P4 = rnd.Next(1,11)
			if P4 == 1:
				self._Player4.BackgroundImage = Ace
			if P4 == 2:
				self._Player4.BackgroundImage = Two
			if P4 == 3:
				self._Player4.BackgroundImage = Three
			if P4 == 4:
				self._Player4.BackgroundImage = Four
			if P4 == 5:
				self._Player4.BackgroundImage = Five
			if P4 == 6:
				self._Player4.BackgroundImage = Six
			if P4 == 7:
				self._Player4.BackgroundImage = Seven
			if P4 == 8:
				self._Player4.BackgroundImage = Eight
			if P4 == 9:
				self._Player4.BackgroundImage = Nine
			if P4 == 10:
				self._Player4.BackgroundImage = Ten
				
		elif self._Player5.BackgroundImage == Back:
			P5 = rnd.Next(1,11)
			if P5 == 1:
				self._Player5.BackgroundImage = Ace
			if P5 == 2:
				self._Player5.BackgroundImage = Two
			if P5 == 3:
				self._Player5.BackgroundImage = Three
			if P5 == 4:
				self._Player5.BackgroundImage = Four
			if P5 == 5:
				self._Player5.BackgroundImage = Five
			if P5 == 6:
				self._Player5.BackgroundImage = Six
			if P5 == 7:
				self._Player5.BackgroundImage = Seven
			if P5 == 8:
				self._Player5.BackgroundImage = Eight
			if P5 == 9:
				self._Player5.BackgroundImage = Nine
			if P5 == 10:
				self._Player5.BackgroundImage = Ten
				
		elif self._Player6.BackgroundImage == Back:
			P6 = rnd.Next(1,11)
			if P6 == 1:
				self._Player6.BackgroundImage = Ace
			if P6 == 2:
				self._Player6.BackgroundImage = Two
			if P6 == 3:
				self._Player6.BackgroundImage = Three
			if P6 == 4:
				self._Player6.BackgroundImage = Four
			if P6 == 5:
				self._Player6.BackgroundImage = Five
			if P6 == 6:
				self._Player6.BackgroundImage = Six
			if P6 == 7:
				self._Player6.BackgroundImage = Seven
			if P6 == 8:
				self._Player6.BackgroundImage = Eight
			if P6 == 9:
				self._Player6.BackgroundImage = Nine
			if P6 == 10:
				self._Player6.BackgroundImage = Ten
				
		elif self._Player7.BackgroundImage == Back:
			P7 = rnd.Next(1,11)
			if P7 == 1:
				self._Player7.BackgroundImage = Ace
			if P7 == 2:
				self._Player7.BackgroundImage = Two
			if P7 == 3:
				self._Player7.BackgroundImage = Three
			if P7 == 4:
				self._Player7.BackgroundImage = Four
			if P7 == 5:
				self._Player7.BackgroundImage = Five
			if P7 == 6:
				self._Player7.BackgroundImage = Six
			if P7 == 7:
				self._Player7.BackgroundImage = Seven
			if P7 == 8:
				self._Player7.BackgroundImage = Eight
			if P7 == 9:
				self._Player7.BackgroundImage = Nine
			if P7 == 10:
				self._Player7.BackgroundImage = Ten
				
				
	# The Gambler's Turn
		GS = rnd.Next(1,11)
		G2 = rnd.Next(1,11)
		G3 = rnd.Next(1,11)		
		G4 = rnd.Next(1,11)
		G5 = rnd.Next(1,11)
		G6 = rnd.Next(1,11)
		G7 = rnd.Next(1,11)
		
		GScore = GC1 + GC2 + GC3 + GC4 + GC5 + GC6 + GC7
		
		GC1=0
		GC2=0
		GC3=0
		GC4=0
		GC5=0
		GC6=0
		GC7=0
		
		if self._GamblerSecret.BackgroundImage == Back:
			if GS == 1:
				self._GamblerSecret.BackgroundImage = Ace
			elif GS == 2:
				self._GamblerSecret.BackgroundImage = Two
			elif GS == 3:
				self._GamblerSecret.BackgroundImage= Three
			elif GS == 4:
				self._GamblerSecret.BackgroundImage= Four
			elif GS == 5:
				self._GamblerSecret.BackgroundImage= Five
			elif GS == 6:
				self._GamblerSecret.BackgroundImage= Six
			elif GS == 7:
				self._GamblerSecret.BackgroundImage= Seven
			elif GS == 8:	
				self._GamblerSecret.BackgroundImage = Eight
			elif GS == 9:
				self._GamblerSecret.BackgroundImage = Nine
			elif GS == 10:
				self._GamblerSecret.BackgroundImage = Ten
		
		
		if self._GamblerSecret.BackgroundImage == Ace:
			GC1 = 11
		if self._GamblerSecret.BackgroundImage == Two:
			GC1 = 2
		if self._GamblerSecret.BackgroundImage == Three:
			GC1 = 3
		if self._GamblerSecret.BackgroundImage == Four:
			GC1 = 4
		if self._GamblerSecret.BackgroundImage == Five:
			GC1 = 5
		if self._GamblerSecret.BackgroundImage == Six:
			GC1 = 6
		if self._GamblerSecret.BackgroundImage == Seven:
			GC1 = 7
		if self._GamblerSecret.BackgroundImage == Eight:
			GC1 = 8
		if self._GamblerSecret.BackgroundImage == Nine:
			GC1 = 9	
		if self._GamblerSecret.BackgroundImage == Ten:
			GC1 = 10
				
		if self._GamblerSecret.BackgroundImage == Ace:
			GC2 = 11
		if self._Gambler2.BackgroundImage == Two:
			GC2 = 2
		if self._Gambler2.BackgroundImage == Three:
			GC2 = 3
		if self._Gambler2.BackgroundImage == Four:
			GC2 = 4
		if self._Gambler2.BackgroundImage == Five:
			GC2 = 5
		if self._Gambler2.BackgroundImage == Six:
			GC2 = 6
		if self._Gambler2.BackgroundImage == Seven:
			GC2 = 7
		if self._Gambler2.BackgroundImage == Eight:
			GC2 = 8
		if self._Gambler2.BackgroundImage == Nine:
			GC2 = 9
		if self._Gambler2.BackgroundImage == Ten:
			GC2 = 10
				
			GScore = GC1 + GC2 
			
			GCollect = GScore + GC3 + GC4 + GC5 + GC6 + GC7
			
		if GScore <= 21:
			self._GamblerLabel.Text = "Hit Me"
					
			if self._Gambler3.BackgroundImage == Back:
				if G3 == 1:
					self._Gambler3.BackgroundImage = Ace
					if GCollect > 10:
						G3 = 1
					else:
						G3 = 11
				if G3 == 2:
					self._Gambler3.BackgroundImage = Two
					G3 = 2
				if G3 == 3:
					self._Gambler3.BackgroundImage = Three
					G3 = 3
				if G3 == 4:
					self._Gambler3.BackgroundImage = Four
					G3 = 4
				if G3 == 5:
					self._Gambler3.BackgroundImage = Five
					G3 = 5
				if G3 == 6:
					self._Gambler3.BackgroundImage = Six
					G3 = 6
				if G3 == 7:
					self._Gambler3.BackgroundImage = Seven
					G3 = 7
				if G3 == 8:
					self._Gambler3.BackgroundImage = Eight
					G3 = 8
				if G3 == 9:
					self._Gambler3.BackgroundImage = Nine
					G3 = 9
				if G3 == 10:
					self._Gambler3.BackgroundImage = Ten
					G3 = 10
					
			elif self._Gambler4.BackgroundImage == Back:
                if G4 == 1:
                    self._Gambler4.BackgroundImage = Ace
                    if GCollect > 10:
                        G4 = 1
                    else:
                        G4 = 11
                if G4 == 2:
                    self._Gambler4.BackgroundImage = Two
                    G4 = 2
                if G4 == 3:
                    self._Gambler4.BackgroundImage = Three
                    G4 = 3
                if G4 == 4:
                    self._Gambler4.BackgroundImage = Four
                    G4 = 4
                if G4 == 5:
                    self._Gambler4.BackgroundImage = Five
                    G4 = 5
                if G4 == 6:
                    self._Gambler4.BackgroundImage = Six
                    G4 = 6
                if G4 == 7:
                    self._Gambler4.BackgroundImage = Seven
                    G4 = 7
                if G4 == 8:
                    self._Gambler4.BackgroundImage = Eight
                    G4 = 8
                if G4 == 9:
                    self._Gambler4.BackgroundImage = Nine
                    G4 = 9
                if G4 == 10:
                    self._Gambler4.BackgroundImage = Ten
                    G4 = 10
					
			elif self._Gambler5.BackgroundImage == Back:                
                if G5 == 1:
                    self._Gambler5.BackgroundImage = Ace
                    if GCollect > 10:
                        G5 = 1
                    else:
                        G5 = 11
                if G5 == 2:
                    self._Gambler5.BackgroundImage = Two
                    G5 = 2
                if G5 == 3:
                    self._Gambler5.BackgroundImage = Three
                    G5 = 3
                if G5 == 4:
                    self._Gambler5.BackgroundImage = Four
                    G5 = 4
                if G5 == 5:
                    self._Gambler5.BackgroundImage = Five
                    G5 = 5
                if G5 == 6:
                    self._Gambler5.BackgroundImage = Six
                    G5 = 6
                if G5 == 7:
                    self._Gambler5.BackgroundImage = Seven
                    G5 = 7
                if G5 == 8:
                    self._Gambler5.BackgroundImage = Eight
                    G5 = 8
                if G5 == 9:
                    self._Gambler5.BackgroundImage = Nine
                    G5 = 9
                if G5 == 10:
                    self._Gambler5.BackgroundImage = Ten
                    G5 = 10

						
			elif self._Gambler6.BackgroundImage == Back:
                	if G6 == 1:
                    self._Gambler6.BackgroundImage = Ace
                    if GCollect > 10:
                        G6 = 1
                    else:
                        G6 = 11
                if G6 == 2:
                    self._Gambler6.BackgroundImage = Two
                    G6 = 2
                if G6 == 3:
                    self._Gambler6.BackgroundImage = Three
                    G6 = 3
                if G6 == 4:
                    self._Gambler6.BackgroundImage = Four
                    G6 = 4
                if G6 == 5:
                    self._Gambler6.BackgroundImage = Five
                    G6 = 5
                if G6 == 6:
                    self._Gambler6.BackgroundImage = Six
                    G6 = 6
                if G6 == 7:
                    self._Gambler6.BackgroundImage = Seven
                    G6 = 7
                if G6 == 8:
                    self._Gambler6.BackgroundImage = Eight
                    G6 = 8
                if G6 == 9:
                    self._Gambler6.BackgroundImage = Nine
                    G6 = 9
                if G6 == 10:
                    self._Gambler6.BackgroundImage = Ten
                    G6 = 10
						
			elif self._Gambler7.BackgroundImage == Back:
                	if G7 == 1:
                    self._Gambler7.BackgroundImage = Ace
                    if GCollect > 10:
                        G7 = 1
                    else:
                        G7 = 11
                if G7 == 2:
                    self._Gambler7.BackgroundImage = Two
                    G7 = 2
                if G7 == 3:
                    self._Gambler7.BackgroundImage = Three
                    G7 = 3
                if G7 == 4:
                    self._Gambler7.BackgroundImage = Four
                    G7 = 4
                if G7 == 5:
                    self._Gambler7.BackgroundImage = Five
                    G7 = 5
                if G7 == 6:
                    self._Gambler7.BackgroundImage = Six
                    G7 = 6
                if G7 == 7:
                    self._Gambler7.BackgroundImage = Seven
                    G7 = 7
                if G7 == 8:
                    self._Gambler7.BackgroundImage = Eight
                    G7 = 8
                if G7 == 9:
                    self._Gambler7.BackgroundImage = Nine
                    G7 = 9
                if G7 == 10:
                    self._Gambler7.BackgroundImage = Ten
                    G7 = 10
		else:
				self._GamblerLabel.Text = "I'll Stay"

			
	
	