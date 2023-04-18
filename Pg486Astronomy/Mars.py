
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Mars(Form):
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
		self._label1.Text = """Mars
Type Terrestrial
Average distance from the sun 1.5237 AU
Mass 0.6424 × 1024 kg
Surface temperature –140°C to 20°C
"""
		# 
		# Mars
		# 
		self.ClientSize = System.Drawing.Size(248, 123)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "Mars"
		self.Text = "Mars"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.parent.Show()
		self.Hide()