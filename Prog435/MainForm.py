import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(778, 316)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 336)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(272, 69)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(291, 336)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(234, 69)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(531, 336)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(260, 69)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(803, 409)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog435"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._listBox1.Items.Add("Car Type:" + "\t\t" + "Base Toll:" + "\t\t" + "Factor:" + "\t\t" + "Cost"
		
		for car in range(1,7)
		Compact Car == 1
		Small Car == 2
		Mid Size Car == 3
		Full Size Car == 4
		Truck == 5
		16 Wheeler = 6