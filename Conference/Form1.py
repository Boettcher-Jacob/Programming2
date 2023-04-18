
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.parent=parent
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._button1 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._checkBox2)
		self._groupBox1.Controls.Add(self._checkBox1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(315, 154)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Conference"
		# 
		# checkBox1
		# 
		self._checkBox1.Font = System.Drawing.Font("Microsoft YaHei", 12)
		self._checkBox1.Location = System.Drawing.Point(7, 20)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(271, 45)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "Conference Registration: $896"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Font = System.Drawing.Font("Microsoft YaHei", 12)
		self._checkBox2.Location = System.Drawing.Point(7, 84)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(271, 64)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "Opening Dinner Night and Keynote: $30"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._radioButton4)
		self._groupBox2.Controls.Add(self._radioButton3)
		self._groupBox2.Controls.Add(self._radioButton2)
		self._groupBox2.Controls.Add(self._radioButton1)
		self._groupBox2.Location = System.Drawing.Point(334, 13)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(323, 154)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Preconference Workshops"
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(6, 41)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(154, 49)
		self._radioButton1.TabIndex = 2
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Intro to E-Commerce"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(6, 96)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(154, 52)
		self._radioButton2.TabIndex = 3
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Future of the Web"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(166, 41)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(151, 49)
		self._radioButton3.TabIndex = 4
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Advanced Visual Basic"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# radioButton4
		# 
		self._radioButton4.Location = System.Drawing.Point(166, 96)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(151, 52)
		self._radioButton4.TabIndex = 4
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "Network Security"
		self._radioButton4.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 173)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(150, 41)
		self._button1.TabIndex = 2
		self._button1.Text = "Return"
		self._button1.UseVisualStyleBackColor = True
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(669, 226)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "Form1"
		self.Text = "Form1"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)

