import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._btnShow = System.Windows.Forms.Button()
		self._btnClear = System.Windows.Forms.Button()
		self._btnExit = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# btnShow
		# 
		self._btnShow.BackColor = System.Drawing.Color.CornflowerBlue
		self._btnShow.Font = System.Drawing.Font("Microsoft Sans Serif", 16)
		self._btnShow.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._btnShow.Location = System.Drawing.Point(13, 197)
		self._btnShow.Name = "btnShow"
		self._btnShow.Size = System.Drawing.Size(103, 52)
		self._btnShow.TabIndex = 0
		self._btnShow.Text = "Show"
		self._btnShow.UseVisualStyleBackColor = False
		self._btnShow.Click += self.BtnShowClick
		# 
		# btnClear
		# 
		self._btnClear.BackColor = System.Drawing.Color.CornflowerBlue
		self._btnClear.Font = System.Drawing.Font("Microsoft Sans Serif", 16)
		self._btnClear.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._btnClear.Location = System.Drawing.Point(169, 197)
		self._btnClear.Name = "btnClear"
		self._btnClear.Size = System.Drawing.Size(103, 52)
		self._btnClear.TabIndex = 1
		self._btnClear.Text = "Clear"
		self._btnClear.UseVisualStyleBackColor = False
		self._btnClear.Click += self.BtnClearClick
		# 
		# btnExit
		# 
		self._btnExit.BackColor = System.Drawing.Color.DarkRed
		self._btnExit.ForeColor = System.Drawing.SystemColors.Control
		self._btnExit.Location = System.Drawing.Point(104, 168)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(75, 23)
		self._btnExit.TabIndex = 2
		self._btnExit.Text = "EXIT"
		self._btnExit.UseVisualStyleBackColor = False
		self._btnExit.Click += self.BtnExitClick
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Tempus Sans ITC", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(260, 156)
		self._label1.TabIndex = 3
		self._label1.Click += self.Label1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlDark
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._btnClear)
		self.Controls.Add(self._btnShow)
		self.Name = "MainForm"
		self.Text = "YourName"
		self.ResumeLayout(False)


	def BtnShowClick(self, sender, e):
		self._label1.Text="Jacob A. Boettcher"

	def BtnClearClick(self, sender, e):
		self._label1.Text=""

	def BtnExitClick(self, sender, e):
		Application.Exit()

	def Label1Click(self, sender, e):
		pass