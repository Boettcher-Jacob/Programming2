﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("OCR A Extended", 11)
		self._button1.Location = System.Drawing.Point(369, 122)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 29)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(350, 29)
		self._label1.TabIndex = 1
		self._label1.Text = "Annual salary:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(13, 55)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(350, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Pay Periods per year :"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(13, 90)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(350, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "Salary per pay period :"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(369, 15)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 29)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(369, 50)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 29)
		self._textBox2.TabIndex = 5
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("OCR A Extended", 11)
		self._button2.Location = System.Drawing.Point(263, 122)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 29)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
		self._button3.Font = System.Drawing.Font("OCR A Extended", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.Control
		self._button3.Location = System.Drawing.Point(12, 122)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(58, 29)
		self._button3.TabIndex = 8
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.Window
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(369, 86)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 27)
		self._label4.TabIndex = 9
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(481, 157)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg153SalaryCalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox3TextChanged(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		# Salary Calculation
		decAnnualSalary = 0.0
		intPayPeriods = 0
		decSalary = 0.0
		
		decAnnualSalary = float(self._textBox1.Text)
		intPayPeriods = int(self._textBox2.Text)
		decSalary = decAnnualSalary / intPayPeriods
		self._label4.Text = str(round(decSalary,2))

	def Button2Click(self, sender, e):
		self._label4.Text=""
		self._textBox1.Text=""
		self._textBox2.Text=""

	def Button3Click(self, sender, e):
		Application.Exit()