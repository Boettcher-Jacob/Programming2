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
		self._listBox1 = System.Windows.Forms.ListBox()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(215, 63)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(13, 82)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(215, 63)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(12, 151)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(215, 63)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(235, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(452, 303)
		self._listBox1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ControlDark
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 217)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(215, 107)
		self._label1.TabIndex = 4
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(699, 333)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang152a"
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		self._label1.Text=""

	def Button1Click(self, sender, e):
		sum = 0
		for num in range(3, 9670, 3):
			answer=num(num + sum)
			
			self._label1.Text=int(answer)
			self._listBox1.Items.Add(str(num))