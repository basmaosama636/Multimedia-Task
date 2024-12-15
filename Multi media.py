import tkinter as ttk
from tkinter import messagebox
import subprocess
def download_video(quality_flag):
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    try:
        command = ['yt-dlp', '-f', quality_flag, "-o", "%(title)s.%(ext)s", url]
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", "Download completed!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
root = ttk.Tk()
root.title("YouTube Downloader")
ttk.Label(root, text="Enter YouTube URL:").grid(row=0, column=0, columnspan=2, pady=5)
url_entry = ttk.Entry(root, width=50)
url_entry.grid(row=1, column=0, columnspan=2, pady=5)
ttk.Button(root, text="High Resolution", command=lambda: download_video("bestvideo+bestaudio")).grid(row=2, column=0, padx=5, pady=5)
ttk.Button(root, text="Low Resolution", command=lambda: download_video("worstvideo+bestaudio")).grid(row=2, column=1, padx=5, pady=5)
ttk.Button(root, text="Audio Only", command=lambda: download_video("bestaudio")).grid(row=3, column=0, columnspan=2, pady=5)
root.mainloop()