import System.Drawing
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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label6 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("OCR A Extended", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(228, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter your first name:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("OCR A Extended", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label2.Location = System.Drawing.Point(13, 64)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(228, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Enter your last name:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("OCR A Extended", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label3.Location = System.Drawing.Point(13, 120)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(241, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "This is your full name:"
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button1.Location = System.Drawing.Point(3, 181)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(135, 43)
		self._button1.TabIndex = 3
		self._button1.Text = "Show Name"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button2.Location = System.Drawing.Point(144, 181)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(135, 43)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button3.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._button3.Location = System.Drawing.Point(285, 197)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(88, 27)
		self._button3.TabIndex = 5
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label6.Font = System.Drawing.Font("Microsoft YaHei UI", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.SystemColors.ControlDark
		self._label6.Location = System.Drawing.Point(260, 120)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(111, 23)
		self._label6.TabIndex = 8
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(260, 2)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 35)
		self._textBox1.TabIndex = 9
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(260, 53)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 35)
		self._textBox2.TabIndex = 10
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(372, 236)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog119Fullname"
		self.ResumeLayout(False)
		self.PerformLayout()


	def BtnShowClick (self, sender, e):
		strFirName = (self._textBox1.Text)
		strSecName = (self._textBox2.Text)
		strfulName = (strFirName) + " " + (strSecName)
		self._lblFullName.Text = strFullName