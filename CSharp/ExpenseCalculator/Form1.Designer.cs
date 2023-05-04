namespace ExpenseCalculator
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.transaction1 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.walletlbl = new System.Windows.Forms.Label();
            this.transaction2 = new System.Windows.Forms.Label();
            this.transaction4 = new System.Windows.Forms.Label();
            this.transaction3 = new System.Windows.Forms.Label();
            this.transaction8 = new System.Windows.Forms.Label();
            this.transaction7 = new System.Windows.Forms.Label();
            this.transaction6 = new System.Windows.Forms.Label();
            this.transaction5 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(128)))), ((int)(((byte)(128)))));
            this.button1.Font = new System.Drawing.Font("Microsoft YaHei", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button1.Location = new System.Drawing.Point(12, 114);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(364, 58);
            this.button1.TabIndex = 0;
            this.button1.Text = "Withdraw";
            this.button1.UseVisualStyleBackColor = false;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
            this.button2.Font = new System.Drawing.Font("Microsoft YaHei", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button2.Location = new System.Drawing.Point(12, 178);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(364, 58);
            this.button2.TabIndex = 1;
            this.button2.Text = "Deposit";
            this.button2.UseVisualStyleBackColor = false;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // label1
            // 
            this.label1.BackColor = System.Drawing.SystemColors.Control;
            this.label1.Font = new System.Drawing.Font("Microsoft YaHei", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(12, 24);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(179, 33);
            this.label1.TabIndex = 2;
            this.label1.Text = "Amount";
            this.label1.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            // 
            // label2
            // 
            this.label2.BackColor = System.Drawing.SystemColors.Control;
            this.label2.Font = new System.Drawing.Font("Microsoft YaHei", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(197, 24);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(179, 33);
            this.label2.TabIndex = 3;
            this.label2.Text = "Memo";
            this.label2.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            // 
            // textBox1
            // 
            this.textBox1.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textBox1.Location = new System.Drawing.Point(12, 77);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(179, 31);
            this.textBox1.TabIndex = 4;
            // 
            // textBox2
            // 
            this.textBox2.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textBox2.Location = new System.Drawing.Point(197, 77);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(179, 31);
            this.textBox2.TabIndex = 5;
            // 
            // transaction1
            // 
            this.transaction1.BackColor = System.Drawing.SystemColors.Control;
            this.transaction1.Font = new System.Drawing.Font("Microsoft YaHei", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.transaction1.Location = new System.Drawing.Point(12, 249);
            this.transaction1.Name = "transaction1";
            this.transaction1.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.transaction1.Size = new System.Drawing.Size(364, 39);
            this.transaction1.TabIndex = 6;
            this.transaction1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label3
            // 
            this.label3.BackColor = System.Drawing.SystemColors.Control;
            this.label3.Font = new System.Drawing.Font("Microsoft YaHei", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(382, 24);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(43, 49);
            this.label3.TabIndex = 7;
            this.label3.Text = "$";
            this.label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // walletlbl
            // 
            this.walletlbl.BackColor = System.Drawing.SystemColors.Control;
            this.walletlbl.Font = new System.Drawing.Font("Microsoft YaHei", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.walletlbl.Location = new System.Drawing.Point(411, 24);
            this.walletlbl.Name = "walletlbl";
            this.walletlbl.Size = new System.Drawing.Size(127, 49);
            this.walletlbl.TabIndex = 8;
            this.walletlbl.Text = "120";
            this.walletlbl.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // transaction2
            // 
            this.transaction2.BackColor = System.Drawing.SystemColors.ButtonHighlight;
            this.transaction2.Font = new System.Drawing.Font("Microsoft YaHei", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.transaction2.Location = new System.Drawing.Point(12, 288);
            this.transaction2.Name = "transaction2";
            this.transaction2.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.transaction2.Size = new System.Drawing.Size(364, 39);
            this.transaction2.TabIndex = 9;
            this.transaction2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // transaction4
            // 
            this.transaction4.BackColor = System.Drawing.SystemColors.ButtonHighlight;
            this.transaction4.Font = new System.Drawing.Font("Microsoft YaHei", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.transaction4.Location = new System.Drawing.Point(12, 366);
            this.transaction4.Name = "transaction4";
            this.transaction4.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.transaction4.Size = new System.Drawing.Size(364, 39);
            this.transaction4.TabIndex = 11;
            this.transaction4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // transaction3
            // 
            this.transaction3.BackColor = System.Drawing.SystemColors.Control;
            this.transaction3.Font = new System.Drawing.Font("Microsoft YaHei", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.transaction3.Location = new System.Drawing.Point(12, 327);
            this.transaction3.Name = "transaction3";
            this.transaction3.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.transaction3.Size = new System.Drawing.Size(364, 39);
            this.transaction3.TabIndex = 10;
            this.transaction3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // transaction8
            // 
            this.transaction8.BackColor = System.Drawing.SystemColors.ButtonHighlight;
            this.transaction8.Font = new System.Drawing.Font("Microsoft YaHei", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.transaction8.Location = new System.Drawing.Point(12, 522);
            this.transaction8.Name = "transaction8";
            this.transaction8.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.transaction8.Size = new System.Drawing.Size(364, 39);
            this.transaction8.TabIndex = 15;
            this.transaction8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // transaction7
            // 
            this.transaction7.BackColor = System.Drawing.SystemColors.Control;
            this.transaction7.Font = new System.Drawing.Font("Microsoft YaHei", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.transaction7.Location = new System.Drawing.Point(12, 483);
            this.transaction7.Name = "transaction7";
            this.transaction7.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.transaction7.Size = new System.Drawing.Size(364, 39);
            this.transaction7.TabIndex = 14;
            this.transaction7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // transaction6
            // 
            this.transaction6.BackColor = System.Drawing.SystemColors.ButtonHighlight;
            this.transaction6.Font = new System.Drawing.Font("Microsoft YaHei", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.transaction6.Location = new System.Drawing.Point(12, 444);
            this.transaction6.Name = "transaction6";
            this.transaction6.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.transaction6.Size = new System.Drawing.Size(364, 39);
            this.transaction6.TabIndex = 13;
            this.transaction6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // transaction5
            // 
            this.transaction5.BackColor = System.Drawing.SystemColors.Control;
            this.transaction5.Font = new System.Drawing.Font("Microsoft YaHei", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.transaction5.Location = new System.Drawing.Point(12, 405);
            this.transaction5.Name = "transaction5";
            this.transaction5.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.transaction5.Size = new System.Drawing.Size(364, 39);
            this.transaction5.TabIndex = 12;
            this.transaction5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(224)))), ((int)(((byte)(192)))));
            this.ClientSize = new System.Drawing.Size(742, 600);
            this.Controls.Add(this.transaction8);
            this.Controls.Add(this.transaction7);
            this.Controls.Add(this.transaction6);
            this.Controls.Add(this.transaction5);
            this.Controls.Add(this.transaction4);
            this.Controls.Add(this.transaction3);
            this.Controls.Add(this.transaction2);
            this.Controls.Add(this.walletlbl);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.transaction1);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Label transaction1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label walletlbl;
        private System.Windows.Forms.Label transaction2;
        private System.Windows.Forms.Label transaction4;
        private System.Windows.Forms.Label transaction3;
        private System.Windows.Forms.Label transaction8;
        private System.Windows.Forms.Label transaction7;
        private System.Windows.Forms.Label transaction6;
        private System.Windows.Forms.Label transaction5;
    }
}

