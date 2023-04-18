import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._lbldatetoday = System.Windows.Forms.Label()
		self._lbltimetoday = System.Windows.Forms.Label()
		self._btnCalculate = System.Windows.Forms.Button()
		self._btnClear = System.Windows.Forms.Button()
		self._btnExit = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("MV Boli", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(155, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(249, 35)
		self._label1.TabIndex = 0
		self._label1.Text = "Highlander Hotel"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(107, 67)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(179, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Today's Date:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(186, 136)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Time:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# lbldatetoday
		# 
		self._lbldatetoday.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._lbldatetoday.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lbldatetoday.Location = System.Drawing.Point(292, 44)
		self._lbldatetoday.Name = "lbldatetoday"
		self._lbldatetoday.Size = System.Drawing.Size(100, 58)
		self._lbldatetoday.TabIndex = 3
		self._lbldatetoday.Text = """
"""
		# 
		# lbltimetoday
		# 
		self._lbltimetoday.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._lbltimetoday.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lbltimetoday.Location = System.Drawing.Point(292, 117)
		self._lbltimetoday.Name = "lbltimetoday"
		self._lbltimetoday.Size = System.Drawing.Size(100, 58)
		self._lbltimetoday.TabIndex = 4
		self._lbltimetoday.Text = """
"""
		# 
		# btnCalculate
		# 
		self._btnCalculate.Location = System.Drawing.Point(68, 313)
		self._btnCalculate.Name = "btnCalculate"
		self._btnCalculate.Size = System.Drawing.Size(165, 67)
		self._btnCalculate.TabIndex = 5
		self._btnCalculate.Text = "Calculate Charges"
		self._btnCalculate.UseVisualStyleBackColor = True
		self._btnCalculate.Click += self.BtnCalculateClick
		# 
		# btnClear
		# 
		self._btnClear.Location = System.Drawing.Point(239, 313)
		self._btnClear.Name = "btnClear"
		self._btnClear.Size = System.Drawing.Size(165, 67)
		self._btnClear.TabIndex = 6
		self._btnClear.Text = "Clear"
		self._btnClear.UseVisualStyleBackColor = True
		# 
		# btnExit
		# 
		self._btnExit.Location = System.Drawing.Point(239, 386)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(165, 67)
		self._btnExit.TabIndex = 7
		self._btnExit.Text = "EXIT"
		self._btnExit.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(558, 545)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._btnClear)
		self.Controls.Add(self._btnCalculate)
		self.Controls.Add(self._lbltimetoday)
		self.Controls.Add(self._lbldatetoday)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg162RoomCharge"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		# Get today's date from the system and display it.
		from datetime import date.
		self._lblDateToday.Text = date.today().strftime("%A, %B %d, $Y")
		# Get the current time from the suystem and display it
		import time
		self.lblTimeToday.Text = time.strftime{"%1 : #")

	def BtnCalculateClick(self, sender, e):
		pass
	@ Decalres variable for the calculations
	decRoomCharges = 0.0 
	decAddCharges = 0.0
	decSubtotal = 0.0
	decTax = 0.0
	decTotal = 0.0
	DecTAX_RATE = 0.08
	
	try:
		decAddCharges = float(self.txtRoomService.Text) + \
			float(self._txtTelephone.Text) + \
			float(self._txtMisc.Text)
			self.lblAddCharges.Text = str(round(DecAddCharges