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
            string message = (string.Format("#{0}  -  ${1} Withdrawn - Reason:{2}",listView1.Items.Count+1,amount, memo)); 
            listView1.Items.Add(message);
            foreach (ListViewItem item in listView1.Items)
            
            label4.Text = (tran);
            if (wallet <= 0)
            {
                MessageBox.Show("Warning: Balance Below 0");
            }

            
           
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
            string message = (string.Format("#{0}  -  ${1} Deposited - Reason:{2}", listView1.Items.Count + 1, amount, memo));
            listView1.Items.Add(message);
            
            label4.Text = (tran);
            if (wallet <= 0)
            {
                MessageBox.Show("Warning: Balance Below 0");
            }


        }

        private void transaction7_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            label4.Text = (textBox3.Text);
            label6.Visible = false;
            button3.Visible = false;
            textBox3.Visible = false;
        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
            listView1.Items.RemoveAt(0);
        }

        private void button5_Click(object sender, EventArgs e)
        {
           
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click_1(object sender, EventArgs e)
        {
            int id = int.Parse(textBox4.Text);

            removetransaction(id);
        }
        public void removetransaction(int id)
        {
            int rmindex = -1;
            for (int lcv = 0; lcv < listView1.Items.Count; lcv++)
            {
                string sid = listView1.Items[lcv].Text.Split(' ')[0];
                int pid = int.Parse(sid.Substring(1));
                if (pid == id)
                {
                    rmindex = pid;
                }
            }
            if (rmindex > -1) listView1.Items.RemoveAt(rmindex-1);
        }
    }
}
