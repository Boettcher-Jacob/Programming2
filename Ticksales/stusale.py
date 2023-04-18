
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form2(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.parent = parent
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._txtNumTickets = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._lblTickets = System.Windows.Forms.Label()
		self._lblTax = System.Windows.Forms.Label()
		self._lblTotal = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Controls.Add(self._txtNumTickets)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(342, 55)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "How Many Tickets"
		# 
		# txtNumTickets
		# 
		self._txtNumTickets.Location = System.Drawing.Point(181, 22)
		self._txtNumTickets.Name = "txtNumTickets"
		self._txtNumTickets.Size = System.Drawing.Size(100, 20)
		self._txtNumTickets.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(15, 22)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(160, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "Number of Tickets"
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.SystemColors.ControlDark
		self._groupBox2.Controls.Add(self._label2)
		self._groupBox2.Controls.Add(self._label3)
		self._groupBox2.Controls.Add(self._label4)
		self._groupBox2.Controls.Add(self._lblTotal)
		self._groupBox2.Controls.Add(self._lblTax)
		self._groupBox2.Controls.Add(self._lblTickets)
		self._groupBox2.Location = System.Drawing.Point(13, 74)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(342, 141)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Total"
		# 
		# lblTickets
		# 
		self._lblTickets.BackColor = System.Drawing.SystemColors.Control
		self._lblTickets.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblTickets.Location = System.Drawing.Point(219, 25)
		self._lblTickets.Name = "lblTickets"
		self._lblTickets.Size = System.Drawing.Size(100, 23)
		self._lblTickets.TabIndex = 0
		self._lblTickets.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblTax
		# 
		self._lblTax.BackColor = System.Drawing.SystemColors.Control
		self._lblTax.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblTax.Location = System.Drawing.Point(219, 62)
		self._lblTax.Name = "lblTax"
		self._lblTax.Size = System.Drawing.Size(100, 23)
		self._lblTax.TabIndex = 1
		self._lblTax.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblTotal
		# 
		self._lblTotal.BackColor = System.Drawing.SystemColors.Control
		self._lblTotal.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblTotal.Location = System.Drawing.Point(219, 100)
		self._lblTotal.Name = "lblTotal"
		self._lblTotal.Size = System.Drawing.Size(100, 23)
		self._lblTotal.TabIndex = 2
		self._lblTotal.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.Control
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(15, 100)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(198, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Final Total"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.Control
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(15, 62)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(198, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Tax"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.Control
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(15, 25)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(198, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Number of Tickets"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(362, 23)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(84, 45)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(362, 90)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(84, 45)
		self._button2.TabIndex = 3
		self._button2.Text = "Return"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# Form2
		# 
		self.ClientSize = System.Drawing.Size(458, 227)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "Form2"
		self.Text = "Student Sales"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		intNumTickets = 0 
		decTicketCost = 0.0
		decSalesTax = 0.0
		decTotal = 0.0
		
		intNumTickets = int(self._txtNumTickets.Text)
		decTicketCost = intNumTickets * 7
		decSalesTax = CalcTax(decTicketCost)
		decTotal = decTicketCost + decSalesTax
		
		self._lblTickets.Text = "Tickets:" + "  " + str(round(decTicketCost), 2)
		self._LblTax.Text = "Tax:" + "  " + str(round(decSalesTax), 2)
		self._lblTotal.Text = "Total:" + "  " + str(round(decTotal), 2)

	def Button2Click(self, sender, e):
		self.Close()
		self.parent.Show()