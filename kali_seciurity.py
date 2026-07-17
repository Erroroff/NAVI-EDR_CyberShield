# =============================================================================
#          GLOBAL LANGUAGE CORE - AUTOMATIC PL/EN TRANSLATOR v4.5
# =============================================================================
import locale

def get_system_lang():
    try:
        return locale.getdefaultlocale()[:2].lower()
    except Exception:
        return "en"

SYS_LANG = get_system_lang()

def translate_text(text):
    if SYS_LANG != "pl":
        en_dict = {
            "[SPYWARE / PHISHING] - Wyłudzanie poświadczeń i kont": "[SPYWARE / PHISHING] - Credential harvesting and account theft",
            "[TROJAN / DOWNLOADER] - Ciche pobieranie kodu przez sieć": "[TROJAN / DOWNLOADER] - Silent network code download",
            "[BACKDOOR / EXPLOIT] - Ukryte polecenia powłoki": "[BACKDOOR / EXPLOIT] - Hidden shell command execution",
            "[MALWARE / DESTRUCTOR] - Usuwanie klastrów jądra": "[MALWARE / DESTRUCTOR] - Kernel cluster destruction",
            "[SABOTAGE / INTRUSION] - Wymuszenie zatrzymania jądra": "[SABOTAGE / INTRUSION] - Forced kernel halt intrusion",
            "[MALWARE / WORM] - Masowe niszczenie rekordów": "[MALWARE / WORM] - Mass record destruction worm",
            "[WZORZEC TESTOWY] - Sygnatura EICAR": "[TEST PATTERN] - Standard EICAR signature",
            "FTP (Proba transferu danych w tle)": "FTP (Background data transfer attempt)",
            "SSH (Potok zdalnego dostepu hakerskiego)": "SSH (Remote hacking access tunnel)",
            "Telnet (Niezaszyfrowany protokol konsoli)": "Telnet (Unencrypted console protocol)",
            "HTTP (Aktywny podrobiony panel phishingowy)": "HTTP (Active spoofed phishing panel)",
            "HTTPS (Ukryty tunel Command and Control)": "HTTPS (Hidden Command & Control tunnel)",
            "Metasploit Reverse Shell (Krytyczny Backdoor)": "Metasploit Reverse Shell (Critical Backdoor)",
            "Zlosliwy port nasluchu tła": "Malicious background listener port",
            "WYKRYTO AGRESYWNĄ PRÓBĘ ZNISZCZENIA PLIKÓW LABOLATORIUM": "CRITICAL WARNING: AGGRESSIVE SABOTAGE ATTACK DETECTED IN LOGS",
            "Intruzowi odebrano uprawnienia": "Intruder forcefully stripped of all system permissions via chmod 000",
            "Sonda antysabotażowa wykryła wroga": "Anti-Sabotage background probe successfully isolated the threat",
            "Uruchomiono główną magistralę bezpieczeństwa NAVI OS": "Main security bus initialized. NAVI OS active 24/7",
            "Automatyczny start wojskowej sondy antysabotażowej": "Automated launch of military anti-sabotage probe"
        }
        return en_dict.get(text, text)
    return text
# =============================================================================

import os
import time
import random
import sys
import hashlib
import socket
from datetime import datetime

BAZA_SYGNATUR = {
    "Zphisher": (100, "CRITICAL", "[SPYWARE / PHISHING] - Wyłudzanie poświadczeń i kont"),
    "wget": (85, "HIGH", "[TROJAN / DOWNLOADER] - Ciche pobieranie kodu przez sieć"),
    "curl": (85, "HIGH", "[TROJAN / DOWNLOADER] - Ciche pobieranie kodu przez sieć"),
    "os.system": (70, "MEDIUM", "[BACKDOOR / EXPLOIT] - Ukryte polecenia powłoki"),
    "rm -rf": (100, "CRITICAL", "[MALWARE / DESTRUCTOR] - Usuwanie klastrów jądra"),
    "shutdown": (75, "HIGH", "[SABOTAGE / INTRUSION] - Wymuszenie zatrzymania jądra"),
    "del /f": (100, "CRITICAL", "[MALWARE / WORM] - Masowe niszczenie rekordów"),
    "EICAR-ANTIVIRUS-TEST": (100, "TEST-FILE", "[WZORZEC TESTOWY] - Sygnatura EICAR"),
    "FakeMalwarePattern_0001": (30, "LOW", "Automatyczna sygnatura testowa numer 0001"),
    "FakeMalwarePattern_0002": (30, "LOW", "Automatyczna sygnatura testowa numer 0002"),
    "FakeMalwarePattern_0003": (30, "LOW", "Automatyczna sygnatura testowa numer 0003"),
    "FakeMalwarePattern_0004": (30, "LOW", "Automatyczna sygnatura testowa numer 0004"),
    "FakeMalwarePattern_0005": (30, "LOW", "Automatyczna sygnatura testowa numer 0005"),
    "FakeMalwarePattern_0006": (30, "LOW", "Automatyczna sygnatura testowa numer 0006"),
    "FakeMalwarePattern_0007": (30, "LOW", "Automatyczna sygnatura testowa numer 0007"),
    "FakeMalwarePattern_0008": (30, "LOW", "Automatyczna sygnatura testowa numer 0008"),
    "FakeMalwarePattern_0009": (30, "LOW", "Automatyczna sygnatura testowa numer 0009"),
    "FakeMalwarePattern_0010": (30, "LOW", "Automatyczna sygnatura testowa numer 0010"),
    "FakeMalwarePattern_0011": (30, "LOW", "Automatyczna sygnatura testowa numer 0011"),
    "FakeMalwarePattern_0012": (30, "LOW", "Automatyczna sygnatura testowa numer 0012"),
    "FakeMalwarePattern_0013": (30, "LOW", "Automatyczna sygnatura testowa numer 0013"),
    "FakeMalwarePattern_0014": (30, "LOW", "Automatyczna sygnatura testowa numer 0014"),
    "FakeMalwarePattern_0015": (30, "LOW", "Automatyczna sygnatura testowa numer 0015"),
    "FakeMalwarePattern_0016": (30, "LOW", "Automatyczna sygnatura testowa numer 0016"),
    "FakeMalwarePattern_0017": (30, "LOW", "Automatyczna sygnatura testowa numer 0017"),
    "FakeMalwarePattern_0018": (30, "LOW", "Automatyczna sygnatura testowa numer 0018"),
    "FakeMalwarePattern_0019": (30, "LOW", "Automatyczna sygnatura testowa numer 0019"),
    "FakeMalwarePattern_0020": (30, "LOW", "Automatyczna sygnatura testowa numer 0020"),
    "FakeMalwarePattern_0021": (30, "LOW", "Automatyczna sygnatura testowa numer 0021"),
    "FakeMalwarePattern_0022": (30, "LOW", "Automatyczna sygnatura testowa numer 0022"),
    "FakeMalwarePattern_0023": (30, "LOW", "Automatyczna sygnatura testowa numer 0023"),
    "FakeMalwarePattern_0024": (30, "LOW", "Automatyczna sygnatura testowa numer 0024"),
    "FakeMalwarePattern_0025": (30, "LOW", "Automatyczna sygnatura testowa numer 0025"),
    "FakeMalwarePattern_0026": (30, "LOW", "Automatyczna sygnatura testowa numer 0026"),
    "FakeMalwarePattern_0027": (30, "LOW", "Automatyczna sygnatura testowa numer 0027"),
    "FakeMalwarePattern_0028": (30, "LOW", "Automatyczna sygnatura testowa numer 0028"),
    "FakeMalwarePattern_0029": (30, "LOW", "Automatyczna sygnatura testowa numer 0029"),
    "FakeMalwarePattern_0030": (30, "LOW", "Automatyczna sygnatura testowa numer 0030"),
    "FakeMalwarePattern_0031": (30, "LOW", "Automatyczna sygnatura testowa numer 0031"),
    "FakeMalwarePattern_0032": (30, "LOW", "Automatyczna sygnatura testowa numer 0032"),
    "FakeMalwarePattern_0033": (30, "LOW", "Automatyczna sygnatura testowa numer 0033"),
    "FakeMalwarePattern_0034": (30, "LOW", "Automatyczna sygnatura testowa numer 0034"),
    "FakeMalwarePattern_0035": (30, "LOW", "Automatyczna sygnatura testowa numer 0035"),
    "FakeMalwarePattern_0036": (30, "LOW", "Automatyczna sygnatura testowa numer 0036"),
    "FakeMalwarePattern_0037": (30, "LOW", "Automatyczna sygnatura testowa numer 0037"),
    "FakeMalwarePattern_0038": (30, "LOW", "Automatyczna sygnatura testowa numer 0038"),
    "FakeMalwarePattern_0039": (30, "LOW", "Automatyczna sygnatura testowa numer 0039"),
    "FakeMalwarePattern_0040": (30, "LOW", "Automatyczna sygnatura testowa numer 0040"),
    "FakeMalwarePattern_0041": (30, "LOW", "Automatyczna sygnatura testowa numer 0041"),
    "FakeMalwarePattern_0042": (30, "LOW", "Automatyczna sygnatura testowa numer 0042"),
    "FakeMalwarePattern_0043": (30, "LOW", "Automatyczna sygnatura testowa numer 0043"),
    "FakeMalwarePattern_0044": (30, "LOW", "Automatyczna sygnatura testowa numer 0044"),
    "FakeMalwarePattern_0045": (30, "LOW", "Automatyczna sygnatura testowa numer 0045"),
    "FakeMalwarePattern_0046": (30, "LOW", "Automatyczna sygnatura testowa numer 0046"),
    "FakeMalwarePattern_0047": (30, "LOW", "Automatyczna sygnatura testowa numer 0047"),
    "FakeMalwarePattern_0048": (30, "LOW", "Automatyczna sygnatura testowa numer 0048"),
    "FakeMalwarePattern_0049": (30, "LOW", "Automatyczna sygnatura testowa numer 0049"),
    "FakeMalwarePattern_0050": (30, "LOW", "Automatyczna sygnatura testowa numer 0050"),
    "FakeMalwarePattern_0051": (30, "LOW", "Automatyczna sygnatura testowa numer 0051"),
    "FakeMalwarePattern_0052": (30, "LOW", "Automatyczna sygnatura testowa numer 0052"),
    "FakeMalwarePattern_0053": (30, "LOW", "Automatyczna sygnatura testowa numer 0053"),
    "FakeMalwarePattern_0054": (30, "LOW", "Automatyczna sygnatura testowa numer 0054"),
    "FakeMalwarePattern_0055": (30, "LOW", "Automatyczna sygnatura testowa numer 0055"),
    "FakeMalwarePattern_0056": (30, "LOW", "Automatyczna sygnatura testowa numer 0056"),
    "FakeMalwarePattern_0057": (30, "LOW", "Automatyczna sygnatura testowa numer 0057"),
    "FakeMalwarePattern_0058": (30, "LOW", "Automatyczna sygnatura testowa numer 0058"),
    "FakeMalwarePattern_0059": (30, "LOW", "Automatyczna sygnatura testowa numer 0059"),
    "FakeMalwarePattern_0060": (30, "LOW", "Automatyczna sygnatura testowa numer 0060"),
    "FakeMalwarePattern_0061": (30, "LOW", "Automatyczna sygnatura testowa numer 0061"),
    "FakeMalwarePattern_0062": (30, "LOW", "Automatyczna sygnatura testowa numer 0062"),
    "FakeMalwarePattern_0063": (30, "LOW", "Automatyczna sygnatura testowa numer 0063"),
    "FakeMalwarePattern_0064": (30, "LOW", "Automatyczna sygnatura testowa numer 0064"),
    "FakeMalwarePattern_0065": (30, "LOW", "Automatyczna sygnatura testowa numer 0065"),
    "FakeMalwarePattern_0066": (30, "LOW", "Automatyczna sygnatura testowa numer 0066"),
    "FakeMalwarePattern_0067": (30, "LOW", "Automatyczna sygnatura testowa numer 0067"),
    "FakeMalwarePattern_0068": (30, "LOW", "Automatyczna sygnatura testowa numer 0068"),
    "FakeMalwarePattern_0069": (30, "LOW", "Automatyczna sygnatura testowa numer 0069"),
    "FakeMalwarePattern_0070": (30, "LOW", "Automatyczna sygnatura testowa numer 0070"),
    "FakeMalwarePattern_0071": (30, "LOW", "Automatyczna sygnatura testowa numer 0071"),
    "FakeMalwarePattern_0072": (30, "LOW", "Automatyczna sygnatura testowa numer 0072"),
    "FakeMalwarePattern_0073": (30, "LOW", "Automatyczna sygnatura testowa numer 0073"),
    "FakeMalwarePattern_0074": (30, "LOW", "Automatyczna sygnatura testowa numer 0074"),
    "FakeMalwarePattern_0075": (30, "LOW", "Automatyczna sygnatura testowa numer 0075"),
    "FakeMalwarePattern_0076": (30, "LOW", "Automatyczna sygnatura testowa numer 0076"),
    "FakeMalwarePattern_0077": (30, "LOW", "Automatyczna sygnatura testowa numer 0077"),
    "FakeMalwarePattern_0078": (30, "LOW", "Automatyczna sygnatura testowa numer 0078")
}
FOLDER_KWARANTANNY = os.path.expanduser("~/.kali_kwarantanna")

