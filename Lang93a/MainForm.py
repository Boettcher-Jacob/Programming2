import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ControlDark
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(184, 30)
		self._label1.TabIndex = 0
		self._label1.Text = "Kilowatts Used :"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.Control
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(197, 43)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(104, 30)
		self._label3.TabIndex = 3
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.Control
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(13, 43)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(184, 30)
		self._label4.TabIndex = 2
		self._label4.Text = "Base Rate :"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ControlDark
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(197, 73)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(104, 30)
		self._label5.TabIndex = 5
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ControlDark
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(13, 73)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(184, 30)
		self._label6.TabIndex = 4
		self._label6.Text = "Surcharge :"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.Control
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(197, 176)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(104, 30)
		self._label7.TabIndex = 11
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.Control
		self._label8.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(13, 176)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(184, 30)
		self._label8.TabIndex = 10
		self._label8.Text = "After 12/5/22 :"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.ControlDark
		self._label9.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(197, 146)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(104, 30)
		self._label9.TabIndex = 9
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.SystemColors.ControlDark
		self._label10.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(13, 146)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(184, 30)
		self._label10.TabIndex = 8
		self._label10.Text = "Due Pay :"
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.SystemColors.Control
		self._label11.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(197, 103)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(104, 30)
		self._label11.TabIndex = 7
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.SystemColors.Control
		self._label12.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(13, 103)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(184, 30)
		self._label12.TabIndex = 6
		self._label12.Text = "City Tax :"
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(197, 8)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(104, 35)
		self._textBox1.TabIndex = 12
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 209)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(135, 48)
		self._button1.TabIndex = 13
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(166, 209)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(135, 48)
		self._button2.TabIndex = 14
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
		self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._button3.ForeColor = System.Drawing.SystemColors.Control
		self._button3.Location = System.Drawing.Point(122, 263)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 15
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self.ClientSize = System.Drawing.Size(318, 295)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang93a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		watt = int(self._textBox1.Text)
		
		base = watt * 0.0475
		base = round(base,2)
		sur = base * .1
		sur = round(sur,2)
		city = base * .03
		city = round(city,2)
		total = base + sur + city
		
		latetax = total * .04
		latetax = round(latetax,2)
		late = latetax + total
		
		self._label3.Text=str(base)
		self._label5.Text=str(sur)
		self._label11.Text=str(city)
		self._label9.Text=str(total)
		self._label7.Text=str(late)

	def Button2Click(self, sender, e):
		self._label3.Text=""
		self._label5.Text=""
		self._label11.Text=""
		self._label9.Text=""
		self._label7.Text=""

	def Button3Click(self, sender, e):
		Application.Exit()