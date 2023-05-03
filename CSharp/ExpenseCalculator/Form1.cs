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
            int amount = int.Parse(textBox1.Text);
            var memo = textBox2.Text;
            int wallet = int.Parse(walletlbl.Text);
            
            if (memo == "")
            {
                memo = "Unknown";
            }
            if (transaction1.Text == "")
            {
                transaction1.Text = ("$" + amount + " " + "Withdrawn" + " - " + "Reason:" + " " + memo);
                string value = (amount - wallet);
                wallet = (value);
            }
            else if (transaction2.Text == "")
            {
                transaction2.Text = ("$" + amount + " " + "Withdrawn" + " - " + "Reason:" + " " + memo);
            }
            else if (transaction3.Text == "")
            {
                transaction3.Text = ("$" + amount + " " + "Withdrawn" + " - " + "Reason:" + " " + memo);
            }
            else if (transaction4.Text == "")
            {
                transaction4.Text = ("$" + amount + " " + "Withdrawn" + " - " + "Reason:" + " " + memo);
            }
            else if (transaction5.Text == "")
            {
                transaction5.Text = ("$" + amount + " " + "Withdrawn" + " - " + "Reason:" + " " + memo);
            }
            else if (transaction6.Text == "")
            {
                transaction6.Text = ("$" + amount + " " + "Withdrawn" + " - " + "Reason:" + " " + memo);
            }
            else if (transaction7.Text == "")
            {
                transaction7.Text = ("$" + amount + " " + "Withdrawn" + " - " + "Reason:" + " " + memo);
            }
            else if (transaction8.Text == "")
            {
                transaction8.Text = ("$" + amount + " " + "Withdrawn" + " - " + "Reason:" + " " + memo);
            }
            
           
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int amount = int.Parse(textBox1.Text);
            var memo = textBox2.Text;
            int wallet = int.Parse(walletlbl.Text);
            int transaction = (wallet + amount);

            if (memo == "")
            {
                memo = "Unknown";
            }
            if (transaction1.Text == "")
            {
                transaction1.Text = ("$" + amount + " " + "Deposited" + " - " + "Reason:" + " " + memo);
                int value = (wallet + amount);
                wallet = value;
            }
            else if (transaction2.Text == "")
            {
                transaction2.Text = ("$" + amount + " " + "Deposited" + " - " + "Reason:" + " " + memo);
            }
            else if (transaction3.Text == "")
            {
                transaction3.Text = ("$" + amount + " " + "Deposited" + " - " + "Reason:" + " " + memo);
            }
            else if (transaction4.Text == "")
            {
                transaction4.Text = ("$" + amount + " " + "Deposited" + " - " + "Reason:" + " " + memo);
            }
            else if (transaction5.Text == "")
            {
                transaction5.Text = ("$" + amount + " " + "Deposited" + " - " + "Reason:" + " " + memo);
            }
            else if (transaction6.Text == "")
            {
                transaction6.Text = ("$" + amount + " " + "Deposited" + " - " + "Reason:" + " " + memo);
            }
            else if (transaction7.Text == "")
            {
                transaction7.Text = ("$" + amount + " " + "Deposited" + " - " + "Reason:" + " " + memo);
            }
            else if (transaction8.Text == "")
            {
                transaction8.Text = ("$" + amount + " " + "Deposited" + " - " + "Reason:" + " " + memo);
            }


        }
    }
}
