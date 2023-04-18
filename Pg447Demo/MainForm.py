import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._lblMessage = System.Windows.Forms.Label()
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._mnuFile = System.Windows.Forms.ToolStripMenuItem()
		self._mnuFileExit = System.Windows.Forms.ToolStripMenuItem()
		self._mnuColor = System.Windows.Forms.ToolStripMenuItem()
		self._mnuColorRed = System.Windows.Forms.ToolStripMenuItem()
		self._mnuColorGreen = System.Windows.Forms.ToolStripMenuItem()
		self._mnuColorBlue = System.Windows.Forms.ToolStripMenuItem()
		self._mnuColorBlack = System.Windows.Forms.ToolStripMenuItem()
		self._toolStripMenuItem1 = System.Windows.Forms.ToolStripSeparator()
		self._mnuColorVisible = System.Windows.Forms.ToolStripMenuItem()
		self._mnuHelpAbout = System.Windows.Forms.ToolStripMenuItem()
		self._contextMenuStrip1 = System.Windows.Forms.ContextMenuStrip(self._components)
		self._helpToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._renameToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._menuStrip1.SuspendLayout()
		self._contextMenuStrip1.SuspendLayout()
		self.SuspendLayout()
		# 
		# lblMessage
		# 
		self._lblMessage.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblMessage.Location = System.Drawing.Point(13, 257)
		self._lblMessage.Name = "lblMessage"
		self._lblMessage.Size = System.Drawing.Size(473, 63)
		self._lblMessage.TabIndex = 0
		self._lblMessage.Text = "Hello World"
		self._lblMessage.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# menuStrip1
		# 
		self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._mnuFile,
			self._mnuColor,
			self._mnuHelpAbout]))
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(498, 24)
		self._menuStrip1.TabIndex = 1
		self._menuStrip1.Text = "menuStrip1"
		# 
		# mnuFile
		# 
		self._mnuFile.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._mnuFileExit]))
		self._mnuFile.Name = "mnuFile"
		self._mnuFile.Size = System.Drawing.Size(37, 20)
		self._mnuFile.Text = "&File"
		# 
		# mnuFileExit
		# 
		self._mnuFileExit.Name = "mnuFileExit"
		self._mnuFileExit.ShortcutKeys = System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.Q
		self._mnuFileExit.Size = System.Drawing.Size(136, 22)
		self._mnuFileExit.Text = "&Exit"
		self._mnuFileExit.Click += self.MnuFileExitClick
		# 
		# mnuColor
		# 
		self._mnuColor.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._mnuColorRed,
			self._mnuColorGreen,
			self._mnuColorBlue,
			self._mnuColorBlack,
			self._toolStripMenuItem1,
			self._mnuColorVisible]))
		self._mnuColor.Name = "mnuColor"
		self._mnuColor.Size = System.Drawing.Size(48, 20)
		self._mnuColor.Text = "&Color"
		# 
		# mnuColorRed
		# 
		self._mnuColorRed.Name = "mnuColorRed"
		self._mnuColorRed.Size = System.Drawing.Size(108, 22)
		self._mnuColorRed.Text = "&Red"
		self._mnuColorRed.Click += self.MnuColorRedClick
		# 
		# mnuColorGreen
		# 
		self._mnuColorGreen.Name = "mnuColorGreen"
		self._mnuColorGreen.Size = System.Drawing.Size(108, 22)
		self._mnuColorGreen.Text = "&Green"
		self._mnuColorGreen.Click += self.MnuColorGreenClick
		# 
		# mnuColorBlue
		# 
		self._mnuColorBlue.Name = "mnuColorBlue"
		self._mnuColorBlue.Size = System.Drawing.Size(108, 22)
		self._mnuColorBlue.Text = "&Blue"
		self._mnuColorBlue.Click += self.MnuColorBlueClick
		# 
		# mnuColorBlack
		# 
		self._mnuColorBlack.Name = "mnuColorBlack"
		self._mnuColorBlack.Size = System.Drawing.Size(108, 22)
		self._mnuColorBlack.Text = "&Black"
		self._mnuColorBlack.Click += self.MnuColorBlackClick
		# 
		# toolStripMenuItem1
		# 
		self._toolStripMenuItem1.Name = "toolStripMenuItem1"
		self._toolStripMenuItem1.Size = System.Drawing.Size(105, 6)
		# 
		# mnuColorVisible
		# 
		self._mnuColorVisible.Checked = True
		self._mnuColorVisible.CheckState = System.Windows.Forms.CheckState.Checked
		self._mnuColorVisible.Name = "mnuColorVisible"
		self._mnuColorVisible.Size = System.Drawing.Size(108, 22)
		self._mnuColorVisible.Text = "&Visible"
		self._mnuColorVisible.Click += self.MnuColorVisibleClick
		# 
		# mnuHelpAbout
		# 
		self._mnuHelpAbout.Name = "mnuHelpAbout"
		self._mnuHelpAbout.Size = System.Drawing.Size(44, 20)
		self._mnuHelpAbout.Text = "&Help"
		self._mnuHelpAbout.Click += self.MnuHelpAboutClick
		# 
		# contextMenuStrip1
		# 
		self._contextMenuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._helpToolStripMenuItem,
			self._renameToolStripMenuItem]))
		self._contextMenuStrip1.Name = "contextMenuStrip1"
		self._contextMenuStrip1.Size = System.Drawing.Size(153, 70)
		self._contextMenuStrip1.Text = "Customer Support"
		self._contextMenuStrip1.Opening += self.ContextMenuStrip1Opening
		# 
		# helpToolStripMenuItem
		# 
		self._helpToolStripMenuItem.Name = "helpToolStripMenuItem"
		self._helpToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._helpToolStripMenuItem.Text = "Help"
		# 
		# renameToolStripMenuItem
		# 
		self._renameToolStripMenuItem.Name = "renameToolStripMenuItem"
		self._renameToolStripMenuItem.Size = System.Drawing.Size(152, 22)
		self._renameToolStripMenuItem.Text = "Rename"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(498, 332)
		self.Controls.Add(self._lblMessage)
		self.Controls.Add(self._menuStrip1)
		self.MainMenuStrip = self._menuStrip1
		self.Name = "MainForm"
		self.Text = "Menu Demo"
		self._menuStrip1.ResumeLayout(False)
		self._menuStrip1.PerformLayout()
		self._contextMenuStrip1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()


	def MnuFileExitClick(self, sender, e):
		Application.Exit()

	def MnuColorRedClick(self, sender, e):
		self._lblMessage.ForeColor = Color.Red

	def MnuColorGreenClick(self, sender, e):
		self._lblMessage.ForeColor = Color.Green

	def MnuColorBlueClick(self, sender, e):
		self._lblMessage.ForeColor = Color.Blue

	def MnuColorBlackClick(self, sender, e):
		self._lblMessage.ForeColor = Color.Black

	def MnuColorVisibleClick(self, sender, e):
		if self._mnuColorVisible.Checked == True:
			self._lblMessage.Visible = True
		else:
			self._lblMessage.Visible = False

	def MnuHelpAboutClick(self, sender, e):
		MessageBox.Show("Menu System Demo\n"  \
						"Designed for Starting out "  \
						"with Windows Form Applications",
						"About Menu Demo")
						

	def ContextMenuStrip1Opening(self, sender, e):
		pass