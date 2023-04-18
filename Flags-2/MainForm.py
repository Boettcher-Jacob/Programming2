import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("Flags_2.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self._radioButton7 = System.Windows.Forms.RadioButton()
		self._radioButton8 = System.Windows.Forms.RadioButton()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._radioButton9 = System.Windows.Forms.RadioButton()
		self._radioButton10 = System.Windows.Forms.RadioButton()
		self._radioButton11 = System.Windows.Forms.RadioButton()
		self._radioButton12 = System.Windows.Forms.RadioButton()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._radioButton13 = System.Windows.Forms.RadioButton()
		self._radioButton14 = System.Windows.Forms.RadioButton()
		self._radioButton15 = System.Windows.Forms.RadioButton()
		self._radioButton16 = System.Windows.Forms.RadioButton()
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._pictureBox2 = System.Windows.Forms.PictureBox()
		self._pictureBox3 = System.Windows.Forms.PictureBox()
		self._pictureBox4 = System.Windows.Forms.PictureBox()
		self._label1 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self._groupBox4.SuspendLayout()
		self._pictureBox1.BeginInit()
		self._pictureBox2.BeginInit()
		self._pictureBox3.BeginInit()
		self._pictureBox4.BeginInit()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.SystemColors.ControlDark
		self._groupBox1.Controls.Add(self._radioButton4)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(216, 199)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Country"
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.SystemColors.Control
		self._radioButton1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.Location = System.Drawing.Point(6, 19)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(204, 39)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Australia"
		self._radioButton1.UseVisualStyleBackColor = False
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.SystemColors.Control
		self._radioButton2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.Location = System.Drawing.Point(6, 64)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(204, 39)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Canada"
		self._radioButton2.UseVisualStyleBackColor = False
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.SystemColors.Control
		self._radioButton3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.Location = System.Drawing.Point(6, 109)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(204, 39)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Ukraine"
		self._radioButton3.UseVisualStyleBackColor = False
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# radioButton4
		# 
		self._radioButton4.BackColor = System.Drawing.SystemColors.Control
		self._radioButton4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton4.Location = System.Drawing.Point(6, 154)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(204, 39)
		self._radioButton4.TabIndex = 3
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "Russia"
		self._radioButton4.UseVisualStyleBackColor = False
		self._radioButton4.CheckedChanged += self.RadioButton4CheckedChanged
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.SystemColors.ControlDark
		self._groupBox2.Controls.Add(self._radioButton5)
		self._groupBox2.Controls.Add(self._radioButton6)
		self._groupBox2.Controls.Add(self._radioButton7)
		self._groupBox2.Controls.Add(self._radioButton8)
		self._groupBox2.Location = System.Drawing.Point(13, 218)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(216, 199)
		self._groupBox2.TabIndex = 4
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Text Color"
		# 
		# radioButton5
		# 
		self._radioButton5.BackColor = System.Drawing.SystemColors.Control
		self._radioButton5.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton5.Location = System.Drawing.Point(6, 19)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(204, 39)
		self._radioButton5.TabIndex = 3
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "Black"
		self._radioButton5.UseVisualStyleBackColor = False
		self._radioButton5.CheckedChanged += self.RadioButton5CheckedChanged
		# 
		# radioButton6
		# 
		self._radioButton6.BackColor = System.Drawing.SystemColors.Control
		self._radioButton6.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton6.Location = System.Drawing.Point(6, 64)
		self._radioButton6.Name = "radioButton6"
		self._radioButton6.Size = System.Drawing.Size(204, 39)
		self._radioButton6.TabIndex = 2
		self._radioButton6.TabStop = True
		self._radioButton6.Text = "Red"
		self._radioButton6.UseVisualStyleBackColor = False
		self._radioButton6.CheckedChanged += self.RadioButton6CheckedChanged
		# 
		# radioButton7
		# 
		self._radioButton7.BackColor = System.Drawing.SystemColors.Control
		self._radioButton7.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton7.Location = System.Drawing.Point(6, 109)
		self._radioButton7.Name = "radioButton7"
		self._radioButton7.Size = System.Drawing.Size(204, 39)
		self._radioButton7.TabIndex = 1
		self._radioButton7.TabStop = True
		self._radioButton7.Text = "Yellow"
		self._radioButton7.UseVisualStyleBackColor = False
		self._radioButton7.CheckedChanged += self.RadioButton7CheckedChanged
		# 
		# radioButton8
		# 
		self._radioButton8.BackColor = System.Drawing.SystemColors.Control
		self._radioButton8.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton8.Location = System.Drawing.Point(6, 154)
		self._radioButton8.Name = "radioButton8"
		self._radioButton8.Size = System.Drawing.Size(204, 39)
		self._radioButton8.TabIndex = 0
		self._radioButton8.TabStop = True
		self._radioButton8.Text = "Blue"
		self._radioButton8.UseVisualStyleBackColor = False
		self._radioButton8.CheckedChanged += self.RadioButton8CheckedChanged
		# 
		# groupBox3
		# 
		self._groupBox3.BackColor = System.Drawing.SystemColors.ControlDark
		self._groupBox3.Controls.Add(self._radioButton9)
		self._groupBox3.Controls.Add(self._radioButton10)
		self._groupBox3.Controls.Add(self._radioButton11)
		self._groupBox3.Controls.Add(self._radioButton12)
		self._groupBox3.Location = System.Drawing.Point(235, 13)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(216, 199)
		self._groupBox3.TabIndex = 4
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Text Size"
		# 
		# radioButton9
		# 
		self._radioButton9.BackColor = System.Drawing.SystemColors.Control
		self._radioButton9.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton9.Location = System.Drawing.Point(6, 19)
		self._radioButton9.Name = "radioButton9"
		self._radioButton9.Size = System.Drawing.Size(204, 39)
		self._radioButton9.TabIndex = 3
		self._radioButton9.TabStop = True
		self._radioButton9.Text = "10"
		self._radioButton9.UseVisualStyleBackColor = False
		self._radioButton9.CheckedChanged += self.RadioButton9CheckedChanged
		# 
		# radioButton10
		# 
		self._radioButton10.BackColor = System.Drawing.SystemColors.Control
		self._radioButton10.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton10.Location = System.Drawing.Point(6, 64)
		self._radioButton10.Name = "radioButton10"
		self._radioButton10.Size = System.Drawing.Size(204, 39)
		self._radioButton10.TabIndex = 2
		self._radioButton10.TabStop = True
		self._radioButton10.Text = "12"
		self._radioButton10.UseVisualStyleBackColor = False
		self._radioButton10.CheckedChanged += self.RadioButton10CheckedChanged
		# 
		# radioButton11
		# 
		self._radioButton11.BackColor = System.Drawing.SystemColors.Control
		self._radioButton11.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton11.Location = System.Drawing.Point(6, 109)
		self._radioButton11.Name = "radioButton11"
		self._radioButton11.Size = System.Drawing.Size(204, 39)
		self._radioButton11.TabIndex = 1
		self._radioButton11.TabStop = True
		self._radioButton11.Text = "16"
		self._radioButton11.UseVisualStyleBackColor = False
		self._radioButton11.CheckedChanged += self.RadioButton11CheckedChanged
		# 
		# radioButton12
		# 
		self._radioButton12.BackColor = System.Drawing.SystemColors.Control
		self._radioButton12.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton12.Location = System.Drawing.Point(6, 154)
		self._radioButton12.Name = "radioButton12"
		self._radioButton12.Size = System.Drawing.Size(204, 39)
		self._radioButton12.TabIndex = 0
		self._radioButton12.TabStop = True
		self._radioButton12.Text = "32"
		self._radioButton12.UseVisualStyleBackColor = False
		self._radioButton12.CheckedChanged += self.RadioButton12CheckedChanged
		# 
		# groupBox4
		# 
		self._groupBox4.BackColor = System.Drawing.SystemColors.ControlDark
		self._groupBox4.Controls.Add(self._radioButton13)
		self._groupBox4.Controls.Add(self._radioButton14)
		self._groupBox4.Controls.Add(self._radioButton15)
		self._groupBox4.Controls.Add(self._radioButton16)
		self._groupBox4.Location = System.Drawing.Point(235, 218)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(216, 199)
		self._groupBox4.TabIndex = 4
		self._groupBox4.TabStop = False
		self._groupBox4.Text = "Text Style"
		# 
		# radioButton13
		# 
		self._radioButton13.BackColor = System.Drawing.SystemColors.Control
		self._radioButton13.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton13.Location = System.Drawing.Point(6, 19)
		self._radioButton13.Name = "radioButton13"
		self._radioButton13.Size = System.Drawing.Size(204, 39)
		self._radioButton13.TabIndex = 3
		self._radioButton13.TabStop = True
		self._radioButton13.Text = "Underline"
		self._radioButton13.UseVisualStyleBackColor = False
		self._radioButton13.CheckedChanged += self.RadioButton13CheckedChanged
		# 
		# radioButton14
		# 
		self._radioButton14.BackColor = System.Drawing.SystemColors.Control
		self._radioButton14.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton14.Location = System.Drawing.Point(6, 64)
		self._radioButton14.Name = "radioButton14"
		self._radioButton14.Size = System.Drawing.Size(204, 39)
		self._radioButton14.TabIndex = 2
		self._radioButton14.TabStop = True
		self._radioButton14.Text = "Bold"
		self._radioButton14.UseVisualStyleBackColor = False
		self._radioButton14.CheckedChanged += self.RadioButton14CheckedChanged
		# 
		# radioButton15
		# 
		self._radioButton15.BackColor = System.Drawing.SystemColors.Control
		self._radioButton15.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton15.Location = System.Drawing.Point(6, 109)
		self._radioButton15.Name = "radioButton15"
		self._radioButton15.Size = System.Drawing.Size(204, 39)
		self._radioButton15.TabIndex = 1
		self._radioButton15.TabStop = True
		self._radioButton15.Text = "Italic"
		self._radioButton15.UseVisualStyleBackColor = False
		self._radioButton15.CheckedChanged += self.RadioButton15CheckedChanged
		# 
		# radioButton16
		# 
		self._radioButton16.BackColor = System.Drawing.SystemColors.Control
		self._radioButton16.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton16.Location = System.Drawing.Point(6, 154)
		self._radioButton16.Name = "radioButton16"
		self._radioButton16.Size = System.Drawing.Size(204, 39)
		self._radioButton16.TabIndex = 0
		self._radioButton16.TabStop = True
		self._radioButton16.Text = "Strikeout"
		self._radioButton16.UseVisualStyleBackColor = False
		self._radioButton16.CheckedChanged += self.RadioButton16CheckedChanged
		# 
		# pictureBox1
		# 
		self._pictureBox1.Image = resources.GetObject("pictureBox1.Image")
		self._pictureBox1.Location = System.Drawing.Point(457, 12)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(150, 134)
		self._pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._pictureBox1.TabIndex = 5
		self._pictureBox1.TabStop = False
		self._pictureBox1.Visible = False
		# 
		# pictureBox2
		# 
		self._pictureBox2.Image = resources.GetObject("pictureBox2.Image")
		self._pictureBox2.Location = System.Drawing.Point(613, 12)
		self._pictureBox2.Name = "pictureBox2"
		self._pictureBox2.Size = System.Drawing.Size(150, 134)
		self._pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._pictureBox2.TabIndex = 6
		self._pictureBox2.TabStop = False
		self._pictureBox2.Visible = False
		# 
		# pictureBox3
		# 
		self._pictureBox3.Image = resources.GetObject("pictureBox3.Image")
		self._pictureBox3.Location = System.Drawing.Point(457, 152)
		self._pictureBox3.Name = "pictureBox3"
		self._pictureBox3.Size = System.Drawing.Size(150, 134)
		self._pictureBox3.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._pictureBox3.TabIndex = 7
		self._pictureBox3.TabStop = False
		self._pictureBox3.Visible = False
		# 
		# pictureBox4
		# 
		self._pictureBox4.Image = resources.GetObject("pictureBox4.Image")
		self._pictureBox4.Location = System.Drawing.Point(613, 152)
		self._pictureBox4.Name = "pictureBox4"
		self._pictureBox4.Size = System.Drawing.Size(150, 134)
		self._pictureBox4.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._pictureBox4.TabIndex = 8
		self._pictureBox4.TabStop = False
		self._pictureBox4.Visible = False
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.CornflowerBlue
		self._label1.Font = System.Drawing.Font("Snap ITC", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(457, 298)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(306, 113)
		self._label1.TabIndex = 9
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(782, 433)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._pictureBox4)
		self.Controls.Add(self._pictureBox3)
		self.Controls.Add(self._pictureBox2)
		self.Controls.Add(self._pictureBox1)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Flags-2"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self._groupBox4.ResumeLayout(False)
		self._pictureBox1.EndInit()
		self._pictureBox2.EndInit()
		self._pictureBox3.EndInit()
		self._pictureBox4.EndInit()
		self.ResumeLayout(False)

	# Countries
	def RadioButton1CheckedChanged(self, sender, e):
		self._pictureBox1.Visible = True
		self._pictureBox2.Visible = False
		self._pictureBox3.Visible = False
		self._pictureBox4.Visible = False
		self._label1.Text = "Australia"

	def RadioButton2CheckedChanged(self, sender, e):
		self._pictureBox1.Visible = False
		self._pictureBox2.Visible = True
		self._pictureBox3.Visible = False
		self._pictureBox4.Visible = False
		self._label1.Text = "Canada"

	def RadioButton3CheckedChanged(self, sender, e):
		self._pictureBox1.Visible = False
		self._pictureBox2.Visible = False
		self._pictureBox3.Visible = True
		self._pictureBox4.Visible = False
		self._label1.Text = "Ukraine"

	def RadioButton4CheckedChanged(self, sender, e):
		self._pictureBox1.Visible = False
		self._pictureBox2.Visible = False
		self._pictureBox3.Visible = False
		self._pictureBox4.Visible = True
		self._label1.Text = "Russia"
		
	# Text Color 

	def RadioButton5CheckedChanged(self, sender, e):
		self._label1.ForeColor = Color.Black

	def RadioButton6CheckedChanged(self, sender, e):
		self._label1.ForeColor = Color.Red

	def RadioButton7CheckedChanged(self, sender, e):
		self._label1.ForeColor = Color.Yellow

	def RadioButton8CheckedChanged(self, sender, e):
		self._label1.ForeColor = Color.Blue
		
	# Text Size

	def RadioButton9CheckedChanged(self, sender, e):
		self._label1.Font = Font(self._label1.Font.Name, 10, self._label1.Font.Style, self._label1.Font.Unit)

	def RadioButton10CheckedChanged(self, sender, e):
		self._label1.Font = Font(self._label1.Font.Name, 12, self._label1.Font.Style, self._label1.Font.Unit)

	def RadioButton11CheckedChanged(self, sender, e):
		self._label1.Font = Font(self._label1.Font.Name, 16, self._label1.Font.Style, self._label1.Font.Unit)

	def RadioButton12CheckedChanged(self, sender, e):
		self._label1.Font = Font(self._label1.Font.Name, 32, self._label1.Font.Style, self._label1.Font.Unit)
		
	# Text Style
	

	def RadioButton13CheckedChanged(self, sender, e):
		self._label1.Font = Font(self._label1.Font.Name, self._label1.Font.Size, FontStyle.Underline, self._label1.Font.Unit)

	def RadioButton14CheckedChanged(self, sender, e):
		self._label1.Font = Font(self._label1.Font.Name, self._label1.Font.Size, FontStyle.Bold, self._label1.Font.Unit)

	def RadioButton15CheckedChanged(self, sender, e):
		self._label1.Font = Font(self._label1.Font.Name, self._label1.Font.Size, FontStyle.Italic, self._label1.Font.Unit)

	def RadioButton16CheckedChanged(self, sender, e):
		self._label1.Font = Font(self._label1.Font.Name, self._label1.Font.Size, FontStyle.Strikeout , self._label1.Font.Unit)