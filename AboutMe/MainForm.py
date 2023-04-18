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
		self._lbl1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# btnShow
		# 
		self._btnShow.BackColor = System.Drawing.Color.OliveDrab
		self._btnShow.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._btnShow.Font = System.Drawing.Font("Microsoft Sans Serif", 26)
		self._btnShow.ForeColor = System.Drawing.Color.FloralWhite
		self._btnShow.Location = System.Drawing.Point(73, 13)
		self._btnShow.Name = "btnShow"
		self._btnShow.Size = System.Drawing.Size(139, 54)
		self._btnShow.TabIndex = 0
		self._btnShow.Text = "Show"
		self._btnShow.UseVisualStyleBackColor = False
		self._btnShow.Click += self.BtnShowClick
		# 
		# btnClear
		# 
		self._btnClear.BackColor = System.Drawing.Color.OliveDrab
		self._btnClear.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._btnClear.Font = System.Drawing.Font("Microsoft Sans Serif", 26)
		self._btnClear.ForeColor = System.Drawing.Color.FloralWhite
		self._btnClear.Location = System.Drawing.Point(73, 230)
		self._btnClear.Name = "btnClear"
		self._btnClear.Size = System.Drawing.Size(139, 54)
		self._btnClear.TabIndex = 1
		self._btnClear.Text = "Clear"
		self._btnClear.UseVisualStyleBackColor = False
		self._btnClear.Click += self.BtnClearClick
		# 
		# btnExit
		# 
		self._btnExit.BackColor = System.Drawing.Color.DarkRed
		self._btnExit.Font = System.Drawing.Font("Microsoft Sans Serif", 26)
		self._btnExit.ForeColor = System.Drawing.Color.SeaShell
		self._btnExit.Location = System.Drawing.Point(578, 350)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(139, 54)
		self._btnExit.TabIndex = 2
		self._btnExit.Text = "EXIT"
		self._btnExit.UseVisualStyleBackColor = False
		self._btnExit.Click += self.BtnExitClick
		# 
		# lbl1
		# 
		self._lbl1.BackColor = System.Drawing.Color.MintCream
		self._lbl1.Font = System.Drawing.Font("Book Antiqua", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lbl1.ForeColor = System.Drawing.Color.Black
		self._lbl1.Location = System.Drawing.Point(252, 13)
		self._lbl1.Name = "lbl1"
		self._lbl1.Size = System.Drawing.Size(465, 334)
		self._lbl1.TabIndex = 3
		self._lbl1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Teal
		self.ClientSize = System.Drawing.Size(729, 416)
		self.Controls.Add(self._lbl1)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._btnClear)
		self.Controls.Add(self._btnShow)
		self.Name = "MainForm"
		self.Text = "AboutMe"
		self.ResumeLayout(False)


	def BtnShowClick(self, sender, e):
		self._lbl1.Text = "I dabble in 3D softwares like blender and play a few games."

	def BtnClearClick(self, sender, e):
		self._lbl1.Text = ""

	def BtnExitClick(self, sender, e):
		Application.Exit()