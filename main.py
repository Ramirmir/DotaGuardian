import tkinter as tk
from tkinter import font
import threading
import time
import os
import difflib
import re

LOG_FILE = 'dotaexp_logs.txt'
WHITELIST = ['steamcommunity.com', 'steampowered.com', 'dota2.com']
root = None

def check_phishing(text):
    urls = re.findall(r'(https?://[^\s/]+)', text)
    for url in urls:
        domain = url.replace('https://', '').replace('http://', '').split('/')[0]
        if domain in WHITELIST: continue
        for white in WHITELIST:
            ratio = difflib.SequenceMatcher(None, domain, white).ratio()
            if 0.75 <= ratio < 1.0:
                return True, domain, int(ratio*100)
    return False, None, 0

def _create_alert(text, target, score):
    alert = tk.Toplevel(root)
    alert.title("SECURITY ALERT")
    alert.attributes('-topmost', True)
    alert.overrideredirect(True)
    alert.configure(bg='#8B0000')
    
    w, h = 500, 200
    screen_w = alert.winfo_screenwidth()
    screen_h = alert.winfo_screenheight()
    
    x = 20
    y = screen_h - h - 60
    
    alert.geometry(f'{w}x{h}+{int(x)}+{int(y)}')

    f1 = font.Font(family="Helvetica", size=18, weight="bold")
    f2 = font.Font(family="Helvetica", size=11)

    tk.Label(alert, text="🚨 DOTA GUARDIAN ALERT", bg='#8B0000', fg='white', font=f1).pack(pady=15)
    info = f"УГРОЗА: {text}\nИМИТАЦИЯ: {target} ({score}%)"
    tk.Label(alert, text=info, bg='#8B0000', fg='white', font=f2).pack(pady=5)
    tk.Button(alert, text="ОК", bg='white', command=alert.destroy, width=10).pack(pady=15)
    alert.bell()

def monitor():
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w').close()
    last_size = os.path.getsize(LOG_FILE)
    while True:
        curr_size = os.path.getsize(LOG_FILE)
        if curr_size > last_size:
            with open(LOG_FILE, 'r', encoding='utf-8') as f:
                f.seek(last_size)
                for line in f.read().splitlines():
                    res, target, score = check_phishing(line)
                    if res:
                        root.after(0, _create_alert, line, target, score)
            last_size = curr_size
        time.sleep(0.5)

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    threading.Thread(target=monitor, daemon=True).start()
    root.mainloop()
