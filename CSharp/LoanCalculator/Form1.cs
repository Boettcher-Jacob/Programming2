using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace LoanCalculator
{
    public partial class Form1 : Form
    {
        const int intMINMONTHS = 6;
        const int intMAXMONTHS = 48;
        const float sngMONTHS_YEAR = 12f;

        const double dblNEW_RATE = 0.089;
        const double dblUSED_RATE = 0.095;

        double dblAnnualRate = dblNEW_RATE;

        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int intCount = 0;
            int intMonths = 0;
            double dblLoan = 0.0;
            double dblPayment = 0.0;
            double dblInterest = 0.0;
            double dblPrincipal = 0.0;

            try
            {
                intMonths = int.Parse(txtMonths.Text);
                dblLoan = double.Parse(txtCost.Text) - double.Parse(txtDownPayment.Text);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Please Enter Numeric Value");
                return;
            }
            dblPayment = Financial.Pmt(dblAnnualRate / sngMONTHS_YEAR, intMonths, -dblLoan);
            
            Output.Items.Clear();

            for (intCount = 1, intCount <= intMonths; intCount++) {

            }
        }
    }
}
