import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._button1 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._radioButton4)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(316, 204)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "groupBox1"
		# 
		# radioButton1
		# 
		self._radioButton1.Font = System.Drawing.Font("Segoe Print", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.Location = System.Drawing.Point(6, 19)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(302, 41)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Allen Hall $1,500 per semester"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Font = System.Drawing.Font("Segoe Print", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.Location = System.Drawing.Point(6, 66)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(302, 41)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Pike Hall $1,600 per semester"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Font = System.Drawing.Font("Segoe Print", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.Location = System.Drawing.Point(6, 113)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(302, 42)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Farthing Hall $1,200 per semester"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# radioButton4
		# 
		self._radioButton4.Font = System.Drawing.Font("Segoe Print", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton4.Location = System.Drawing.Point(6, 161)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(301, 40)
		self._radioButton4.TabIndex = 3
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "University Suites $1,800 per semester"
		self._radioButton4.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Segoe Marker", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(336, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(244, 107)
		self._button1.TabIndex = 1
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(592, 272)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "MealPlan"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)

