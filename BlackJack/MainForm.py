import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("BlackJack.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._DealerPic = System.Windows.Forms.PictureBox()
		self._DealCard1 = System.Windows.Forms.PictureBox()
		self._DealCard2 = System.Windows.Forms.PictureBox()
		self._PlayCard1 = System.Windows.Forms.PictureBox()
		self._PlayCard2 = System.Windows.Forms.PictureBox()
		self._PlayCard3 = System.Windows.Forms.PictureBox()
		self._moneylbl = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._wallet = System.Windows.Forms.Label()
		self._ButtonGamble = System.Windows.Forms.Button()
		self._ButtonHit = System.Windows.Forms.Button()
		self._ButtonStay = System.Windows.Forms.Button()
		self._ButtonSteal = System.Windows.Forms.Button()
		self._ButtonQuit = System.Windows.Forms.Button()
		self._PicAce = System.Windows.Forms.PictureBox()
		self._PicTwo = System.Windows.Forms.PictureBox()
		self._PicThre = System.Windows.Forms.PictureBox()
		self._PicFor = System.Windows.Forms.PictureBox()
		self._PicFiv = System.Windows.Forms.PictureBox()
		self._PicSix = System.Windows.Forms.PictureBox()
		self._PicSev = System.Windows.Forms.PictureBox()
		self._PicNin = System.Windows.Forms.PictureBox()
		self._PicTen = System.Windows.Forms.PictureBox()
		self._PicAte = System.Windows.Forms.PictureBox()
		self._PicBak = System.Windows.Forms.PictureBox()
		self._textBet = System.Windows.Forms.TextBox()
		self._DealChat = System.Windows.Forms.Label()
		self._ButtonWarn = System.Windows.Forms.Button()
		self._Wins = System.Windows.Forms.Label()
		self._TotalWins = System.Windows.Forms.Label()
		self._TotalLosses = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._DealerPic.BeginInit()
		self._DealCard1.BeginInit()
		self._DealCard2.BeginInit()
		self._PlayCard1.BeginInit()
		self._PlayCard2.BeginInit()
		self._PlayCard3.BeginInit()
		self._PicAce.BeginInit()
		self._PicTwo.BeginInit()
		self._PicThre.BeginInit()
		self._PicFor.BeginInit()
		self._PicFiv.BeginInit()
		self._PicSix.BeginInit()
		self._PicSev.BeginInit()
		self._PicNin.BeginInit()
		self._PicTen.BeginInit()
		self._PicAte.BeginInit()
		self._PicBak.BeginInit()
		self.SuspendLayout()
		# 
		# DealerPic
		# 
		self._DealerPic.BackColor = System.Drawing.Color.White
		self._DealerPic.BackgroundImage = resources.GetObject("DealerPic.BackgroundImage")
		self._DealerPic.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._DealerPic.Cursor = System.Windows.Forms.Cursors.Arrow
		self._DealerPic.Location = System.Drawing.Point(321, 13)
		self._DealerPic.Name = "DealerPic"
		self._DealerPic.Size = System.Drawing.Size(172, 207)
		self._DealerPic.TabIndex = 1
		self._DealerPic.TabStop = False
		# 
		# DealCard1
		# 
		self._DealCard1.BackColor = System.Drawing.Color.FromArgb(64, 0, 0)
		self._DealCard1.Location = System.Drawing.Point(13, 13)
		self._DealCard1.Name = "DealCard1"
		self._DealCard1.Size = System.Drawing.Size(148, 207)
		self._DealCard1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._DealCard1.TabIndex = 2
		self._DealCard1.TabStop = False
		# 
		# DealCard2
		# 
		self._DealCard2.BackColor = System.Drawing.Color.FromArgb(64, 0, 0)
		self._DealCard2.Location = System.Drawing.Point(167, 13)
		self._DealCard2.Name = "DealCard2"
		self._DealCard2.Size = System.Drawing.Size(148, 207)
		self._DealCard2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._DealCard2.TabIndex = 3
		self._DealCard2.TabStop = False
		# 
		# PlayCard1
		# 
		self._PlayCard1.BackColor = System.Drawing.Color.FromArgb(64, 0, 0)
		self._PlayCard1.Location = System.Drawing.Point(13, 275)
		self._PlayCard1.Name = "PlayCard1"
		self._PlayCard1.Size = System.Drawing.Size(148, 207)
		self._PlayCard1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._PlayCard1.TabIndex = 4
		self._PlayCard1.TabStop = False
		# 
		# PlayCard2
		# 
		self._PlayCard2.BackColor = System.Drawing.Color.FromArgb(64, 0, 0)
		self._PlayCard2.Location = System.Drawing.Point(167, 275)
		self._PlayCard2.Name = "PlayCard2"
		self._PlayCard2.Size = System.Drawing.Size(148, 207)
		self._PlayCard2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._PlayCard2.TabIndex = 5
		self._PlayCard2.TabStop = False
		# 
		# PlayCard3
		# 
		self._PlayCard3.BackColor = System.Drawing.Color.FromArgb(64, 0, 0)
		self._PlayCard3.Location = System.Drawing.Point(321, 275)
		self._PlayCard3.Name = "PlayCard3"
		self._PlayCard3.Size = System.Drawing.Size(148, 207)
		self._PlayCard3.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._PlayCard3.TabIndex = 6
		self._PlayCard3.TabStop = False
		# 
		# moneylbl
		# 
		self._moneylbl.BackColor = System.Drawing.Color.FromArgb(221, 245, 245)
		self._moneylbl.Font = System.Drawing.Font("Rockwell", 20)
		self._moneylbl.ForeColor = System.Drawing.Color.Black
		self._moneylbl.Location = System.Drawing.Point(500, 9)
		self._moneylbl.Name = "moneylbl"
		self._moneylbl.Size = System.Drawing.Size(129, 63)
		self._moneylbl.TabIndex = 8
		self._moneylbl.Text = "Wallet:"
		self._moneylbl.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(221, 245, 245)
		self._label2.Font = System.Drawing.Font("Rockwell", 20)
		self._label2.ForeColor = System.Drawing.Color.Black
		self._label2.Location = System.Drawing.Point(499, 87)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(130, 64)
		self._label2.TabIndex = 9
		self._label2.Text = "Player's Bet:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# wallet
		# 
		self._wallet.BackColor = System.Drawing.Color.FromArgb(221, 245, 245)
		self._wallet.Font = System.Drawing.Font("Rockwell", 20)
		self._wallet.ForeColor = System.Drawing.Color.Black
		self._wallet.Location = System.Drawing.Point(635, 9)
		self._wallet.Name = "wallet"
		self._wallet.Size = System.Drawing.Size(140, 63)
		self._wallet.TabIndex = 11
		self._wallet.Text = "200"
		self._wallet.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# ButtonGamble
		# 
		self._ButtonGamble.BackColor = System.Drawing.Color.FromArgb(198, 14, 14)
		self._ButtonGamble.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._ButtonGamble.Font = System.Drawing.Font("Showcard Gothic", 15)
		self._ButtonGamble.ForeColor = System.Drawing.Color.FromArgb(255, 239, 0)
		self._ButtonGamble.Location = System.Drawing.Point(535, 154)
		self._ButtonGamble.Name = "ButtonGamble"
		self._ButtonGamble.Size = System.Drawing.Size(195, 50)
		self._ButtonGamble.TabIndex = 12
		self._ButtonGamble.Text = "Gamble"
		self._ButtonGamble.UseVisualStyleBackColor = False
		self._ButtonGamble.Click += self.ButtonGambleClick
		# 
		# ButtonHit
		# 
		self._ButtonHit.BackColor = System.Drawing.Color.FromArgb(198, 14, 14)
		self._ButtonHit.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._ButtonHit.Font = System.Drawing.Font("Showcard Gothic", 15)
		self._ButtonHit.ForeColor = System.Drawing.Color.FromArgb(255, 239, 0)
		self._ButtonHit.Location = System.Drawing.Point(535, 210)
		self._ButtonHit.Name = "ButtonHit"
		self._ButtonHit.Size = System.Drawing.Size(89, 45)
		self._ButtonHit.TabIndex = 13
		self._ButtonHit.Text = "Hit"
		self._ButtonHit.UseVisualStyleBackColor = False
		self._ButtonHit.Visible = False
		self._ButtonHit.Click += self.ButtonHitClick
		# 
		# ButtonStay
		# 
		self._ButtonStay.BackColor = System.Drawing.Color.FromArgb(198, 14, 14)
		self._ButtonStay.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._ButtonStay.Font = System.Drawing.Font("Showcard Gothic", 15)
		self._ButtonStay.ForeColor = System.Drawing.Color.FromArgb(255, 239, 0)
		self._ButtonStay.Location = System.Drawing.Point(630, 210)
		self._ButtonStay.Name = "ButtonStay"
		self._ButtonStay.Size = System.Drawing.Size(100, 45)
		self._ButtonStay.TabIndex = 14
		self._ButtonStay.Text = "Stay"
		self._ButtonStay.UseVisualStyleBackColor = False
		self._ButtonStay.Visible = False
		self._ButtonStay.Click += self.ButtonStayClick
		# 
		# ButtonSteal
		# 
		self._ButtonSteal.BackColor = System.Drawing.Color.FromArgb(198, 14, 14)
		self._ButtonSteal.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._ButtonSteal.Font = System.Drawing.Font("Showcard Gothic", 15)
		self._ButtonSteal.ForeColor = System.Drawing.Color.FromArgb(255, 239, 0)
		self._ButtonSteal.Location = System.Drawing.Point(535, 261)
		self._ButtonSteal.Name = "ButtonSteal"
		self._ButtonSteal.Size = System.Drawing.Size(195, 63)
		self._ButtonSteal.TabIndex = 15
		self._ButtonSteal.Text = "PickPocket"
		self._ButtonSteal.UseVisualStyleBackColor = False
		self._ButtonSteal.Click += self.ButtonStealClick
		# 
		# ButtonQuit
		# 
		self._ButtonQuit.BackColor = System.Drawing.Color.FromArgb(198, 14, 14)
		self._ButtonQuit.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._ButtonQuit.Font = System.Drawing.Font("Showcard Gothic", 15)
		self._ButtonQuit.ForeColor = System.Drawing.Color.FromArgb(255, 239, 0)
		self._ButtonQuit.Location = System.Drawing.Point(535, 330)
		self._ButtonQuit.Name = "ButtonQuit"
		self._ButtonQuit.Size = System.Drawing.Size(195, 54)
		self._ButtonQuit.TabIndex = 16
		self._ButtonQuit.Text = "Cashout"
		self._ButtonQuit.UseVisualStyleBackColor = False
		self._ButtonQuit.Click += self.ButtonQuitClick
		# 
		# PicAce
		# 
		self._PicAce.BackgroundImage = resources.GetObject("PicAce.BackgroundImage")
		self._PicAce.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._PicAce.Image = resources.GetObject("PicAce.Image")
		self._PicAce.Location = System.Drawing.Point(655, 446)
		self._PicAce.Name = "PicAce"
		self._PicAce.Size = System.Drawing.Size(30, 36)
		self._PicAce.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._PicAce.TabIndex = 17
		self._PicAce.TabStop = False
		self._PicAce.Visible = False
		# 
		# PicTwo
		# 
		self._PicTwo.BackgroundImage = resources.GetObject("PicTwo.BackgroundImage")
		self._PicTwo.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._PicTwo.Image = resources.GetObject("PicTwo.Image")
		self._PicTwo.Location = System.Drawing.Point(619, 446)
		self._PicTwo.Name = "PicTwo"
		self._PicTwo.Size = System.Drawing.Size(30, 36)
		self._PicTwo.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._PicTwo.TabIndex = 18
		self._PicTwo.TabStop = False
		self._PicTwo.Visible = False
		# 
		# PicThre
		# 
		self._PicThre.BackgroundImage = resources.GetObject("PicThre.BackgroundImage")
		self._PicThre.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._PicThre.Image = resources.GetObject("PicThre.Image")
		self._PicThre.Location = System.Drawing.Point(583, 446)
		self._PicThre.Name = "PicThre"
		self._PicThre.Size = System.Drawing.Size(30, 36)
		self._PicThre.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._PicThre.TabIndex = 19
		self._PicThre.TabStop = False
		self._PicThre.Visible = False
		# 
		# PicFor
		# 
		self._PicFor.BackgroundImage = resources.GetObject("PicFor.BackgroundImage")
		self._PicFor.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._PicFor.Image = resources.GetObject("PicFor.Image")
		self._PicFor.Location = System.Drawing.Point(547, 446)
		self._PicFor.Name = "PicFor"
		self._PicFor.Size = System.Drawing.Size(30, 36)
		self._PicFor.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._PicFor.TabIndex = 20
		self._PicFor.TabStop = False
		self._PicFor.Visible = False
		# 
		# PicFiv
		# 
		self._PicFiv.BackgroundImage = resources.GetObject("PicFiv.BackgroundImage")
		self._PicFiv.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._PicFiv.Image = resources.GetObject("PicFiv.Image")
		self._PicFiv.Location = System.Drawing.Point(511, 446)
		self._PicFiv.Name = "PicFiv"
		self._PicFiv.Size = System.Drawing.Size(30, 36)
		self._PicFiv.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._PicFiv.TabIndex = 21
		self._PicFiv.TabStop = False
		self._PicFiv.Visible = False
		# 
		# PicSix
		# 
		self._PicSix.BackgroundImage = resources.GetObject("PicSix.BackgroundImage")
		self._PicSix.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._PicSix.Image = resources.GetObject("PicSix.Image")
		self._PicSix.Location = System.Drawing.Point(475, 446)
		self._PicSix.Name = "PicSix"
		self._PicSix.Size = System.Drawing.Size(30, 36)
		self._PicSix.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._PicSix.TabIndex = 22
		self._PicSix.TabStop = False
		self._PicSix.Visible = False
		# 
		# PicSev
		# 
		self._PicSev.BackgroundImage = resources.GetObject("PicSev.BackgroundImage")
		self._PicSev.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._PicSev.Image = resources.GetObject("PicSev.Image")
		self._PicSev.Location = System.Drawing.Point(619, 404)
		self._PicSev.Name = "PicSev"
		self._PicSev.Size = System.Drawing.Size(30, 36)
		self._PicSev.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._PicSev.TabIndex = 23
		self._PicSev.TabStop = False
		self._PicSev.Visible = False
		# 
		# PicNin
		# 
		self._PicNin.BackgroundImage = resources.GetObject("PicNin.BackgroundImage")
		self._PicNin.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._PicNin.Image = resources.GetObject("PicNin.Image")
		self._PicNin.Location = System.Drawing.Point(547, 404)
		self._PicNin.Name = "PicNin"
		self._PicNin.Size = System.Drawing.Size(30, 36)
		self._PicNin.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._PicNin.TabIndex = 24
		self._PicNin.TabStop = False
		self._PicNin.Visible = False
		# 
		# PicTen
		# 
		self._PicTen.BackgroundImage = resources.GetObject("PicTen.BackgroundImage")
		self._PicTen.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._PicTen.Image = resources.GetObject("PicTen.Image")
		self._PicTen.Location = System.Drawing.Point(511, 404)
		self._PicTen.Name = "PicTen"
		self._PicTen.Size = System.Drawing.Size(30, 36)
		self._PicTen.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._PicTen.TabIndex = 25
		self._PicTen.TabStop = False
		self._PicTen.Visible = False
		# 
		# PicAte
		# 
		self._PicAte.BackgroundImage = resources.GetObject("PicAte.BackgroundImage")
		self._PicAte.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._PicAte.Image = resources.GetObject("PicAte.Image")
		self._PicAte.Location = System.Drawing.Point(583, 404)
		self._PicAte.Name = "PicAte"
		self._PicAte.Size = System.Drawing.Size(30, 36)
		self._PicAte.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._PicAte.TabIndex = 26
		self._PicAte.TabStop = False
		self._PicAte.Visible = False
		# 
		# PicBak
		# 
		self._PicBak.BackgroundImage = resources.GetObject("PicBak.BackgroundImage")
		self._PicBak.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._PicBak.Image = resources.GetObject("PicBak.Image")
		self._PicBak.Location = System.Drawing.Point(475, 404)
		self._PicBak.Name = "PicBak"
		self._PicBak.Size = System.Drawing.Size(30, 36)
		self._PicBak.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._PicBak.TabIndex = 27
		self._PicBak.TabStop = False
		self._PicBak.Visible = False
		# 
		# textBet
		# 
		self._textBet.BackColor = System.Drawing.Color.FromArgb(221, 245, 245)
		self._textBet.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._textBet.ForeColor = System.Drawing.Color.Black
		self._textBet.Location = System.Drawing.Point(635, 100)
		self._textBet.Name = "textBet"
		self._textBet.Size = System.Drawing.Size(140, 38)
		self._textBet.TabIndex = 10
		self._textBet.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# DealChat
		# 
		self._DealChat.BackColor = System.Drawing.Color.FromArgb(221, 245, 245)
		self._DealChat.Font = System.Drawing.Font("Showcard Gothic", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._DealChat.Location = System.Drawing.Point(475, 404)
		self._DealChat.Name = "DealChat"
		self._DealChat.Size = System.Drawing.Size(300, 81)
		self._DealChat.TabIndex = 28
		self._DealChat.Text = "Dealer's Chat"
		self._DealChat.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# ButtonWarn
		# 
		self._ButtonWarn.BackColor = System.Drawing.Color.FromArgb(198, 14, 14)
		self._ButtonWarn.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._ButtonWarn.Font = System.Drawing.Font("Showcard Gothic", 15)
		self._ButtonWarn.ForeColor = System.Drawing.Color.FromArgb(255, 239, 0)
		self._ButtonWarn.Location = System.Drawing.Point(535, 261)
		self._ButtonWarn.Name = "ButtonWarn"
		self._ButtonWarn.Size = System.Drawing.Size(195, 63)
		self._ButtonWarn.TabIndex = 29
		self._ButtonWarn.Text = "PickPocket"
		self._ButtonWarn.UseVisualStyleBackColor = False
		self._ButtonWarn.Visible = False
		self._ButtonWarn.Click += self.ButtonWarnClick
		# 
		# Wins
		# 
		self._Wins.BackColor = System.Drawing.Color.White
		self._Wins.Location = System.Drawing.Point(358, 230)
		self._Wins.Name = "Wins"
		self._Wins.Size = System.Drawing.Size(100, 23)
		self._Wins.TabIndex = 30
		self._Wins.Text = "0"
		self._Wins.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._Wins.Visible = False
		# 
		# TotalWins
		# 
		self._TotalWins.BackColor = System.Drawing.Color.White
		self._TotalWins.Location = System.Drawing.Point(167, 230)
		self._TotalWins.Name = "TotalWins"
		self._TotalWins.Size = System.Drawing.Size(100, 23)
		self._TotalWins.TabIndex = 31
		self._TotalWins.Text = "0"
		self._TotalWins.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._TotalWins.Visible = False
		# 
		# TotalLosses
		# 
		self._TotalLosses.BackColor = System.Drawing.Color.White
		self._TotalLosses.Location = System.Drawing.Point(13, 230)
		self._TotalLosses.Name = "TotalLosses"
		self._TotalLosses.Size = System.Drawing.Size(100, 23)
		self._TotalLosses.TabIndex = 32
		self._TotalLosses.Text = "0"
		self._TotalLosses.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._TotalLosses.Visible = False
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(198, 14, 14)
		self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._button1.Font = System.Drawing.Font("Showcard Gothic", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.FromArgb(255, 239, 0)
		self._button1.Location = System.Drawing.Point(463, 226)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(66, 32)
		self._button1.TabIndex = 33
		self._button1.Text = "ALL IN"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(120, 0, 0)
		self.ClientSize = System.Drawing.Size(787, 494)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._TotalLosses)
		self.Controls.Add(self._TotalWins)
		self.Controls.Add(self._Wins)
		self.Controls.Add(self._ButtonWarn)
		self.Controls.Add(self._DealChat)
		self.Controls.Add(self._PicBak)
		self.Controls.Add(self._PicAte)
		self.Controls.Add(self._PicTen)
		self.Controls.Add(self._PicNin)
		self.Controls.Add(self._PicSev)
		self.Controls.Add(self._PicSix)
		self.Controls.Add(self._PicFiv)
		self.Controls.Add(self._PicFor)
		self.Controls.Add(self._PicThre)
		self.Controls.Add(self._PicTwo)
		self.Controls.Add(self._PicAce)
		self.Controls.Add(self._ButtonQuit)
		self.Controls.Add(self._ButtonSteal)
		self.Controls.Add(self._ButtonStay)
		self.Controls.Add(self._ButtonHit)
		self.Controls.Add(self._ButtonGamble)
		self.Controls.Add(self._wallet)
		self.Controls.Add(self._textBet)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._moneylbl)
		self.Controls.Add(self._PlayCard3)
		self.Controls.Add(self._PlayCard2)
		self.Controls.Add(self._PlayCard1)
		self.Controls.Add(self._DealCard2)
		self.Controls.Add(self._DealCard1)
		self.Controls.Add(self._DealerPic)
		self.Name = "MainForm"
		self.Text = "BlackJack"
		self._DealerPic.EndInit()
		self._DealCard1.EndInit()
		self._DealCard2.EndInit()
		self._PlayCard1.EndInit()
		self._PlayCard2.EndInit()
		self._PlayCard3.EndInit()
		self._PicAce.EndInit()
		self._PicTwo.EndInit()
		self._PicThre.EndInit()
		self._PicFor.EndInit()
		self._PicFiv.EndInit()
		self._PicSix.EndInit()
		self._PicSev.EndInit()
		self._PicNin.EndInit()
		self._PicTen.EndInit()
		self._PicAte.EndInit()
		self._PicBak.EndInit()
		self.ResumeLayout(False)
		self.PerformLayout()


	def ButtonStealClick(self, sender, e):
		rnd = System.Random()
		attempt = 0
		attempt = rnd.Next(1,51)
		
		if attempt >= 25:
			self._DealChat.Text= "Hey! Don't try that again!"
			self._ButtonSteal.Visible = False
			self._ButtonWarn.Visible = True
		else:
			wallet = float(self._wallet.Text)
			self._wallet.Text = str(round(attempt+wallet,2))
			
	

	def ButtonGambleClick(self, sender, e):
		Ace = self._PicAce.Image
		Two = self._PicTwo.Image
		Three = self._PicThre.Image
		Four = self._PicFor.Image
		Five = self._PicFiv.Image
		Six = self._PicSix.Image
		Seven = self._PicSev.Image
		Eight = self._PicAte.Image
		Nine = self._PicNin.Image
		Ten = self._PicTen.Image
		Back = self._PicBak.Image
		rnd = System.Random()
		
		wins = float(self._Wins.Text)
		bet = float(self._textBet.Text)
		wallet = float(self._wallet.Text)
		money = wallet - bet
		reward = (bet * 2)
		if wallet == 0:
			self._DealChat.Text = "Sorry sir, seems like you've run out of chips."
		if bet == 0:
			self._DealChat.Text = "Sorry sir, gotta place a bet to play."
		elif bet < 1:
			self._DealChat.Text = "Sorry sir, but you need to bet atleast a dollar."
		elif bet > wallet and bet > money:
			self._DealChat.Text = "Sorry sir, doesn't seem like you have sufficent for that bet."
		else:
			self._wallet.Text = str(money)
			PlayCard1 = self._PlayCard1
			PlayCard2 = self._PlayCard2
			PlayCard2 = self._PlayCard3
			DealCard1 = self._DealCard1
			DealCard2 = self._DealCard2
			Card1 = 0
			Card2 = 0
			Card3 = 0
			DCard1 = 0
			DCard2 = 0 
			
			Card1 = rnd.Next(1,11)
			Card2 = rnd.Next(1,11)
			Card3 = rnd.Next(1,11)
			
			self._PlayCard3.Visible = False
			
			if Card1 == 1:
				PlayCard1.Image = Ace
			if Card1 == 2:
				PlayCard1.Image = Two
			if Card1 == 3:
				PlayCard1.Image = Three
			if Card1 == 4:
				PlayCard1.Image = Four
			if Card1 == 5:
				PlayCard1.Image = Five
			if Card1 == 6:
				PlayCard1.Image = Six
			if Card1 == 7:
				PlayCard1.Image = Seven
			if Card1 == 8:
				PlayCard1.Image = Eight
			if Card1 == 9:
				PlayCard1.Image = Nine
			if Card1 == 10:
				PlayCard1.Image = Ten
				
			#Card 2
			if Card2 == 1:
				self._PlayCard2.Image = Ace
			if Card2 == 2:
				self._PlayCard2.Image = Two
			if Card2 == 3:
				self._PlayCard2.Image = Three
			if Card2 == 4:
				self._PlayCard2.Image = Four
			if Card2 == 5:
				self._PlayCard2.Image = Five
			if Card2 == 6:
				self._PlayCard2.Image = Six
			if Card2 == 7:
				self._PlayCard2.Image = Seven
			if Card2 == 8:
				self._PlayCard2.Image = Eight
			if Card2 == 9:
				self._PlayCard2.Image = Nine
			if Card2 == 10:
				self._PlayCard2.Image = Ten
				
			if Card3 == 1:
				self._PlayCard3.Image = Ace
			if Card3 == 2:
				self._PlayCard3.Image = Two
			if Card3 == 3:
				self._PlayCard3.Image = Three
			if Card3 == 4:
				self._PlayCard3.Image = Four
			if Card3 == 5:
				self._PlayCard3.Image = Five
			if Card3 == 6:
				self._PlayCard3.Image = Six
			if Card3 == 7:
				self._PlayCard3.Image = Seven
			if Card3 == 8:
				self._PlayCard3.Image = Eight
			if Card3 == 9:
				self._PlayCard3.Image = Nine
			if Card3 == 10:
				self._PlayCard3.Image = Ten
				
			DCard2 = rnd.Next(1,11)
			self._DealCard1.Image = Back
			#Dealer's Open Card
			if wins < 3:
				
				DCard2 = rnd.Next(1,11)
				
				if DCard2 == 1:
					self._DealCard2.Image = Ace
				if DCard2 == 2:
					self._DealCard2.Image = Two
				if DCard2 == 3:
					self._DealCard2.Image = Three
				if DCard2 == 4:
					self._DealCard2.Image = Four
				if DCard2 == 5:
					self._DealCard2.Image = Five
				if DCard2 == 6:
					self._DealCard2.Image = Six
				if DCard2 == 7:
					self._DealCard2.Image = Seven
				if DCard2 == 8:
					self._DealCard2.Image = Eight
				if DCard2 == 9:
					self._DealCard2.Image = Nine
				if DCard2 == 10:
					self._DealCard2.Image = Ten
			else:
				
				DCard2 = rnd.Next(1,5)
				
				if DCard2 == 1:
					self._DealCard2.Image = Ace
				if DCard2 == 2:
					self._DealCard2.Image = Ten
				if DCard2 == 3:
					self._DealCard2.Image = Nine
				if DCard2 == 4:
					self._DealCard2.Image = Eight
				if DCard2 == 5:
					self._DealCard2.Image = Seven
					
		self._ButtonHit.Visible = True
		self._ButtonStay.Visible = True
			
	def ButtonHitClick(self, sender, e):
		wins = float(self._Wins.Text)
		self._PlayCard3.Visible = True
		bet = int(self._textBet.Text)
		wallet = float(self._wallet.Text)
		TotalWin = float(self._TotalWins.Text)
		TotalLoss = float(self._TotalLosses.Text)
		reward = int(bet*2)
		C1Weight = 0
		C2Weight = 0
		C3Weight = 0
		D1Weight = 0
		D2Weight = 0
		C1C2Weight = int(C1Weight + C2Weight)
		PlayWeight = int(C1Weight + C2Weight + C3Weight)
		DealWeight = int(D1Weight + D2Weight)
		rnd = System.Random()
		Ace = self._PicAce.Image
		Two = self._PicTwo.Image
		Three = self._PicThre.Image
		Four = self._PicFor.Image
		Five = self._PicFiv.Image
		Six = self._PicSix.Image
		Seven = self._PicSev.Image
		Eight = self._PicAte.Image
		Nine = self._PicNin.Image
		Ten = self._PicTen.Image
		Back = self._PicBak.Image
		
		if wins < 3:
			DCard1 = rnd.Next(1,11)
		
			if DCard1 == 1:
				D1Weight = 11
				self._DealCard1.Image = Ace
			if DCard1 == 2:
				D1Weight = 2
				self._DealCard1.Image = Two
			if DCard1 == 3:
				D1Weight = 3
				self._DealCard1.Image = Three
			if DCard1 == 4: 
				D1Weight = 4
				self._DealCard1.Image = Four
			if DCard1 == 5:
				D1Weight = 5
				self._DealCard1.Image = Five
			if DCard1 == 6:
				D1Weight = 6
				self._DealCard1.Image = Six
			if DCard1 == 7:
				D1Weight = 7
				self._DealCard1.Image = Seven
			if DCard1 == 8:
				D1Weight = 8
				self._DealCard1.Image = Eight
			if DCard1 == 9:
				D1Weight = 9
				self._DealCard1.Image = Nine
			if DCard1 == 10:
				D1Weight = 10
				self._DealCard1.Image = Ten
		else:
			DCard1 = rnd.Next(1,6)
			if DCard1 == 1:
				D1Weight = 7
				self._DealCard1.Image = Seven
			if DCard1 == 2:
				D1Weight = 8
				self._DealCard1.Image = Eight
			if DCard1 == 3:
				D1Weight = 9
				self._DealCard1.Image = Nine
			if DCard1 == 4:
				D1Weight = 10
				self._DealCard1.Image = Ten
			if DCard1 == 5:
				D1Weight = 11
				self._DealCard1.Image = Ace
		
		
		if self._DealCard2.Image == Ace:
			if D1Weight == 11:
				D2Weight = 1
			else:
				D2Weight = 11
		if self._DealCard2.Image == Two:
			D2Weight = 2
		if self._DealCard2.Image == Three:
			D2Weight = 3
		if self._DealCard2.Image == Four:
			D2Weight = 4
		if self._DealCard2.Image == Five:
			D2Weight = 5
		if self._DealCard2.Image == Six:
			D2Weight = 6
		if self._DealCard2.Image == Seven:
			D2Weight = 7
		if self._DealCard2.Image == Eight:
			D2Weight = 8		
		if self._DealCard2.Image == Nine:
			D2Weight = 9
		if self._DealCard2.Image == Ten:
			D2Weight = 10
			
		if self._PlayCard1.Image == Ace:
			C1Weight = 11
		if self._PlayCard1.Image == Two:
			C1Weight = 2 
		if self._PlayCard1.Image == Three:
			C1Weight = 3
		if self._PlayCard1.Image == Four:
			C1Weight = 4 
		if self._PlayCard1.Image == Five:
			C1Weight = 5
		if self._PlayCard1.Image == Six:
			C1Weight = 6
		if self._PlayCard1.Image == Seven:
			C1Weight = 7
		if self._PlayCard1.Image == Eight:
			C1Weight = 8
		if self._PlayCard1.Image == Nine:
			C1Weight = 9
		if self._PlayCard1.Image == Ten:
			C1Weight = 10
			
		if self._PlayCard2.Image == Ace:
			if C1Weight == 11:
				C2Weight = 1
			else:
				C2Weight = 11
		if self._PlayCard2.Image == Two:
			C2Weight = 2 
		if self._PlayCard2.Image == Three:
			C2Weight = 3
		if self._PlayCard2.Image == Four:
			C2Weight = 4 
		if self._PlayCard2.Image == Five:
			C2Weight = 5
		if self._PlayCard2.Image == Six:
			C2Weight = 6
		if self._PlayCard2.Image == Seven:
			C2Weight = 7
		if self._PlayCard2.Image == Eight:
			C2Weight = 8
		if self._PlayCard2.Image == Nine:
			C2Weight = 9
		if self._PlayCard2.Image == Ten:
			C2Weight = 10
			
		C1C2Weight = int(C1Weight + C2Weight)
		
		if self._PlayCard3.Image == Ace:
			if C1Weight+C2Weight >= 11:
				C3Weight = 1
			else:
				C3Weight = 11
		if self._PlayCard3.Image == Two:
			C3Weight = 2 
		if self._PlayCard3.Image == Three:
			C3Weight = 3
		if self._PlayCard3.Image == Four:
			C3Weight = 4 
		if self._PlayCard3.Image == Five:
			C3Weight = 5
		if self._PlayCard3.Image == Six:
			C3Weight = 6
		if self._PlayCard3.Image == Seven:
			C3Weight = 7
		if self._PlayCard3.Image == Eight:
			C3Weight = 8
		if self._PlayCard3.Image == Nine:
			C3Weight = 9
		if self._PlayCard3.Image == Ten:
			C3Weight = 10
				
		PlayWeight = int(C1Weight + C2Weight + C3Weight)
		DealWeight = int(D1Weight+D2Weight) 
			
		MessageBox.Show("Player's Hand"+"   "+str(PlayWeight) + "   " + "Dealer's Hand"+"   "+str(DealWeight))
		
		if PlayWeight > 21:
			self._DealChat.Text="Bust!"
			self._Wins.Text = str(0)
			self._TotalLosses.Text = str(TotalLoss + 1)
		elif PlayWeight < DealWeight:
			self._DealChat.Text="The House Wins!"
			self._Wins.Text = str(0)
			self._TotalLosses.Text = str(TotalLoss + 1)
		elif PlayWeight == 21:
			self._wallet.Text = str(reward + reward + wallet)
			self._DealChat.Text="Player Wins" + "  " + str(reward + reward) + "  " + "Dollars!"
			self._Wins.Text = str(wins + 1)
			self._TotalWins.Text = str(TotalWin + 1)
		elif PlayWeight > DealWeight:
			self._wallet.Text = str(reward + wallet)
			self._DealChat.Text="Player Wins" + "  " + str(reward) + "  " + "Dollars!"
			self._Wins.Text = str(wins + 1)
			self._TotalWins.Text = str(TotalWin + 1)
		elif PlayWeight == DealWeight:
			self._DealChat.Text="It's A Draw!"
			self._wallet.Text = str(bet + wallet)
		
		self._ButtonHit.Visible = False
		self._ButtonStay.Visible = False

	def ButtonStayClick(self, sender, e):
		wins = float(self._Wins.Text)
		bet = int(self._textBet.Text)
		wallet = float(self._wallet.Text)
		TotalWin = float(self._TotalWins.Text)
		TotalLoss = float(self._TotalLosses.Text)
		reward = int(bet*2)
		C1Weight = 0
		C2Weight = 0
		D1Weight = 0
		D2Weight = 0
		PlayWeight = int(C1Weight + C2Weight)
		DealWeight = int(D1Weight + D2Weight)
		rnd = System.Random()
		Ace = self._PicAce.Image
		Two = self._PicTwo.Image
		Three = self._PicThre.Image
		Four = self._PicFor.Image
		Five = self._PicFiv.Image
		Six = self._PicSix.Image
		Seven = self._PicSev.Image
		Eight = self._PicAte.Image
		Nine = self._PicNin.Image
		Ten = self._PicTen.Image
		Back = self._PicBak.Image
		if wins < 5:
			DCard1 = rnd.Next(1,11)
		
			if DCard1 == 1:
				D1Weight = 11
				self._DealCard1.Image = Ace
			if DCard1 == 2:
				D1Weight = 2
				self._DealCard1.Image = Two
			if DCard1 == 3:
				D1Weight = 3
				self._DealCard1.Image = Three
			if DCard1 == 4: 
				D1Weight = 4
				self._DealCard1.Image = Four
			if DCard1 == 5:
				D1Weight = 5
				self._DealCard1.Image = Five
			if DCard1 == 6:
				D1Weight = 6
				self._DealCard1.Image = Six
			if DCard1 == 7:
				D1Weight = 7
				self._DealCard1.Image = Seven
			if DCard1 == 8:
				D1Weight = 8
				self._DealCard1.Image = Eight
			if DCard1 == 9:
				D1Weight = 9
				self._DealCard1.Image = Nine
			if DCard1 == 10:
				D1Weight = 10
				self._DealCard1.Image = Ten
		else:
			DCard1 = rnd.Next(1,6)
			if DCard1 == 1:
				D1Weight = 7
				self._DealCard1.Image = Seven
			if DCard1 == 2:
				D1Weight = 8
				self._DealCard1.Image = Eight
			if DCard1 == 3:
				D1Weight = 9
				self._DealCard1.Image = Nine
			if DCard1 == 4:
				D1Weight = 10
				self._DealCard1.Image = Ten
			if DCard1 == 5:
				D1Weight = 11
				self._DealCard1.Image = Ace
		
		
		if self._DealCard2.Image == Ace:
			if D1Weight == 11:
				D2Weight = 1
			else:
				D2Weight = 11
		if self._DealCard2.Image == Two:
			D2Weight = 2
		if self._DealCard2.Image == Three:
			D2Weight = 3
		if self._DealCard2.Image == Four:
			D2Weight = 4
		if self._DealCard2.Image == Five:
			D2Weight = 5
		if self._DealCard2.Image == Six:
			D2Weight = 6
		if self._DealCard2.Image == Seven:
			D2Weight = 7
		if self._DealCard2.Image == Eight:
			D2Weight = 8		
		if self._DealCard2.Image == Nine:
			D2Weight = 9
		if self._DealCard2.Image == Ten:
			D2Weight = 10
			
		if self._PlayCard1.Image == Ace:
			C1Weight = 11
		if self._PlayCard1.Image == Two:
			C1Weight = 2 
		if self._PlayCard1.Image == Three:
			C1Weight = 3
		if self._PlayCard1.Image == Four:
			C1Weight = 4 
		if self._PlayCard1.Image == Five:
			C1Weight = 5
		if self._PlayCard1.Image == Six:
			C1Weight = 6
		if self._PlayCard1.Image == Seven:
			C1Weight = 7
		if self._PlayCard1.Image == Eight:
			C1Weight = 8
		if self._PlayCard1.Image == Nine:
			C1Weight = 9
		if self._PlayCard1.Image == Ten:
			C1Weight = 10
			
		if self._PlayCard2.Image == Ace:
			if C1Weight == 11:
				C2Weight = 1
			else:
				C2Weight = 11
		if self._PlayCard2.Image == Two:
			C2Weight = 2 
		if self._PlayCard2.Image == Three:
			C2Weight = 3
		if self._PlayCard2.Image == Four:
			C2Weight = 4 
		if self._PlayCard2.Image == Five:
			C2Weight = 5
		if self._PlayCard2.Image == Six:
			C2Weight = 6
		if self._PlayCard2.Image == Seven:
			C2Weight = 7
		if self._PlayCard2.Image == Eight:
			C2Weight = 8
		if self._PlayCard2.Image == Nine:
			C2Weight = 9
		if self._PlayCard2.Image == Ten:
			C2Weight = 10
			
			
		PlayWeight = int(C1Weight + C2Weight)
		DealWeight = int(D1Weight+D2Weight) 
			
		MessageBox.Show("Player's Hand"+"   "+str(PlayWeight) + "   " + "Dealer's Hand"+"   "+str(DealWeight))
		
		if PlayWeight > 21:
			self._DealChat.Text="Bust!"
			self._Wins.Text = str(0)
			self._TotalLosses.Text = str(TotalLoss + 1)
		elif PlayWeight < DealWeight:
			self._DealChat.Text="The House Wins!"
			self._Wins.Text = str(0)
			self._TotalLosses.Text = str(TotalLoss + 1)
		elif PlayWeight == 21:
			self._wallet.Text = str(reward + reward + wallet)
			self._DealChat.Text="Player Wins" + "  " + str(reward + reward) + "  " + "Dollars!"
			self._Wins.Text = str(wins + 1)
			self._TotalWins.Text = str(TotalWin + 1)
		elif PlayWeight > DealWeight:
			self._wallet.Text = str(reward + wallet)
			self._DealChat.Text="Player Wins" + "  " + str(reward) + "  " + "Dollars!"
			self._Wins.Text = str(wins + 1)
			self._TotalWins.Text = str(TotalWin + 1)
		elif PlayWeight == DealWeight:
			self._DealChat.Text="It's A Draw!"
			self._wallet.Text = str(bet + wallet)
			
		self._ButtonHit.Visible = False
		self._ButtonStay.Visible = False

	def ButtonQuitClick(self, sender, e):
		self._DealChat.Text=str(self._wallet.Text)+" "+"was your final total!"
		MessageBox.Show("Come Back Soon!")
		MessageBox.Show(str(self._TotalWins.Text) + " " + "Wins" + " " + "Vs" + str(self._TotalLosses.Text) + " " + "Losses")
		Application.Exit()

	def ButtonWarnClick(self, sender, e):
		rnd = System.Random()
		attempt = 0
		attempt = rnd.Next(1,101)
		
		if attempt >= 50:
			self._DealChat.Text= "That's it, out with you!"
			MessageBox.Show("You've been kicked out of the Casino!")
			MessageBox.Show(str(self._TotalWins.Text) + " " + "Wins" + " " + "Vs" + str(self._TotalLosses.Text) + " " + "Losses")
			Application.Exit()
		else:
			wallet = float(self._wallet.Text)
			self._wallet.Text = str(round(attempt+wallet,2))

	def Button1Click(self, sender, e):
		Allin = self._wallet.Text
		
		self._textBet.Text = str(Allin)