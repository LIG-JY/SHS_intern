using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

//Telegram using
using Telegram.Bot;
using Telegram.Bot.Exceptions;
using Telegram.Bot.Polling;
using Telegram.Bot.Types;
using Telegram.Bot.Types.Enums;
using Telegram.Bot.Types.Payments;
using Telegram.Bot.Types.ReplyMarkups;


namespace TelegramAPI_test
{
    public partial class Form1 : Form
    {
        private TelegramBotClient botClient;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            botClient = new TelegramBotClient("6836280679:AAHqTH-tFBhilDlodg69mKraZHhEh2gC6dU");
            StartReciever();
        }

        // Start Telegram Bot
        public async Task StartReciever()
        {
            var token = new CancellationTokenSource();
            var cancelToken = token.Token;
            var ReOpt = new ReceiverOptions { AllowedUpdates = { } };
            await botClient.ReceiveAsync(OnMessage, ErrorMessage, ReOpt, cancelToken);
        }

        // Receiver Message from Bot
        public async Task OnMessage(ITelegramBotClient botClient, Update update, CancellationToken cancellation)
        {
            if (update.Message is Telegram.Bot.Types.Message message)
            {
                SendMessage(message);
            }
        }

        // Error Message
        public async Task ErrorMessage(ITelegramBotClient telegramBot, Exception e, CancellationToken cancellation)
        {
            if (e is ApiRequestException requestException)
            {
                await botClient.SendTextMessageAsync("", e.Message.ToString());
            }
        }

        public async Task SendMessage(Telegram.Bot.Types.Message message)
        {
            await this.botClient.SendTextMessageAsync(message.Chat.Id, "Hello Bro!"); // 응답 메세지 로직
        }

    }
}