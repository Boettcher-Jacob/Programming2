
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Jupiter(Form):
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
		self._button1.TabIndex = 7
		self._button1.Text = "Return"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(219, 72)
		self._label1.TabIndex = 6
		self._label1.Text = """Jupiter
Type Jovian
Average distance from the sun 5.2028 AU
Mass 1.899 × 1027 kg
Temperature at cloud tops –110°C"""
		# 
		# Jupiter
		# 
		self.ClientSize = System.Drawing.Size(253, 128)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "Jupiter"
		self.Text = "Jupiter"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.parent.Show()
		self.Hide()