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
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Uighur", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(161, 54)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Uighur", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(12, 73)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(161, 54)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkRed
		self._button3.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._button3.Location = System.Drawing.Point(52, 133)
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
		self._label1.Font = System.Drawing.Font("MS PGothic", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(189, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(317, 54)
		self._label1.TabIndex = 3
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label2.Font = System.Drawing.Font("MS PGothic", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(189, 73)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(317, 54)
		self._label2.TabIndex = 4
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label3.Font = System.Drawing.Font("MS PGothic", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(189, 133)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(317, 54)
		self._label3.TabIndex = 5
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label4.Font = System.Drawing.Font("MS PGothic", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(189, 197)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(317, 54)
		self._label4.TabIndex = 6
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label5.Font = System.Drawing.Font("MS PGothic", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(189, 262)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(317, 54)
		self._label5.TabIndex = 7
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlDark
		self.ClientSize = System.Drawing.Size(518, 329)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Phonesnumbers"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label1.Text="(608) 754-2226"
		self._label2.Text="1 (800) 440-0680"
		self._label3.Text="1 (800) 925-6278"
		self._label4.Text="1 (734) 930-3030"
		self._label5.Text="1 (888) 624-8140"

	def Button2Click(self, sender, e):
		self._label1.Text=""
		self._label2.Text=""
		self._label3.Text=""
		self._label4.Text=""
		self._label5.Text=""

	def Button3Click(self, sender, e):
		Application.Exit()