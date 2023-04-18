import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
		self._button1.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 105)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(164, 38)
		self._button1.TabIndex = 0
		self._button1.Text = "Mercury"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._button2.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(11, 180)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(164, 38)
		self._button2.TabIndex = 1
		self._button2.Text = "Venus"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._button3.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.FromArgb(0, 64, 0)
		self._button3.Location = System.Drawing.Point(12, 255)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(164, 38)
		self._button3.TabIndex = 2
		self._button3.Text = "Earth"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._button4.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(12, 330)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(164, 38)
		self._button4.TabIndex = 3
		self._button4.Text = "Mars"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._button5.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(182, 104)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(164, 38)
		self._button5.TabIndex = 4
		self._button5.Text = "Jupiter"
		self._button5.UseVisualStyleBackColor = False
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._button6.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(181, 179)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(164, 38)
		self._button6.TabIndex = 5
		self._button6.Text = "Saturn"
		self._button6.UseVisualStyleBackColor = False
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._button7.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(181, 330)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(164, 38)
		self._button7.TabIndex = 7
		self._button7.Text = "Neptune"
		self._button7.UseVisualStyleBackColor = False
		self._button7.Click += self.Button7Click
		# 
		# button8
		# 
		self._button8.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button8.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(182, 255)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(164, 38)
		self._button8.TabIndex = 6
		self._button8.Text = "Uranus"
		self._button8.UseVisualStyleBackColor = False
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.BackColor = System.Drawing.Color.Black
		self._button9.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button9.ForeColor = System.Drawing.Color.White
		self._button9.Location = System.Drawing.Point(100, 405)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(164, 38)
		self._button9.TabIndex = 8
		self._button9.Text = "Pluto"
		self._button9.UseVisualStyleBackColor = False
		self._button9.Click += self.Button9Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Segoe Marker", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(334, 69)
		self._label1.TabIndex = 9
		self._label1.Text = "Select a Planet for The Data involved with it."
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(361, 455)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg486Astronomy"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Mercury import *
		
		merc=Mercury(self)
		merc.Show()
		self.Hide()

	def Button2Click(self, sender, e):
		from Venus import *
		
		ven=Venus(self)
		ven.Show()
		self.Hide()

	def Button3Click(self, sender, e):
		from Earth import *
		
		ert=Earth(self)
		ert.Show()
		self.Hide()

	def Button4Click(self, sender, e):
		from Mars import *
		
		mar=Mars(self)
		mar.Show()
		self.Hide()

	def Button5Click(self, sender, e):
		from Jupiter import *
		
		jup=Jupiter(self)
		jup.Show()
		self.Hide()

	def Button6Click(self, sender, e):
		from Saturn import *
		
		sat=Saturn(self)
		sat.Show()
		self.Hide()

	def Button8Click(self, sender, e):
		from Uranus import *
		
		ur=Uranus(self)
		ur.Show()
		self.Hide()

	def Button7Click(self, sender, e):
		from Neptune import *
		
		nep=Neptune(self)
		nep.Show()
		self.Hide()

	def Button9Click(self, sender, e):
		from Pluto import *
		
		pluto=Pluto(self)
		pluto.Show()
		self.Hide()

	def MainFormLoad(self, sender, e):
		pass