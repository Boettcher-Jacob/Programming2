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
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.Control
		self._label1.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(176, 49)
		self._label1.TabIndex = 0
		self._label1.Text = "Variable 1:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.Control
		self._label2.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(13, 62)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(176, 49)
		self._label2.TabIndex = 1
		self._label2.Text = "Variable 2:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.Control
		self._label3.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(13, 111)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(176, 49)
		self._label3.TabIndex = 2
		self._label3.Text = "Variable 3:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.Control
		self._label4.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(13, 160)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(176, 49)
		self._label4.TabIndex = 3
		self._label4.Text = "Variable 4:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 16)
		self._textBox1.Location = System.Drawing.Point(195, 22)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 32)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 16)
		self._textBox2.Location = System.Drawing.Point(195, 71)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 32)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 16)
		self._textBox3.Location = System.Drawing.Point(195, 120)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 32)
		self._textBox3.TabIndex = 6
		# 
		# textBox4
		# 
		self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 16)
		self._textBox4.Location = System.Drawing.Point(195, 169)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 32)
		self._textBox4.TabIndex = 7
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._button1.Font = System.Drawing.Font("OCR A Extended", 16.25)
		self._button1.Location = System.Drawing.Point(12, 212)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(283, 52)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._button2.Font = System.Drawing.Font("OCR A Extended", 9.25)
		self._button2.Location = System.Drawing.Point(12, 270)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(133, 25)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._button3.Font = System.Drawing.Font("OCR A Extended", 9.25)
		self._button3.ForeColor = System.Drawing.SystemColors.Control
		self._button3.Location = System.Drawing.Point(151, 270)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(144, 25)
		self._button3.TabIndex = 10
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.Control
		self._label5.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 298)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(283, 49)
		self._label5.TabIndex = 11
		self._label5.Text = "Sum:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.Control
		self._label6.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(13, 347)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(282, 49)
		self._label6.TabIndex = 12
		self._label6.Text = "Average:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(812, 405)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog54b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		V1 = float(self._textBox1.Text)
		V2 = float(self._textBox2.Text)
		V3 = float(self._textBox3.Text)
		V4 = float(self._textBox4.Text)
		
		sum = V1 + V2 + V3 + V4
		
		average = (V1 + V2 + V3 + V4) / 4
		
		self._label5.Text = "Sum:" + str(sum)
		self._label6.Text = "Average:" + str(average)