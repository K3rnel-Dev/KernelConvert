# Coded by K3rnel Dev 
# Used library moviepy
# Contact me: telegram (@K3RNEL1337)
# https://github.com/K3rnel-Dev/
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import moviepy.editor


def select_video():
    video_path = filedialog.askopenfilename(filetypes=[('Video Files', '*.mp4')])
    video_entry.delete(0, tk.END)
    video_entry.insert(0, video_path)


def select_save_directory():
    save_dir = filedialog.askdirectory()
    save_entry.delete(0, tk.END)
    save_entry.insert(0, save_dir)


def convert_video():
    video_path = video_entry.get()
    audio_name = audio_entry.get()
    save_dir = save_entry.get()

    if not save_dir or not audio_name:
        result_label.config(text='Укажите название файла и папку для сохранения!', foreground='red')
        return

    audio_path = f'{save_dir}/{audio_name}.mp3'

    video = moviepy.editor.VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

    result_label.config(text='Конвертация завершена!', foreground='#fccf03')


# Создание окна
window = tk.Tk()
window.title('Конвертер видео в аудио')
window.geometry('400x610')
window.title('Mp4-To-Mp3 CONVERTOR[by k3rnel-dev]')
window.resizable(False, False)
window.configure(bg='#111')


# Стили
title_style = ttk.Style()
title_style.configure('Title.TLabel', foreground='#fccf03', background='#111', font=('Orbitron', 16))

label_style = ttk.Style()
label_style.configure('Label.TLabel', foreground='#fff', background='#111', font=('Orbitron', 12))

entry_style = ttk.Style()
entry_style.configure('Entry.TEntry', foreground='black', background='#111', font=('Orbitron', 12))

button_style = ttk.Style()
button_style.configure('Button.TButton', foreground='#fff', background='#fccf03', font=('Orbitron', 12))

# Элементы интерфейса
title_label = ttk.Label(window, text='Конвертер видео в аудио', style='Title.TLabel')
title_label.pack(pady=20)

logo_image = tk.PhotoImage(file='screens/logo.png').subsample(3, 3)  # Изменение размера логотипа
logo_label = ttk.Label(window, image=logo_image, background='#111')
logo_label.pack(pady=10)

video_label = ttk.Label(window, text='Выберите видео:', style='Label.TLabel')
video_label.pack()

video_entry = ttk.Entry(window, width=40, style='Entry.TEntry')
video_entry.pack(pady=10)

video_button = ttk.Button(window, text='Выбрать', style='Button.TButton', command=select_video)
video_button.pack()

audio_label = ttk.Label(window, text='Название аудио файла:', style='Label.TLabel')
audio_label.pack()

audio_frame = ttk.Frame(window, style='Frame.TFrame')
audio_frame.pack(pady=10)

audio_entry = ttk.Entry(audio_frame, width=30, style='Entry.TEntry')
audio_entry.pack(side=tk.LEFT)

save_button = ttk.Button(audio_frame, text='Выбрать папку', style='Button.TButton', command=select_save_directory)
save_button.pack(side=tk.LEFT, padx=5)

save_label = ttk.Label(window, text='Папка для сохранения:', style='Label.TLabel')
save_label.pack()

save_entry = ttk.Entry(window, width=40, style='Entry.TEntry')
save_entry.pack(pady=10)

convert_button = ttk.Button(window, text='Переконвертировать', style='Button.TButton', command=convert_video)
convert_button.pack(pady=10)

result_label = ttk.Label(window, text='', style='Label.TLabel')
result_label.pack(pady=20)

# Запуск приложения
window.mainloop()
