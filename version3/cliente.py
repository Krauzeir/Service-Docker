import urllib.request
import json
import time
import pandas as pd

# rotas do servico de noticias (jogatina)
JOGATINA_URL_SERVICO = "http://172.28.1.1:5000/"
JOGATINA_IS_ALIVE = JOGATINA_URL_SERVICO + "isalive/"
JOGATINA_NOTICIAS = JOGATINA_URL_SERVICO + "noticias/"

# rotas do servico de noticias (sistemas)
SISTEMAS_URL_SERVICO = "http://172.28.1.2:5000/"
SISTEMAS_IS_ALIVE = SISTEMAS_URL_SERVICO + "isalive/"
SISTEMAS_NOTICIAS = SISTEMAS_URL_SERVICO + "noticias/"


def acessar(url):
    print("acessando a url:", url)

    response = urllib.request.urlopen(url)
    data = response.read()

    return data.decode("utf-8")


def jogatina_is_alive():
    alive = False

    if acessar(JOGATINA_IS_ALIVE) == "yes":
        alive = True

    return alive

def sistemas_is_alive():
    alive = False

    if acessar(SISTEMAS_IS_ALIVE) == "yes":
        alive = True

    return alive


def get_jogatina():
    data = acessar(JOGATINA_NOTICIAS)
    noticias = json.loads(data)

    return noticias


def get_sistemas():
    data = acessar(SISTEMAS_NOTICIAS)
    noticias = json.loads(data)

    return noticias


def imprimir_noticias(noticias):
    frame = pd.DataFrame(noticias)
    print(frame.T)


if __name__ == "__main__":
    while True:
        # verificar se o servico de jogatina estah ativo
        if jogatina_is_alive():
            # se estiver ativo
            print("serviço de jogatina está ativo. Solicitando noticias...")
            # imprimir as noticias sobre jogos eletronicos
            noticias = get_jogatina()
            imprimir_noticias(noticias)
        # se nao estiver (ativo) informar que o servico estah inativo
        else:
            print("serviço de jogatina não está ativo!")

        # verificar se o servico de sistemas estah ativo
        if sistemas_is_alive():
            # se estiver ativo
            print("serviço de sistemas está ativo. Solicitando noticias...")
            # imprimir as noticias sobre sistemas operacionais
            noticias = get_sistemas()
            imprimir_noticias(noticias)
        # se nao estiver, informar que o servico estah inativo
        else:
            print("serviço de sistemas não está ativo!")

        time.sleep(5)
