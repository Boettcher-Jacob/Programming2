
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent, msg):
		self.InitializeComponent()
		self.parent = parent
		self.msg = msg
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("MV Boli", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(495, 147)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Wingdings", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 2)
		self._button1.Location = System.Drawing.Point(13, 164)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(495, 267)
		self._button1.TabIndex = 1
		self._button1.Text = "hehehhehe bazinga"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(520, 443)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "Form1"
		self.Text = "Form1"
		self.Load += self.Form1Load
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass
	def Form1Load(self, sender, e):
		self._label1.Text = self.msg
	
	def Form1FormClosing(self, sender, e):
		self.parent.Show()

	def Button1Click(self, sender, e):
		self.Close()
		self.parent.Show()