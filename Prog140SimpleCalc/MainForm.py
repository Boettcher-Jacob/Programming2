import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._btnadd = System.Windows.Forms.Button()
		self._btnflodiv = System.Windows.Forms.Button()
		self._btnX = System.Windows.Forms.Button()
		self._btndiv = System.Windows.Forms.Button()
		self._btnsub = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._lblOp = System.Windows.Forms.Label()
		self._lblRe = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._btnexp = System.Windows.Forms.Button()
		self._btnMOD = System.Windows.Forms.Button()
		self._Clear = System.Windows.Forms.Button()
		self._Exit = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# btnadd
		# 
		self._btnadd.BackColor = System.Drawing.SystemColors.ButtonFace
		self._btnadd.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._btnadd.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnadd.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._btnadd.Location = System.Drawing.Point(322, 15)
		self._btnadd.Name = "btnadd"
		self._btnadd.Size = System.Drawing.Size(61, 40)
		self._btnadd.TabIndex = 0
		self._btnadd.Text = "+"
		self._btnadd.UseVisualStyleBackColor = False
		self._btnadd.Click += self.BtnaddClick
		# 
		# btnflodiv
		# 
		self._btnflodiv.BackColor = System.Drawing.SystemColors.ButtonFace
		self._btnflodiv.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._btnflodiv.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnflodiv.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._btnflodiv.Location = System.Drawing.Point(456, 61)
		self._btnflodiv.Name = "btnflodiv"
		self._btnflodiv.Size = System.Drawing.Size(61, 40)
		self._btnflodiv.TabIndex = 1
		self._btnflodiv.Text = "//"
		self._btnflodiv.UseVisualStyleBackColor = False
		self._btnflodiv.Click += self.BtnflodivClick
		# 
		# btnX
		# 
		self._btnX.BackColor = System.Drawing.SystemColors.ButtonFace
		self._btnX.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._btnX.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnX.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._btnX.Location = System.Drawing.Point(456, 15)
		self._btnX.Name = "btnX"
		self._btnX.Size = System.Drawing.Size(61, 40)
		self._btnX.TabIndex = 2
		self._btnX.Text = "*"
		self._btnX.UseVisualStyleBackColor = False
		self._btnX.Click += self.BtnXClick
		# 
		# btndiv
		# 
		self._btndiv.BackColor = System.Drawing.SystemColors.ButtonFace
		self._btndiv.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._btndiv.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btndiv.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._btndiv.Location = System.Drawing.Point(389, 15)
		self._btndiv.Name = "btndiv"
		self._btndiv.Size = System.Drawing.Size(61, 40)
		self._btndiv.TabIndex = 3
		self._btndiv.Text = "/"
		self._btndiv.UseVisualStyleBackColor = False
		self._btndiv.Click += self.BtndivClick
		# 
		# btnsub
		# 
		self._btnsub.BackColor = System.Drawing.SystemColors.ButtonFace
		self._btnsub.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._btnsub.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnsub.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._btnsub.Location = System.Drawing.Point(322, 61)
		self._btnsub.Name = "btnsub"
		self._btnsub.Size = System.Drawing.Size(61, 40)
		self._btnsub.TabIndex = 4
		self._btnsub.Text = "-"
		self._btnsub.UseVisualStyleBackColor = False
		self._btnsub.Click += self.BtnsubClick
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.Control
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(138, 31)
		self._label1.TabIndex = 5
		self._label1.Text = "Number 1 :"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.Control
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 82)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(138, 31)
		self._label2.TabIndex = 6
		self._label2.Text = "Number 2 :"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ButtonShadow
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 51)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(138, 31)
		self._label3.TabIndex = 7
		self._label3.Text = "Operation :"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblOp
		# 
		self._lblOp.BackColor = System.Drawing.SystemColors.ButtonShadow
		self._lblOp.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblOp.Location = System.Drawing.Point(156, 51)
		self._lblOp.Name = "lblOp"
		self._lblOp.Size = System.Drawing.Size(138, 31)
		self._lblOp.TabIndex = 10
		self._lblOp.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblRe
		# 
		self._lblRe.BackColor = System.Drawing.SystemColors.ButtonShadow
		self._lblRe.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblRe.Location = System.Drawing.Point(156, 113)
		self._lblRe.Name = "lblRe"
		self._lblRe.Size = System.Drawing.Size(138, 31)
		self._lblRe.TabIndex = 12
		self._lblRe.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ButtonShadow
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 113)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(138, 31)
		self._label5.TabIndex = 11
		self._label5.Text = "Result :"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# btnexp
		# 
		self._btnexp.BackColor = System.Drawing.SystemColors.ButtonFace
		self._btnexp.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._btnexp.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnexp.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._btnexp.Location = System.Drawing.Point(389, 61)
		self._btnexp.Name = "btnexp"
		self._btnexp.Size = System.Drawing.Size(61, 40)
		self._btnexp.TabIndex = 13
		self._btnexp.Text = "^"
		self._btnexp.UseVisualStyleBackColor = False
		self._btnexp.Click += self.BtnexpClick
		# 
		# btnMOD
		# 
		self._btnMOD.BackColor = System.Drawing.SystemColors.ButtonFace
		self._btnMOD.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._btnMOD.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnMOD.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._btnMOD.Location = System.Drawing.Point(322, 107)
		self._btnMOD.Name = "btnMOD"
		self._btnMOD.Size = System.Drawing.Size(76, 40)
		self._btnMOD.TabIndex = 14
		self._btnMOD.Text = "MOD"
		self._btnMOD.UseVisualStyleBackColor = False
		self._btnMOD.Click += self.BtnMODClick
		# 
		# Clear
		# 
		self._Clear.BackColor = System.Drawing.SystemColors.ButtonFace
		self._Clear.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._Clear.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Clear.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._Clear.Location = System.Drawing.Point(404, 107)
		self._Clear.Name = "Clear"
		self._Clear.Size = System.Drawing.Size(113, 47)
		self._Clear.TabIndex = 15
		self._Clear.Text = "Clear"
		self._Clear.UseVisualStyleBackColor = False
		self._Clear.Click += self.Button8Click
		# 
		# Exit
		# 
		self._Exit.BackColor = System.Drawing.Color.Maroon
		self._Exit.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._Exit.Font = System.Drawing.Font("OCR A Extended", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._Exit.ForeColor = System.Drawing.SystemColors.Control
		self._Exit.Location = System.Drawing.Point(12, 150)
		self._Exit.Name = "Exit"
		self._Exit.Size = System.Drawing.Size(75, 23)
		self._Exit.TabIndex = 16
		self._Exit.Text = "EXIT"
		self._Exit.UseVisualStyleBackColor = False
		self._Exit.Click += self.Button9Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(156, 18)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(138, 35)
		self._textBox1.TabIndex = 17
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(156, 80)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(138, 35)
		self._textBox2.TabIndex = 18
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(536, 185)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._Exit)
		self.Controls.Add(self._Clear)
		self.Controls.Add(self._btnMOD)
		self.Controls.Add(self._btnexp)
		self.Controls.Add(self._lblRe)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._lblOp)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._btnsub)
		self.Controls.Add(self._btndiv)
		self.Controls.Add(self._btnX)
		self.Controls.Add(self._btnflodiv)
		self.Controls.Add(self._btnadd)
		self.Name = "MainForm"
		self.Text = "Prog140SimpleCalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button8Click(self, sender, e):
		self._textBox1.Text=""
		self._lblOp.Text=""
		self._textBox2.Text=""
		self._lblRe.Text=""

	def Button9Click(self, sender, e):
		Application.Exit()

	def BtnaddClick(self, sender, e):
		#Addition
		one= float(self._textBox1.Text)
		two= float(self._textBox2.Text)
		sum = one + two
		self._lblOp.Text="+"
		self._lblRe.Text=str(sum)

	def BtnsubClick(self, sender, e):
		#Subtraction
		one = float(self._textBox1.Text)
		two = float(self._textBox2.Text)
		difference = one - two 
		self._lblOp.Text="-"
		self._lblRe.Text=str(difference)
		

	def BtnexpClick(self, sender, e):
		#Exponent
		one = float(self._textBox1.Text)
		two = float(self._textBox2.Text)
		answer = one ** two 
		self._lblOp.Text="^"
		self._lblRe.Text=str(answer)

	def BtnXClick(self, sender, e):
		#Multiply
		one = float(self._textBox1.Text)
		two = float(self._textBox2.Text)
		product = one * two 
		self._lblOp.Text="*"
		self._lblRe.Text=str(product)

	def BtndivClick(self, sender, e):
		#Float Division
		one = float(self._textBox1.Text)
		two = float(self._textBox2.Text)
		answer = one / two 
		self._lblOp.Text="/"
		self._lblRe.Text=str(answer)

	def BtnflodivClick(self, sender, e):
		#Integer Division
		one = float(self._textBox1.Text)
		two = float(self._textBox2.Text)
		answer = one // two 
		self._lblOp.Text="//"
		self._lblRe.Text=str(answer)

	def BtnMODClick(self, sender, e):
		#Mod
		one = float(self._textBox1.Text)
		two = float(self._textBox2.Text)
		answer = one % two 
		self._lblOp.Text="%"
		self._lblRe.Text=str(answer)