import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._radadult = System.Windows.Forms.RadioButton()
		self._radchild = System.Windows.Forms.RadioButton()
		self._radstudent = System.Windows.Forms.RadioButton()
		self._radsenior = System.Windows.Forms.RadioButton()
		self._radyoga = System.Windows.Forms.RadioButton()
		self._radkarate = System.Windows.Forms.RadioButton()
		self._radtrainer = System.Windows.Forms.RadioButton()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._txtmonths = System.Windows.Forms.TextBox()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._lblmonths = System.Windows.Forms.Label()
		self._lbltotal = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self._groupBox4.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._radsenior)
		self._groupBox1.Controls.Add(self._radstudent)
		self._groupBox1.Controls.Add(self._radchild)
		self._groupBox1.Controls.Add(self._radadult)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(200, 163)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Type of Membership"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._radtrainer)
		self._groupBox2.Controls.Add(self._radkarate)
		self._groupBox2.Controls.Add(self._radyoga)
		self._groupBox2.Location = System.Drawing.Point(219, 13)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(200, 163)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Options"
		# 
		# radadult
		# 
		self._radadult.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radadult.Location = System.Drawing.Point(7, 19)
		self._radadult.Name = "radadult"
		self._radadult.Size = System.Drawing.Size(177, 27)
		self._radadult.TabIndex = 0
		self._radadult.TabStop = True
		self._radadult.Text = "Standard Adult"
		self._radadult.UseVisualStyleBackColor = True
		self._radadult.CheckedChanged += self.RadadultCheckedChanged
		# 
		# radchild
		# 
		self._radchild.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radchild.Location = System.Drawing.Point(6, 52)
		self._radchild.Name = "radchild"
		self._radchild.Size = System.Drawing.Size(177, 27)
		self._radchild.TabIndex = 1
		self._radchild.TabStop = True
		self._radchild.Text = "Child (12 or Under)"
		self._radchild.UseVisualStyleBackColor = True
		# 
		# radstudent
		# 
		self._radstudent.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radstudent.Location = System.Drawing.Point(7, 85)
		self._radstudent.Name = "radstudent"
		self._radstudent.Size = System.Drawing.Size(177, 27)
		self._radstudent.TabIndex = 2
		self._radstudent.TabStop = True
		self._radstudent.Text = "Student"
		self._radstudent.UseVisualStyleBackColor = True
		# 
		# radsenior
		# 
		self._radsenior.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radsenior.Location = System.Drawing.Point(7, 118)
		self._radsenior.Name = "radsenior"
		self._radsenior.Size = System.Drawing.Size(177, 27)
		self._radsenior.TabIndex = 3
		self._radsenior.TabStop = True
		self._radsenior.Text = "Senior"
		self._radsenior.UseVisualStyleBackColor = True
		# 
		# radyoga
		# 
		self._radyoga.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radyoga.Location = System.Drawing.Point(7, 35)
		self._radyoga.Name = "radyoga"
		self._radyoga.Size = System.Drawing.Size(188, 35)
		self._radyoga.TabIndex = 0
		self._radyoga.TabStop = True
		self._radyoga.Text = "Yoga"
		self._radyoga.UseVisualStyleBackColor = True
		# 
		# radkarate
		# 
		self._radkarate.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radkarate.Location = System.Drawing.Point(7, 65)
		self._radkarate.Name = "radkarate"
		self._radkarate.Size = System.Drawing.Size(188, 35)
		self._radkarate.TabIndex = 1
		self._radkarate.TabStop = True
		self._radkarate.Text = "Karate"
		self._radkarate.UseVisualStyleBackColor = True
		self._radkarate.CheckedChanged += self.RadioButton6CheckedChanged
		# 
		# radtrainer
		# 
		self._radtrainer.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radtrainer.Location = System.Drawing.Point(6, 106)
		self._radtrainer.Name = "radtrainer"
		self._radtrainer.Size = System.Drawing.Size(187, 35)
		self._radtrainer.TabIndex = 2
		self._radtrainer.TabStop = True
		self._radtrainer.Text = "Personal Trainer"
		self._radtrainer.UseVisualStyleBackColor = True
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._txtmonths)
		self._groupBox3.Controls.Add(self._label1)
		self._groupBox3.Location = System.Drawing.Point(13, 183)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(200, 156)
		self._groupBox3.TabIndex = 2
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "groupBox3"
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(7, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(187, 54)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the Amount of Months"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# txtmonths
		# 
		self._txtmonths.Location = System.Drawing.Point(7, 77)
		self._txtmonths.Name = "txtmonths"
		self._txtmonths.Size = System.Drawing.Size(187, 20)
		self._txtmonths.TabIndex = 1
		# 
		# groupBox4
		# 
		self._groupBox4.Controls.Add(self._lbltotal)
		self._groupBox4.Controls.Add(self._lblmonths)
		self._groupBox4.Controls.Add(self._label3)
		self._groupBox4.Controls.Add(self._label2)
		self._groupBox4.Location = System.Drawing.Point(220, 183)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(199, 156)
		self._groupBox4.TabIndex = 3
		self._groupBox4.TabStop = False
		self._groupBox4.Text = "groupBox4"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(6, 43)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(74, 43)
		self._label2.TabIndex = 0
		self._label2.Text = "Monthly Fee"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(6, 97)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(74, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Total"
		# 
		# lblmonths
		# 
		self._lblmonths.BackColor = System.Drawing.SystemColors.ControlLight
		self._lblmonths.Location = System.Drawing.Point(86, 51)
		self._lblmonths.Name = "lblmonths"
		self._lblmonths.Size = System.Drawing.Size(100, 23)
		self._lblmonths.TabIndex = 4
		self._lblmonths.Text = "--"
		self._lblmonths.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lbltotal
		# 
		self._lbltotal.BackColor = System.Drawing.SystemColors.ControlLight
		self._lbltotal.Location = System.Drawing.Point(86, 98)
		self._lbltotal.Name = "lbltotal"
		self._lbltotal.Size = System.Drawing.Size(100, 23)
		self._lbltotal.TabIndex = 5
		self._lbltotal.Text = "--"
		self._lbltotal.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 346)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(200, 23)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(220, 346)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(199, 23)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(175, 375)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(87, 33)
		self._button3.TabIndex = 6
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(433, 411)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg250Membershipfee"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self._groupBox3.PerformLayout()
		self._groupBox4.ResumeLayout(False)
		self.ResumeLayout(False)	

	def Button1Click(self, sender, e):
		total = plan + option
		monthly = float(self._txtmonths.Text)
		
		
		
		
		
		if monthly > 1 or >= 3:
			pass
		elif monthly > 4 or >= 6:
			discount = (total * .05)
			newtotal = amount - total
		elif monthly > 7 or >= 9:
			discount = (total * .08)
			newtotal = amount - total
		elif monthly >= 10:					
			discount = (total * .10)
			newtotal = amount - total