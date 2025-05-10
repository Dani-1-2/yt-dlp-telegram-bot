import os
import telebot
import yt_dlp

BOT_TOKEN = ""
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands = ["start"])
def start(message):
    bot.reply_to(message, "Test test")
@bot.message_handler(commands = ["download"])
def download(message):
    sent_msg = bot.send_message(message.chat.id, "Enter the link of the video:", parse_mode = "Markdown")
    bot.register_next_step_handler(sent_msg, resolution)
def resolution(message):
    global url
    url = message.text
    sent_msg = bot.send_message(message.chat.id, "Enter the desired resolution", parse_mode = "Markdown")
    bot.register_next_step_handler(sent_msg, downloader)
def downloader(message):
    res = int(message.text)
    ydl_opts = {
        "format": f"bestvideo[height<={res}]+bestaudio/best",
        "outtmpl": "video.%(ext)s",
            "format_sort": [
        "vcodec:h264",
        "lang",
        "quality",
        "res",
        "fps",
        "hdr:12",
        "acodec:aac"
    ],
    "merge_output_format": "mp4",
    "final_ext": "mp4",
    "postprocessors": [
        {
            "key": "FFmpegVideoRemuxer",
            "preferedformat": "mp4"
        }
    ]

    }
    yt_dlp.YoutubeDL(ydl_opts).download([url])
    video = open("video.mp4", "rb")
    bot.send_video(message.chat.id, video)
    os.remove("video.mp4")
def download(message):
    sent_msg = bot.send_message(message.chat.id, "Enter the link of the video:", parse_mode = "Markdown")
    bot.register_next_step_handler(sent_msg, resolution)
def resolution(message):
    global url
    url = message.text
    sent_msg = bot.send_message(message.chat.id, "Enter the desired resolution", parse_mode = "Markdown")
    bot.register_next_step_handler(sent_msg, downloader)
def downloader(message):
    res = int(message.text)
    ydl_opts = {
        "format": f"bestvideo[height<={res}]+bestaudio/best",
        "outtmpl": "video.%(ext)s",
            "format_sort": [
        "vcodec:h264",
        "lang",
        "quality",
        "res",
        "fps",
        "hdr:12",
        "acodec:aac"
    ],
    "merge_output_format": "mp4",
    "final_ext": "mp4",
    "postprocessors": [
        {
            "key": "FFmpegVideoRemuxer",
            "preferedformat": "mp4"
        }
    ]

    }
    yt_dlp.YoutubeDL(ydl_opts).download([url])
    video = open("video.mp4", "rb")
    bot.send_video(message.chat.id, video)
@bot.message_handler(commands = ["downloadaudio"])
def audiodownload(message):
    sent_msg = bot.send_message(message.chat.id, "Enter the link of the video:", parse_mode = "Markdown")
    bot.register_next_step_handler(sent_msg, audiodownloader)
def audiodownloader(message):
    url = message.text
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "audio.%(ext)s",
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
    }
    yt_dlp.YoutubeDL(ydl_opts).download([url])
    audio = open("audio.mp3", "rb")
    bot.send_audio(message.chat.id, audio)
    os.remove("audio.mp3")
bot.infinity_polling()