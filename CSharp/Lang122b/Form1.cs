﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lang122b
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox1.Items.Add("Hours\t\tPay");
            int lcv = 1;
            while (lcv <= 50)
            {
                int pay = lcv * 2;
                listBox1.Items.Add(lcv + pay);
                lcv+;
            }
        }
    }
}
