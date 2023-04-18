import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("BossBattle.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._bosstitle = System.Windows.Forms.Label()
		self._bossheth = System.Windows.Forms.Label()
		self._playhealth = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._eggoboss = System.Windows.Forms.PictureBox()
		self._johnboss = System.Windows.Forms.PictureBox()
		self._grapeboss = System.Windows.Forms.PictureBox()
		self._button4 = System.Windows.Forms.Button()
		self._bosshealth = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._cooldown = System.Windows.Forms.Label()
		self._playerdmg = System.Windows.Forms.Label()
		self._bossdmg = System.Windows.Forms.Label()
		self._pictureBox1.BeginInit()
		self._eggoboss.BeginInit()
		self._johnboss.BeginInit()
		self._grapeboss.BeginInit()
		self.SuspendLayout()
		# 
		# pictureBox1
		# 
		self._pictureBox1.Location = System.Drawing.Point(148, 73)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(113, 168)
		self._pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
		self._pictureBox1.TabIndex = 0
		self._pictureBox1.TabStop = False
		# 
		# bosstitle
		# 
		self._bosstitle.BackColor = System.Drawing.SystemColors.ControlDark
		self._bosstitle.Font = System.Drawing.Font("Showcard Gothic", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._bosstitle.Location = System.Drawing.Point(106, 9)
		self._bosstitle.Name = "bosstitle"
		self._bosstitle.Size = System.Drawing.Size(194, 61)
		self._bosstitle.TabIndex = 1
		self._bosstitle.Text = "Boss:"
		self._bosstitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# bossheth
		# 
		self._bossheth.BackColor = System.Drawing.SystemColors.ControlDark
		self._bossheth.Font = System.Drawing.Font("Showcard Gothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._bossheth.Location = System.Drawing.Point(106, 244)
		self._bossheth.Name = "bossheth"
		self._bossheth.Size = System.Drawing.Size(194, 26)
		self._bossheth.TabIndex = 2
		self._bossheth.Text = "Boss Health:"
		self._bossheth.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# playhealth
		# 
		self._playhealth.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._playhealth.Font = System.Drawing.Font("Showcard Gothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._playhealth.Location = System.Drawing.Point(148, 428)
		self._playhealth.Name = "playhealth"
		self._playhealth.Size = System.Drawing.Size(88, 54)
		self._playhealth.TabIndex = 3
		self._playhealth.Text = "100"
		self._playhealth.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Showcard Gothic", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 368)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(88, 54)
		self._button1.TabIndex = 4
		self._button1.Text = "Attack"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Showcard Gothic", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(148, 368)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(88, 54)
		self._button2.TabIndex = 5
		self._button2.Text = "Block"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Showcard Gothic", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(280, 368)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(88, 54)
		self._button3.TabIndex = 6
		self._button3.Text = "Heal"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# eggoboss
		# 
		self._eggoboss.Image = resources.GetObject("eggoboss.Image")
		self._eggoboss.Location = System.Drawing.Point(12, 9)
		self._eggoboss.Name = "eggoboss"
		self._eggoboss.Size = System.Drawing.Size(34, 43)
		self._eggoboss.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
		self._eggoboss.TabIndex = 7
		self._eggoboss.TabStop = False
		self._eggoboss.Visible = False
		# 
		# johnboss
		# 
		self._johnboss.Image = resources.GetObject("johnboss.Image")
		self._johnboss.Location = System.Drawing.Point(12, 58)
		self._johnboss.Name = "johnboss"
		self._johnboss.Size = System.Drawing.Size(34, 43)
		self._johnboss.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
		self._johnboss.TabIndex = 8
		self._johnboss.TabStop = False
		self._johnboss.Visible = False
		# 
		# grapeboss
		# 
		self._grapeboss.Image = resources.GetObject("grapeboss.Image")
		self._grapeboss.Location = System.Drawing.Point(12, 107)
		self._grapeboss.Name = "grapeboss"
		self._grapeboss.Size = System.Drawing.Size(34, 43)
		self._grapeboss.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
		self._grapeboss.TabIndex = 9
		self._grapeboss.TabStop = False
		self._grapeboss.Visible = False
		# 
		# button4
		# 
		self._button4.Font = System.Drawing.Font("Stencil", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(12, 9)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(356, 473)
		self._button4.TabIndex = 10
		self._button4.Text = "Are You Ready to Rumble?!?!"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# bosshealth
		# 
		self._bosshealth.BackColor = System.Drawing.SystemColors.ControlDark
		self._bosshealth.Font = System.Drawing.Font("Showcard Gothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._bosshealth.Location = System.Drawing.Point(106, 270)
		self._bosshealth.Name = "bosshealth"
		self._bosshealth.Size = System.Drawing.Size(194, 26)
		self._bosshealth.TabIndex = 11
		self._bosshealth.Text = "1000/1000"
		self._bosshealth.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._label1.Font = System.Drawing.Font("Showcard Gothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 428)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(88, 54)
		self._label1.TabIndex = 12
		self._label1.Text = "Health"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# cooldown
		# 
		self._cooldown.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._cooldown.Location = System.Drawing.Point(307, 339)
		self._cooldown.Name = "cooldown"
		self._cooldown.Size = System.Drawing.Size(29, 23)
		self._cooldown.TabIndex = 13
		self._cooldown.Text = "0"
		self._cooldown.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# playerdmg
		# 
		self._playerdmg.BackColor = System.Drawing.Color.Transparent
		self._playerdmg.Font = System.Drawing.Font("Showcard Gothic", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._playerdmg.Location = System.Drawing.Point(267, 189)
		self._playerdmg.Name = "playerdmg"
		self._playerdmg.Size = System.Drawing.Size(98, 55)
		self._playerdmg.TabIndex = 14
		self._playerdmg.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# bossdmg
		# 
		self._bossdmg.BackColor = System.Drawing.Color.Transparent
		self._bossdmg.Font = System.Drawing.Font("Showcard Gothic", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._bossdmg.Location = System.Drawing.Point(255, 430)
		self._bossdmg.Name = "bossdmg"
		self._bossdmg.Size = System.Drawing.Size(81, 52)
		self._bossdmg.TabIndex = 15
		self._bossdmg.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self.ClientSize = System.Drawing.Size(390, 497)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._bossdmg)
		self.Controls.Add(self._playerdmg)
		self.Controls.Add(self._cooldown)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._bosshealth)
		self.Controls.Add(self._grapeboss)
		self.Controls.Add(self._johnboss)
		self.Controls.Add(self._eggoboss)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._playhealth)
		self.Controls.Add(self._bossheth)
		self.Controls.Add(self._bosstitle)
		self.Controls.Add(self._pictureBox1)
		self.Name = "MainForm"
		self.Text = "BossBattle"
		self._pictureBox1.EndInit()
		self._eggoboss.EndInit()
		self._johnboss.EndInit()
		self._grapeboss.EndInit()
		self.ResumeLayout(False)


	def Button4Click(self, sender, e):
		self._button4.Visible = False
		
		Eggo = self._eggoboss.Image
		John = self._johnboss.Image
		Thanos = self._grapeboss.Image
		
		rnd = System.Random()
		rng = rnd.Next(1,101)
		
		if rng >= 1 and rng <= 50:
			self._pictureBox1.Image = Thanos
			self._bosshealth.Text= "200"
			self._bosstitle.Text = "Boss: Old Man Raisin"
		elif rng > 50 and rng <90:
			self._pictureBox1.Image=John
			self._bosshealth.Text= "500"
			self._bosstitle.Text = "Boss: John 'Can't See' Cena"
		elif rng >=90:
			self._pictureBox1.Image = Eggo
			self._bosshealth.Text= "1000"
			self._bosstitle.Text = "Boss: Leggo My Eggo"
		

	def Button1Click(self, sender, e):
		# Attack Command
		
		rnd = System.Random()
		
		attackrng = rnd.Next(1,26)
		playcritical = rnd.Next(1,101)
		bosscritical = rnd.Next(1,101)
		BossHP = float(self._bosshealth.Text)
		PlayerHP = float(self._playhealth.Text)
		
		if playcritical > 75:
			crithit = attackrng * 2
			self._bosshealth.Text = str(BossHP - crithit)
			self._playerdmg.Text = "Critical Hit!" + " " + str(crithit)
		else:
			self._bosshealth.Text = str(BossHP - attackrng)
			self._playerdmg.Text = str(attackrng)
			
		# The Boss' Turn
		
		bossrng = rnd.Next(1,21)
		PlayerHP = float(self._playhealth.Text)
		
		if bosscritical > 75:
			bosscrithit = attackrng * 2
			self._playhealth.Text = str(PlayerHP - bosscrithit)
			self._bossdmg.Text = "Critical Hit!" + " " + str(bosscrithit)
		else:
			self._playhealth.Text = str(PlayerHP - bossrng)
			self._bossdmg.Text = str(bossrng)
			
		if self._cooldown.Text == "0":
			self._button3.Visible = True
		else:
			self._button3.Visible = False
			
		if PlayerHP <= 0:
			MessageBox.Show("You've Been Defeated")
			Application.Exit()
		if BossHP <= 0:
			MessageBox.Show("You have Defeated The Boss")
		
	def Button2Click(self, sender, e):
		# Block/Dodge Command
		
		rnd = System.Random()
		bossrng = rnd.Next(1,21)
		PlayerHP = float(self._playhealth.Text)
		blockrng = rnd.Next(1,21)
		BossHP = float(self._bosshealth.Text)
		
		if blockrng > 5 and blockrng < 20:
			blockdmg = int(bossrng) / 2
			finaldamage = int(PlayerHP) - int(blockdmg)
			self._playhealth.Text = str(finaldamage)
			self._bossdmg.Text = str(blockdmg)
		
		elif blockrng > 0 and blockrng <= 5:
			finaldamage = int(PlayerHP) - int(bossrng)
			self._playhealth.Text = str(finaldamage)
			self._bossdmg.Text = "Blocked" + " " + str(bossrng)
		
		elif blockrng == 20:
			self._bossdmg.Text = "Dodged"
			
		cooldown = float(self._cooldown.Text)
		
		if cooldown < 0:
			CD = str(cooldown) - 1
			self._cooldown.Text = str(CD)
		else:
			pass
		
		if cooldown == 5:
			self._button3.Visible = False
			self._cooldown.Text = "4"
		elif cooldown == 4:
			self._button3.Visible = False
			self._cooldown.Text = "3"
		elif cooldown == 3:
			self._button3.Visible = False
			self._cooldown.Text = "2"
		elif cooldown == 2:
			self._button3.Visible = False
			self._cooldown.Text = "1"
		elif cooldown == 1:
			self._button3.Visible = False
			self._cooldown.Text = "0"
			
		if cooldown == 0:
			self._button3.Visible = True
			
		if PlayerHP <= 0:
			MessageBox.Show("You've Been Defeated")
			Application.Exit()
		if BossHP <= 0:
			MessageBox.Show("You have Defeated The Boss")
			
	def Button3Click(self, sender, e):
		# Attempt a Heal Command
		
		PlayerHP = float(self._playhealth.Text)
		if PlayerHP <= 0:
			MessageBox.Show("You've Been Defeated")
			Application.Exit()
		
		self._cooldown.Text = "5"
		self._playhealth.Text = "100"
		self._button3.Visible=False
		