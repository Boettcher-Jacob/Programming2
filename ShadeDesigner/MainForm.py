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
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self._radioButton7 = System.Windows.Forms.RadioButton()
		self._radioButton8 = System.Windows.Forms.RadioButton()
		self._radioButton9 = System.Windows.Forms.RadioButton()
		self._radioButton10 = System.Windows.Forms.RadioButton()
		self._radioButton11 = System.Windows.Forms.RadioButton()
		self._radioButton12 = System.Windows.Forms.RadioButton()
		self._label1 = System.Windows.Forms.Label()
		self._Shade = System.Windows.Forms.Label()
		self._Sizes = System.Windows.Forms.Label()
		self._Colors = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(13, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(200, 133)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Shade"
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
		self._groupBox2.Controls.Add(self._radioButton7)
		self._groupBox2.Controls.Add(self._radioButton6)
		self._groupBox2.Controls.Add(self._radioButton5)
		self._groupBox2.Controls.Add(self._radioButton4)
		self._groupBox2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.Location = System.Drawing.Point(13, 151)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(200, 143)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Sizes"
		# 
		# groupBox3
		# 
		self._groupBox3.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._groupBox3.Controls.Add(self._radioButton12)
		self._groupBox3.Controls.Add(self._radioButton11)
		self._groupBox3.Controls.Add(self._radioButton10)
		self._groupBox3.Controls.Add(self._radioButton9)
		self._groupBox3.Controls.Add(self._radioButton8)
		self._groupBox3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox3.Location = System.Drawing.Point(13, 298)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(200, 203)
		self._groupBox3.TabIndex = 2
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Colors"
		# 
		# radioButton2
		# 
		self._radioButton2.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.Location = System.Drawing.Point(6, 58)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(187, 32)
		self._radioButton2.TabIndex = 0
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Folding Shades: Adds $10"
		self._radioButton2.UseVisualStyleBackColor = True
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# radioButton1
		# 
		self._radioButton1.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.Location = System.Drawing.Point(6, 20)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(187, 32)
		self._radioButton1.TabIndex = 1
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Regular Shades: Adds $0"
		self._radioButton1.UseVisualStyleBackColor = True
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.Location = System.Drawing.Point(6, 96)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(187, 32)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Roman Shades: Adds $15"
		self._radioButton3.UseVisualStyleBackColor = True
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# radioButton4
		# 
		self._radioButton4.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton4.Location = System.Drawing.Point(6, 19)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(187, 26)
		self._radioButton4.TabIndex = 0
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "25 inches wide: Adds $0"
		self._radioButton4.UseVisualStyleBackColor = True
		self._radioButton4.CheckedChanged += self.RadioButton4CheckedChanged
		# 
		# radioButton5
		# 
		self._radioButton5.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton5.Location = System.Drawing.Point(6, 51)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(187, 26)
		self._radioButton5.TabIndex = 1
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "27 inches wide: Adds $2"
		self._radioButton5.UseVisualStyleBackColor = True
		self._radioButton5.CheckedChanged += self.RadioButton5CheckedChanged
		# 
		# radioButton6
		# 
		self._radioButton6.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton6.Location = System.Drawing.Point(6, 83)
		self._radioButton6.Name = "radioButton6"
		self._radioButton6.Size = System.Drawing.Size(187, 26)
		self._radioButton6.TabIndex = 2
		self._radioButton6.TabStop = True
		self._radioButton6.Text = "32 inches wide: Adds $4"
		self._radioButton6.UseVisualStyleBackColor = True
		self._radioButton6.CheckedChanged += self.RadioButton6CheckedChanged
		# 
		# radioButton7
		# 
		self._radioButton7.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton7.Location = System.Drawing.Point(6, 115)
		self._radioButton7.Name = "radioButton7"
		self._radioButton7.Size = System.Drawing.Size(187, 26)
		self._radioButton7.TabIndex = 3
		self._radioButton7.TabStop = True
		self._radioButton7.Text = "40 inches wide: Adds $6"
		self._radioButton7.UseVisualStyleBackColor = True
		self._radioButton7.CheckedChanged += self.RadioButton7CheckedChanged
		# 
		# radioButton8
		# 
		self._radioButton8.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton8.Location = System.Drawing.Point(7, 20)
		self._radioButton8.Name = "radioButton8"
		self._radioButton8.Size = System.Drawing.Size(187, 30)
		self._radioButton8.TabIndex = 0
		self._radioButton8.TabStop = True
		self._radioButton8.Text = "Natural: Adds $5"
		self._radioButton8.UseVisualStyleBackColor = True
		self._radioButton8.CheckedChanged += self.RadioButton8CheckedChanged
		# 
		# radioButton9
		# 
		self._radioButton9.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton9.Location = System.Drawing.Point(6, 56)
		self._radioButton9.Name = "radioButton9"
		self._radioButton9.Size = System.Drawing.Size(187, 30)
		self._radioButton9.TabIndex = 1
		self._radioButton9.TabStop = True
		self._radioButton9.Text = "Blue: Adds $0"
		self._radioButton9.UseVisualStyleBackColor = True
		self._radioButton9.CheckedChanged += self.RadioButton9CheckedChanged
		# 
		# radioButton10
		# 
		self._radioButton10.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton10.Location = System.Drawing.Point(6, 92)
		self._radioButton10.Name = "radioButton10"
		self._radioButton10.Size = System.Drawing.Size(187, 30)
		self._radioButton10.TabIndex = 2
		self._radioButton10.TabStop = True
		self._radioButton10.Text = "Teal: Adds $0"
		self._radioButton10.UseVisualStyleBackColor = True
		self._radioButton10.CheckedChanged += self.RadioButton10CheckedChanged
		# 
		# radioButton11
		# 
		self._radioButton11.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton11.Location = System.Drawing.Point(6, 128)
		self._radioButton11.Name = "radioButton11"
		self._radioButton11.Size = System.Drawing.Size(187, 30)
		self._radioButton11.TabIndex = 3
		self._radioButton11.TabStop = True
		self._radioButton11.Text = "Red: Adds $0"
		self._radioButton11.UseVisualStyleBackColor = True
		self._radioButton11.CheckedChanged += self.RadioButton11CheckedChanged
		# 
		# radioButton12
		# 
		self._radioButton12.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton12.Location = System.Drawing.Point(6, 164)
		self._radioButton12.Name = "radioButton12"
		self._radioButton12.Size = System.Drawing.Size(187, 30)
		self._radioButton12.TabIndex = 4
		self._radioButton12.TabStop = True
		self._radioButton12.Text = "Green: Adds $0"
		self._radioButton12.UseVisualStyleBackColor = True
		self._radioButton12.CheckedChanged += self.RadioButton12CheckedChanged
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(220, 23)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(248, 61)
		self._label1.TabIndex = 3
		self._label1.Text = "Shade Design Lab"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# Shade
		# 
		self._Shade.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Shade.Location = System.Drawing.Point(273, 88)
		self._Shade.Name = "Shade"
		self._Shade.Size = System.Drawing.Size(47, 23)
		self._Shade.TabIndex = 4
		self._Shade.Text = "0"
		self._Shade.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._Shade.Visible = False
		# 
		# Sizes
		# 
		self._Sizes.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Sizes.Location = System.Drawing.Point(326, 88)
		self._Sizes.Name = "Sizes"
		self._Sizes.Size = System.Drawing.Size(47, 23)
		self._Sizes.TabIndex = 5
		self._Sizes.Text = "0"
		self._Sizes.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._Sizes.Visible = False
		# 
		# Colors
		# 
		self._Colors.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Colors.Location = System.Drawing.Point(379, 88)
		self._Colors.Name = "Colors"
		self._Colors.Size = System.Drawing.Size(47, 23)
		self._Colors.TabIndex = 6
		self._Colors.Text = "0"
		self._Colors.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._Colors.Visible = False
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(220, 450)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(248, 51)
		self._label2.TabIndex = 7
		self._label2.Text = "Final Total:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(220, 354)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(248, 57)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(241, 417)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(81, 30)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(367, 417)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(81, 30)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
		self.ClientSize = System.Drawing.Size(480, 513)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._Colors)
		self.Controls.Add(self._Sizes)
		self.Controls.Add(self._Shade)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "ShadeDesigner"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		
		color = int(self._Colors.Text)
		size = int(self._Sizes.Text)
		shade = int(self._Shade.Text)
		
		final = float(color) + float(size) + float(shade) + 30
		
		self._label2.Text= "Final Total:" + " " + str(final)
		
		

	def RadioButton1CheckedChanged(self, sender, e):
		self._Shade.Text="0"
	def RadioButton2CheckedChanged(self, sender, e):
		self._Shade.Text="10"
	def RadioButton3CheckedChanged(self, sender, e):
		self._Shade.Text="15"
	def RadioButton4CheckedChanged(self, sender, e):
		self._Sizes.Text="0"
	def RadioButton5CheckedChanged(self, sender, e):
		self._Sizes.Text="2"
	def RadioButton6CheckedChanged(self, sender, e):
		self._Sizes.Text="4"
	def RadioButton7CheckedChanged(self, sender, e):
		self._Sizes.Text="6"
	def RadioButton8CheckedChanged(self, sender, e):
		self._Colors.Text="5"
	def RadioButton9CheckedChanged(self, sender, e):
		self._Colors.Text="0"
	def RadioButton10CheckedChanged(self, sender, e):
		self._Colors.Text="0"
	def RadioButton11CheckedChanged(self, sender, e):
		self._Colors.Text="0"
	def RadioButton12CheckedChanged(self, sender, e):
		self._Colors.Text="0"

	def Button2Click(self, sender, e):
		self._Colors.Text="0"
		self._Shade.Text="0"
		self._Sizes.Text="0"
		self._label2.Text="Final Total:"
		

	def Button3Click(self, sender, e):
		Application.Exit()