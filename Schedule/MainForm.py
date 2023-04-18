import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 26)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(153, 71)
		self._button1.TabIndex = 0
		self._button1.Text = "Schedule"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75)
		self._button2.Location = System.Drawing.Point(13, 104)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(153, 71)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Maroon
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 8.75)
		self._button3.ForeColor = System.Drawing.SystemColors.Control
		self._button3.Location = System.Drawing.Point(13, 419)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(190, 26)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(211, 35)
		self._label1.TabIndex = 3
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(190, 61)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(211, 35)
		self._label2.TabIndex = 4
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(190, 96)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(211, 35)
		self._label3.TabIndex = 5
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(190, 131)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(211, 35)
		self._label4.TabIndex = 6
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(190, 169)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(211, 35)
		self._label5.TabIndex = 7
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(190, 211)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(211, 35)
		self._label6.TabIndex = 8
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label6.Click += self.Label6Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(190, 253)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(211, 35)
		self._label7.TabIndex = 9
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label8.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(190, 293)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(211, 35)
		self._label8.TabIndex = 10
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(550, 454)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Schedule"
		self.ResumeLayout(False)


	def Label4Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label1.Text="Digital Art 1"
		self._label2.Text="Computer Programming"
		self._label3.Text="Algebra II"
		self._label4.Text="Web Design"
		self._label5.Text="Advanced studio drawing"
		self._label6.Text="Creative Writing"
		self._label7.Text="Civil Engineering"
		self._label8.Text="Writing Through Films"
		

	def Button2Click(self, sender, e):
		self._label1.Text=""
		self._label2.Text=""
		self._label3.Text=""
		self._label4.Text=""
		self._label5.Text=""
		self._label6.Text=""
		self._label7.Text=""
		self._label8.Text=""

	def Button3Click(self, sender, e):
		Application.Exit()