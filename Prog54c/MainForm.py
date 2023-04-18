import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._labelpi = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(85, 35)
		self._label1.TabIndex = 0
		self._label1.Text = "Radius"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# labelpi
		# 
		self._labelpi.Location = System.Drawing.Point(-3, -7)
		self._labelpi.Name = "labelpi"
		self._labelpi.Size = System.Drawing.Size(100, 23)
		self._labelpi.TabIndex = 1
		self._labelpi.Text = "3.14159"
		self._labelpi.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._labelpi.Visible = False
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(103, 16)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(185, 35)
		self._textBox1.TabIndex = 2
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 54)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(276, 43)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 100)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(276, 35)
		self._label2.TabIndex = 4
		self._label2.Text = "Circumference: "
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 140)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(276, 35)
		self._label3.TabIndex = 5
		self._label3.Text = "Area:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label4.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 180)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(276, 35)
		self._label4.TabIndex = 6
		self._label4.Text = "Diameter:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(12, 218)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(141, 41)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(159, 218)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(129, 41)
		self._button3.TabIndex = 8
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label5.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(344, 127)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(141, 35)
		self._label5.TabIndex = 9
		self._label5.Text = "BAZINGA"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(313, 269)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._labelpi)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		r = float(self._textBox1.Text)
		pi = 3.14159
		
		circum = 2 * pi * r
		area = pi*(r**2)
		diam = 2 * r
		
		
		self._label2.Text= "Circumference:" + str(round(circum,3))
		self._label3.Text= "Area:" + str(round(area, 3))
		self._label4.Text= "Diameter:" + str(round(diam, 3))
			

	def Button2Click(self, sender, e):
		self._label2.Text="Circumference:"
		self._label3.Text="Area:"
		self._label4.Text="Diameter:"
		self._textBox1.Text=""

	def Button3Click(self, sender, e):
		Application.Exit()