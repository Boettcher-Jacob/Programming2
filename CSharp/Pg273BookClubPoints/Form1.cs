using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg273BookClubPoints
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double book = int.Parse(textBox1.Text);
          
            if (book == 1)
            {
                label3.Text = ("Rewards: 5 points!");
            } 
            else if (book == 2)
            {
                label3.Text = ("Rewards: 15 points!");
            }
            else if (book == 3)
            {
                label3.Text = ("Rewards: 30 points!");
            }
            else if (book >= 4) 
            { 
                label3.Text = ("Rewards: 60 points!");
            }
    }

        private void Form1_Load(object sender, EventArgs e)
        {
        
        }
}
