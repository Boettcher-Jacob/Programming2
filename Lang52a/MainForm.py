import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LightCoral
		self._textBox1.Location = System.Drawing.Point(127, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(160, 38)
		self._textBox1.TabIndex = 0
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.LightCoral
		self._textBox2.Location = System.Drawing.Point(127, 79)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(160, 38)
		self._textBox2.TabIndex = 1
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 310)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(275, 44)
		self._button1.TabIndex = 2
		self._button1.Text = "CLEAR"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(109, 35)
		self._label1.TabIndex = 3
		self._label1.Text = "Length:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._label2.Location = System.Drawing.Point(12, 79)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(92, 35)
		self._label2.TabIndex = 4
		self._label2.Text = "Width:"
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._label3.Location = System.Drawing.Point(12, 246)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(145, 37)
		self._label3.TabIndex = 5
		self._label3.Text = "Perimeter:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._label4.Location = System.Drawing.Point(163, 195)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(124, 37)
		self._label4.TabIndex = 6
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._label5.Location = System.Drawing.Point(12, 195)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 37)
		self._label5.TabIndex = 7
		self._label5.Text = "Area:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._label6.Location = System.Drawing.Point(163, 246)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(124, 37)
		self._label6.TabIndex = 8
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._button2.Location = System.Drawing.Point(12, 134)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(275, 40)
		self._button2.TabIndex = 9
		self._button2.Text = "Calculate"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkRed
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 8)
		self._button3.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._button3.Location = System.Drawing.Point(12, 424)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 10
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.CornflowerBlue
		self.ClientSize = System.Drawing.Size(313, 459)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self.Name = "MainForm"
		self.Text = "Lang52a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		length =int(self._textBox1.Text)
		width =int(self._textBox2.Text)
		area = length * width
		perim = 2 * length + 2 * width
		self._label4.Text=str(area)
		self._label6.Text=str(perim)

	def Button1Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text= ""
		self._label6.Text= ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def TextBox1TextChanged(self, sender, e):
		pass