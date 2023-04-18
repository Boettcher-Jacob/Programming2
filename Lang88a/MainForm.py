﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(109, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(176, 35)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(109, 72)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(176, 35)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ControlDark
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(48, 165)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(176, 30)
		self._label1.TabIndex = 2
		self._label1.Text = "Sum:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.CornflowerBlue
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(237, 165)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(176, 30)
		self._label2.TabIndex = 3
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlDark
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(48, 197)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(176, 30)
		self._label3.TabIndex = 5
		self._label3.Text = "Difference:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.CornflowerBlue
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(237, 197)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(176, 30)
		self._label4.TabIndex = 4
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(48, 115)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(365, 38)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(299, 9)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(151, 35)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(299, 72)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(151, 35)
		self._button3.TabIndex = 8
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ControlDark
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(48, 232)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(176, 30)
		self._label5.TabIndex = 12
		self._label5.Text = "Product:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.CornflowerBlue
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(237, 232)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(176, 30)
		self._label6.TabIndex = 11
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ControlDark
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(48, 269)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(176, 30)
		self._label7.TabIndex = 10
		self._label7.Text = "Average:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.CornflowerBlue
		self._label8.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(237, 269)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(176, 30)
		self._label8.TabIndex = 9
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.ControlDark
		self._label9.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(48, 303)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(176, 30)
		self._label9.TabIndex = 16
		self._label9.Text = "Absolute Val:"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.CornflowerBlue
		self._label10.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(237, 303)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(176, 30)
		self._label10.TabIndex = 15
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.SystemColors.ControlDark
		self._label11.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(48, 339)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(176, 30)
		self._label11.TabIndex = 14
		self._label11.Text = "Max:"
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.CornflowerBlue
		self._label12.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(237, 339)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(176, 30)
		self._label12.TabIndex = 13
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.SystemColors.ControlDark
		self._label13.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(48, 374)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(176, 30)
		self._label13.TabIndex = 18
		self._label13.Text = "Min:"
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.CornflowerBlue
		self._label14.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(237, 374)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(176, 30)
		self._label14.TabIndex = 17
		self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.SystemColors.ControlDark
		self._label15.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.Location = System.Drawing.Point(3, 63)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(100, 47)
		self._label15.TabIndex = 20
		self._label15.Text = "Num 2:"
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.SystemColors.ControlDark
		self._label16.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label16.Location = System.Drawing.Point(3, 3)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(100, 47)
		self._label16.TabIndex = 19
		self._label16.Text = "Num 1:"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(462, 442)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "Lang88a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Sum = num1 + num2
		Difference = num1 - num2
		Product = num1 * num2
		Average = (num1 + num2)/2
		Absolute = abs(num1 + num2)
		
		Max = 0
		Min = 0
		if num1 >= num2:
			Max = num1
		else:
			Max = num2
		if num1 < num2:
			Min = num1
		else:
			Min = num2
			
		self._label2.Text= str(Sum)
		self._label4.Text= str(Difference)
		self._label6.Text= str(Product)
		self._label8.Text= str(Average)
		self._label10.Text= str(Absolute)
		self._label12.Text= str(Max)
		self._label14.Text= str(Min)

	def Button2Click(self, sender, e):
		self._label2.Text= ""
		self._label4.Text= ""
		self._label6.Text= ""
		self._label8.Text= ""
		self._label10.Text= ""
		self._label12.Text= ""
		self._label14.Text= ""
		self._textBox1.Text= ""
		self._textBox2.Text= ""

	def Button3Click(self, sender, e):
		Application.Exit()