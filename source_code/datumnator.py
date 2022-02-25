import os
from menudownload import *
import random
from time import mktime, localtime, strftime, strptime
import regex
from winregistry import WinRegistry
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from einfuehrung import einfuehrung
from farbprinter.farbprinter import Farbprinter
drucker =Farbprinter()
tagedict ={1: 'ersten', 2: 'zweiten', 3: 'dritten', 4: 'vierten', 5: 'fünften', 6: 'sechsten', 7: 'siebten', 8: 'achten', 9: 'neunten', 10: 'zehnten', 11: 'elften', 12: 'zwölften', 13: 'dreizehnten', 14: 'vierzehnten', 15: 'fünfzehnten', 16: 'sechzehnten', 17: 'siebzehnten', 18: 'achtzehnten', 19: 'neunzehnten', 20: 'zwanzigsten', 21: 'einundzwanzigsten', 22: 'zweiundzwanzigsten', 23: 'dreiundzwanzigsten', 24: 'vierundzwanzigsten', 25: 'fünfundzwanzigsten', 26: 'sechsundzwanzigsten', 27: 'siebenundzwanzigsten', 28: 'achtundzwanzigsten', 29: 'neunundzwanzigsten', 30: 'dreißigsten', 31: 'einunddreißigsten'}

monatdict = {1: ['Ersten', 'Januar'], 2: ['Zweiten','Februar'], 3: ['Dritten','März'], 4: ['Vierten', 'April'], 5: ['Fünften', 'Mai'], 6: ['Sechsten', 'Juni'], 7: ['Siebten', 'Juli'], 8: ['Achten', 'August'], 9: ['Neunten', 'September'], 10: ['Zehnten', 'Oktober'], 11: ['Elften', 'November'], 12: ['Zwölften', 'Dezember']}

