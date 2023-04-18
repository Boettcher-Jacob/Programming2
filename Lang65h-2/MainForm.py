﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ControlDark
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(98, 34)
		self._label1.TabIndex = 0
		self._label1.Text = "Pound"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ControlDark
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(117, 13)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(98, 34)
		self._label2.TabIndex = 1
		self._label2.Text = "Shilling"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlDark
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(221, 13)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(98, 34)
		self._label3.TabIndex = 2
		self._label3.Text = "Pence"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(13, 60)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(98, 35)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(117, 60)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(98, 35)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(221, 60)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(98, 35)
		self._textBox3.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.YellowGreen
		self._button1.Font = System.Drawing.Font("Ravie", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 101)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(306, 37)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Maroon
		self._button2.Font = System.Drawing.Font("OCR A Extended", 18)
		self._button2.ForeColor = System.Drawing.SystemColors.Control
		self._button2.Location = System.Drawing.Point(117, 314)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(98, 36)
		self._button2.TabIndex = 7
		self._button2.Text = "EXIT"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ControlDark
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(13, 184)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(306, 32)
		self._label4.TabIndex = 8
		self._label4.Text = "New Monetary System:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.CornflowerBlue
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(13, 227)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(306, 84)
		self._label5.TabIndex = 9
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Orange
		self._button3.Font = System.Drawing.Font("Ravie", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(13, 144)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(306, 37)
		self._button3.TabIndex = 10
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(331, 362)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang65h-2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Pound = int(self._textBox1.Text)
		Shilling = int(self._textBox2.Text)
		Pence = int(self._textBox3.Text)
		NewPence = (Shilling * 12) + Pence
		Decimal = (NewPence / 2.4) / 100
		NewPound = (Pound + Decimal)
		self._label5.Text=str(NewPound)
		

	def Button3Click(self, sender, e):
		self._textBox1.Text=""
		self._textBox2.Text=""
		self._textBox3.Text=""
		self._label5.Text=""

	def Button2Click(self, sender, e):
		Application.Exit()