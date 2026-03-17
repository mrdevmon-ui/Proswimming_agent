require('dotenv').config(); // Загружаем переменные окружения из .env

const { createMaxBot } = require('max-bot-sdk');

// Инициализация бота
const bot = createMaxBot({
  token: process.env.BOT_TOKEN, // Токен бота из переменной окружения
});

// Обработка команды /start
bot.onText(/\/start/, async (ctx) => {
  await ctx.reply(`
Вас приветствует бот школы плавания Proswimming.ru.
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

// Остальные обработчики команд
bot.onText(/Выбрать бассейн/i, async (ctx) => {
  await