jahredict = {1970: ['neunzehnhundertsiebzig',
        'eintausendneunhundertsiebzig',
        'tausendneunhundertsiebzig'],
 1971: ['neunzehnhunderteinundsiebzig',
        'eintausendneunhunderteinundsiebzig',
        'tausendneunhunderteinundsiebzig'],
 1972: ['neunzehnhundertzweiundsiebzig',
        'eintausendneunhundertzweiundsiebzig',
        'tausendneunhundertzweiundsiebzig'],
 1973: ['neunzehnhundertdreiundsiebzig',
        'eintausendneunhundertdreiundsiebzig',
        'tausendneunhundertdreiundsiebzig'],
 1974: ['neunzehnhundertvierundsiebzig',
        'eintausendneunhundertvierundsiebzig',
        'tausendneunhundertvierundsiebzig'],
 1975: ['neunzehnhundertfünfundsiebzig',
        'eintausendneunhundertfünfundsiebzig',
        'tausendneunhundertfünfundsiebzig'],
 1976: ['neunzehnhundertsechsundsiebzig',
        'eintausendneunhundertsechsundsiebzig',
        'tausendneunhundertsechsundsiebzig'],
 1977: ['neunzehnhundertsiebenundsiebzig',
        'eintausendneunhundertsiebenundsiebzig',
        'tausendneunhundertsiebenundsiebzig'],
 1978: ['neunzehnhundertachtundsiebzig',
        'eintausendneunhundertachtundsiebzig',
        'tausendneunhundertachtundsiebzig'],
 1979: ['neunzehnhundertneunundsiebzig',
        'eintausendneunhundertneunundsiebzig',
        'tausendneunhundertneunundsiebzig'],
 1980: ['neunzehnhundertachtzig',
        'eintausendneunhundertachtzig',
        'tausendneunhundertachtzig'],
 1981: ['neunzehnhunderteinundachtzig',
        'eintausendneunhunderteinundachtzig',
        'tausendneunhunderteinundachtzig'],
 1982: ['neunzehnhundertzweiundachtzig',
        'eintausendneunhundertzweiundachtzig',
        'tausendneunhundertzweiundachtzig'],
 1983: ['neunzehnhundertdreiundachtzig',
        'eintausendneunhundertdreiundachtzig',
        'tausendneunhundertdreiundachtzig'],
 1984: ['neunzehnhundertvierundachtzig',
        'eintausendneunhundertvierundachtzig',
        'tausendneunhundertvierundachtzig'],
 1985: ['neunzehnhundertfünfundachtzig',
        'eintausendneunhundertfünfundachtzig',
        'tausendneunhundertfünfundachtzig'],
 1986: ['neunzehnhundertsechsundachtzig',
        'eintausendneunhundertsechsundachtzig',
        'tausendneunhundertsechsundachtzig'],
 1987: ['neunzehnhundertsiebenundachtzig',
        'eintausendneunhundertsiebenundachtzig',
        'tausendneunhundertsiebenundachtzig'],
 1988: ['neunzehnhundertachtundachtzig',
        'eintausendneunhundertachtundachtzig',
        'tausendneunhundertachtundachtzig'],
 1989: ['neunzehnhundertneunundachtzig',
        'eintausendneunhundertneunundachtzig',
        'tausendneunhundertneunundachtzig'],
 1990: ['neunzehnhundertneunzig',
        'eintausendneunhundertneunzig',
        'tausendneunhundertneunzig'],
 1991: ['neunzehnhunderteinundneunzig',
        'eintausendneunhunderteinundneunzig',
        'tausendneunhunderteinundneunzig'],
 1992: ['neunzehnhundertzweiundneunzig',
        'eintausendneunhundertzweiundneunzig',
        'tausendneunhundertzweiundneunzig'],
 1993: ['neunzehnhundertdreiundneunzig',
        'eintausendneunhundertdreiundneunzig',
        'tausendneunhundertdreiundneunzig'],
 1994: ['neunzehnhundertvierundneunzig',
        'eintausendneunhundertvierundneunzig',
        'tausendneunhundertvierundneunzig'],
 1995: ['neunzehnhundertfünfundneunzig',
        'eintausendneunhundertfünfundneunzig',
        'tausendneunhundertfünfundneunzig'],
 1996: ['neunzehnhundertsechsundneunzig',
        'eintausendneunhundertsechsundneunzig',
        'tausendneunhundertsechsundneunzig'],
 1997: ['neunzehnhundertsiebenundneunzig',
        'eintausendneunhundertsiebenundneunzig',
        'tausendneunhundertsiebenundneunzig'],
 1998: ['neunzehnhundertachtundneunzig',
        'eintausendneunhundertachtundneunzig',
        'tausendneunhundertachtundneunzig'],
 1999: ['neunzehnhundertneunundneunzig',
        'eintausendneunhundertneunundneunzig',
        'tausendneunhundertneunundneunzig'],
 2000: ['zweitausend'],
 2001: ['zweitausendeins'],
 2002: ['zweitausendzwei'],
 2003: ['zweitausenddrei'],
 2004: ['zweitausendvier'],
 2005: ['zweitausendfünf'],
 2006: ['zweitausendsechs'],
 2007: ['zweitausendsieben'],
 2008: ['zweitausendacht'],
 2009: ['zweitausendneun'],
 2010: ['zweitausendzehn'],
 2011: ['zweitausendelf'],
 2012: ['zweitausendzwölf'],
 2013: ['zweitausenddreizehn'],
 2014: ['zweitausendvierzehn'],
 2015: ['zweitausendfünfzehn'],
 2016: ['zweitausendsechzehn'],
 2017: ['zweitausendsiebzehn'],
 2018: ['zweitausendachtzehn'],
 2019: ['zweitausendneunzehn'],
 2020: ['zweitausendzwanzig'],
 2021: ['zweitausendeinundzwanzig'],
 2022: ['zweitausendzweiundzwanzig'],
 2023: ['zweitausenddreiundzwanzig'],
 2024: ['zweitausendvierundzwanzig'],
 2025: ['zweitausendfünfundzwanzig'],
 2026: ['zweitausendsechsundzwanzig'],
 2027: ['zweitausendsiebenundzwanzig'],
 2028: ['zweitausendachtundzwanzig'],
 2029: ['zweitausendneunundzwanzig'],
 2030: ['zweitausenddreißig'],
 2031: ['zweitausendeinunddreißig'],
 2032: ['zweitausendzweiunddreißig'],
 2033: ['zweitausenddreiunddreißig'],
 2034: ['zweitausendvierunddreißig'],
 2035: ['zweitausendfünfunddreißig'],
 2036: ['zweitausendsechsunddreißig'],
 2037: ['zweitausendsiebenunddreißig'],
 2038: ['zweitausendachtunddreißig'],
 2039: ['zweitausendneununddreißig'],
 2040: ['zweitausendvierzig'],
 2041: ['zweitausendeinundvierzig'],
 2042: ['zweitausendzweiundvierzig'],
 2043: ['zweitausenddreiundvierzig'],
 2044: ['zweitausendvierundvierzig'],
 2045: ['zweitausendfünfundvierzig'],
 2046: ['zweitausendsechsundvierzig'],
 2047: ['zweitausendsiebenundvierzig'],
 2048: ['zweitausendachtundvierzig'],
 2049: ['zweitausendneunundvierzig'],
 2050: ['zweitausendfünfzig'],
 2051: ['zweitausendeinundfünfzig'],
 2052: ['zweitausendzweiundfünfzig'],
 2053: ['zweitausenddreiundfünfzig'],
 2054: ['zweitausendvierundfünfzig'],
 2055: ['zweitausendfünfundfünfzig'],
 2056: ['zweitausendsechsundfünfzig'],
 2057: ['zweitausendsiebenundfünfzig'],
 2058: ['zweitausendachtundfünfzig'],
 2059: ['zweitausendneunundfünfzig'],
 2060: ['zweitausendsechzig'],
 2061: ['zweitausendeinundsechzig'],
 2062: ['zweitausendzweiundsechzig'],
 2063: ['zweitausenddreiundsechzig'],
 2064: ['zweitausendvierundsechzig'],
 2065: ['zweitausendfünfundsechzig'],
 2066: ['zweitausendsechsundsechzig'],
 2067: ['zweitausendsiebenundsechzig'],
 2068: ['zweitausendachtundsechzig'],
 2069: ['zweitausendneunundsechzig'],
 2070: ['zweitausendsiebzig'],
 2071: ['zweitausendeinundsiebzig'],
 2072: ['zweitausendzweiundsiebzig'],
 2073: ['zweitausenddreiundsiebzig'],
 2074: ['zweitausendvierundsiebzig'],
 2075: ['zweitausendfünfundsiebzig'],
 2076: ['zweitausendsechsundsiebzig'],
 2077: ['zweitausendsiebenundsiebzig'],
 2078: ['zweitausendachtundsiebzig'],
 2079: ['zweitausendneunundsiebzig'],
 2080: ['zweitausendachtzig'],
 2081: ['zweitausendeinundachtzig'],
 2082: ['zweitausendzweiundachtzig'],
 2083: ['zweitausenddreiundachtzig'],
 2084: ['zweitausendvierundachtzig'],
 2085: ['zweitausendfünfundachtzig'],
 2086: ['zweitausendsechsundachtzig'],
 2087: ['zweitausendsiebenundachtzig'],
 2088: ['zweitausendachtundachtzig'],
 2089: ['zweitausendneunundachtzig'],
 2090: ['zweitausendneunzig'],
 2091: ['zweitausendeinundneunzig'],
 2092: ['zweitausendzweiundneunzig'],
 2093: ['zweitausenddreiundneunzig'],
 2094: ['zweitausendvierundneunzig'],
 2095: ['zweitausendfünfundneunzig'],
 2096: ['zweitausendsechsundneunzig'],
 2097: ['zweitausendsiebenundneunzig'],
 2098: ['zweitausendachtundneunzig']}



