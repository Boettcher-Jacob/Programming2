import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(634, 264)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(260, 284)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(166, 63)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(260, 353)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(166, 52)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkRed
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._button3.Location = System.Drawing.Point(572, 284)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 33)
		self._button3.TabIndex = 3
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(659, 443)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Lang122c"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for num in range(2, 11, 2):
			A = num
			B = num + 1
			C = num * 2
			D = num**2
			self._listBox1.Items.Add(str(A) + "\t\t" + str(B) + "\t\t" + str(C) + "\t\t" + str(D))

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()