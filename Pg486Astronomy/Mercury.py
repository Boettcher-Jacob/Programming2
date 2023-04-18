
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Mercury(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.parent = parent
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(219, 72)
		self._label1.TabIndex = 0
		self._label1.Text = """Mercury
Type: Terrestrial
Average distance from the sun: 0.387 AU
Mass: 3.31 × 1023 kg
Surface temperature –173°C to 430°C"""
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 89)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(219, 31)
		self._button1.TabIndex = 1
		self._button1.Text = "Return"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# Mercury
		# 
		self.ClientSize = System.Drawing.Size(244, 132)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "Mercury"
		self.Text = "Mercury"
		self.ResumeLayout(False)
		
	def Button1Click(self, sender, e):
		self.parent.Show()
		self.Hide()