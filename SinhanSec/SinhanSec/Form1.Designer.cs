using System;

namespace SinhanSec
{
    partial class Form1
    {
        /// <summary>
        /// 필수 디자이너 변수입니다.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 사용 중인 모든 리소스를 정리합니다.
        /// </summary>
        /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 디자이너에서 생성한 코드

        /// <summary>
        /// 디자이너 지원에 필요한 메서드입니다. 
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.Ticker = new System.Windows.Forms.TextBox();
            this.targetPrice = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.currentPrice = new System.Windows.Forms.TextBox();
            this.currentCheck = new System.Windows.Forms.Button();
            this.targetCall = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.correctionPrice = new System.Windows.Forms.TextBox();
            this.correctionCall = new System.Windows.Forms.Button();
            this.targetQuantity = new System.Windows.Forms.TextBox();
            this.immediateCall = new System.Windows.Forms.Button();
            this.cancel = new System.Windows.Forms.Button();
            this.cancelQuantity = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.immediateQuantity = new System.Windows.Forms.TextBox();
            this.tickerSave = new System.Windows.Forms.Button();
            this.CorrectionQuantity = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(17, 18);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(57, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "종목 코드";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(17, 94);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(69, 12);
            this.label2.TabIndex = 1;
            this.label2.Text = "지정가 주문";
            this.label2.Click += new System.EventHandler(this.label2_Click);
            // 
            // Ticker
            // 
            this.Ticker.Location = new System.Drawing.Point(92, 15);
            this.Ticker.Name = "Ticker";
            this.Ticker.Size = new System.Drawing.Size(157, 21);
            this.Ticker.TabIndex = 2;
            this.Ticker.TextChanged += new System.EventHandler(this.Ticker_TextChanged);
            // 
            // targetPrice
            // 
            this.targetPrice.Location = new System.Drawing.Point(92, 91);
            this.targetPrice.Name = "targetPrice";
            this.targetPrice.Size = new System.Drawing.Size(158, 21);
            this.targetPrice.TabIndex = 3;
            this.targetPrice.Text = "원";
            this.targetPrice.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.targetPrice.TextChanged += new System.EventHandler(this.targetPrice_TextChanged);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(17, 58);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(69, 12);
            this.label3.TabIndex = 4;
            this.label3.Text = "현재가 조회";
            this.label3.Click += new System.EventHandler(this.label3_Click);
            // 
            // currentPrice
            // 
            this.currentPrice.Location = new System.Drawing.Point(92, 55);
            this.currentPrice.Name = "currentPrice";
            this.currentPrice.Size = new System.Drawing.Size(157, 21);
            this.currentPrice.TabIndex = 5;
            this.currentPrice.Text = "원";
            this.currentPrice.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.currentPrice.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // currentCheck
            // 
            this.currentCheck.Location = new System.Drawing.Point(269, 54);
            this.currentCheck.Name = "currentCheck";
            this.currentCheck.Size = new System.Drawing.Size(80, 21);
            this.currentCheck.TabIndex = 6;
            this.currentCheck.Text = "조회";
            this.currentCheck.UseVisualStyleBackColor = true;
            this.currentCheck.Click += new System.EventHandler(this.currentCheck_Click);
            // 
            // targetCall
            // 
            this.targetCall.Location = new System.Drawing.Point(357, 90);
            this.targetCall.Name = "targetCall";
            this.targetCall.Size = new System.Drawing.Size(78, 21);
            this.targetCall.TabIndex = 7;
            this.targetCall.Text = "주문";
            this.targetCall.UseVisualStyleBackColor = true;
            this.targetCall.Click += new System.EventHandler(this.button2_Click);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(17, 129);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(53, 12);
            this.label4.TabIndex = 8;
            this.label4.Text = "정정하기";
            this.label4.Click += new System.EventHandler(this.label4_Click);
            // 
            // correctionPrice
            // 
            this.correctionPrice.Location = new System.Drawing.Point(92, 125);
            this.correctionPrice.Name = "correctionPrice";
            this.correctionPrice.Size = new System.Drawing.Size(158, 21);
            this.correctionPrice.TabIndex = 9;
            this.correctionPrice.Text = "원";
            this.correctionPrice.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // correctionCall
            // 
            this.correctionCall.Location = new System.Drawing.Point(357, 124);
            this.correctionCall.Name = "correctionCall";
            this.correctionCall.Size = new System.Drawing.Size(80, 21);
            this.correctionCall.TabIndex = 10;
            this.correctionCall.Text = "정정";
            this.correctionCall.UseVisualStyleBackColor = true;
            this.correctionCall.Click += new System.EventHandler(this.button3_Click);
            // 
            // targetQuantity
            // 
            this.targetQuantity.Location = new System.Drawing.Point(269, 91);
            this.targetQuantity.Name = "targetQuantity";
            this.targetQuantity.Size = new System.Drawing.Size(80, 21);
            this.targetQuantity.TabIndex = 11;
            this.targetQuantity.Text = "주";
            this.targetQuantity.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.targetQuantity.TextChanged += new System.EventHandler(this.targetQuantity_TextChanged);
            // 
            // immediateCall
            // 
            this.immediateCall.Location = new System.Drawing.Point(192, 203);
            this.immediateCall.Name = "immediateCall";
            this.immediateCall.Size = new System.Drawing.Size(78, 21);
            this.immediateCall.TabIndex = 14;
            this.immediateCall.Text = "주문";
            this.immediateCall.UseVisualStyleBackColor = true;
            // 
            // cancel
            // 
            this.cancel.Location = new System.Drawing.Point(192, 163);
            this.cancel.Name = "cancel";
            this.cancel.Size = new System.Drawing.Size(78, 21);
            this.cancel.TabIndex = 15;
            this.cancel.Text = "취소";
            this.cancel.UseVisualStyleBackColor = true;
            this.cancel.Click += new System.EventHandler(this.button6_Click);
            // 
            // cancelQuantity
            // 
            this.cancelQuantity.Location = new System.Drawing.Point(92, 163);
            this.cancelQuantity.Name = "cancelQuantity";
            this.cancelQuantity.Size = new System.Drawing.Size(80, 21);
            this.cancelQuantity.TabIndex = 17;
            this.cancelQuantity.Text = "주";
            this.cancelQuantity.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(17, 166);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(53, 12);
            this.label5.TabIndex = 18;
            this.label5.Text = "취소하기";
            this.label5.Click += new System.EventHandler(this.label5_Click);
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(17, 208);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(69, 12);
            this.label8.TabIndex = 21;
            this.label8.Text = "최우선 주문";
            // 
            // immediateQuantity
            // 
            this.immediateQuantity.Location = new System.Drawing.Point(92, 204);
            this.immediateQuantity.Name = "immediateQuantity";
            this.immediateQuantity.Size = new System.Drawing.Size(80, 21);
            this.immediateQuantity.TabIndex = 22;
            this.immediateQuantity.Text = "주";
            this.immediateQuantity.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // tickerSave
            // 
            this.tickerSave.Location = new System.Drawing.Point(269, 15);
            this.tickerSave.Name = "tickerSave";
            this.tickerSave.Size = new System.Drawing.Size(80, 21);
            this.tickerSave.TabIndex = 23;
            this.tickerSave.Text = "설정";
            this.tickerSave.UseVisualStyleBackColor = true;
            this.tickerSave.Click += new System.EventHandler(this.tickerSave_Click);
            // 
            // CorrectionQuantity
            // 
            this.CorrectionQuantity.Location = new System.Drawing.Point(269, 126);
            this.CorrectionQuantity.Name = "CorrectionQuantity";
            this.CorrectionQuantity.Size = new System.Drawing.Size(80, 21);
            this.CorrectionQuantity.TabIndex = 24;
            this.CorrectionQuantity.Text = "주";
            this.CorrectionQuantity.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.CorrectionQuantity.TextChanged += new System.EventHandler(this.CorrectionQuantity_TextChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(491, 265);
            this.Controls.Add(this.CorrectionQuantity);
            this.Controls.Add(this.tickerSave);
            this.Controls.Add(this.immediateQuantity);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.cancelQuantity);
            this.Controls.Add(this.cancel);
            this.Controls.Add(this.immediateCall);
            this.Controls.Add(this.targetQuantity);
            this.Controls.Add(this.correctionCall);
            this.Controls.Add(this.correctionPrice);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.targetCall);
            this.Controls.Add(this.currentCheck);
            this.Controls.Add(this.currentPrice);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.targetPrice);
            this.Controls.Add(this.Ticker);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox Ticker;
        private System.Windows.Forms.TextBox targetPrice;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox currentPrice;
        private System.Windows.Forms.Button currentCheck;
        private System.Windows.Forms.Button targetCall;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox correctionPrice;
        private System.Windows.Forms.Button correctionCall;
        private System.Windows.Forms.TextBox targetQuantity;
        private System.Windows.Forms.Button immediateCall;
        private System.Windows.Forms.Button cancel;
        private System.Windows.Forms.TextBox cancelQuantity;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.TextBox immediateQuantity;
        private System.Windows.Forms.Button tickerSave;
        private readonly EventHandler correctionQuantity_TextChanged;
        private System.Windows.Forms.TextBox CorrectionQuantity;
    }
}

