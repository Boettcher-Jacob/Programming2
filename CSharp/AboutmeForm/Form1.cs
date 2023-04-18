using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AboutmeForm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            label2.Text = "My Name is Jacob.";
            Random rnd = new Random();
            double num = rnd.Next(1, 101);

            if (num <= 5)
            {
                pictureBox1.Visible = true;
                button6.Visible = true;
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            pictureBox1.Visible = false;
            button6.Visible = false;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label2.Text = "My favorite club is DnD.";
            Random rnd = new Random();
            double num = rnd.Next(1, 101);

            if (num <= 5)
            {
                pictureBox1.Visible = true;
                button6.Visible = true;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            label2.Text = "If I don't have todo something, I won't. If I must, I'll do it as quickly possible.";
            Random rnd = new Random();
            double num = rnd.Next(1, 101);

            if (num <= 5)
            {
                pictureBox1.Visible = true;
                button6.Visible = true;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            label2.Text = "It's gotta be 'Puss In Boots: The Last Wish'.";
            Random rnd = new Random();
            double num = rnd.Next(1, 101);

            if (num <= 5)
            {
                pictureBox1.Visible = true;
                button6.Visible = true;
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            label2.Text = "100% It's Minecraft.";
            Random rnd = new Random();
            double num = rnd.Next(1, 101);

            if (num <= 5)
            {
                pictureBox1.Visible = true;
                button6.Visible = true;
            }
        }
    }
}
