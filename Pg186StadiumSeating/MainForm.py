import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(200, 158)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "groupBox1"
		# 
		# groupBox2
		# 
		self._groupBox2.Location = System.Drawing.Point(215, 13)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(200, 158)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "groupBox2"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(7, 20)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(187, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(6, 46)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(187, 20)
		self._textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(6, 72)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(187, 20)
		self._textBox3.TabIndex = 2
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(427, 328)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg186StadiumSeating"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)

