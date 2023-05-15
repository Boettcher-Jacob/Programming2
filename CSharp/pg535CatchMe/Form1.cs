using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg535CatchMe
{
    public partial class Form1 : Form
    {
        private string[] strCaption = { "Click Here", "Try Harder", "Try Again", "Not Even Close", 
                                       "I'm Over Here!"};
        private Random rand = new Random();


        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("You Got Me!", "", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            Application.Exit();
        }

        private void Form1_MouseEnter(object sender, EventArgs e)
        {
            int intIndex = rand.Next(strCaption.Length);
            button1.Text = strCaption[index];
        }
    }
}
