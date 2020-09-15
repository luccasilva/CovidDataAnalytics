import requests
import ast
from bs4 import BeautifulSoup

file = open("dicionario.txt", "r")

contents = file.read()
base_url = ast.literal_eval(contents)

file.close()


def busca_base (base,url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    text = str(soup)

    if base=="AM" or base=="DF":
        with open(base+".csv", "w", encoding="latin1") as f:
            f.write(text)
    else:
        with open(base+".csv", "w", encoding="utf-8") as f:
            f.write(text)

def main():
    for base, url in base_url.items():
        busca_base(base,url)
        print(base +' done!')
    print("All done!")    


if(__name__=="__main__"):
    main()