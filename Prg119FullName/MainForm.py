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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonShadow
		self._label1.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(147, 32)
		self._label1.TabIndex = 0
		self._label1.Text = "First Name"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonShadow
		self._label2.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 69)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(147, 32)
		self._label2.TabIndex = 1
		self._label2.Text = "Last Name"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 16)
		self._textBox1.Location = System.Drawing.Point(165, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(243, 32)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 16)
		self._textBox2.Location = System.Drawing.Point(165, 69)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(243, 32)
		self._textBox2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ButtonShadow
		self._label3.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 146)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(147, 60)
		self._label3.TabIndex = 4
		self._label3.Text = "Full Name"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.Window
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(165, 146)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(243, 60)
		self._label4.TabIndex = 5
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 104)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(395, 39)
		self._button1.TabIndex = 6
		self._button1.Text = "Full Name-ify"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(12, 209)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(147, 40)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Maroon
		self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._button3.Location = System.Drawing.Point(165, 209)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(243, 40)
		self._button3.TabIndex = 8
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(420, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prg119FullName"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label4.Text = (self._textBox1.Text) + " " + (self._textBox2.Text)

	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()