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
		self._listBox1.Size = System.Drawing.Size(471, 342)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei UI", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 367)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(192, 75)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei UI", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(292, 367)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(192, 75)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Maroon
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.Control
		self._button3.Location = System.Drawing.Point(211, 399)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(493, 454)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "lang122h-2"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for x in range(1, 21):
			num= x
			square = x * x
			sqrt= math.sqrt(x)
			sqrt= round(sqrt, 4)
			cube= x * x * x
			four= math.sqrt(math.sqrt(x))
			four= round(four, 4)
			self._listBox1.Items.Add(str(num) + "\t\t" + str(square) + "\t\t" + str(sqrt) + "\t\t"+ str(cube) + "\t\t" + str(four))
		

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
	

	def Button3Click(self, sender, e):
		Application.Exit()