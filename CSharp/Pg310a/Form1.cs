using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg310a
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Random ran = new Random();

            for (int lcv = 0; lcv < ran.Next(5, 11); lcv++) {
                double hist = ran.Next(0, 21) + ran.NextDouble();
                string msg = "";
                int max = (int)Math.Round(hist);
                for (int lcv2 = 0; lcv2 < max; lcv2++)
                {
                    msg += "*";
                } 
                msg += " " + Math.Round(hist, 2);
                listBox1.Items.Add(msg);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Ha! You got Egg'd!");
            Application.Exit();
        }
    }
}
