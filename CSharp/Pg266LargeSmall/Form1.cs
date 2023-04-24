using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg266LargeSmall
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double a = int.Parse(textBox1.Text);
            double b = int.Parse(textBox2.Text);

            if (a > b)
            {
                label3.Text = ("A is larger than B"); 
            }

            else if (a < b) 
            {
                label3.Text = ("B is larger than A"); 
            }
            else if (a == b)
            {
                label3.Text = ("They are the same value");
            }
        }
    }
}
