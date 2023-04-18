import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._BtnCal = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._AverageBox = System.Windows.Forms.Label()
		self._SumBox = System.Windows.Forms.Label()
		self._btnClear = System.Windows.Forms.Button()
		self._btnExit = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(13, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(97, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(116, 13)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(97, 20)
		self._textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(219, 13)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(97, 20)
		self._textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(322, 13)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(97, 20)
		self._textBox4.TabIndex = 3
		# 
		# BtnCal
		# 
		self._BtnCal.Location = System.Drawing.Point(13, 39)
		self._BtnCal.Name = "BtnCal"
		self._BtnCal.Size = System.Drawing.Size(407, 23)
		self._BtnCal.TabIndex = 6
		self._BtnCal.Text = "Calculate"
		self._BtnCal.UseVisualStyleBackColor = True
		self._BtnCal.Click += self.BtnCalClick
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.Control
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._label1.Location = System.Drawing.Point(89, 85)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(124, 33)
		self._label1.TabIndex = 7
		self._label1.Text = "Average"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.Control
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._label2.Location = System.Drawing.Point(89, 139)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(124, 33)
		self._label2.TabIndex = 8
		self._label2.Text = "Sum"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# AverageBox
		# 
		self._AverageBox.BackColor = System.Drawing.SystemColors.Control
		self._AverageBox.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._AverageBox.Location = System.Drawing.Point(219, 85)
		self._AverageBox.Name = "AverageBox"
		self._AverageBox.Size = System.Drawing.Size(124, 33)
		self._AverageBox.TabIndex = 9
		self._AverageBox.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# SumBox
		# 
		self._SumBox.BackColor = System.Drawing.SystemColors.Control
		self._SumBox.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._SumBox.Location = System.Drawing.Point(219, 139)
		self._SumBox.Name = "SumBox"
		self._SumBox.Size = System.Drawing.Size(124, 33)
		self._SumBox.TabIndex = 10
		self._SumBox.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# btnClear
		# 
		self._btnClear.Location = System.Drawing.Point(156, 175)
		self._btnClear.Name = "btnClear"
		self._btnClear.Size = System.Drawing.Size(124, 40)
		self._btnClear.TabIndex = 11
		self._btnClear.Text = "Clear"
		self._btnClear.UseVisualStyleBackColor = True
		self._btnClear.Click += self.BtnClearClick
		# 
		# btnExit
		# 
		self._btnExit.BackColor = System.Drawing.Color.DarkRed
		self._btnExit.ForeColor = System.Drawing.SystemColors.Control
		self._btnExit.Location = System.Drawing.Point(12, 206)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(75, 23)
		self._btnExit.TabIndex = 12
		self._btnExit.Text = "EXIT"
		self._btnExit.UseVisualStyleBackColor = False
		self._btnExit.Click += self.BtnExitClick
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlDark
		self.ClientSize = System.Drawing.Size(433, 241)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._btnClear)
		self.Controls.Add(self._SumBox)
		self.Controls.Add(self._AverageBox)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._BtnCal)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Lang54a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def BtnCalClick(self, sender, e):
		one =int(self._textBox1.Text)
		two =int(self._textBox2.Text)
		three =int(self._textBox3.Text)
		four =int(self._textBox4.Text)
		sum = one + two + three + four
		average = (one + two + three + four)/4
		self._SumBox.Text=str(sum)
		self._AverageBox.Text=str(average)

	def BtnClearClick(self, sender, e):
		self._SumBox.Text=""
		self._AverageBox.Text=""

	def BtnExitClick(self, sender, e):
		Application.Exit()