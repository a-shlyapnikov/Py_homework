import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from pytube import YouTube
import emoji
import datetime

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(emoji.emojize('Привет:vulcan_salute:\nЯ телеграм-бот, который может скачивать ролики с Youtube\n'
                        'Отправь мне ссылку :backhand_index_pointing_down:'))

@dp.message_handler()
async def download_video(message: types.Message):
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://www.youtube.com/' or 'https://youtu.be/':
        await message.answer(f'Начинаю загрузку видео' + emoji.emojize(':video_camera:') + f': {yt.title}\n'
                            f'С канала: [{yt.author}]({yt.channel_url})  ', parse_mode='Markdown')
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}' )
        with open(f'{message.chat.id}/{message.chat.id}_{yt.title}', 'rb') as video:
            await message.answer_video(video, caption= ('Вот ваше видео' + emoji.emojize(':index_pointing_up:')))
            os.remove(f'{message.chat.id}/{message.chat.id}_{yt.title}')
            os.rmdir(f'{message.chat.id}')
        log(message.from_user.first_name, message.from_user.last_name, yt.title, url, message.from_user.id)
            
def log(user_name, user_lastname, yt_title, yt_url, user_id):
    database = open('data.csv', 'a', encoding= 'utf-8')
    database.write(f'{user_name} {user_lastname}, {yt_title}, {yt_url}, {user_id}, {datetime.datetime.now()}\n')
    database.close()

    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
