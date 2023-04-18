import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._textBox1.Location = System.Drawing.Point(94, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(162, 38)
		self._textBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Gray
		self._button1.Font = System.Drawing.Font("Modern No. 20", 23.9999981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._button1.Location = System.Drawing.Point(12, 56)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(162, 65)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Gray
		self._button2.Font = System.Drawing.Font("Modern No. 20", 23.9999981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._button2.Location = System.Drawing.Point(12, 127)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(162, 65)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkRed
		self._button3.ForeColor = System.Drawing.Color.Snow
		self._button3.Location = System.Drawing.Point(12, 232)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(76, 25)
		self._button3.TabIndex = 3
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Snow
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(228, 71)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 38)
		self._label1.TabIndex = 4
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Snow
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(228, 127)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 65)
		self._label2.TabIndex = 5
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Coral
		self.ClientSize = System.Drawing.Size(340, 269)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Lang54c"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		Radius = float(self._textBox1.Text)
		pi = 3.14159
		circum = 2 * pi * Radius
		area = pi * Radius**2
		Area = round(area, 3)
		Circum= round(circum, 3)
		self._label1.Text=str(Circum)
		self._label2.Text=str(Area)
		

	def Button2Click(self, sender, e):
		self._label1.Text=""
		self._label2.Text=""
		self._textBox1.Text=""
		

	def Button3Click(self, sender, e):
		Application.Exit()