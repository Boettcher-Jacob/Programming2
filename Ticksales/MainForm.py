﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._button2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Controls.Add(self._button1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(437, 193)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Selection"
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(7, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(276, 67)
		self._label1.TabIndex = 0
		self._label1.Text = "Selection for General Public Sales"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(286, 19)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(145, 68)
		self._button1.TabIndex = 1
		self._button1.Text = "General Public Sales"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(286, 111)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(145, 68)
		self._button2.TabIndex = 2
		self._button2.Text = "Student Sales"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(7, 112)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(276, 67)
		self._label2.TabIndex = 3
		self._label2.Text = """Selection for Student Sales
"""
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.Control
		self._button3.Location = System.Drawing.Point(375, 212)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 1
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(462, 247)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Ticksales"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Form1 import *
		form1=Form1(self)
		form1.Show()
		self.Hide()

	def Button2Click(self, sender, e):
		from stusale import *
		form2=Form2(self)
		form2.Show()
		self.Hide()