import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# radioButton1
		# 
		self._radioButton1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.Location = System.Drawing.Point(6, 19)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(174, 41)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Choice I"
		self._radioButton1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# checkBox1
		# 
		self._checkBox1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox1.Location = System.Drawing.Point(6, 19)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(174, 41)
		self._checkBox1.TabIndex = 1
		self._checkBox1.Text = "Choice I"
		self._checkBox1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(186, 166)
		self._groupBox1.TabIndex = 2
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "groupBox1"
		# 
		# radioButton2
		# 
		self._radioButton2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.Location = System.Drawing.Point(6, 66)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(174, 41)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Choice II"
		self._radioButton2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.Location = System.Drawing.Point(6, 113)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(174, 41)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Choice III"
		self._radioButton3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._checkBox3)
		self._groupBox2.Controls.Add(self._checkBox2)
		self._groupBox2.Controls.Add(self._checkBox1)
		self._groupBox2.Location = System.Drawing.Point(203, 13)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(186, 166)
		self._groupBox2.TabIndex = 3
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "groupBox2"
		# 
		# checkBox2
		# 
		self._checkBox2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox2.Location = System.Drawing.Point(6, 67)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(174, 41)
		self._checkBox2.TabIndex = 2
		self._checkBox2.Text = "Choice I"
		self._checkBox2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox3.Location = System.Drawing.Point(6, 114)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(174, 41)
		self._checkBox3.TabIndex = 3
		self._checkBox3.Text = "Choice I"
		self._checkBox3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._checkBox3.UseVisualStyleBackColor = True
		self._checkBox3.CheckedChanged += self.CheckBox3CheckedChanged
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(99, 185)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 38)
		self._button1.TabIndex = 4
		self._button1.Text = "Ok"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(202, 185)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(108, 38)
		self._button2.TabIndex = 5
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(401, 235)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg247Radio"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)

	def Button1Click(self, sender, e):
		if self._radioButton1.Checked == True:
			strMessage = "You selected Choice 1"
		if self._radioButton2.Checked == True:
			strMessage = "You selected Choice 2"
		if self._radioButton3.Checked == True:
			strMessage = "You selected Choice 3"
			
		if self.checkBox1.Checked == True:
			strMessage +=