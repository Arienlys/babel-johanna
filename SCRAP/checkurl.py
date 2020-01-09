""" 
Regarder la doc sur python. Python request
Site d'un journal. 
Re HTTP
Header HTTP
text HTML HTTP
"""
import requests
import json
import os
from bs4 import BeautifulSoup

dataset = []


def get(url):
    """
    On va récupérer le header des sites internet via un url. 
    Avec un user_agent pour passer la sécurité
    """
    user_agent_text = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
    headerdict = {"User-Agent": user_agent_text}
    r = requests.get(url, headers=headerdict)
    r.raise_for_status()
    return r


def get_urls(arglist, is_verbose=False):
    """
    Pour chaque url, on gère le cas ou on ne pourrait pas se connecter pour X raison.
    La dite raison est indiquée.
    """
    for url_en_arg in arglist:
        try:
            r = get(url_en_arg)

        except Exception as e:
            print(f"Erreur de requests vers {url_en_arg}")
            print(str(e))
            r = None

        if r:
            displayurl(r, is_verbose)
            writetodict(r, is_verbose)


"""
Initialisation du premier dictionnaire    
"""
F_URL = "url"
F_STATUS = "status_code"
# F_HTML = "content"
# F_TITLE = "title"


def writetodict(r, is_verbose=False):
    """
    On rempli les dictionnaire que l'on a créé avec les informations récupéré du header ainsi que leur status lors de la connexion.
    la fonction update permet de fusionner les deux dictionnaire
    """
    dict_html = {F_URL: r.url, F_STATUS: r.status_code}  # F_HTML: r.text[:1000]
    dict_meta = search_meta(r.text)
    if dict_meta:
        dict_html.update(dict_meta)

    global dataset
    dataset.append(dict_html)


"""
Initialisation du second dictionnaire
"""
F_DESC = "description"
F_IMG = "image"
F_MURL = "murl"
F_TITLE = "title"
F_DESC = "description"
F_IMG = "image"
F_H1 = "h1"
F_H2 = "h2"


def search_meta(text):
    """
    Utilisation de Beautiful Soup pour mettre en forme et récupérer plus facilement ce que l'on désire
    les différents éléments choisi sont ensuite enregistré dans le dictionnaire qui est retourné.
    """
    soup = BeautifulSoup(text, "lxml")
    dict_meta = dict()

    meta_title = soup.find("meta", property="og:title")
    if not meta_title:
        meta_title = soup.title.string
    else:
        dict_meta[F_TITLE] = meta_title["content"]

    meta_description = soup.find("meta", property="og:description")
    dict_meta[F_DESC] = meta_description["content"] if meta_description else ""

    meta_image = soup.find("meta", property="og:image")
    dict_meta[F_IMG] = meta_image["content"] if meta_image else ""

    d1 = soup.find_all("h1")
    if d1:
        dict_meta[F_H1] = []
        for h1 in d1:
            dict_meta[F_H1].append(h1.text)
            print(f"--> h1 : {h1.text}")

    d2 = soup.find_all("h2")
    if d2:
        dict_meta[F_H2] = []
        for h2 in d2:
            dict_meta[F_H2].append(h2.text)
            print(f"--> h2 : {h2.text}")

    print("-" * 100)
    print(type(meta_title))
    print(meta_title["content"])
    return dict_meta

    """
    s = (
        str(meta_title)
        .replace('<meta content="', "")
        .replace('" property="og:title"/>', "")
    )

    begin = s.find('content="')
    if begin != -1:
        end = s.find('"', begin)
        if end != -1:
            s = s[begin:end]

    print(meta_title["content"])
    print(s)
    print("-" * 100)
    """


"""
def search_title_by_bs4(text):
    # code de la veille
    soup = BeautifulSoup(text, "lxml")
    print(soup.title.string)



    return soup.title.string
"""

"""
def search_title(text):
    # DEPRECIATED! Use Beautiful Soup instead
    retbuffer = begin = 0
    end = None
    begin = text.find("<title>")
    if begin != -1:
        begin += len("<title>")
        end = text[begin:].find("</title>")
        if end != -1:
            end += begin
            retbuffer = text[begin:end]
    print(f"Test search_title : {begin}, {end}, {retbuffer}")
    return retbuffer
"""


def displayurl(r, is_verbose=False):
    """
    récupération des valeurs pour les rentrer dans le premier dictionnaire sous forme de clé valeurs. 
    """
    print(f"->> Il y a {len(r.text)} octets and {r.url}")
    if is_verbose:
        print(r.status_code)
        # print(r.headers)
        # print(json.dumps(r.headers))
        for key, value in r.headers.items():
            print(f"{key} : {value}")

        print("-" * 30)


"""
def displayurl(r):
    print(r)
    print(r.status_code)
    print(r.headers)
    print(r.text)
"""

if __name__ == "__main__":
    ltqp = ["matin", "midi", "soir", "minuit", "aube"]
    for item in ltqp:
        print(item)

    dataset = []
    listedesurls = [
        "https://www.midilibre.fr/",
        "https://www.liberation.fr/",
        "https://www.20minutes.fr/",
        "https://www.lemonde.fr/",
        "https://www.bbc.co.uk/news",
        "https://www.theguardian.com/uk",
        "http://www.leparisien.fr/",
    ]

    get_urls(listedesurls, True)

    # ATTENTION! Dataset est défini en global comme une liste
    print(len(dataset))

    # affiche le nom du fichier .py
    print(__file__)
    # affiche le repertoire absolue pour le système d'exploitation
    print(os.path.abspath(__file__))
    # affiche le repertoire contenant le fichier .py
    print(os.path.dirname(__file__))
    # récupère le répertoire dans la configuration du système d'exploitation
    basedir = os.path.dirname(os.path.abspath(__file__))
    print(basedir)

    dataset_api = {"count": len(dataset), "dataset": dataset}
    # Creation du fichier checkurl.json dans le repertoire scrap
    filename = basedir + "/" + "checkurl.json"
    with open(filename, "w", encoding="utf8") as f:
        json.dump(dataset_api, f)
        print(f"file {filename} created!")
    # prend un objet python et un handle de fichier et écrit dedant

    """
    Ces trois lignes équivalent aux deux lignes du with!!
    
    f= open(test.json", "w+", encoding="utf8")
    json.dump(dataset, f)
    f.close()
    """
