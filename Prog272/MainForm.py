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
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._Rating = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(258, 226)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Rating"
		# 
		# radioButton1
		# 
		self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.Location = System.Drawing.Point(7, 20)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(245, 60)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Daytime"
		self._radioButton1.UseVisualStyleBackColor = True
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.Location = System.Drawing.Point(6, 86)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(246, 60)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Evening"
		self._radioButton2.UseVisualStyleBackColor = True
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.Location = System.Drawing.Point(6, 152)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(246, 60)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Off-Peak"
		self._radioButton3.UseVisualStyleBackColor = True
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 246)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(133, 30)
		self._label1.TabIndex = 1
		self._label1.Text = "Call Time:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(153, 246)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(118, 31)
		self._textBox1.TabIndex = 2
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 462)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(259, 30)
		self._label2.TabIndex = 3
		self._label2.Text = "Total Due:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._button1.Location = System.Drawing.Point(12, 292)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(259, 41)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._button2.Location = System.Drawing.Point(13, 339)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(259, 41)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# Rating
		# 
		self._Rating.Location = System.Drawing.Point(13, 383)
		self._Rating.Name = "Rating"
		self._Rating.Size = System.Drawing.Size(43, 29)
		self._Rating.TabIndex = 6
		self._Rating.Text = "0.0"
		self._Rating.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._Rating.Visible = False
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(293, 501)
		self.Controls.Add(self._Rating)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Prog272"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Rating = float(self._Rating.Text)
		Minutes = float(self._textBox1.Text)
			
		Total = Minutes * Rating
		
		self._label2.Text = "Total Due:" + "  " + str(Total)

	def Button2Click(self, sender, e):
		self._label2.Text = "Total Due:"

	def RadioButton1CheckedChanged(self, sender, e):
		self._Rating.Text= str(0.07)

	def RadioButton2CheckedChanged(self, sender, e):
		self._Rating.Text= str(0.12)

	def RadioButton3CheckedChanged(self, sender, e):
		self._Rating.Text= str(0.05)