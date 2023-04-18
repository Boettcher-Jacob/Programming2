
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.parent = parent
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._txtNumTickets = System.Windows.Forms.TextBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._radSectionA = System.Windows.Forms.RadioButton()
		self._radSectionB = System.Windows.Forms.RadioButton()
		self._radSectionC = System.Windows.Forms.RadioButton()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._lblTickets = System.Windows.Forms.Label()
		self._lblTax = System.Windows.Forms.Label()
		self._lblTotal = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._PriceEachTicket = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._txtNumTickets)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(406, 65)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Tickets"
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(6, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(239, 34)
		self._label1.TabIndex = 0
		self._label1.Text = "Number of Tickets:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# txtNumTickets
		# 
		self._txtNumTickets.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._txtNumTickets.Location = System.Drawing.Point(251, 19)
		self._txtNumTickets.Name = "txtNumTickets"
		self._txtNumTickets.Size = System.Drawing.Size(149, 35)
		self._txtNumTickets.TabIndex = 1
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._radSectionC)
		self._groupBox2.Controls.Add(self._radSectionB)
		self._groupBox2.Controls.Add(self._radSectionA)
		self._groupBox2.Location = System.Drawing.Point(13, 85)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(200, 111)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Selection"
		# 
		# radSectionA
		# 
		self._radSectionA.Location = System.Drawing.Point(7, 20)
		self._radSectionA.Name = "radSectionA"
		self._radSectionA.Size = System.Drawing.Size(187, 24)
		self._radSectionA.TabIndex = 0
		self._radSectionA.TabStop = True
		self._radSectionA.Text = "Section A"
		self._radSectionA.UseVisualStyleBackColor = True
		self._radSectionA.CheckedChanged += self.RadSectionACheckedChanged
		# 
		# radSectionB
		# 
		self._radSectionB.Location = System.Drawing.Point(6, 50)
		self._radSectionB.Name = "radSectionB"
		self._radSectionB.Size = System.Drawing.Size(187, 24)
		self._radSectionB.TabIndex = 1
		self._radSectionB.TabStop = True
		self._radSectionB.Text = "Section B"
		self._radSectionB.UseVisualStyleBackColor = True
		# 
		# radSectionC
		# 
		self._radSectionC.Location = System.Drawing.Point(7, 80)
		self._radSectionC.Name = "radSectionC"
		self._radSectionC.Size = System.Drawing.Size(187, 24)
		self._radSectionC.TabIndex = 2
		self._radSectionC.TabStop = True
		self._radSectionC.Text = "Section C"
		self._radSectionC.UseVisualStyleBackColor = True
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._lblTotal)
		self._groupBox3.Controls.Add(self._lblTax)
		self._groupBox3.Controls.Add(self._lblTickets)
		self._groupBox3.Location = System.Drawing.Point(219, 85)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(200, 111)
		self._groupBox3.TabIndex = 3
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Total Cost"
		# 
		# lblTickets
		# 
		self._lblTickets.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lblTickets.Location = System.Drawing.Point(7, 20)
		self._lblTickets.Name = "lblTickets"
		self._lblTickets.Size = System.Drawing.Size(187, 23)
		self._lblTickets.TabIndex = 0
		self._lblTickets.Text = "Tickets:"
		# 
		# lblTax
		# 
		self._lblTax.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lblTax.Location = System.Drawing.Point(7, 50)
		self._lblTax.Name = "lblTax"
		self._lblTax.Size = System.Drawing.Size(187, 23)
		self._lblTax.TabIndex = 1
		self._lblTax.Text = "Tax:"
		# 
		# lblTotal
		# 
		self._lblTotal.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lblTotal.Location = System.Drawing.Point(7, 80)
		self._lblTotal.Name = "lblTotal"
		self._lblTotal.Size = System.Drawing.Size(187, 23)
		self._lblTotal.TabIndex = 2
		self._lblTotal.Text = "Total:"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(244, 202)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 4
		self._button1.Text = "Return"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(109, 202)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 5
		self._button2.Text = "Calculate"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# PriceEachTicket
		# 
		self._PriceEachTicket.Location = System.Drawing.Point(325, 199)
		self._PriceEachTicket.Name = "PriceEachTicket"
		self._PriceEachTicket.Size = System.Drawing.Size(35, 18)
		self._PriceEachTicket.TabIndex = 6
		self._PriceEachTicket.Text = "0.0"
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(437, 226)
		self.Controls.Add(self._PriceEachTicket)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "Form1"
		self.Text = "Form1"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self.ResumeLayout(False)

	

	def Button1Click(self, sender, e):
		self.Close()
		self.parent.Show()
		
	def Form1FormClosing(self, sender, e):
		self.parent.Show()
		
	# Exiting the form ^^^

	def RadSectionACheckedChanged(self, sender, e):
		self._PriceEachTicket.Text = 20
		
	def RadSectionBCheckedChanged(self, sender, e):
		self._PriceEachTicket.Text = 15
	
	def RadSectionCCheckedChanged(self, sender, e):
		self._PriceEachTicket.Text = 10


	def Button2Click(self, sender, e):
		intNumTickets = 0.0 
		decTicketCost = 0.0
		decSalesTax = 0.0
		decTotal = 0.0
		
		
		intNumTickets = int(self._txtNumTickets.Text)
		decTicketCost = intNumTickets * self._PriceEachTicket.Text
		decSalesTax = decTicketCost * 0.06
		decTotal = decTicketCost + decSalesTax
		
		self._lblTickets.Text = "Tickets:" + "  " + str(round(decTicketCost), 2)
		self._lblTax.Text = "Tax:" + "  " + str(round(decSalesTax), 2)
		self._lblTotal.Text = "Total:" + "  " + str(round(decTotal), 2)

	