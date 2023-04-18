import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 61)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 39)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkRed
		self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._button3.Font = System.Drawing.Font("Poor Richard", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.Control
		self._button3.Location = System.Drawing.Point(33, 274)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(63, 28)
		self._button3.TabIndex = 2
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(12, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 43)
		self._textBox1.TabIndex = 3
		# 
		# button2
		# 
		self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(12, 106)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 39)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(118, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(300, 290)
		self._listBox1.TabIndex = 5
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(430, 316)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "lang152b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		base = int(self._textBox1.Text)
		
		for evens in range(len(base),2):
			2 + 2						 