import requests
import tkinter as tk

class EDMCTSC():
    exists = tk.StringVar()

def plugin_start3(plugin_dir: str) -> str:
    return "EDMC-TSC"

def dashboard_entry(cmdr: str, is_beta: bool, entry):
    destination = entry["Destination"]["Name"]
    r = requests.get("https://www.edsm.net/api-v1/system", params={'systemName': destination})
    EDMCTSC.exists.set(f"Target system: {'Exists' if (r.text != '[]') else 'Does NOT exist'}")

def plugin_app(parent: tk.Frame) -> tk.Label:
    return tk.Label(parent, textvariable=EDMCTSC.exists)
