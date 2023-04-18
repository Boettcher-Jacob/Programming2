import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._btnShow = System.Windows.Forms.Button()
		self._btnClear = System.Windows.Forms.Button()
		self._btnExit = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.Control
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(504, 277)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# btnShow
		# 
		self._btnShow.BackColor = System.Drawing.Color.MidnightBlue
		self._btnShow.Font = System.Drawing.Font("MS Gothic", 20)
		self._btnShow.ForeColor = System.Drawing.Color.White
		self._btnShow.Location = System.Drawing.Point(12, 289)
		self._btnShow.Name = "btnShow"
		self._btnShow.Size = System.Drawing.Size(128, 58)
		self._btnShow.TabIndex = 1
		self._btnShow.Text = "Show"
		self._btnShow.UseVisualStyleBackColor = False
		self._btnShow.Click += self.BtnShowClick
		# 
		# btnClear
		# 
		self._btnClear.BackColor = System.Drawing.Color.MidnightBlue
		self._btnClear.Font = System.Drawing.Font("MS Gothic", 20)
		self._btnClear.ForeColor = System.Drawing.Color.White
		self._btnClear.Location = System.Drawing.Point(388, 289)
		self._btnClear.Name = "btnClear"
		self._btnClear.Size = System.Drawing.Size(128, 58)
		self._btnClear.TabIndex = 2
		self._btnClear.Text = "Clear"
		self._btnClear.UseVisualStyleBackColor = False
		self._btnClear.Click += self.Button2Click
		# 
		# btnExit
		# 
		self._btnExit.BackColor = System.Drawing.Color.Firebrick
		self._btnExit.ForeColor = System.Drawing.Color.White
		self._btnExit.Location = System.Drawing.Point(225, 414)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(75, 23)
		self._btnExit.TabIndex = 3
		self._btnExit.Text = "EXIT"
		self._btnExit.UseVisualStyleBackColor = False
		self._btnExit.Click += self.BtnExitClick
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self.ClientSize = System.Drawing.Size(528, 449)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._btnClear)
		self.Controls.Add(self._btnShow)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "CraigRules"
		self.ResumeLayout(False)
		
		

	def BtnShowClick(self, sender, e):
		self._label1.Text = "Craig Rules!"

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def BtnExitClick(self, sender, e):
		Application.Exit()