def richtig(leerzeichen=5):
    global userpunkte
    global gesamtpunkte
    gesamtpunkte = gesamtpunkte + 1
    userpunkte = userpunkte + 1
    print(drucker.f.black.brightgreen.normal(f'\nDeine Antwort ist richtig! \nErreichte Punkte:\t\t') +   drucker.f.black.brightgreen.negative(
        f'  {userpunkte}  ') + drucker.f.black.brightgreen.normal(f'\nMaximale Punktanzahl:\t\t') + drucker.f.black.brightgreen.negative(
        f'  {gesamtpunkte}  ') + drucker.f.black.brightgreen.normal(f'\n'))
    print('\n' * leerzeichen)


def falsch(richtigeantwort, leerzeichen=5):
    global userpunkte
    global gesamtpunkte
    gesamtpunkte = gesamtpunkte + 1
    print(drucker.f.black.brightred.normal(f'\nDeine Antwort ist falsch! Die richtige Antwort ist: {richtigeantwort}\nErreichte Punkte:\t\t') +   drucker.f.black.brightred.negative(
        f'  {userpunkte}  ') + drucker.f.black.brightred.normal(f'\nMaximale Punktanzahl:\t\t') + drucker.f.black.brightred.negative(
        f'  {gesamtpunkte}  ') + drucker.f.black.brightred.normal(f'\n'))
    print('\n' * leerzeichen)

