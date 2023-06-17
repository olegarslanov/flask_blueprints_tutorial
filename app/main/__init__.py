from flask import Blueprint

# sukuriam blueprint objekta "bp". Perduodami argumentai: "main" - vardas ir __name__ - speciali kintamoji, kuri laiko savyje sio Python modulio pavadinima
bp = Blueprint("main", __name__)

# su situ uzrasu su blue print kartu bus registruoti jo marsrutai
from app.main import routes


# cia sukuriama schema ir dadetas marsrutas