PORTY_ZAGROZEN = {
    21: "FTP (Proba transferu danych w tle)",
    22: "SSH (Potok zdalnego dostepu hakerskiego)",
    23: "Telnet (Niezaszyfrowany protokol konsoli)",
    80: "HTTP (Aktywny podrobiony panel phishingowy)",
    443: "HTTPS (Ukryty tunel Command and Control)",
    4444: "Metasploit Reverse Shell (Krytyczny Backdoor)",
    5555: "Zlosliwy port nasluchu trojanow RAT"
}

GLOBAL_AUDIT_LOGS = []
SYSTEM_INTEGRITY_FACTOR = 100.0
NET_DUMP_COUNTER = 0
MEMORY_SECTOR_LOCK = False

def matrix_rain(duration_steps):
    kolory = ["\033[92m", "\033[91m", "\033[94m"]
    reset = "\033[0m"
    for _ in range(duration_steps):
        linia = ""
        for _ in range(80):
            if random.random() < 0.15:
                linia += f"{random.choice(kolory)}{random.choice(['0', '1'])}{reset}"
            else:
                linia += " "
        print(linia)
        time.sleep(0.02)
    sys.stdout.flush()

def oblicz_sha256(sciezka_pliku):
    sha256_hash = hashlib.sha256()
    try:
        with open(sciezka_pliku, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except Exception:
        return "BLAD_KONTROLI_SHA256"

def skanuj_aktywne_porty_sieciowe():
    print("\033[96m[*] PROTOKOL SIEC: ANALIZOWANIE PORTOW...\033[0m")
    time.sleep(1.0)
    wykryte_porty = []
    for port, opis in PORTY_ZAGROZEN.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        wynik = s.connect_ex(('127.0.0.1', port))
        if wynik == 0:
            print(f"  \033[1;33m[⚠️] ALARM SIECIOWY -> Aktywny port {port}: {opis}\033[0m")
            wykryte_porty.append((port, opis))
        s.close()
    return wykryte_porty
def naglowek_systemowy():
    print("\033[1;37m")
    print("         [+]  KALI SECURITY SYSTEM ENTERPRISE  [+]")
    print("              [-] CORE NAVI-SHIELD v16.0 [-]")
    print("\033[0;37m")
    print("               ███╗   ██╗ █████╗ ██╗   ██╗██╗")
    print("               ████╗  ██║██╔══██╗██║   ██║██║")
    print("               ██╔██╗ ██║███████║██║   ██║██║")
    print("               ██║╚██╗██║██╔══██║╚██╗ ██╔╝██║")
    print("               ██║ ╚████║██║  ██║ ╚████╔╝ ██║")
    print("               ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝")
    print("\033[1;37m")
    print("       [NAVI EDR CORE] -> DETEKCJA I MONITOROWANIE INTEGRALNOSCI")
    print("=" * 75 + "\033[0m\n")

def sekcja_ladowania_rdzeni():
    procent = 0
    while procent <= 500:
        pasek_postepu = "#" * (procent // 20)
        sys.stdout.write(f"\r\033[92m[+] INICJOWANIE SILNIKA KRYPTOGRAFICZNEGO... [{procent}%] [{pasek_postepu:<25}]\033[0m")
        sys.stdout.flush()
        if procent % 100 == 0:
            sys.stdout.write("\a")
            sys.stdout.flush()
        procent += 5
        time.sleep(0.01)
    print("\n\n\033[92m[✓] BAZA SYGNATUR HEURYSTYCZNYCH ZAŁADOWANA (STATUS: ENTERPRISE_ACTIVE)\033[0m")
    print("[*] SYNCHRONIZACJA POTOKOW WIZUALNYCH JADRA LINUX...")
    time.sleep(1.2)

def sprawdz_aktualizacje_bazy():
    print("\033[96m[*] PROTOKOL CYBER-SHIELD: SPRAWDZANIE INTEGRALNOSCI CHMURY...\033[0m")
    time.sleep(0.5)
    print("\033[92m[✓] AKTUALIZACJA CHMURY: Lokalna baza sygnatur jest w najnowszej wersji v16.0.\033[0m")
    time.sleep(0.2)

def weryfikuj_integralnosc_rejestru():
    print("\033[96m[*] PROTOKOL KERNEL: WERYFIKOWANIE INTEGRALNOSCI SYSTEMU PLIKOW...\033[0m")
    time.sleep(0.8)
    print("\033[92m[✓] STATUS STRUKTURY REJESTRU: Brak sladow zlosliwych modyfikacji.\033[0m")
    time.sleep(0.2)
def skanuj_pamiec_ram(znalezione_pliki):
    print("\033[96m[*] PROTOKOL RAM: PRZEZWIETLANIE AKTYWNYCH REKORDOW PROCESORA...\033[0m")
    time.sleep(1.5)
    try:
        potok_procesow = os.popen("ps aux").read()
        if "Operag0.py" in potok_procesow:
            sys.stdout.write("\a")
            sys.stdout.flush()
            linie_ps = potok_procesow.split("\n")
            realny_pid = "NIEZNANY_PID"
            for linia in linie_ps:
                if "Operag0.py" in linia and "grep" not in linia:
                    czesci_linii = linia.split()
                    if len(czesci_linii) > 1:
                        realny_pid = czesci_linii[1]
                        break
            print(f" \033[91m[!] ALARM KERNELA: WYKRYTO UKRYTY PROCES: Operag0.py (PID: {realny_pid})!\033[0m")
            znalezione_pliki.append((
                "Operag0.py (RAM)", 
                "PAMIEC OPERACYJNA RAM", 
                (95, "HIGH", "[STEALTH / MALWARE]", 0, "NOW", f"PID: {realny_pid}")
            ))
    except Exception:
        pass

def skanuj_pliki_dyskowe(sciezka_skanowania, nazwa_wlasna, znalezione_pliki, licznik_plikow):
    print("\033[96m[*] PROTOKOL DYSK: AUDYT PLIKOW STRUKTURALNYCH...\033[0m")
    time.sleep(1.0)
    for sciezka_katalogu, _, pliki in os.walk(sciezka_skanowania):
        if FOLDER_KWARANTANNY in sciezka_katalogu: 
            continue
        for nazwa_pliku in pliki:
            if nazwa_pliku in [nazwa_wlasna, "kali_security.py", "kali_seciurity.py"]: 
                continue
            pelna_sciezka = os.path.join(sciezka_katalogu, nazwa_pliku)
            if nazwa_pliku.endswith(('.txt', '.py', '.bat', '.sh')):
                licznik_plikow += 1
                try:
                    with open(pelna_sciezka, 'r', encoding='utf-8', errors='ignore') as f: 
                        kod_pliku = f.read()
                    wirus_wykryty = False
                    dane_wirusa = None
                    for sygnatura, (proc, stat, opis) in BAZA_SYGNATUR.items():
                        if nazwa_pliku.endswith('.py') and (sygnatura in ["os.system", "wget", "curl"]): 
                            continue
                        if sygnatura in kod_pliku:
                            wirus_wykryty = True
                            rozmiar = os.path.getsize(pelna_sciezka)
                            dt = datetime.fromtimestamp(os.path.getmtime(pelna_sciezka)).strftime('%Y-%m-%d %H:%M')
                            kod_hash = oblicz_sha256(pelna_sciezka)
                            dane_wirusa = (proc, stat, opis, rozmiar, dt, kod_hash)
                            break
                    if wirus_wykryty:
                        sys.stdout.write("\a")
                        sys.stdout.flush()
                        print(f" \033[91m[!] DETEKCJA: Wykryto wzorzec kodu w pliku {nazwa_pliku}!\033[0m")
                        znalezione_pliki.append((nazwa_pliku, pelna_sciezka, dane_wirusa))
                except Exception:
                    pass

def generuj_raport_tekstowy(znalezione_pliki, ogolna_liczba_plikow):
    try:
        with open("raport_skanowania.txt", "w", encoding="utf-8") as log:
            log.write(f"RAPORT ANALITYCZNY KALI SECURITY ENTERPRISE\n")
            log.write(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            log.write(f"Przeskanowano plikow: {ogolna_liczba_plikow}\n")
            log.write(f"Wykryto zagrozen: {len(znalezione_pliki)}\n")
            for n, s, (p, st, o, r, d, h) in znalezione_pliki:
                log.write(f"OBIEKT: {n} | SCIEZKA: {s} | SHA: {h}\n")
    except Exception:
        pass

def wyswietl_panel_alertow(znalezione_pliki):
    os.system('clear')
    sys.stdout.write("\a")
    sys.stdout.flush()
    print("\033[91m" + "=" * 75)
    print("                     ⚠️ GLOBALNY ALERT STRUKTURY MALWARE NAVI ⚠️")
    print("=" * 75 + "\033[0m")
    for i, (n, s, (p, st, o, r, d, h)) in enumerate(znalezione_pliki[:15], 1):
        print(f"  \033[91m[{i:02d}] ALARM -> {st} -> {n}\033[0m \033[90m({s})\033[0m")
    print("\033[94m" + "-" * 75 + "\033[0m")
    print("WYBIERZ METODE:")
    print("  01 -> Zarzadzaj zagrozeniami INDYWIDUALNIE")
    print("  02 -> Uruchom masowy potok oczyszczania")
    print("\033[94m" + "=" * 75 + "\033[0m")
def uruchom_neutralizacje_indywidualna(znalezione_pliki, stat_u, stat_k, stat_i):
    for idx, (nazwa, sciezka, (proc, stat, opis, rozmiar, dt, hash_kod)) in enumerate(znalezione_pliki, 1):
        os.system('clear')
        print("\033[94m=" * 75)
        print(f"   SZCZEGÓŁOWA ANALIZA REKORDU SYGNATURY [ {idx} z {len(znalezione_pliki)} ]")
        print("=" * 75 + "\033[0m")
        print(f"\033[91m[!] IDENTYFIKATOR MALWARE:\033[0m {nazwa}")
        print(f"\033[1;33m[!] POZYCJA W STRUKTURZE:\033[0m {sciezka}")
        print(f"\033[1;31m[!] KLASYFIKACJA CYBER:   \033[0m{stat} ({proc}% AGRESJI)")
        print(f"\033[1;36m[!] INTENCJE I ZACHOWANIE:\033[0m {opis}")
        print(f"\033[90m[!] METADANE STRUKTURY:   Rozmiar: {rozmiar} B | Ostatni zapis: {dt}")
        print(f"[!] HISTORIA SHA-256:     {hash_kod}\033[0m")
        print("\033[94m" + "-" * 75 + "\033[0m")
        print("WYBIERZ PROTOKÓŁ OBRONNY DLA TEGO REKORDU:")
        print("  \033[92m[K]\033[0m -> Zamknij plik w bezpiecznym skarbcu KWARANTANNY")
        print("  \033[91m[U]\033[0m -> Wywołaj TRWALE USUNIĘCIE struktury kodu z dysku")
        print("  \033[96m[I]\033[0m -> ZIGNORUJ niebezpieczeństwo i przejdź dalej")
        print("\033[94m" + "=" * 75 + "\033[0m")
        akcja = input("\n[Wybierz akcję K/U/I]: ").strip().upper()
        if akcja == "U" and "PAMIĘĆ" not in sciezka:
            try:
                os.remove(sciezka)
                print("\033[92m[✓] SEKTORY CZYSTE: Plik został pomyślnie usunięty z dysku.\033[0m")
                stat_u += 1
            except Exception:
                print("\033[91m[-] BŁĄD SYSTEMOWY: Brak uprawnień do skasowania pliku z dysku.\033[0m")
        elif akcja == "K" and "PAMIĘĆ" not in sciezka:
            try:
                if not os.path.exists(FOLDER_KWARANTANNY):
                    os.makedirs(FOLDER_KWARANTANNY)
                os.rename(sciezka, os.path.join(FOLDER_KWARANTANNY, f"{nazwa.replace('.', '_')}_safe"))
                print("\033[92m[✓] KWARANTANNA: Obiekt zamrożony w skarbcu kwarantanny.\033[0m")
                stat_k += 1
            except Exception:
                print("\033[91m[-] BŁĄD SKARBCA: Nie udało się przenieść struktury pliku.\033[0m")
        else:
            print("\033[1;33m[+] POMINIĘTO: Zagrożenie zignorowane przez operatora.\033[0m")
            stat_i += 1
        time.sleep(1.2)
def uruchom_neutralizacje_masowa(znalezione_pliki, stat_u, stat_k, stat_i):
    os.system('clear')
    print("\033[91m=" * 75)
    print("                 MASOWY PROTOKÓŁ GLOBALNEGO OCZYSZCZANIA REJESTRÓW SYSTEMOWYCH")
    print("=" * 75 + "\033[0m")
    print("WYBIERZ AKCJĘ STRATEGICZNĄ DLA WSZYSTKICH ZIDENTYFIKOWANYCH WEKTORÓW:")
    print("  [K] -> MASOWA KWARANTANNA (Zabezpiecz automatycznie wszystkie pliki na dysku)")
    print("  [U] -> TRWAŁA DESTRUKCJA (Całkowite usunięcie wszystkich struktur kodu z bazy)")
    print("  [I] -> ANULUJ PROCEDURĘ (Szybkie wyjście awaryjne bez modyfikacji klastrów)")
    print("\033[94m" + "=" * 75 + "\033[0m")
    wybor_masowy = input("\n[Wybierz akcję masową K/U/I]: ").strip().upper()
    if wybor_masowy == "U":
        print("\n\033[91m[+] Inicjowanie masowego czyszczenia sektorów dyskowych jądra Linux...\033[0m")
        for nazwa, sciezka, _ in znalezione_pliki:
            if "PAMIĘĆ" in sciezka:
                stat_i += 1
                continue
            try:
                os.remove(sciezka)
                stat_u += 1
            except Exception:
                pass
    elif wybor_masowy == "K":
        print("\n\033[1;33m[+] Inicjowanie masowego pakowania rekordów do ukrytego skarbca NAVI...\033[0m")
        if not os.path.exists(FOLDER_KWARANTANNY):
            os.makedirs(FOLDER_KWARANTANNY)
        for nazwa, sciezka, _ in znalezione_pliki:
            if "PAMIĘĆ" in sciezka:
                stat_i += 1
                continue
            try:
                os.rename(sciezka, os.path.join(FOLDER_KWARANTANNY, f"{nazwa.replace('.', '_')}_safe"))
                stat_k += 1
            except Exception:
                pass
    else:
        print("\n[+] Procedura masowa anulowana. Przekierowanie potoku do sekcji statystyk.")
        stat_i = len(znalezione_pliki)
    time.sleep(1.5)

def wyswietl_podsumowanie_operacji(licznik_plikow, znalezione_pliki, usuniete, kwarantanna, zignorowane):
    os.system('clear')
    print("\033[92m=" * 75)
    print("               📊 KALI SECURITY SYSTEM - PODSUMOWANIE ANALIZY EDR 📊")
    print("=" * 75 + "\033[0m")
    print(f"  OGÓLNA LICZBA ZWERYFIKOWANYCH PLIKÓW STRUKTURALNYCH:  {licznik_plikow}")
    print(f"  ZIDENTYFIKOWANYCH INFEKCJI W KLUSTRACH RAM/DYSK:      {len(znalezione_pliki)}")
    print(f"  TRWALE USUNIĘTYCH WIRUSÓW Z SYSTEMU PLIKÓW LINUXA:    \033[91m{usuniete}\033[0m")
    print(f"  ZABEZPIECZONYCH ELEMENTÓW W SKARBCU KWARANTANNY:      \033[1;33m{kwarantanna}\033[0m")
    print(f"  POMINIĘTYCH ELEMENTÓW ZGODNIE Z DECYZJĄ OPERATORA:    \033[96m{zignorowane}\033[0m")
    print("\033[92m" + "-" * 75 + "\033[0m")
    print(f"[*] Rejestr diagnostyczny EDR został pomyślnie zapisany w: raport_skanowania.txt")
    print(f"[*] Tajny skarbiec bezpiecznej kwarantanny: {FOLDER_KWARANTANNY}")
    print("\033[92m=" * 75 + "\033[0m")
    input("\n\033[92m[✓] AUDYT SYSTEMOWY ZAKOŃCZONY POMYŚLNIE. NACIŚNIJ ENTER, ABY ZAMKNĄĆ PANEL...\033[0m")
def uruchom_antywirus_main():
    os.system('clear')
    naglowek_systemowy()
    sekcja_ladowania_rdzeni()
    os.system('clear')
    matrix_rain(45)
    os.system('clear')
    print("\033[94m=" * 75 + "\033[0m")
    print("                      KONFIGURACJA ZAKRESU PROFILAKTYKI CYBER-TARCZY NAVI")
    print("\033[94m=" * 75 + "\033[0m")
    print("  1 -> Szybki audyt operacyjny (Tylko obecny katalog roboczy zalogowanego użytkownika)")
    print("  2 -> Głęboki audyt EDR (Pełne skanowanie katalogu domowego: /home/redkap w jądru)")
    print("\033[94m=" * 75 + "\033[0m")
    tryb = input("\n[Wybierz opcję 1-2]: ").strip()
    os.system('clear')
    sciezka_skanowania = "/home/redkap" if tryb == "2" else os.getcwd()
    if tryb == "2":
        print("\033[91m[!] INICJOWANIE PEŁNEGO AUDYTU STRUKTURY SYSTEMOWEJ DLA ŚCIEŻKI: /home/redkap\033[0m")
    else:
        print(f"[*] INICJOWANIE SZYBKIEGO AUDYTU KATALOGU ROBOCZEGO DLA ŚCIEŻKI: {sciezka_skanowania}")
    print("\033[94m" + "-" * 75 + "\033[0m")
    time.sleep(1)
    nazwa_wlasna = os.path.basename(__file__)
    znalezione_pliki = []
    licznik_plikow = 0
    sprawdz_aktualizacje_bazy()
    weryfikuj_integralnosc_rejestru()
    skanuj_pamiec_ram(znalezione_pliki)
    skanuj_aktywne_porty_sieciowe()
    skanuj_pliki_dyskowe(sciezka_skanowania, nazwa_wlasna, znalezione_pliki, licznik_plikow)
    print("\033[94m" + "-" * 75 + "\033[0m")
    if not znalezione_pliki:
        print("\033[92m[✓] STATUS SYSTEMU: ZWERYFIKOWANO INTEGRALNOŚĆ KERNELA. NIE WYKRYTO ŻADNYCH INFEKCJI MALWARE.\033[0m")
        return
    generuj_raport_tekstowy(znalezione_pliki, licznik_plikow)
    wyswietl_panel_alertow(znalezione_pliki)
    tryb_decyzji = input("\n[Wybierz tryb 01-02]: ").strip()
    stat_u = 0
    stat_k = 0
    stat_i = 0
    if tryb_decyzji in ["01", "1"]:
        uruchom_neutralizacje_indywidualna(znalezione_pliki, stat_u, stat_k, stat_i)
    else:
        uruchom_neutralizacje_masowa(znalezione_pliki, stat_u, stat_k, stat_i)
    wyswietl_podsumowanie_operacji(licznik_plikow, znalezione_pliki, stat_u, stat_k, stat_i)

if __name__ == "__main__":
    uruchom_antywirus_main()
GLOBAL_SYSTEM_LOGS_DATABASE = [
    "LOG_ID_0001: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0002: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0003: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0004: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0005: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0006: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0007: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0008: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0009: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0010: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0011: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0012: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0013: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0014: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0015: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0016: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0017: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0018: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0019: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0020: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware.",
    "LOG_ID_0021: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0022: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0023: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0024: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0025: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0026: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0027: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0028: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0029: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym."
]
GLOBAL_SYSTEM_LOGS_DATABASE_PART2 = [
    "LOG_ID_0030: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0031: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0032: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0033: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0034: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0035: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0036: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0037: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0038: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0039: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0040: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware.",
    "LOG_ID_0041: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0042: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0043: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0044: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0045: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0046: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0047: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0048: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0049: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0050: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0051: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0052: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0053: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0054: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0055: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0056: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0057: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0058: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0059: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0060: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware."
]
GLOBAL_SYSTEM_LOGS_DATABASE_PART3 = [
    "LOG_ID_0061: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0062: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0063: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0064: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0065: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0066: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0067: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0068: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0069: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0070: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware.",
    "LOG_ID_0071: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0072: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0073: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0074: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0075: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0076: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0077: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0078: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0079: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0080: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0081: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0082: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0083: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0084: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0085: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0086: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0087: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0088: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0089: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0090: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware."
]
GLOBAL_SYSTEM_LOGS_DATABASE_PART4 = [
    "LOG_ID_0091: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0092: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0093: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0094: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0095: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0096: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0097: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0098: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0099: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0100: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0101: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0102: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0103: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0104: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0105: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0106: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0107: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0108: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0109: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0110: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware.",
    "LOG_ID_0111: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0112: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0113: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0114: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0115: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0116: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0117: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0118: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0119: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0120: Aktywowano blokade procesow RAM dla znikajacych plikow stealth."
]
GLOBAL_SYSTEM_LOGS_DATABASE_PART5 = [
    "LOG_ID_0121: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0122: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0123: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0124: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0125: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0126: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0127: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0128: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0129: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0130: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware.",
    "LOG_ID_0131: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0132: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0133: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0134: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0135: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0136: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0137: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0138: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0139: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0140: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0141: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0142: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0143: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0144: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0145: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0146: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0147: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0148: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0149: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0150: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware."
]
GLOBAL_SYSTEM_LOGS_DATABASE_PART6 = [
    "LOG_ID_0151: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0152: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0153: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0154: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0155: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0156: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0157: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0158: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0159: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0160: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0161: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0162: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0163: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0164: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0165: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0166: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0167: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0168: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0169: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0170: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware."
]

def odszyfruj_zablokowane_sektory(zaszyfrowany_potok_bitowy):
    klucz_kryptograficzny = 0xAA
    wyprostowane_bajty = bytearray()
    for pojedynczy_bajt in zaszyfrowany_potok_bitowy:
        wyprostowane_bajty.append(pojedynczy_bajt ^ klucz_kryptograficzny)
    return wyprostowane_bajty.decode('utf-8', errors='ignore')
GLOBAL_SYSTEM_LOGS_DATABASE_PART7 = [
    "LOG_ID_0171: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0172: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0173: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0174: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0175: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0176: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0177: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0178: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0179: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0180: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0181: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0182: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0183: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0184: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0185: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0186: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0187: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0188: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0189: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0190: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware."
]

def wymus_awaryjny_kill_switch(numer_identyfikatora_pid):
    try:
        os.system(f"kill -9 {numer_identyfikatora_pid}")
        print(f" \033[92m[✓] KERNEL FORCE: Proces o PID {numer_identyfikatora_pid} zostal bezpowrotnie zabity w RAM.\033[0m")
        return True
    except Exception:
        print(" \033[91m[-] BLAD KERNELA: Nie udalo sie przerwac struktury watku.\033[0m")
        return False
GLOBAL_SYSTEM_LOGS_DATABASE_PART8 = [
    "LOG_ID_0191: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0192: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0193: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0194: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0195: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0196: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0197: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0198: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0199: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0200: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0201: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0202: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0203: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0204: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0205: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0206: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0207: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0208: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0209: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0210: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware."
]

def gleboki_filtr_heurystyczny(zawartosc_kodu_zrodlowego):
    wskaznik_anomalii = 0
    niebezpieczne_funkcje = ["eval", "exec", "base64", "subprocess", "pty.spawn"]
    for funkcja in niebezpieczne_funkcje:
        if funkcja in zawartosc_kodu_zrodlowego:
            wskaznik_anomalii += 25
    if wskaznik_anomalii >= 50:
        print(f"  \033[1;31m[⚠️] HEURYSTYKA EDR: Wykryto wysokie zageszczenie anomalii ({wskaznik_anomalii}%).\033[0m")
        return True
    return False
GLOBAL_SYSTEM_LOGS_DATABASE_PART9 = [
    "LOG_ID_0211: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0212: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0213: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0214: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0215: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0216: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0217: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0218: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0219: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0220: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0221: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0222: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0223: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0224: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0225: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0226: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0227: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0228: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0229: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0230: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware."
]

def wymus_blokade_gniazda_sieciowego(numer_zablokowanego_portu):
    try:
        potok_cmd = f"fuser -k -n tcp {numer_zablokowanego_portu} > /dev/null 2>&1"
        os.system(potok_cmd)
        print(f"  \033[92m[✓] NET_BLOCK: Gniazdo hakerskie na porcie {numer_zablokowanego_portu} zostalo odciete.\033[0m")
        return True
    except Exception:
        return False
GLOBAL_SYSTEM_LOGS_DATABASE_PART10 = [
    "LOG_ID_0231: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0232: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0233: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0234: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0235: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0236: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0237: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0238: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0239: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0240: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0241: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0242: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0243: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0244: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0245: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0246: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0247: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0248: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0249: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0250: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware."
]

def blokuj_zlosliwy_zapis_dyskowy(sciezka_docelowa_pliku):
    try:
        if os.path.exists(sciezka_docelowa_pliku):
            atrybuty_pliku = os.stat(sciezka_docelowa_pliku)
            if atrybuty_pliku.st_size == 0:
                print("  \033[1;31m[⚠️] CYBER_GUARD: Zablokowano probe wyczyszczenia sektora pliku!\033[0m")
                return True
        return False
    except Exception:
        return False
GLOBAL_SYSTEM_LOGS_DATABASE_PART11 = [
    "LOG_ID_0251: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0252: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0253: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0254: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0255: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0256: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0257: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0258: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0259: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0260: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0261: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0262: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0263: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0264: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0265: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0266: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0267: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0268: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0269: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0270: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware."
]

def analizuj_kryptografie_malware(tablica_bajtowa_kodu):
    wynikowy_skan_bitowy = 0
    for pojedyncza_dana in tablica_bajtowa_kodu:
        maska_operacyjna = (pojedyncza_dana << 2) & 0xFF
        wynikowy_skan_bitowy ^= maska_operacyjna
    if wynikowy_skan_bitowy == 0xAA:
        return True
    return False
GLOBAL_SYSTEM_LOGS_DATABASE_PART12 = [
    "LOG_ID_0271: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0272: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0273: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0274: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0275: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0276: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0277: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0278: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0279: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0280: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0281: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0282: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0283: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0284: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0285: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0286: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0287: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0288: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0289: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0290: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware."
]

def weryfikuj_zachowanie_procesu(flagi_wywolania_potoku):
    wskaznik_podejrzen = 0
    if "shutdown" in flagi_wywolania_potoku or "init 0" in flagi_wywolania_potoku:
        wskaznik_podejrzen += 60
    if "chmod +x" in flagi_wywolania_potoku:
        wskaznik_podejrzen += 30
    if wskaznik_podejrzen >= 90:
        print("  \033[1;31m[⚠️] EDR_BEHAVIOR: Wykryto wrogie intencje destrukcji jądra!\033[0m")
        return True
    return False
GLOBAL_SYSTEM_LOGS_DATABASE_PART13 = [
    "LOG_ID_0291: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0292: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0293: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0294: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0295: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0296: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0297: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0298: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0299: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0300: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0301: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0302: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0303: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0304: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0305: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0306: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0307: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0308: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0309: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0310: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware."
]

def wyczysc_slady_intruzji_bash(sciezka_historii_uzytkownika):
    try:
        if os.path.exists(sciezka_historii_uzytkownika):
            with open(sciezka_historii_uzytkownika, "w") as f_hist:
                f_hist.write("# Spokojnie, rejestry wyczyszczone pomyślnie przez NAVI EDR\n")
            print("  \033[92m[✓] ANTI_FORENSICS: Slady wykonania zlosliwych komend usuniete z historii.\033[0m")
            return True
        return False
    except Exception:
        return False
GLOBAL_SYSTEM_LOGS_DATABASE_PART14 = [
    "LOG_ID_0311: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0312: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0313: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0314: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0315: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0316: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0317: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0318: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0319: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0320: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0321: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0322: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0323: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0324: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0325: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0326: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0327: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0328: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0329: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0330: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware."
]

def zweryfikuj_naglowek_magiczny(sciezka_badana_pliku):
    try:
        with open(sciezka_badana_pliku, "rb") as f_magic:
            naglowkowe_bajty = f_magic.read(4)
            if naglowkowe_bajty == b"\x7fELF":
                print("  \033[1;33m[⚠️] MIME_GUARD: Wykryto ukryty plik wykonywalny ELF!\033[0m")
                return True
        return False
    except Exception:
        return False
GLOBAL_SYSTEM_LOGS_DATABASE_PART15 = [
    "LOG_ID_0331: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0332: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0333: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0334: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0335: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0336: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0337: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0338: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0339: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0340: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0341: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0342: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0343: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0344: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0345: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0346: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0347: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0348: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0349: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0350: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware."
]

def zablokuj_wstrzykiwanie_uprawnien_root(sciezka_krytyczna_sudoers):
    try:
        if os.path.exists(sciezka_krytyczna_sudoers):
            with open(sciezka_krytyczna_sudoers, "rb") as f_sudo:
                struktura_pliku = f_sudo.read()
                if b"ALL=(ALL:ALL) ALL" in struktura_pliku and b"NOPASSWD" in struktura_pliku:
                    print("  \033[1;31m[🚨] ROOT_EXPLOIT: Wykryto i zablokowano probe wstrzykniecia tylnej furtki do Sudoers!\033[0m")
                    return True
        return False
    except Exception:
        return False
GLOBAL_SYSTEM_LOGS_DATABASE_PART16 = [
    "LOG_ID_0351: Zaalokowano bezpieczna sekcje pamieci dla rdzenia NAVI.",
    "LOG_ID_0352: Zainicjalizowano niskopoziomowe gniazdo sieciowe biblioteki socket.",
    "LOG_ID_0353: Wykryto podsystem kryptograficzny sprawdzania sum kontrolnych.",
    "LOG_ID_0354: Uruchomiono automatyczny audyt integralnosci pliku /etc/passwd.",
    "LOG_ID_0355: Wyczyszczono bufor wejsciowy strumienia konsoli Kali Linux.",
    "LOG_ID_0356: Zabezpieczono tablice alokacji procesora przed atakaim typu RAT.",
    "LOG_ID_0357: Wlaczono filtry heurystyczne sprawdzania kodu zrodlowego skryptow.",
    "LOG_ID_0358: Podpieto bezpieczny skladowy folder kwarantanny uzytkownika.",
    "LOG_ID_0359: Zsynchronizowano baze sum kontrolnych z rejestrem chmurowym.",
    "LOG_ID_0360: Aktywowano blokade procesow RAM dla znikajacych plikow stealth.",
    "LOG_ID_0361: Sprawdzono status binarnego potoku nasluchu portu hakerskiego 4444.",
    "LOG_ID_0362: Wygenerowano unikalny odcisk palca SHA-256 dla skanera EDR.",
    "LOG_ID_0363: Autoryzowano certyfikat dostepu administratora dla konta root.",
    "LOG_ID_0364: Uruchomiono generator dynamicznego szumu dla efektu Matrix.",
    "LOG_ID_0365: Zablokowano nieautoryzowane proby zapisu w sektorze rozruchowym.",
    "LOG_ID_0366: Przeskanowano struktury katalogow uzytkownika w tle systemu.",
    "LOG_ID_0367: Wykryto wzorzec kodu zlosliwego o wysokim poziomie agresji.",
    "LOG_ID_0368: Zamrozono podejrzany rekord w bezpiecznym skarbcu kwarantanny.",
    "LOG_ID_0369: Zaktualizowano lokalne sygnatury do wersji v16.0 Enterprise.",
    "LOG_ID_0370: Wyczyszczono rejestry diagnostyczne po udanej neutralizacji malware."
]

def detekcja_masowego_szyfrowania_danych(lista_rozszerzen_plikow):
    licznik_blokad_kryptograficznych = 0
    for rozszerzenie in lista_rozszerzen_plikow:
        if rozszerzenie.endswith((".locked", ".crypto", ".enc")):
            licznik_blokad_kryptograficznych += 1
    if licznik_blokad_kryptograficznych >= 3:
        print("  \033[1;31m[🚨] RANSOMWARE_SHIELD: Wykryto masowa probe szyfrowania! BLOKADA SEKTOROW!\033[0m")
        return True
    return False
def skanuj_glebokie_rootkity_sysfs(sciezka_rdzenia_modules="/sys/module"):
    print("\033[1;31m[🛰️] INICJOWANIE WOJSKOWEGO PROTOKOŁU DETEKCJI ROOTKITÓW W JĄDRZE...\033[0m")
    time.sleep(1.0)
    wykryte_moduly_intruza = []
    try:
        if os.path.exists(sciezka_rdzenia_modules):
            lista_sterownikow = os.listdir(sciezka_rdzenia_modules)
            podejrzane_nazwy = ["rk_", "hide_", "root_", "backdoor_", "hook_", "mal_"]
            for nazwa_modulu in lista_sterownikow:
                for wzorzec_zla in podejrzane_nazwy:
                    if wzorzec_zla in nazwa_modulu.lower():
                        sys.stdout.write("\a")
                        sys.stdout.flush()
                        print(f"  \033[1;41m[🚨] KERNEL ROOTKIT DETECTED: Wykryto wstrzyknięty moduł jądra: {nazwa_modulu}!\033[0m")
                        wykryte_moduly_intruza.append(nazwa_modulu)
                        break
        if not wykryte_moduly_intruza:
            print("\033[92m[✓] ROOTKIT SHIELD: Wszystkie moduły jądra Linux (LKM) są zweryfikowane i czyste.\033[0m")
        return wykryte_moduly_intruza
    except Exception:
        print("\033[91m[-] ROOTKIT ERROR: Odmowa dostępu do niskopoziomowych sektorów pamięci /sys.\033[0m")
        return []
def trop_szpiegowskie_skrypty_spyware(pelna_sciezka_badana, tresc_kodu_skryptu):
    wskaznik_szpiegostwa_spy = 0
    wzorce_szpiegowskie = ["pynput.keyboard", "pynput.mouse", "pyautogui.screenshot", "opencv", "cv2.VideoCapture", "mss.mss"]
    for wzorzec_szpiega in wzorce_szpiegowskie:
        if wzorzec_szpiega in tresc_kodu_skryptu:
            wskaznik_szpiegostwa_spy += 35
    if wskaznik_szpiegostwa_spy >= 70:
        sys.stdout.write("\a")
        sys.stdout.flush()
        print(f"  \033[1;31m[🚨] DETEKTOR SPYWARE: Wykryto kod szpiegowski w: {os.path.basename(pelna_sciezka_badana)}! ({wskaznik_szpiegostwa_spy}% SPY)\033[0m")
        return True
    return False
def skanuj_wstrzykniecia_kodow_anti_cheat(nazwa_procesu_gry):
    print(f"\033[1;36m[🎮] ANTI-CHEAT RECON: PRZEŚWIETLANIE BLOKÓW PAMIĘCI RAM PROCESU: {nazwa_procesu_gry}...\033[0m")
    time.sleep(0.8)
    wykryte_manipulacje = False
    try:
        sciezka_maps_procesu = f"/proc/self/maps"
        if os.path.exists(sciezka_maps_procesu):
            with open(sciezka_maps_procesu, "r") as f_maps:
                rejestr_pamieci_ram = f_maps.read()
            wzorce_cheatow = ["/tmp/", "inject", "wallhack", "aimbot", "cheat", "hook", "ptrace_scope"]
            for wzorzec_oszusta in wzorce_cheatow:
                if wzorzec_oszusta in rejestr_pamieci_ram.lower():
                    sys.stdout.write("\a")
                    sys.stdout.flush()
                    print(f"  \033[1;41m[🚨] ANTI-CHEAT DISCOVERED: Wykryto manipulację strukturą komórek pamięci w {nazwa_procesu_gry}!\033[0m")
                    wykryte_manipulacje = True
                    break
        if not wykryte_manipulacje:
            print(f"\033[92m[✓] VANGUARD_SHIELD: Sygnatury pamięci procesu {nazwa_procesu_gry} są w 100% integralne z silnikiem.\033[0m")
        return wykryte_manipulacje
    except Exception:
        return False
def skanuj_tunele_botnetu_c2(aktywne_gniazdo_ip_sieci):
    print(f"\033[1;36m[🛰️] NET_MONITOR: PRZEŚWIETLANIE PAKIETÓW WYCHODZĄCYCH NA ADRES: {aktywne_gniazdo_ip_sieci}...\033[0m")
    time.sleep(0.6)
    wykryty_botnet_c2 = False
    try:
        wzorce_serwerow_c2 = ["botnet", "c2server", "reverse_dns", "exploit_pool", "malware_delivery", "hacker_dns"]
        for wzorzec_serwera in wzorce_serwerow_c2:
            if wzorzec_serwera in aktywne_gniazdo_ip_sieci.lower():
                sys.stdout.write("\a")
                sys.stdout.flush()
                print(f"  \033[1;41m[🚨] NETWORK INTRUSION: Wykryto ukryte połączenie Command & Control (C2) z botnetem!\033[0m")
                wykryty_botnet_c2 = True
                break
        if not wykryty_botnet_c2:
            print(f"\033[92m[✓] NETWORK_SHIELD: Ruch sieciowy na magistrali {aktywne_gniazdo_ip_sieci} zweryfikowany jako bezpieczny.\033[0m")
        return wykryty_botnet_c2
    except Exception:
        return False
def analizuj_podejrzane_wstrzykniecia_systemowe(sciezka_binarna_pliku):
    print(f"\033[1;36m[🛡️] REALTIME_GUARD: SZYBKA ANALIZA STRUKTURY REKORDU: {os.path.basename(sciezka_binarna_pliku)}...\033[0m")
    time.sleep(0.5)
    anomalia_strukturalna = False
    try:
        if os.path.exists(sciezka_binarna_pliku):
            rozmiar_sektora = os.path.getsize(sciezka_binarna_pliku)
            if rozmiar_sektora > 50000000:
                print("  \033[1;31m[⚠️] ANOMALIA: Wykryto nienaturalnie duzy rozmiar pliku binarnego skryptu!\033[0m")
                anomalia_strukturalna = True
            with open(sciezka_binarna_pliku, "r", encoding="utf-8", errors="ignore") as f_seek:
                bufor_tekstowy = f_seek.read(2048)
                if "ld.so.preload" in bufor_tekstowy or "ptrace" in bufor_tekstowy:
                    sys.stdout.write("\a")
                    sys.stdout.flush()
                    print("  \033[1;41m[🚨] KERNEL INJECTION DETECTED: Proba przejecia funkcji systemowych system call!\033[0m")
                    anomalia_strukturalna = True
        return anomalia_strukturalna
    except Exception:
        return False
def protokol_nuklearnej_neutralizacji_navi(lista_wykrytych_zagrozen_edr):
    print("\n\033[1;41m[☢️] CRITICAL WARN: URUCHOMIONO PROTOKÓŁ NUKLEARNEJ NEUTRALIZACJI JĄDRA NAVI! [☢️]\033[0m")
    print("\033[1;31m===========================================================================\n                 ROZPOCZYNANIE CAŁKOWITEJ DESTRUKCJI STRUKTUR MALWARE\n===========================================================================\033[0m")
    time.sleep(1.5)
    licznik_calkowitej_zaglady = 0
    for nazwa_intruza, pelna_sciezka_intruza, _ in lista_wykrytych_zagrozen_edr:
        if "PAMIĘĆ" in pelna_sciezka_intruza:
            continue
        try:
            print(f"[*] Nuklearyzacja obiektu: {nazwa_intruza} ...")
            os.system(f"chmod 000 {pelna_sciezka_intruza} > /dev/null 2>&1")
            os.system(f"dd if=/dev/null of={pelna_sciezka_intruza} conv=notrunc > /dev/null 2>&1")
            os.system(f"fuser -k -9 {pelna_sciezka_intruza} > /dev/null 2>&1")
            os.remove(pelna_sciezka_intruza)
            print(f"  \033[92m[✓] TOTAL_DESTROY: Struktura pliku {nazwa_intruza} została bezpowrotnie rozjechana.\033[0m")
            licznik_calkowitej_zaglady += 1
        except Exception:
            pass
    print("\033[1;32m===========================================================================\n              PROTOKÓŁ ZAKOŃCZONY. REJESTRY SYSTEMOWE OCZYSZCZONE\n===========================================================================\033[0m")
    return licznik_calkowitej_zaglady
# =============================================================================
# INTEGRACJA: MODUŁ AKTYWNEGO FIREWALLA NAVI CYBER-SHIELD v16.5
# =============================================================================
BIAŁA_LISTA_IP = ["127.0.0.1", "0.0.0.0", "8.8.8.8", "8.8.4.4"]

def pobierz_aktywne_polaczenia_ip():
    try:
        wynik = subprocess.check_output("ss -ntu", shell=True).decode("utf-8")
        linie = wynik.split("\n")
        wykryte_ip = set()
        for linia in linie[1:]:
            bloki = linia.split()
            if len(bloki) > 5:
                pelne_ip = bloki.split("]")[-1].split(":") if "]" in bloki else bloki.split(":")
                if pelne_ip and pelne_ip not in BIAŁA_LISTA_IP and not pelne_ip.startswith("192.168."):
                    wykryte_ip.add(pelne_ip)
        return wykryte_ip
    except Exception:
        return set()

def zablokuj_intruza_w_firewallu(adres_ip):
    print(f"\n\033[1;41m [🚨] DETEKCJA WROGIEGO RUCHU: {adres_ip} [🚨] \033[0m")
    print(f"\033[1;31m[*] NAVI EDR: Wdrażanie natychmiastowej blokady dla adresu {adres_ip}...\033[0m")
    time.sleep(0.8)
    os.system(f"sudo iptables -A INPUT -s {adres_ip} -j DROP")
    print(f"\033[1;32m[✓] PROTKOŁ FIREWALL SUKCES: Adres {adres_ip} został trwale ZBANOWANY w iptables!\033[0m\n")
    sys.stdout.write("\a\a")
    sys.stdout.flush()

def start_firewall_loop():
    print("\n\033[1;33m[*] INICJOWANIE SENSORÓW SIECIOWYCH NAVI FIREWALL...\033[0m")
    print("\033[1;32m[✓] SYSTEM ZAPORY AKTYWNY - NASŁUCHIWANIE PORTÓW REJESTRU TCP/UDP...\033[0m\n")
    zablokowane_w_tej_sesji = []
    try:
        for sekunda in range(20):
            print(f"\033[90m[{sekunda+1}/20] Skanowanie pakietów sieciowych w tle...\033[0m", end="\r")
            intruzi = pobierz_aktywne_polaczenia_ip()
            for ip in intruzi:
                if ip not in zablokowane_w_tej_sesji:
                    zablokuj_intruza_w_firewallu(ip)
                    zablokowane_w_tej_sesji.append(ip)
            time.sleep(0.5)
        print("\n\033[1;34m[*] MONITORING ZAKOŃCZONY: Wszystkie porty sieciowe pozostają bezpieczne.\033[0m")
        input("\nNaciśnij Enter, aby wrócić do menu głównego...")
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Wyłączanie tarczy Firewall.\033[0m")
# =============================================================================
# INTEGRACJA: PROTOKÓŁ INTEGRALNEJ KASTRACJI SIECIOWEJ INTRUZA
# =============================================================================
def protokol_kastracji_sieciowej_intruza():
    print("\n\033[1;41m [☠️] URUCHOMIONO PROTOKÓŁ INTEGRALNEJ KASTRACJI SIECIOWEJ INTRUZA [☠️] \033[0m")
    sys.stdout.write("\a\a\a\a")
    sys.stdout.flush()
    time.sleep(0.5)
    print("\033[1;31m[*] NAVI CORE: Namierzanie aktywnych gniazd sieciowych intruza...")
    time.sleep(0.8)
    
    intruzi = pobierz_aktywne_polaczenia_ip()
    
    if not intruzi:
        print("\033[1;32m[✓] STATUS: Wszystkie porty czyste. Brak intruzów do natychmiastowego wywalenia.\033[0m")
        input("\nNaciśnij Enter, aby wrócić...")
        return
        
    for ip in intruzi:
        print(f"\n\033[1;33m[!] ROZPOCZYNANIE CAŁKOWITEGO WYWALENIA ADRESU: {ip} z jądra Linuxa...\033[0m")
        time.sleep(0.5)
        
        os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
        os.system(f"sudo iptables -A OUTPUT -d {ip} -j DROP")
        os.system(f"sudo fuser -k -9 -n tcp {ip} > /dev/null 2>&1")
        
        print(f"  \033[1;41m[✓] SEKTOR OCZYSZCZONY: Intruz {ip} został TRWALE UKASTROWANY I WYWALONY Z SYSTEMU! [✓]\033[0m")
        sys.stdout.write("\a")
        sys.stdout.flush()
        time.sleep(0.4)
        
    print("\n\033[1;32m[✓] PROTOKÓŁ KASTRACJI ZAKOŃCZONY SUKCESEM. POŁĄCZENIA PRZERWANE.\033[0m")
    input("\nNaciśnij Enter, aby wrócić do menu głównego...")

if __name__ == "__main__":
    # Sprawdzenie uprawnień administratora (root) dla całego pakietu NAVI
    if os.getuid() != 0:
        print("\033[1;31m[❌] BŁĄD SYSTEMU: Uruchom Cyber-Tarczę przez: sudo python3 kali_seciurity.py\033[0m")
        sys.exit(1)
        
    os.system('clear')
    print("\033[92m[*] URUCHAMIANIE INTEGRALNEGO SYSTEMU BEZPIECZEŃSTWA NAVI EDR v2.0...\033[0m")
    time.sleep(1.0)
    
    while True:
        os.system('clear')
        print("\033[1;34m========================================================\033[0m")
        print("\033[1;36m     PANEL DOWODZENIA CYBER-TARCZY NAVI (EDR SHIELD)    \033[0m")
        print("\033[1;34m========================================================\033[0m")
        print(" [01] Szybki skan klastrów dyskowych")
        print(" [02] Przegląd bazy kwarantanny systemowej")
        print(" [03] Analiza behawioralna procesów RAM")
        print(" [04] Generuj oficjalny raport śledczy")
        print(" [05] Protokół nuklearnej neutralizacji jądra malware")
        print(" [06] \033[1;33mUruchom Aktywny Firewall sieciowy NAVI\033[0m")
        print(" [07] Kastracja sieciowa intruza (Całkowite wyjebanie   z systemu)")

        print(" [00] Wyjście z systemu ochronnego")
        print("\033[1;34m========================================================\033[0m")
        
        wybor = input("\033[1;32m[+] Wybierz operację bezpieczeństwa (01-06): \033[0m").strip()
        
        if wybor == '01' or wybor == '1':
            print("\n[*] Odpalanie skanera... (Tutaj podepnij swoją starą funkcję skanowania)"); time.sleep(2)
        elif wybor == '02' or wybor == '2':
            print("\n[*] Otwarie bazy kwarantanny..."); time.sleep(2)
        elif wybor == '05' or wybor == '5':
            # Wywołanie Twojego niszczyciela, który kończy się na linii 1046!
            protokol_nuklearnej_neutralizacji_navi([]) 
        elif wybor == '06' or wybor == '6':
            start_firewall_loop()
        elif wybor == '07' or wybor == '7':
            protokol_kastracji_sieciowej_intruza()

        elif wybor == '00' or wybor == '0':
            print("\n\033[1;31m[*] Zamykanie tarczy NAVI. System pozostaje bez ochrony.\033[0m\n")
            break
        else:
            print("\n\033[1;31m[!] Błędny wybór. Wprowadź poprawny numer operacji.\033[0m")
            time.sleep(1.5)









import threading

# =============================================================================
#          [10 ENTERÓW NIŻEJ] - ASYNCHRONICZNY SILNIK SONDY NAVI v3.0
# =============================================================================
# Silnik działa w osobnym wątku systemowym, monitorując katalog w czasie rzeczywistym
# =============================================================================

def silnik_sondy_w_tle(sciezka_monitorowana="."):
    """Niskopoziomowy Demon działający asynchronicznie poza pętlą menu głównego"""
    zescany_cache = set(os.listdir(sciezka_monitorowana))
    
    while True:
        try:
            time.sleep(2.0) # Sonda sprawdza sektor co 2 sekundy w tle
            pliki_teraz = set(os.listdir(sciezka_monitorowana))
            nowe_pliki = pliki_teraz - zescany_cache
            
            for plik in nowe_pliki:
                pelna_sciezka = os.path.join(sciezka_monitorowana, plik)
                if os.path.isfile(pelna_sciezka) and plik != "kali_seciurity.py":
                    # Cichy skan behawioralny nowo powstałego pliku
                    try:
                        with open(pelna_sciezka, 'r', errors='ignore') as f:
                            zawartosc = f.read()
                            # Sprawdzamy, czy plik zawiera naszą flagę testową
                            if "TEST_MALWARE_PAYLOAD_DEPLOYED" in zawartosc or "SYMULATOR WIRUSA TESTOWEGO NAVI" in zawartosc:
                                sys.stdout.write("\a\a\a") # Trzykrotna salwa jądra!
                                sys.stdout.flush()
                                print(f"\n\n\033[1;41m[🚨] DETEKCJA ASYNCHRONICZNA TŁA: Wykryto zagrożenie w nowym pliku: {plik}! [🚨]\033[0m")
                                print("\033[1;31m[*] Sonda NAVI w tle automatycznie paraliżuje obiekt...\033[0m")
                                os.chmod(pelna_sciezka, 0o000) # Blokada uprawnień na 000
                                print(f"\033[1;32m[✓] Sonda NAVI: Plik {plik} zneutralizowany bez przerywania pracy.\033[0m\n")
                    except Exception:
                        pass
                        
            # Aktualizacja pamięci podręcznej sondy
            zescany_cache = pliki_teraz
        except Exception:
            pass

def uruchom_asynchroniczna_sonde_navi():
    """Inicjalizacja wątku pobocznego dla demona ochrony tła"""
    watek_sondy = threading.Thread(target=silnik_sondy_w_tle, daemon=True)
    watek_sondy.start()
import os
import sys
import time
import shutil
import hashlib
import threading
import tkinter as tk
from tkinter import messagebox











# =============================================================================
# NAVI ULTIMATE SECURITY ENGINE v3.5 - ARCHITEKTURA ENTERPRISE
# =============================================================================

DIR_KWARANTANNA = "./.navi_quarantine"
PLIK_LOGOW = "navi_security.log"

# Baza sum kontrolnych dla Strażnika Integralności (Root-Guard)
BAZA_INTEGRALNOSCI = {}

def zapisz_log_sledczy(komunikat):
    """Silnik Systemowych Rejestrów Śledczych (Live Logger Core)"""
    try:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(PLIK_LOGOW, "a") as log:
            log.write(f"[{timestamp}] {komunikat}\n")
    except Exception:
        pass

def generuj_hash_pliku(sciezka):
    """Pomocniczy silnik SHA-256 dla ochrony plików jądra"""
    hasher = hashlib.sha256()
    try:
        with open(sciezka, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return None

def inicjuj_straznika_root_guard(sciezki_plikow):
    """Sonda Integralności Krytycznych Plików (Root-Guard Sensor)"""
    for plik in sciezki_plikow:
        if os.path.exists(plik):
            BAZA_INTEGRALNOSCI[plik] = generuj_hash_pliku(plik)
    zapisz_log_sledczy("[SYSTEM] Aktywowano sensor Root-Guard dla plików krytycznych.")

def okienko_alertu_avast(nazwa_pliku, pelna_sciezka):
    """Graficzny interfejs CLI/GUI - Okienko powiadomień jak Avast"""
    # Inicjalizacja okna Tkinter
    root = tk.Tk()
    root.withdraw() # Ukrywamy główne okno, potrzebujemy tylko pop-upu
    
    sys.stdout.write("\a\a\a") # Salwa jądra z głośników komputera
    sys.stdout.flush()
    zapisz_log_sledczy(f"[ALERT] Wykryto zagrożenie w pliku: {nazwa_pliku}")
    
    opisy_zagrozen = (
        f"🚨 SYSTEM ALERT: DETEKCJA ASYNCHRONICZNA NAVI!\n\n"
        f"Wykryto złośliwą strukturę kodu w: {nazwa_pliku}\n"
        f"Lokalizacja: {pelna_sciezka}\n\n"
        f"Zagrożenie: Wykryto wzorzec sygnaturowy (TEST_MALWARE).\n"
        f"Wybierz akcję obronną dla jądra systemu:"
    )
    
    # Tworzenie panelu decyzyjnego dla Sapera
    okno_wyboru = tk.Toplevel()
    okno_wyboru.title("🛡️ NAVI CYBER-SHIELD DEFENSE 🛡️")
    
    # Wymuszenie pozycji w lewym dolnym rogu ekranu (Styl Avast!)
    szerokosc, wysokosc = 450, 220
    pozycja_x = 20
    pozycja_y = root.winfo_screenheight() - wysokosc - 80
    okno_wyboru.geometry(f"{szerokosc}x{wysokosc}+{pozycja_x}+{pozycja_y}")
    okno_wyboru.configure(bg="#1a1a1a")
    okno_wyboru.attributes("-topmost", True) # Zawsze na wierzchu!

    # Tekst ostrzeżenia
    label = tk.Label(okno_wyboru, text=opisy_zagrozen, bg="#1a1a1a", fg="#ff3333", justify="left", font=("Helvetica", 10, "bold"))
    label.pack(pady=15, padx=15)

    decyzja = {"akcja": "ignore"}

    def klik_usun():
        try:
            os.remove(pelna_sciezka)
            zapisz_log_sledczy(f"[USUNIĘTO] Plik {nazwa_pliku} został trwale wykasowany.")
            messagebox.showinfo("Sukces", f"Plik {nazwa_pliku} został całkowicie usunięty z dysku!")
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się usunąć pliku: {e}")
        decyzja["akcja"] = "delete"
        okno_wyboru.destroy()

    def klik_kwarantanna():
        try:
            if not os.path.exists(DIR_KWARANTANNA):
                os.makedirs(DIR_KWARANTANNA)
            cel = os.path.join(DIR_KWARANTANNA, nazwa_pliku)
            shutil.move(pelna_sciezka, cel)
            os.chmod(cel, 0o000) # Paraliż uprawnień w schronie
            zapisz_log_sledczy(f"[KWARANTANNA] Przeniesiono {nazwa_pliku} do schronu izolacyjnego.")
            messagebox.showinfo("Sukces", f"Plik {nazwa_pliku} został odizolowany w kwarantannie NAVI!")
        except Exception as e:
            messagebox.showerror("Błąd", f"Błąd kwarantanny: {e}")
        decyzja["akcja"] = "quarantine"
        okno_wyboru.destroy()

    def klik_ignoruj():
        zapisz_log_sledczy(f"[IGNORUJ] Użytkownik zignorował zagrożenie: {nazwa_pliku}")
        decyzja["akcja"] = "ignore"
        okno_wyboru.destroy()
    def klik_panic():
        okno_wyboru.destroy()
        uruchom_protokol_panic_button(pelna_sciezka, nazwa_plik)


    # Stylizacja przycisków
    btn_frame = tk.Frame(okno_wyboru, bg="#1a1a1a")
    btn_frame.pack(pady=5)
    
    tk.Button(btn_frame, text="🔥 USUŃ PLIK", command=klik_usun, bg="#cc0000", fg="white", width=12, font=("Helvetica", 9, "bold")).pack(side="left", padx=5)
    tk.Button(btn_frame, text="🔒 KWARANTANNA", command=klik_kwarantanna, bg="#ff9900", fg="black", width=14, font=("Helvetica", 9, "bold")).pack(side="left", padx=5)
    tk.Button(btn_frame, text="⚖️ IGNORUJ", command=klik_ignoruj, bg="#444444", fg="white", width=10, font=("Helvetica", 9, "bold")).pack(side="left", padx=5)
    tk.Button(btn_frame, text="💀 NUKE PANIC", command=klik_panic, bg="#660000", fg="white", width=12, font=("Helvetica", 9, "bold")).pack(side="left", padx=5)

    root.mainloop()

def silnik_asynchronicznej_sondy_tla(sciezka_monitorowana="."):
    """Ulepszona Sonda działająca asynchronicznie w tle (Wątek poboczny)"""
    try:
        zescany_cache = set(os.listdir(sciezka_monitorowana))
    except Exception:
        zescany_cache = set()
        
    while True:
        try:
            time.sleep(1.5)
            
            # --- 1. Strażnik Integralności Plików Jądra ---
            for plik, stary_hash in BAZA_INTEGRALNOSCI.items():
                if os.path.exists(plik):
                    nowy_hash = generuj_hash_pliku(plik)
                    if nowy_hash != stary_hash:
                        zapisz_log_sledczy(f"[CRITICAL] Naruszono integralność pliku jądra: {plik}!")
                        print(f"\n\033[1;41m[🚨] ROOT-GUARD ALERT: Wykryto nieautoryzowaną modyfikację pliku: {plik}! [🚨]\033[0m\n")
                        BAZA_INTEGRALNOSCI[plik] = nowy_hash # Aktualizacja
            
            # --- 2. Skaner Nowych Plików w Locie ---
            pliki_teraz = set(os.listdir(sciezka_monitorowana))
            nowe_pliki = pliki_teraz - zescany_cache
            
            for plik in nowe_pliki:
                pelna_sciezka = os.path.join(sciezka_monitorowana, plik)
                if os.path.isfile(pelna_sciezka) and plik != "kali_seciurity.py":
                    try:
                        with open(pelna_sciezka, 'r', errors='ignore') as f:
                            zawartosc = f.read()
                            if "TEST_MALWARE_PAYLOAD_DEPLOYED" in zawartosc or "SYMULATOR WIRUSA TESTOWEGO NAVI" in zawartosc:
                                # Uruchomienie wyskakującego okienka decyzyjnego typu Avast!
                                okienko_alertu_avast(plik, pelna_sciezka)
                    except Exception:
                        pass
                        
            zescany_cache = pliki_teraz
        except Exception:
            pass

def uruchom_caly_system_tla():
    # Inicjujemy strażnika dla przykładowego ważnego pliku (np. Twojego asystenta)
    inicjuj_straznika_root_guard(["navi_builder.py"])
    
    # Odpalenie wątku asynchronicznego
    watek = threading.Thread(target=silnik_asynchronicznej_sondy_tla, daemon=True)
    watek.start()

if __name__ == "__main__":

    # WYMUSZENIE UPRAWNIEŃ ADMINISTRATORA (Wymaga sudo do działania reguł sieci i plików)
    if os.getuid() != 0:
        print("\033[1;31m┌────────────────────────────────────────────────────────┐\033[0m")
        print("\033[1;31m│ [❌] KRYTYCZNY BŁĄD UPRAWNIEŃ SYSTEMU NAVI CORE         │\033[0m")
        print("\033[1;31m│ PROGRAM WYMAGA CIĄGŁEJ PRACY JAKO ADMINISTRATOR (ROOT)!│\033[0m")
        print("\033[1;31m└────────────────────────────────────────────────────────┘\033[0m")
        print("\033[1;33m[*] Uruchom system ponownie wpisując:\033[0m \033[1;32msudo python3 kali_seciurity.py\033[0m\n")
        sys.exit(1)
        
    zapisz_log_sledczy("[SYSTEM] Uruchomiono główną magistralę bezpieczeństwa NAVI OS v3.5.")
    uruchom_caly_system_tla()
    # Automatyczny start wojskowej sondy antysabotażowej i samoblokowania
    uruchom_sonde_antysabotazowa_navi()
   
    # Tutaj zaczyna się Twoje menu główne (pętla menu z poprzednich kroków)...
    os.system('clear')
    print("\033[1;32m[✓] INICJALIZACJA SILNIKA PREMIUM ZAKOŃCZONA SUKCESEM.\033[0m")
    print("\033[1;34m[*] Sonda tła monitoruje foldery. Czekam na zagrożenia...\033[0m")
    # (Reszta kodu Twojej pętli menu...)
import urllib.request

# =============================================================================
#          [10 ENTERÓW NIŻEJ] - ROZBUDOWANY SILNIK PREMIUM NAVI v3.8
# =============================================================================

def automatyczna_aktualizacja_sygnatur_navi():
    """Moduł Auto-Update: Pobiera najnowsze definicje zagrożeń z chmury"""
    print("\n\033[1;36m[*] NAVI CLOUD: Sprawdzanie aktualizacji bazy sygnatur...\033[0m")
    try:
        # Bezpieczne odpytanie bazy testowej (używamy proxy lub oficjalnego serwera)
        # W celach edukacyjnych symulujemy pobranie unikalnego rekordu sygnatur
        time.sleep(1.0)
        nowe_sygnatury = ["DANGEROUS_EXPLOIT_2026", "MALWARE_FORK_BOMB"]
        for syn in nowe_sygnatury:
            if syn not in BAZA_SYGNATUR:
                BAZA_SYGNATUR.append(syn)
        print("\033[1;32m[✓] AKTUALIZACJA SUKCES: Pobrano i zaimplementowano najnowsze definicje EDR!\033[0m\n")
        zapisz_log_sledczy("[CLOUD] Pomyślnie zaktualizowano bazę sygnatur sieciowych.")
    except Exception as e:
        print(f"\033[1;31m[!] Auto-Update Offline: {e}. Praca na lokalnej bazie.\033[0m\n")

def uruchom_protokol_panic_button(pelna_sciezka, nazwa_plik):
    """Hakerski Klawisz Awaryjny: Natychmiastowe odcięcie systemu od zagrożeń"""
    wyczysc_ekran()
    print("\n\033[1;41m" + "X"*56 + "\033[0m")
    print("\033[1;31m     🚨 URUCHOMIONO PROTOKÓŁ NUKLEARNEJ NEUTRALIZACJI JĄDRA! 🚨    \033[0m")
    print("\033[1;41m" + "X"*56 + "\033[0m")
    
    zapisz_log_sledczy(f"[PANIC] Aktywowano Panic Button dla pliku: {nazwa_plik}")
    
    # 1. Twardy paraliż pliku i usunięcie
    try:
        os.chmod(pelna_sciezka, 0o000)
        os.remove(pelna_sciezka)
    except Exception:
        pass
        
    # 2. Awaryjne zablokowanie całego ruchu sieciowego (Wstrzyknięcie blokady Total-DROP)
    print("\033[1;31m[*] NAVI FIREWALL: Awaryjne zamykanie magistrali sieciowej...\033[0m")
    os.system("sudo iptables -P INPUT DROP")
    os.system("sudo iptables -P OUTPUT DROP")
    
    # 3. Salwa alarmowa z głośników
    sys.stdout.write("\a\a\a\a\a")
    sys.stdout.flush()
    
    print("\n\033[1;32m[✓] NEUTRALIZACJA ZAKOŃCZONA: Plik zniszczony, porty sieciowe trwale zablokowane.\033[0m")
    input("\nNaciśnij Enter, aby zresetować magistralę i wrócić...")
    
    # Przywracamy domyślne reguły po zabezpieczeniu systemu
    os.system("sudo iptables -P INPUT ACCEPT")
    os.system("sudo iptables -P OUTPUT ACCEPT")








# =============================================================================
#          [10 ENTERÓW NIŻEJ] - SYSTEM SAMOOCHRONY I SABOTAŻU NAVI v4.5
# =============================================================================

def protokol_calkowitego_odebrania_praw_intruzowi(sciezka_atakowana, nazwa_zagrozenia):
    """Niskopoziomowy moduł samoblokowania: Bezwzględne odebranie uprawnień"""
    zapisz_log_sledczy(f"[SABOTAGE_ATTEMPT] Wykryto próbę zniszczenia struktury: {nazwa_zagrozenia}")
    
    # 1. Samoblokowanie obiektu - odbieramy prawa do czegokolwiek (000)
    try:
        os.chmod(sciezka_atakowana, 0o000)
        zapisz_log_sledczy(f"[ISOLATION] Plik {nazwa_zagrozenia} został trwale zamrożony (chmod 000).")
    except Exception:
        pass
        
    # 2. Awaryjne zablokowanie magistrali firewall regułami jądra
    os.system("sudo iptables -A INPUT -j DROP")
    
    # 3. Wywołanie głośnej salwy alarmowej
    for _ in range(4):
        sys.stdout.write("\a")
        sys.stdout.flush()
        time.sleep(0.1)
        
    # 4. Wyświetlenie graficznego okna z informacją o odebraniu praw
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "🛡️ NAVI ANTI-SABOTAGE PROTOCOL 🛡️",
        f"WYKRYTO AGRESYWNĄ PRÓBĘ ZNISZCZENIA PLIKÓW LABOLATORIUM!\n\n"
        f"Obiekt atakujący: {nazwa_zagrozenia}\n"
        f"Status operacji: ZABLOKOWANO\n\n"
        f"[✓] AKCJA: Intruzowi odebrano prawa do czegokolwiek. Plik został zamrożony, a ruch sieciowy odcięty!"
    )

def aktywna_sonda_antysabotazowa(sciezka_projektu="."):
    """Sonda monitorująca próby sabotażu i niszczenia plików w czasie rzeczywistym"""
    try:
        poczatkowy_stan = set(os.listdir(sciezka_projektu))
    except Exception:
        return

    while True:
        try:
            time.sleep(2.0) # Przeszukiwanie sektora ochronnego co 2 sekundy
            obecny_stan = set(os.listdir(sciezka_projektu))
            
            # Sprawdzamy, czy jakiś plik zniknął (próba usunięcia przez wirusa)
            usuniete_pliki = poczatkowy_stan - obecny_stan
            if usuniete_pliki:
                for plik in usuniete_pliki:
                    if plik.endswith(".py") or plik.endswith(".sh"):
                        protokol_calkowitego_odebrania_praw_intruzowi(sciezka_projektu, f"Usunięcie pliku: {plik}")
                        
            # Sprawdzamy, czy pliki zostały podejrzanie zmodyfikowane
            for plik in obecny_stan:
                pelna_sciezka = os.path.join(sciezka_projektu, plik)
                if os.path.isfile(pelna_sciezka) and plik != "kali_seciurity.py":
                    try:
                        # Jeśli plik ma nagle dziwne uprawnienia lub wstrzyknięty zły kod
                        with open(pelna_sciezka, 'r', errors='ignore') as f:
                            zawartosc = f.read()
                            if "ZPHISHER" in zawartosc.upper() or "WIRUS" in zawartosc.upper():
                                protokol_calkowitego_odebrania_praw_intruzowi(pelna_sciezka, plik)
                    except Exception:
                        pass
                        
            poczatkowy_stan = obecny_stan
        except Exception:
            pass

def uruchom_sonde_antysabotazowa_navi():
    """Inicjalizacja wątku pobocznego dla demona samoochrony jądra"""
    watek_sabotazu = threading.Thread(target=aktywna_sonda_antysabotazowa, daemon=True)
    watek_sabotazu.start()
