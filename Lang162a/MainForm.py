import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("OCR A Extended", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(173, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(92, 35)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("OCR A Extended", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(173, 85)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(92, 35)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("OCR A Extended", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(155, 35)
		self._label1.TabIndex = 2
		self._label1.Text = "Chairs"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("OCR A Extended", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 85)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(155, 35)
		self._label2.TabIndex = 3
		self._label2.Text = "Guests"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("OCR A Extended", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 123)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(253, 48)
		self._button1.TabIndex = 4
		self._button1.Text = """Calculate
"""
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(369, 283)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 5
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(377, 291)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 6
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("OCR A Extended", 18)
		self._label3.Location = System.Drawing.Point(12, 191)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(199, 35)
		self._label3.TabIndex = 7
		self._label3.Text = "Permutations"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(812, 589)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Lang162a"
		self.ResumeLayout(False)
		self.PerformLayout()

