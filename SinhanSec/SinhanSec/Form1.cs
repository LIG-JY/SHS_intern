using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using Telegram.Bot;
using Telegram.Bot.Exceptions;
using Telegram.Bot.Polling;
using Telegram.Bot.Types;

namespace SinhanSec
{
    public partial class Form1 : Form
    {
        private OrderInfo orderInfo;
        private TelegramBotClient telegramBotClient;



        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            orderInfo = new OrderInfo(); // 폼이 화면에 그려지자마자 OrderInfo 객체 생성
            telegramBotClient = new TelegramBotClient("");
            StartReciever();
        }

        // Start Telegram Bot
        public async Task StartReciever()
        {
            var token = new CancellationTokenSource();
            var cancelToken = token.Token;
            var ReOpt = new ReceiverOptions { AllowedUpdates = { } };
            await telegramBotClient.ReceiveAsync(OnMessage, ErrorMessage, ReOpt, cancelToken);
        }

        // Receiver Message from Bot
        public async Task OnMessage(ITelegramBotClient botClient, Update update, CancellationToken cancellation)
        {
            if (update.Message is Telegram.Bot.Types.Message message)
            {
                await telegramBotClient.SendTextMessageAsync(message.Chat.Id, "Hello Bro!");
            }
        }

        // Error Message
        public async Task ErrorMessage(ITelegramBotClient telegramBot, Exception e, CancellationToken cancellation)
        {
            if (e is ApiRequestException requestException)
            {
                await telegramBotClient.SendTextMessageAsync("6836280679:AAHqTH-tFBhilDlodg69mKraZHhEh2gC6dU", e.Message.ToString());
            }
        }

        /*public async Task SendMessage(Message message)
        {

        }*/

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void Ticker_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void correctionQuantityonQuantity_TextChanged(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        

        private void tickerSave_Click(object sender, EventArgs e)
        {
            string inputText = Ticker.Text;
            if (IsNumeric(inputText))
            {
                long ticker = long.Parse(inputText);
                try
                {
                    orderInfo.Code = ticker; // 입력 받은 종목코드를 orderInfo.setter로 넘긴다. 
                    MessageBox.Show("종목 코드가 저장되었습니다.", "저장 완료", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
                catch (ArgumentException)
                {
                    MessageBox.Show("정상적인 종목 코드를 입력하세요.", "입력 오류", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            else
            {
                MessageBox.Show("숫자만 입력하세요.", "입력 오류", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
        private bool IsNumeric(string text)
        {
            return long.TryParse(text, out _);
        }

        private void currentCheck_Click(object sender, EventArgs e)
        {
            if (orderInfo.IsTickerSaved())
            {
                /*currentPrice*/
            }
        }

        private void targetPrice_TextChanged(object sender, EventArgs e)
        {

        }

        private void targetQuantity_TextChanged(object sender, EventArgs e)
        {

        }

        private void correctionQuantity_TextChanged_1(object sender, EventArgs e)
        {

        }

        private void CorrectionQuantity_TextChanged(object sender, EventArgs e)
        {

        }

    }
}
