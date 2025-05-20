# Projekts
Projekta mērķis ir automātiski iegūt un salīdzināt aktuālās dīzeļdegvielas cenas no trīs tuvākajām DUS Imantā, zinot, ka Neste un CircleK ir vienmēr lētākās cenas Imantā, bet Viada atšķiras par +0.01 centu. Programma apmeklē katras stacijas mājaslapu, nolasot dīzeļdegvielas cenu un vietu, kur šī cena ir spēkā, un izvada šo informāciju lietotājam saprotamā veidā.

Izmantotās Python bibliotēkas un to nozīme
selenium

Degvielas staciju mājaslapas ielādē datus ar JavaScript, tāpēc ar parastu HTTP pieprasījumu (requests) nepietiek. Selenium ļauj automatizēt pārlūka darbību, lai iegūtu pilnībā ielādētu lapas saturu.
Tiek izmantots, lai atvērtu lapu, sagaidītu tabulas ielādi un iegūtu lapas HTML kodu.

BeautifulSoup (bs4)

Lai ērti un strukturēti apstrādātu HTML saturu un atrastu vajadzīgos datus (tabulas, rindas, kolonnas).
Tiek izmantots, lai parsētu HTML un atrastu konkrētas tabulas rindas ar degvielas cenām.

selenium.webdriver.chrome.options.Options, WebDriverWait, expected_conditions

Lai konfigurētu pārlūku (piemēram, headless režīms), sagaidītu, kad lapa pilnībā ielādējas, un nodrošinātu stabilu darbību.

Projektā tiek izmantotas funkcijas, kas atgriež kortežu ar divām vērtībām: (cena, vieta).

def get_neste_dizelis(url):
    ...
    return cena, vieta
    
Izvade uz 19.05.:

Aktuālās dīzeļdegvielas cenas:
Neste: 1.457 €/L (Visās stacijās cenas vienādas)
Circle K: 1.441 €/L (Gunāra Astras iela 17)
Viada: 1.434 EUR €/L (DUS Dārzciema: Dārzciema iela 69, Rīga, DUS Dārzciema 2: Dārzciema iela 62.)
    
