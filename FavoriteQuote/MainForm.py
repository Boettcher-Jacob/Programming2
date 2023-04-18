import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._btnExit = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(761, 294)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Chocolate
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 16)
		self._button1.ForeColor = System.Drawing.Color.Snow
		self._button1.Location = System.Drawing.Point(13, 310)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(140, 42)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Chocolate
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 16)
		self._button2.ForeColor = System.Drawing.Color.Snow
		self._button2.Location = System.Drawing.Point(13, 404)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(140, 42)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# btnExit
		# 
		self._btnExit.BackColor = System.Drawing.Color.DarkRed
		self._btnExit.ForeColor = System.Drawing.Color.Transparent
		self._btnExit.Location = System.Drawing.Point(695, 404)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(79, 33)
		self._btnExit.TabIndex = 3
		self._btnExit.Text = "Exit"
		self._btnExit.UseVisualStyleBackColor = False
		self._btnExit.Click += self.BtnExitClick
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlDark
		self.ClientSize = System.Drawing.Size(786, 449)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "FavoriteQuote"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text="He who goto bed with itchy bum, wake up with smelly finger."

	def Button2Click(self, sender, e):
		self._label1.Text=""

	def BtnExitClick(self, sender, e):
		Application.Exit()