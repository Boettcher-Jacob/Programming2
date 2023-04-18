import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._textBox7 = System.Windows.Forms.TextBox()
		self._textBox8 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox9 = System.Windows.Forms.TextBox()
		self._label9 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._textBox8)
		self._groupBox1.Controls.Add(self._textBox7)
		self._groupBox1.Controls.Add(self._textBox5)
		self._groupBox1.Controls.Add(self._textBox6)
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._textBox4)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label8)
		self._groupBox1.Controls.Add(self._label7)
		self._groupBox1.Controls.Add(self._label6)
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(646, 238)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "groupBox1"
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(49, 21)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(75, 33)
		self._label1.TabIndex = 0
		self._label1.Text = "Name"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(7, 62)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(117, 33)
		self._label2.TabIndex = 1
		self._label2.Text = "Company"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(30, 104)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(94, 33)
		self._label3.TabIndex = 2
		self._label3.Text = "Address"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(67, 146)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(57, 33)
		self._label4.TabIndex = 3
		self._label4.Text = "City"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(284, 20)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(81, 33)
		self._label5.TabIndex = 4
		self._label5.Text = "Phone"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(295, 62)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(70, 33)
		self._label6.TabIndex = 5
		self._label6.Text = "Email"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(149, 193)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(64, 33)
		self._label7.TabIndex = 6
		self._label7.Text = "State"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label8
		# 
		self._label8.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(393, 193)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(45, 33)
		self._label8.TabIndex = 7
		self._label8.Text = "Zip"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(130, 21)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 35)
		self._textBox1.TabIndex = 8
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(130, 62)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 35)
		self._textBox2.TabIndex = 9
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(130, 145)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 35)
		self._textBox3.TabIndex = 11
		# 
		# textBox4
		# 
		self._textBox4.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.Location = System.Drawing.Point(130, 104)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 35)
		self._textBox4.TabIndex = 10
		# 
		# textBox5
		# 
		self._textBox5.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox5.Location = System.Drawing.Point(371, 62)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(100, 35)
		self._textBox5.TabIndex = 13
		# 
		# textBox6
		# 
		self._textBox6.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox6.Location = System.Drawing.Point(371, 21)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(100, 35)
		self._textBox6.TabIndex = 12
		# 
		# textBox7
		# 
		self._textBox7.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox7.Location = System.Drawing.Point(219, 191)
		self._textBox7.Name = "textBox7"
		self._textBox7.Size = System.Drawing.Size(100, 35)
		self._textBox7.TabIndex = 14
		# 
		# textBox8
		# 
		self._textBox8.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox8.Location = System.Drawing.Point(444, 192)
		self._textBox8.Name = "textBox8"
		self._textBox8.Size = System.Drawing.Size(100, 35)
		self._textBox8.TabIndex = 15
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 12)
		self._button1.Location = System.Drawing.Point(12, 334)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(190, 89)
		self._button1.TabIndex = 1
		self._button1.Text = "&Select Conference Settings"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 12)
		self._button2.Location = System.Drawing.Point(232, 334)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(190, 89)
		self._button2.TabIndex = 2
		self._button2.Text = "&Reset"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 12)
		self._button3.Location = System.Drawing.Point(457, 334)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(190, 89)
		self._button3.TabIndex = 3
		self._button3.Text = "E&xit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# textBox9
		# 
		self._textBox9.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox9.Location = System.Drawing.Point(454, 275)
		self._textBox9.Name = "textBox9"
		self._textBox9.Size = System.Drawing.Size(100, 35)
		self._textBox9.TabIndex = 17
		# 
		# label9
		# 
		self._label9.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(327, 277)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(121, 33)
		self._label9.TabIndex = 16
		self._label9.Text = "Total Cost:"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(671, 435)
		self.Controls.Add(self._textBox9)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Conference Registration System"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)
		self.PerformLayout()