def get_vlc_exe_path():
    def datei_auswaehlen_mit_tkinter():
        Tk().withdraw()
        videodatei = askopenfilename(filetypes=[("VLC PLAYER EXE", "vlc.exe")])
        ausgabeordner = regex.sub(r"/[^/]+\.\w+$", "", videodatei)
        print(videodatei, ausgabeordner)
        return videodatei, ausgabeordner
    TEST_REG_PATH = r"HKCR\VLC.3g2\shell\AddToPlaylistVLC"
    with WinRegistry() as client:
        test_entry = client.read_entry(TEST_REG_PATH, "Icon")
        try:
            vlcexe = regex.findall('"[^"]+vlc.exe"', test_entry.value)[0].strip('"')
            print(drucker.f.black.brightgreen.italic(f"vlc.exe Found! {vlcexe}"))
        except Exception as Fehler:
            print(drucker.f.black.brightred.italic(f"vlc.exe not found!"))
            print(drucker.f.black.brightyellow.italic(f"Please select VLC.EXE"))
            vlcexe, _ = datei_auswaehlen_mit_tkinter()
            print(Fehler)
    return vlcexe

def random_date(start, end, prop):
    def get_time(start, end, time_format, prop):
        stime = mktime(strptime(start, time_format))
        etime = mktime(strptime(end, time_format))
        ptime = stime + prop * (etime - stime)
        return strftime(time_format, localtime(ptime))
    zeit = get_time(start, end, '%d/%m/%Y %I:%M %p', prop)
    zeit = regex.findall(r'^\d\d/\d\d/\d\d\d\d', zeit)[0]
    zeit = regex.split('/', zeit)
    zeit = [int(x) for x in zeit if len(x) >= 2]
    return zeit

def get_number_from_user(satzdrucken, farbe='brightyellow'):
    anfang = ''
    while not isinstance(anfang, int):
        try:
            anfang = input(drucker.f.black[farbe].italic(satzdrucken))
            anfang = int(anfang)
        except:
            print(drucker.f.black.brightred.italic('\nEingabe konnte nicht verstanden werden!\n'))
    return anfang

if __name__ == '__main__':
    einfuehrung('Datumnator')
    vlcpath = get_vlc_exe_path()
    gesamtpunkte = 0
    userpunkte = 0
    anzahlaufgaben = get_number_from_user(satzdrucken='\nWie viele Aufgaben sollen erstellt werden?\n', farbe='brightgreen')
    wieoftwiederholen = get_number_from_user(satzdrucken='\nWie oft soll das Audio wiederholt werden?\n', farbe='brightmagenta')

    for aufgabenz in range(anzahlaufgaben):
        lesenhoeren = auswahlmenu_erstellen(optionen=['Nur Audio', 'Audio und Text'], uberschrift='\nMöchtest du nur das Datum hören oder auch lesen?\n', color='brightgreen', unterdemtext='\nDeine Auswahl\n')

        zeit = random_date("1/1/1970 1:30 PM", "1/1/2098 4:50 AM", random.random())
        ausgeschrieben = 'am ' + tagedict[zeit[0]] + ' ' + monatdict[zeit[1]][random.randrange(0,2)] + ' ' + jahredict[zeit[2]][0]
        zeitstring = [str(x) + '.' for x in zeit]
        zeitstring = "".join(zeitstring).strip('.')
        mp3datei = r'zahlen_temp_audioxxxxxx.mp3'
        kommando_google_stimme = f'gtts-cli "{ausgeschrieben}" --lang de --output {mp3datei}'
        os.system(kommando_google_stimme)
        #wieoftwiederholen = 1
        kommando_abspielen_mit_vlc = fr'"{vlcpath}" --input-repeat={wieoftwiederholen} -Idummy --play-and-exit {mp3datei}'
        if lesenhoeren == '2':
            print(drucker.f.black.brightgreen.italic(f'\n{ausgeschrieben}\n'))
        os.system(kommando_abspielen_mit_vlc)
        usereingabe = input(drucker.f.black.brightmagenta.negative(
            '\nSchreibe das Datum: TT.MM.JJJJ \n'))
        usereingabekonvertiert = regex.findall(r'\d+', usereingabe)
        usereingabekonvertiert = [int(x) for x in usereingabekonvertiert]
        try:
            if usereingabekonvertiert[0] == zeit[0] and usereingabekonvertiert[1] == zeit[1] and usereingabekonvertiert[2] == zeit[2]:
                richtig()
                continue

            falsch(richtigeantwort=f'{zeitstring} / {ausgeschrieben}')
        except:
            falsch(richtigeantwort=f'{zeitstring} / {ausgeschrieben}')

    print(drucker.f.black.brightyellow.italic('\nDu hast ') + drucker.f.brightyellow.black.italic(f'     {userpunkte}     ') + drucker.f.black.brightyellow.italic(' von insgesamt ') + drucker.f.brightyellow.black.italic(f'     {gesamtpunkte}     ') + drucker.f.black.brightyellow.italic(' erreicht\n'))

