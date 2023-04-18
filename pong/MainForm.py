import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.R = System.Random()
		self.ballup = 0
		self.balld = 0
		self.flagleft = False
		self.flagright = False
		
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._lbltitle = System.Windows.Forms.Label()
		self._leftscore = System.Windows.Forms.Label()
		self._lblball = System.Windows.Forms.Label()
		self._lblleft = System.Windows.Forms.Label()
		self._rightscore = System.Windows.Forms.Label()
		self._lblright = System.Windows.Forms.Label()
		self._timerright = System.Windows.Forms.Timer(self._components)
		self._timerleft = System.Windows.Forms.Timer(self._components)
		self._timerball = System.Windows.Forms.Timer(self._components)
		self._timermulti = System.Windows.Forms.Timer(self._components)
		self._timerdummy = System.Windows.Forms.Timer(self._components)
		self._timerboolean = System.Windows.Forms.Timer(self._components)
		self.SuspendLayout()
		# 
		# lbltitle
		# 
		self._lbltitle.BackColor = System.Drawing.Color.Transparent
		self._lbltitle.Font = System.Drawing.Font("OCR A Extended", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lbltitle.ForeColor = System.Drawing.Color.White
		self._lbltitle.Location = System.Drawing.Point(12, 25)
		self._lbltitle.Name = "lbltitle"
		self._lbltitle.Size = System.Drawing.Size(958, 52)
		self._lbltitle.TabIndex = 0
		self._lbltitle.Text = "Press ENTER to start or M for Multiplayer."
		self._lbltitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._lbltitle.Click += self.Label1Click
		# 
		# leftscore
		# 
		self._leftscore.BackColor = System.Drawing.Color.Transparent
		self._leftscore.Font = System.Drawing.Font("OCR A Extended", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._leftscore.ForeColor = System.Drawing.Color.White
		self._leftscore.Location = System.Drawing.Point(78, 96)
		self._leftscore.Name = "leftscore"
		self._leftscore.Size = System.Drawing.Size(166, 109)
		self._leftscore.TabIndex = 1
		self._leftscore.Text = "0"
		self._leftscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._leftscore.Click += self.Label2Click
		# 
		# lblball
		# 
		self._lblball.BackColor = System.Drawing.Color.White
		self._lblball.Location = System.Drawing.Point(479, 304)
		self._lblball.Name = "lblball"
		self._lblball.Size = System.Drawing.Size(20, 20)
		self._lblball.TabIndex = 2
		self._lblball.Click += self.Label3Click
		# 
		# lblleft
		# 
		self._lblleft.BackColor = System.Drawing.Color.White
		self._lblleft.Location = System.Drawing.Point(12, 246)
		self._lblleft.Name = "lblleft"
		self._lblleft.Size = System.Drawing.Size(20, 100)
		self._lblleft.TabIndex = 3
		self._lblleft.Click += self.Label4Click
		# 
		# rightscore
		# 
		self._rightscore.BackColor = System.Drawing.Color.Transparent
		self._rightscore.Font = System.Drawing.Font("OCR A Extended", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._rightscore.ForeColor = System.Drawing.Color.White
		self._rightscore.Location = System.Drawing.Point(734, 96)
		self._rightscore.Name = "rightscore"
		self._rightscore.Size = System.Drawing.Size(166, 109)
		self._rightscore.TabIndex = 4
		self._rightscore.Text = "0"
		self._rightscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblright
		# 
		self._lblright.BackColor = System.Drawing.Color.White
		self._lblright.Location = System.Drawing.Point(956, 246)
		self._lblright.Name = "lblright"
		self._lblright.Size = System.Drawing.Size(20, 100)
		self._lblright.TabIndex = 5
		# 
		# timerright
		# 
		self._timerright.Interval = 20
		self._timerright.Tick += self.TimerrightTick
		# 
		# timerleft
		# 
		self._timerleft.Interval = 20
		self._timerleft.Tick += self.TimerleftTick
		# 
		# timerball
		# 
		self._timerball.Interval = 20
		self._timerball.Tick += self.TimerballTick
		# 
		# timermulti
		# 
		self._timermulti.Interval = 20
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(988, 607)
		self.Controls.Add(self._lblright)
		self.Controls.Add(self._rightscore)
		self.Controls.Add(self._lblleft)
		self.Controls.Add(self._lblball)
		self.Controls.Add(self._leftscore)
		self.Controls.Add(self._lbltitle)
		self.Name = "MainForm"
		self.Text = "pong"
		self.Load += self.MainFormLoad
		self.SizeChanged += self.MainFormSizeChanged
		self.KeyDown += self.MainFormKeyDown
		self.ResumeLayout(False)
		

	def TimerballTick(self, sender, e):
		ball = self._lblball
		lpdl = self._lblleft
		rpdl = self._lblright
		ball.Top += 8 * self.balld
		rscore = int(self._rightscore.Text)
		lscore = int(self._leftscore.Text)
		
		if ball.Right >= rpdl.Left and \
		   ball.Bottom >= rpdl.Top and ball.Top <= rpdl.Bottom:
		   self.balld = -1
		   self.ballup = self.R.Next(-4, 5)
		elif ball.Left <= lpdl.Right and ball.Bottom >= lpdl.Top and ball.Top <= lpdl.Bottom:
		   slef.balld = 1
		   self.ballup - self.R.Next(-4, 5)
		
		if ball.Top <= 0:
			self.balld = -1
			ball.Top += 5 * self.balld
			
		if ball.Top >= self.Height:
			self.balld = 1
			ball.Top += 5 * self.balld
			
		if ball.Location.X <= 0 or \
		  (ball.Location.X < lpdl.Left + 20 and ball.Location.Y < lpdl.Top):
			pass
		  	"""Todo left, cause we can't do it as a group ig"""
		   
		if ball.Location.X >= self.Width or \
		  (ball.Location.X > rpdl.Right + 20 and ball.Location.Y > rpdl.Height):
			lscore = lscore + 1
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self._leftscore.Text = str(lscore)
		   
		   
		if lscore == 10: 
			self._timerball.Enabled = False
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2 
			self.ballup = 0 
			self._lbltitle.Visible= True
			self._lbltitle.Text = "Left Player Wins"
			
		if ball.Top <= 0:
			self.ballup += 1
		elif ball.Bottom >= self.Height - 50:
			self.ballup = -1
			
			
		if self._timerboolean.Enabled:
			lpdl.Top = ball.Top - 20
	def MainFormKeyDown(self, sender, e):
		tball = self._timerball
		tdum = self._timerdummy
		tbool = self._timerboolean
		tmult = self._timermulti
		tleft = self._timerleft
		tright = self._timerright
		bl = self.lblball
		lblf = self._lblleft
		lbrt = self._lblright
		
		def reset():
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Press ENTER to start or M for Mulitplayer"
			self._leftscore.Text = "0"
			self._rightscore.Text= "0"
			tball.Enabled = False
			tdum.Enabled = False
			tbool.Enabled = False
			tmult.Enabled = False
			tleft.Enabled = False
			tright.Enabled = False

			bl.Left = self.Width // 2
			bl.Top = self.Height // 2
			lblf.Top = (self.Height//2) - 100 + self.lblleft.Height
			lbrt.Top = (self.Height // 2) - 100 + self.lblright.Height

		if e.Keycode == Keys.Enter:
			tball.Enabled == True
			self._lbltitle.Visible = False
			tdum.Enabled = True
			tbool.Enabled = True
			
		if e.KeyCode == Keys.M:
			reset()
			self.lbltile.Visible = True
			self.lbltitle.Text = "USE w + s for left nad up and down for right"
			tmult.Enabled = True
			if e.Keycode == Keys.Enter:
				self._lbltitle.Visible = False
				tball.Enabled = True
				tdum.Enabled = True
				tmult.Enabled = True
				tbool.Enabled = False
		if tdum.Enabled == True:
			if e.KeyCode == Keys.Up:
				self.flagright = False
				tright.Enabled = True
			elif e.Keycode == Keys.Down:
				self.flagright = True
				tright.Enabled = True
			elif tright.Enabled == True and self.flagright == False:
				tright.Enabled = False
				
		"""TODO MULTI Code"""
		
		if tmult.Enabled and tball.Enabled:
			tbool.enabled = False
			
			if e.KeyCode == Keys.W:
				self.flagleft = False
				tleft.Enabled = True
			if e.KeyCode == Keys.S:
				self.flagleft = True
				tleft.Enabled. True

		
	def MainFormLoad(self, sender, e):
		""" TODO: 3 unique easter eggs in total and finish multiplayer+scoreboard"""
		self.balld = 1
		self.ballup = self.R.Next(-4, 5)
		self._timerball.Enable = False
		self._timerdummy.Enable = False
		self._timermulti.Enalbe = False
	
	
	def pdlTick(self, pdl, flagd, tmr):
		if flagd == True:
			pdl.Top += 5
		if flagD == False:
			pdl.Top -= 5
		if pdl.Top <= 10:
			tmr.Enable = False
		if pdl.Bottom >= self.Height - 50:
			tmr.Enable = False

	def TimerrightTick(self, sender, e):
		self.pdlTick(self._lblright, self.flagright, self._timerright)

	def TimerleftTick(self, sender, e):
		self.pdlTick(self._lblleft, self.flagleft, self._timerleft)

	def MainFormSizeChanged(self, sender, e):
		self._lblright.Left = self.Width - 25 - self._lblright.Width
		self._lblball.Left = self.Width //2
		self._lblball.Top = self.Height //2
		self._lbltitle.Width = self.Width - 25
		self._rightScoore.Left = self.Width - 75 - self._rightscore.Width

	def lblballClick(self, sender, e):
		self._lblball.BackColor = Color.Red
		"""TODO ad ball secrets"""
		