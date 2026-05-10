import os
import re

translations = {
    "ar.ftl": {"channel_mode": "وضع القناة", "channel_mode_stereo": "ستيريو", "channel_mode_mono": "أحادي", "channel_mode_left_only": "الأيسر فقط", "channel_mode_right_only": "الأيمن فقط", "channel_mode_swap_left_right": "تبديل اليسار/اليمين"},
    "de.ftl": {"channel_mode": "Kanalmodus", "channel_mode_stereo": "Stereo", "channel_mode_mono": "Mono", "channel_mode_left_only": "Nur links", "channel_mode_right_only": "Nur rechts", "channel_mode_swap_left_right": "L/R tauschen"},
    "es.ftl": {"channel_mode": "Modo de canal", "channel_mode_stereo": "Estéreo", "channel_mode_mono": "Mono", "channel_mode_left_only": "Solo izquierdo", "channel_mode_right_only": "Solo derecho", "channel_mode_swap_left_right": "Intercambiar I/D"},
    "fr.ftl": {"channel_mode": "Mode de canal", "channel_mode_stereo": "Stéréo", "channel_mode_mono": "Mono", "channel_mode_left_only": "Gauche uniquement", "channel_mode_right_only": "Droite uniquement", "channel_mode_swap_left_right": "Inverser G/D"},
    "gr.ftl": {"channel_mode": "Λειτουργία καναλιού", "channel_mode_stereo": "Στέρεο", "channel_mode_mono": "Μονοφωνικό", "channel_mode_left_only": "Μόνο αριστερά", "channel_mode_right_only": "Μόνο δεξιά", "channel_mode_swap_left_right": "Εναλλαγή Α/Δ"},
    "he.ftl": {"channel_mode": "מצב ערוץ", "channel_mode_stereo": "סטריאו", "channel_mode_mono": "מונו", "channel_mode_left_only": "שמאל בלבד", "channel_mode_right_only": "ימין בלבד", "channel_mode_swap_left_right": "החלף ש/י"},
    "hu.ftl": {"channel_mode": "Csatorna mód", "channel_mode_stereo": "Sztereó", "channel_mode_mono": "Monó", "channel_mode_left_only": "Csak bal", "channel_mode_right_only": "Csak jobb", "channel_mode_swap_left_right": "B/J felcserélése"},
    "ja.ftl": {"channel_mode": "チャンネルモード", "channel_mode_stereo": "ステレオ", "channel_mode_mono": "モノラル", "channel_mode_left_only": "左のみ", "channel_mode_right_only": "右のみ", "channel_mode_swap_left_right": "左右を入れ替え"},
    "ko.ftl": {"channel_mode": "채널 모드", "channel_mode_stereo": "스테레오", "channel_mode_mono": "모노", "channel_mode_left_only": "왼쪽만", "channel_mode_right_only": "오른쪽만", "channel_mode_swap_left_right": "L/R 스왑"},
    "pl.ftl": {"channel_mode": "Tryb kanału", "channel_mode_stereo": "Stereo", "channel_mode_mono": "Mono", "channel_mode_left_only": "Tylko lewy", "channel_mode_right_only": "Tylko prawy", "channel_mode_swap_left_right": "Zamień L/P"},
    "ro.ftl": {"channel_mode": "Mod canal", "channel_mode_stereo": "Stereo", "channel_mode_mono": "Mono", "channel_mode_left_only": "Doar stânga", "channel_mode_right_only": "Doar dreapta", "channel_mode_swap_left_right": "Inversare S/D"},
    "ru.ftl": {"channel_mode": "Режим канала", "channel_mode_stereo": "Стерео", "channel_mode_mono": "Моно", "channel_mode_left_only": "Только левый", "channel_mode_right_only": "Только правый", "channel_mode_swap_left_right": "Поменять Л/П"},
    "tr.ftl": {"channel_mode": "Kanal Modu", "channel_mode_stereo": "Stereo", "channel_mode_mono": "Mono", "channel_mode_left_only": "Sadece sol", "channel_mode_right_only": "Sadece sağ", "channel_mode_swap_left_right": "Sol/Sağ Değiştir"},
    "uk.ftl": {"channel_mode": "Режим каналу", "channel_mode_stereo": "Стерео", "channel_mode_mono": "Моно", "channel_mode_left_only": "Лише лівий", "channel_mode_right_only": "Лише правий", "channel_mode_swap_left_right": "Поміняти Л/П"},
    "zh-CN.ftl": {"channel_mode": "声道模式", "channel_mode_stereo": "立体声", "channel_mode_mono": "单声道", "channel_mode_left_only": "仅左声道", "channel_mode_right_only": "仅右声道", "channel_mode_swap_left_right": "交换左右"},
    "id.ftl": {"channel_mode": "Mode Kanal", "channel_mode_stereo": "Stereo", "channel_mode_mono": "Mono", "channel_mode_left_only": "Hanya kiri", "channel_mode_right_only": "Hanya kanan", "channel_mode_swap_left_right": "Tukar Kiri/Kanan"},
    "pt-BR.ftl": {"channel_mode": "Modo de Canal", "channel_mode_stereo": "Estéreo", "channel_mode_mono": "Mono", "channel_mode_left_only": "Apenas esquerda", "channel_mode_right_only": "Apenas direita", "channel_mode_swap_left_right": "Inverter E/D"},
    "tok.ftl": {"channel_mode": "nasin kalama", "channel_mode_stereo": "kalama tu", "channel_mode_mono": "kalama wan", "channel_mode_left_only": "poka soto taso", "channel_mode_right_only": "poka teje taso", "channel_mode_swap_left_right": "ante soto teje"},
    "tok-SP.ftl": {"channel_mode": "󱥔 󱤴", "channel_mode_stereo": "󱤴 󱥩", "channel_mode_mono": "󱤴 󱥯", "channel_mode_left_only": "󱥭 󱤿 󱥔", "channel_mode_right_only": "󱥭 󱥬 󱥔", "channel_mode_swap_left_right": "󱤴 󱥭"}
}

def replace_in_file(path, replacements):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    for key, val in replacements.items():
        content = re.sub(r'^' + key + r'\s*=.*$', f"{key} = {val}", content, flags=re.MULTILINE)
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

for fname, reps in translations.items():
    path = os.path.join("locales", fname)
    if os.path.exists(path):
        replace_in_file(path, reps)
        print(f"Translated {fname}")

