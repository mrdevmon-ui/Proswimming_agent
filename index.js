require('dotenv').config();

const { createMaxBot } = require('max-bot-sdk');

const bot = createMaxBot({
  token: process.env.BOT_TOKEN
});

bot.onText(/\/start/, async (ctx) => {
  await ctx.reply(`
Вас приветствует бот школы плавания ProsWimming.ru.
Я помогу вам ознакомиться с основной информацией, записаться на бесплатное занятие.
`);

  const keyboard = [
    ["Выбрать бассейн"],
    ["Стоимость занятий"],
    ["Тренерский состав"],
    ["Администратор"],
    ["Личный кабинет"]
  ];

  await ctx.reply("Главная", { keyboard });
});

bot.onText(/Выбрать бассейн/i, async (ctx) => {
  await ctx.reply("Выберите ближайший к вам бассейн:");
});

bot.onText(/Стоимость занятий/i, async (ctx) => {
  await ctx.reply("Стоимость занятий зависит от выбранного бассейна и программы обучения.");
});

bot.onText(/Тренерский состав/i, async (ctx) => {
  await ctx.reply("Наши тренеры имеют многолетний опыт работы и международные сертификаты.");
});

bot.onText(/Администратор/i, async (ctx) => {
  await ctx.reply("Свяжитесь с нашим администратором по телефону: +7 (XXX) XXX-XX-XX");
});

bot.onText(/Личный кабинет/i, async (ctx) => {
  await ctx.reply("Авторизация в личном кабинете доступна по ссылке: http://proswimming.ru/login");
});

bot.launch();
console.log("Bot is running...");
