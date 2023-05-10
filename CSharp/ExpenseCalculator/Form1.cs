using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ExpenseCalculator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            decimal amount = int.Parse(textBox1.Text);
            var memo = textBox2.Text;
            decimal wallet = int.Parse(label4.Text);
            decimal transaction = (wallet - amount);
            string tran = (string.Format("{0}", transaction));
            if (memo == "")
            {
                memo = "Unknown";
            }
            string message = (string.Format("${0} Withdrawn - Reason:{1}", amount, memo));
            listBox1.Items.Add(message);
            listView1.BackColor = System.Drawing.Color.Green;
            label4.Text = (tran);
            
           
        }

        private void button2_Click(object sender, EventArgs e)
        {
            decimal amount = int.Parse(textBox1.Text);
            var memo = textBox2.Text;
            decimal wallet = int.Parse(label4.Text);
            decimal transaction = (wallet + amount);
            string tran = (string.Format("{0}", transaction));
            if (memo == "")
            {
                memo = "Unknown";
            }
            string message = (string.Format("${0} Withdrawn - Reason:{1}", amount, memo));
            listBox1.Items.Add(message);
            listView1.BackColor = System.Drawing.Color.Red; 
            label4.Text = (tran);


        }

        private void transaction7_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            label4.Text = (textBox3.Text);
            label5.Visible = false;
            label6.Visible = false;
            button3.Visible = false;
            textBox3.Visible = false;
        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
            listBox1.Items.RemoveAt(0);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }
    }
}
