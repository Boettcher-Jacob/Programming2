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
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkGray
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._button1.Location = System.Drawing.Point(12, 253)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(284, 62)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkGray
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._button2.Location = System.Drawing.Point(302, 253)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(264, 62)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkRed
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._button3.Location = System.Drawing.Point(12, 321)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(547, 225)
		self._listBox1.TabIndex = 3
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(572, 348)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang122d"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for x in range(-12, 17):
			y = x**6 - 3*x**5 - 93*x**4 + 87*x**13 + 1596*x**2 - 1380*x - 2800
			self._listBox1.Items.Add(str(x) + "\t\t" + str(y))

	def Button2Click(self, sender, e):
		self.listBox1.Items.Clear()
		

	def Button3Click(self, sender, e):
		Application.Exit()