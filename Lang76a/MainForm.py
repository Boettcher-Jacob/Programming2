import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei UI", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(110, 9)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(165, 33)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9)
		self._label2.Location = System.Drawing.Point(4, 74)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(271, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "-------------------------------------------------------------------"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.WhiteSmoke
		self._label3.Location = System.Drawing.Point(4, 95)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(271, 65)
		self._label3.TabIndex = 3
		self._label3.Text = """
555555555"""
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei UI", 8.25)
		self._button2.Location = System.Drawing.Point(4, 48)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 23)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Maroon
		self._button3.Font = System.Drawing.Font("Microsoft YaHei UI", 8.25)
		self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._button3.Location = System.Drawing.Point(110, 48)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(165, 23)
		self._button3.TabIndex = 5
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 16)
		self._textBox1.Location = System.Drawing.Point(4, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 32)
		self._textBox1.TabIndex = 6
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(287, 169)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang76a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		value = self._textBox1.Text
		step = value* 9
		fun = step * 12345679
		self._label3.Text = str(fun)