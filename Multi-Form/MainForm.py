import System.Drawing
import System.Windows.Forms
import Form1 

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(259, 236)
		self._button1.TabIndex = 0
		self._button1.Text = "THIS ISN'T EVEN MY ULTIMATE FORM"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Multi-Form"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self, "Bazinga!")
		form1.Show()
		self.Hide()