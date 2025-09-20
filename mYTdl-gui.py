import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

def download_video():
    url = url_entry.get().strip()
    sub_lang = sub_var.get().strip()
    
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    
    output_template = "%(title)s.%(ext)s"
    
    # Automatically pick highest resolution
    cmd = [
        "yt-dlp",
        "-f", "bestvideo+bestaudio/best",
        "--write-subs",
        f"--sub-langs={sub_lang}",
        "--embed-subs",
        url,
        "-o", output_template
    ]
    
    try:
        subprocess.run(cmd)
        messagebox.showinfo("Success", "Download completed!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("YouTube Downloader")

# URL input
tk.Label(root, text="YouTube URL:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# Subtitle language
tk.Label(root, text="Subtitle language code:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
sub_var = tk.StringVar(value="all")
sub_entry = tk.Entry(root, textvariable=sub_var)
sub_entry.grid(row=1, column=1, padx=5, pady=5)

# Download button
download_btn = tk.Button(root, text="Download", command=download_video)
download_btn.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
