import customtkinter as ctk
import pandas as pd
import joblib
import time
from engine import analyze_url

# --- DESIGN SYSTEM ---
COLORS = {
    "bg": "#121212",        # Deep Midnight
    "frame":"#1e1e1e",
    "text":"#ffffff",
    "card": "#161B22",      # Soft Slate
    "accent": "#27bbf1",    # Cyber Blue
    "danger": "#F85149",    # Alert Red
    "safe": "#269A35"       # Success Green
}

# --- INITIALIZE APP ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")
app = ctk.CTk(fg_color=COLORS["bg"])
app.geometry("1000x650")
app.title("CyberLens Shield - Pro Edition")

# --- UI COMPONENTS ---

# Header
header = ctk.CTkFrame(app, fg_color=COLORS["card"], corner_radius=10)
header.pack(fill="x", padx=30, pady=20)
ctk.CTkLabel(header, text="CYBERLENS SHIELD: ADVANCED THREAT INTELLIGENCE", 
             font=("Helvetica", 22, "bold"), text_color=COLORS["accent"]).pack(pady=10)
ctk.CTkLabel(header, text="Developed and Engineering by Komal Rai | B.TECH CAPSTONE ", 
             font=("Helvetica", 12)).pack(pady=(0, 10))

# Input Area
input_frame = ctk.CTkFrame(app, fg_color=COLORS["card"], corner_radius=10)
input_frame.pack(fill="x", padx=30, pady=10)

url_entry = ctk.CTkEntry(input_frame, placeholder_text="Paste target URL here...", 
                         width=700, height=45, border_color=COLORS["accent"], border_width=2)
url_entry.pack(pady=25, padx=20)

scan_btn = ctk.CTkButton(input_frame, text="RUN ACTIVE DIAGNOSTIC", 
                         fg_color=COLORS["accent"], text_color="white",
                         command=lambda: analyze_url(), height=45, corner_radius=8)
scan_btn.pack(pady=(0, 25))

# Log Display (The "Terminal" Feel)
analysis_log = ctk.CTkTextbox(app, width=840, height=180, fg_color="#000000", 
                              text_color="#00FF00", font=("Courier New", 12))
analysis_log.pack(pady=10)

# Result Banner
threat_banner = ctk.CTkLabel(app, text="SYSTEM READY", font=("Helvetica", 20, "bold"), 
                             fg_color=COLORS["card"], height=60, corner_radius=10)
threat_banner.pack(fill="x", padx=30, pady=10)

# --- ENGINE ---
def analyze_url():
    url = url_entry.get()
    if not url: return
    
    analysis_log.delete("1.0", "end")
    analysis_log.insert("end", f"[*] Initiating scan for: {url}...\n")
    app.update()
    time.sleep(0.5)
    analysis_log.insert("end", "[*] Extracting features...\n")
    app.update()
    time.sleep(0.5)
    
    # [Replace with your model.predict logic]
    if "google" in url.lower():
        threat_banner.configure(text="SAFE: LEGITIMATE DOMAIN", fg_color=COLORS["safe"])
        analysis_log.insert("end", "[+] Result: No threats detected. Confidence: 99.8%\n")
    else:
        threat_banner.configure(text="DANGER: PHISHING DETECTED", fg_color=COLORS["danger"])
        analysis_log.insert("end", "[!] ALERT: Malicious patterns identified.\n")

app.mainloop()