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
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._radioButton7 = System.Windows.Forms.RadioButton()
		self._radioButton8 = System.Windows.Forms.RadioButton()
		self._radioButton9 = System.Windows.Forms.RadioButton()
		self._radioButton10 = System.Windows.Forms.RadioButton()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._radioButton11 = System.Windows.Forms.RadioButton()
		self._radioButton12 = System.Windows.Forms.RadioButton()
		self._radioButton13 = System.Windows.Forms.RadioButton()
		self._radioButton14 = System.Windows.Forms.RadioButton()
		self._radioButton15 = System.Windows.Forms.RadioButton()
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._Decks = System.Windows.Forms.Label()
		self._Extra = System.Windows.Forms.Label()
		self._Wheels = System.Windows.Forms.Label()
		self._Axles = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self._groupBox4.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(215, 170)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Decks"
		# 
		# radioButton1
		# 
		self._radioButton1.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.Location = System.Drawing.Point(7, 20)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(202, 39)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "The Master Thrasher - $60"
		self._radioButton1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._radioButton1.UseVisualStyleBackColor = True
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.Location = System.Drawing.Point(6, 73)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(202, 39)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "The Dictator of Grind - $45"
		self._radioButton2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._radioButton2.UseVisualStyleBackColor = True
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.Location = System.Drawing.Point(6, 131)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(202, 39)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "The Street King - $50"
		self._radioButton3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._radioButton3.UseVisualStyleBackColor = True
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._groupBox2.Controls.Add(self._radioButton4)
		self._groupBox2.Controls.Add(self._radioButton5)
		self._groupBox2.Controls.Add(self._radioButton6)
		self._groupBox2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.Location = System.Drawing.Point(234, 13)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(150, 170)
		self._groupBox2.TabIndex = 3
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Axles"
		# 
		# radioButton4
		# 
		self._radioButton4.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton4.Location = System.Drawing.Point(7, 28)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(137, 39)
		self._radioButton4.TabIndex = 2
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "7.75 axle - $35"
		self._radioButton4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._radioButton4.UseVisualStyleBackColor = True
		self._radioButton4.CheckedChanged += self.RadioButton4CheckedChanged
		# 
		# radioButton5
		# 
		self._radioButton5.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton5.Location = System.Drawing.Point(6, 73)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(137, 39)
		self._radioButton5.TabIndex = 1
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "8 axle - $40"
		self._radioButton5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._radioButton5.UseVisualStyleBackColor = True
		self._radioButton5.CheckedChanged += self.RadioButton5CheckedChanged
		# 
		# radioButton6
		# 
		self._radioButton6.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton6.Location = System.Drawing.Point(7, 131)
		self._radioButton6.Name = "radioButton6"
		self._radioButton6.Size = System.Drawing.Size(137, 39)
		self._radioButton6.TabIndex = 0
		self._radioButton6.TabStop = True
		self._radioButton6.Text = "8.5 axle - $45"
		self._radioButton6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._radioButton6.UseVisualStyleBackColor = True
		self._radioButton6.CheckedChanged += self.RadioButton6CheckedChanged
		# 
		# groupBox3
		# 
		self._groupBox3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._groupBox3.Controls.Add(self._radioButton10)
		self._groupBox3.Controls.Add(self._radioButton9)
		self._groupBox3.Controls.Add(self._radioButton8)
		self._groupBox3.Controls.Add(self._radioButton7)
		self._groupBox3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox3.Location = System.Drawing.Point(390, 13)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(217, 170)
		self._groupBox3.TabIndex = 4
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Wheels"
		# 
		# radioButton7
		# 
		self._radioButton7.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton7.Location = System.Drawing.Point(7, 28)
		self._radioButton7.Name = "radioButton7"
		self._radioButton7.Size = System.Drawing.Size(204, 31)
		self._radioButton7.TabIndex = 0
		self._radioButton7.TabStop = True
		self._radioButton7.Text = "51 mm - $20"
		self._radioButton7.UseVisualStyleBackColor = True
		self._radioButton7.CheckedChanged += self.RadioButton7CheckedChanged
		# 
		# radioButton8
		# 
		self._radioButton8.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton8.Location = System.Drawing.Point(6, 65)
		self._radioButton8.Name = "radioButton8"
		self._radioButton8.Size = System.Drawing.Size(204, 31)
		self._radioButton8.TabIndex = 1
		self._radioButton8.TabStop = True
		self._radioButton8.Text = "55mm - $22"
		self._radioButton8.UseVisualStyleBackColor = True
		self._radioButton8.CheckedChanged += self.RadioButton8CheckedChanged
		# 
		# radioButton9
		# 
		self._radioButton9.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton9.Location = System.Drawing.Point(6, 102)
		self._radioButton9.Name = "radioButton9"
		self._radioButton9.Size = System.Drawing.Size(204, 31)
		self._radioButton9.TabIndex = 2
		self._radioButton9.TabStop = True
		self._radioButton9.Text = "58 mm - $24"
		self._radioButton9.UseVisualStyleBackColor = True
		self._radioButton9.CheckedChanged += self.RadioButton9CheckedChanged
		# 
		# radioButton10
		# 
		self._radioButton10.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton10.Location = System.Drawing.Point(6, 139)
		self._radioButton10.Name = "radioButton10"
		self._radioButton10.Size = System.Drawing.Size(204, 31)
		self._radioButton10.TabIndex = 3
		self._radioButton10.TabStop = True
		self._radioButton10.Text = "61 mm - $26"
		self._radioButton10.UseVisualStyleBackColor = True
		self._radioButton10.CheckedChanged += self.RadioButton10CheckedChanged
		# 
		# groupBox4
		# 
		self._groupBox4.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._groupBox4.Controls.Add(self._radioButton15)
		self._groupBox4.Controls.Add(self._radioButton14)
		self._groupBox4.Controls.Add(self._radioButton13)
		self._groupBox4.Controls.Add(self._radioButton12)
		self._groupBox4.Controls.Add(self._radioButton11)
		self._groupBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox4.Location = System.Drawing.Point(13, 190)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(594, 79)
		self._groupBox4.TabIndex = 5
		self._groupBox4.TabStop = False
		self._groupBox4.Text = "Items and Services"
		# 
		# radioButton11
		# 
		self._radioButton11.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton11.Location = System.Drawing.Point(7, 20)
		self._radioButton11.Name = "radioButton11"
		self._radioButton11.Size = System.Drawing.Size(109, 53)
		self._radioButton11.TabIndex = 0
		self._radioButton11.TabStop = True
		self._radioButton11.Text = "Grip Tape - $10"
		self._radioButton11.UseVisualStyleBackColor = True
		self._radioButton11.CheckedChanged += self.RadioButton11CheckedChanged
		# 
		# radioButton12
		# 
		self._radioButton12.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton12.Location = System.Drawing.Point(122, 20)
		self._radioButton12.Name = "radioButton12"
		self._radioButton12.Size = System.Drawing.Size(109, 53)
		self._radioButton12.TabIndex = 1
		self._radioButton12.TabStop = True
		self._radioButton12.Text = "Bearings - $30"
		self._radioButton12.UseVisualStyleBackColor = True
		self._radioButton12.CheckedChanged += self.RadioButton12CheckedChanged
		# 
		# radioButton13
		# 
		self._radioButton13.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton13.Location = System.Drawing.Point(237, 20)
		self._radioButton13.Name = "radioButton13"
		self._radioButton13.Size = System.Drawing.Size(109, 53)
		self._radioButton13.TabIndex = 2
		self._radioButton13.TabStop = True
		self._radioButton13.Text = "Riser Pads - $2"
		self._radioButton13.UseVisualStyleBackColor = True
		self._radioButton13.CheckedChanged += self.RadioButton13CheckedChanged
		# 
		# radioButton14
		# 
		self._radioButton14.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton14.Location = System.Drawing.Point(352, 20)
		self._radioButton14.Name = "radioButton14"
		self._radioButton14.Size = System.Drawing.Size(109, 53)
		self._radioButton14.TabIndex = 3
		self._radioButton14.TabStop = True
		self._radioButton14.Text = "Nuts-N-Bolts Kit - $3"
		self._radioButton14.UseVisualStyleBackColor = True
		self._radioButton14.CheckedChanged += self.RadioButton14CheckedChanged
		# 
		# radioButton15
		# 
		self._radioButton15.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton15.Location = System.Drawing.Point(458, 20)
		self._radioButton15.Name = "radioButton15"
		self._radioButton15.Size = System.Drawing.Size(109, 53)
		self._radioButton15.TabIndex = 4
		self._radioButton15.TabStop = True
		self._radioButton15.Text = "Assembly - $10"
		self._radioButton15.UseVisualStyleBackColor = True
		self._radioButton15.CheckedChanged += self.RadioButton15CheckedChanged
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button1.Location = System.Drawing.Point(13, 275)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(594, 64)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("OCR A Extended", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(20, 342)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(580, 68)
		self._label1.TabIndex = 7
		self._label1.Text = "Final Total:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(12, 413)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(93, 413)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# Decks
		# 
		self._Decks.Location = System.Drawing.Point(506, 422)
		self._Decks.Name = "Decks"
		self._Decks.Size = System.Drawing.Size(13, 14)
		self._Decks.TabIndex = 10
		self._Decks.Text = "0"
		# 
		# Extra
		# 
		self._Extra.Location = System.Drawing.Point(563, 422)
		self._Extra.Name = "Extra"
		self._Extra.Size = System.Drawing.Size(13, 14)
		self._Extra.TabIndex = 11
		self._Extra.Text = "0"
		# 
		# Wheels
		# 
		self._Wheels.Location = System.Drawing.Point(544, 422)
		self._Wheels.Name = "Wheels"
		self._Wheels.Size = System.Drawing.Size(13, 14)
		self._Wheels.TabIndex = 12
		self._Wheels.Text = "0"
		# 
		# Axles
		# 
		self._Axles.Location = System.Drawing.Point(525, 422)
		self._Axles.Name = "Axles"
		self._Axles.Size = System.Drawing.Size(13, 14)
		self._Axles.TabIndex = 13
		self._Axles.Text = "0"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self.ClientSize = System.Drawing.Size(619, 442)
		self.Controls.Add(self._Axles)
		self.Controls.Add(self._Wheels)
		self.Controls.Add(self._Extra)
		self.Controls.Add(self._Decks)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "SkateboardDesigner"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self._groupBox4.ResumeLayout(False)
		self.ResumeLayout(False)

	def Button1Click(self, sender, e):
		deck = int(self._Decks.Text)
		axle = int(self._Axles.Text)
		wheel = int(self._Wheels.Text)
		extra = int(self._Extra.Text)
		
		Total = float(deck) + float(axle) + float(wheel) + float(extra)
		
		self._label1.Text= "Final Total:" + " " + str(Total)



	def RadioButton3CheckedChanged(self, sender, e):
		self._Decks.Text="50"
	def RadioButton1CheckedChanged(self, sender, e):
		self._Decks.Text="60"
	def RadioButton2CheckedChanged(self, sender, e):
		self._Decks.Text="45"

	def RadioButton4CheckedChanged(self, sender, e):
		self._Axles.Text="35"

	def RadioButton5CheckedChanged(self, sender, e):
		self._Axles.Text="40"

	def RadioButton6CheckedChanged(self, sender, e):
		self._Axles.Text="45"

	def RadioButton7CheckedChanged(self, sender, e):
		self._Wheels.Text="20"

	def RadioButton8CheckedChanged(self, sender, e):
		self._Wheels.Text="22"

	def RadioButton9CheckedChanged(self, sender, e):
		self._Wheels.Text="24"

	def RadioButton10CheckedChanged(self, sender, e):
		self._Wheels.Text="26"

	def RadioButton11CheckedChanged(self, sender, e):
		self._Extra.Text="10"

	def RadioButton12CheckedChanged(self, sender, e):
		self._Extra.Text="30"

	def RadioButton13CheckedChanged(self, sender, e):
		self._Extra.Text="2"

	def RadioButton14CheckedChanged(self, sender, e):
		self._Extra.Text="3"

	def RadioButton15CheckedChanged(self, sender, e):
		self._Extra.Text="10"

	def Button2Click(self, sender, e):
		self._label1.Text= "Final Total: 0.0"
	

	def Button3Click(self, sender, e):
		Application.Exit()