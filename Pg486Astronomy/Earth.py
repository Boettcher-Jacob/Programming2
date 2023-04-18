
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Earth(Form):
	def __init__(self,parent):
		self.InitializeComponent()
		self.parent = parent
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 85)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(219, 31)
		self._button1.TabIndex = 5
		self._button1.Text = "Return"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(219, 72)
		self._label1.TabIndex = 4
		self._label1.Text = """Earth
Type Terrestrial
Average distance from the sun 0.7233 AU
Mass 4.87 × 1024 kg
Surface temperature 472°C"""
		# 
		# Earth
		# 
		self.ClientSize = System.Drawing.Size(241, 127)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "Earth"
		self.Text = "Earth"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.parent.Show()
		self.Hide()
	