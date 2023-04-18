import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ControlDark
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Snow
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(39, 41)
		self._label1.TabIndex = 0
		self._label1.Text = "A"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ControlDark
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Snow
		self._label2.Location = System.Drawing.Point(13, 77)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(39, 41)
		self._label2.TabIndex = 1
		self._label2.Text = "B"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlDark
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Snow
		self._label3.Location = System.Drawing.Point(13, 140)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(39, 41)
		self._label3.TabIndex = 2
		self._label3.Text = "C"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(58, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 38)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(58, 80)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 38)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(58, 143)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 38)
		self._textBox3.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Green
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.Control
		self._button1.Location = System.Drawing.Point(12, 187)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(146, 57)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ControlDark
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.Snow
		self._label4.Location = System.Drawing.Point(220, 9)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(139, 64)
		self._label4.TabIndex = 7
		self._label4.Text = "Negative Root"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ControlLight
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.SystemColors.ControlText
		self._label7.Location = System.Drawing.Point(220, 80)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(139, 104)
		self._label7.TabIndex = 8
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ControlLight
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.SystemColors.ControlText
		self._label5.Location = System.Drawing.Point(379, 80)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(139, 104)
		self._label5.TabIndex = 10
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ControlDark
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.Snow
		self._label6.Location = System.Drawing.Point(379, 9)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(139, 64)
		self._label6.TabIndex = 9
		self._label6.Text = "Positive Root"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Green
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.SystemColors.Control
		self._button2.Location = System.Drawing.Point(164, 187)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(146, 57)
		self._button2.TabIndex = 11
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Firebrick
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.Control
		self._button3.Location = System.Drawing.Point(439, 212)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(79, 32)
		self._button3.TabIndex = 12
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(527, 253)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang58b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		A=int(self._textBox1.Text)
		B=int(self._textBox2.Text)
		C=int(self._textBox3.Text)
		Nroot=str(-b - math.sqrt(B**2 - 4 * A * C)/2 * A)
		Proot=str(-b + math.sqrt(B**2 - 4 * A * C)/2 * A)
		self._label5.Text=str(Proot)
		self._lable7.Text=str(Nroot)