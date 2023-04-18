using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int mass = int.Parse(textBox1.Text);
            double weight = mass * 9.8;

            if (weight > 1000){
                label3.Text = "Too Heavy";
            } else if (weight < 10){
                label3.Text = "Too Light";
            }
            else
            {
                label3.Text = "Accepted";
            }

            label2.Text = ("Weight:" + weight);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            label3.Text = "";
            label2.Text = "Weight:";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
