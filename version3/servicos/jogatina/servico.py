from flask import Flask
from flask import jsonify

servico = Flask(__name__)

# "constantes"
IS_ALIVE = "yes"
VERSION = "0.0.1"
DESCRIPTION = "Servico que retorna noticias sobre jogos eletronicos"
AUTHOR = "Luis Paulo da Silva Carvalho"
EMAIL = "luispscarvalho@gmail.com"

# bd estatico (para testes)
JOGATINA = [
    {
        "id": 1,
        "data": "15/10/2019",
        "titulo": "Stadia, serviço de games na nuvem do Google, será lançado em 19 de Novembro",
        "endereco": "https://g1.globo.com/pop-arte/games/noticia/2019/10/15/stadia-servico-de-games-na-nuvem-do-google-sera-lancado-em-19-de-novembro.ghtml",
    },
    {
        "id": 2,
        "data": "26/04/2019",
        "titulo": "Mortal Kombat: Como fazer todos os fatalities?",
        "endereco": "https://www.uol.com.br/start/ultimas-noticias/2019/04/26/mortal-kombat-11-como-fazer-todas-as-fatalities.htm",
    },
    {
        "id": 3,
        "data": "21/10/2016",
        "titulo": "Conheça 5 distribuições GNU/Linux voltadas para jogos",
        "endereco": "https://sempreupdate.com.br/conheca-5-distribuicoes-gnu-linux-voltadas-para-jogos/",
    }
]

# rotas do meu servico
# rota de ping (o cliente deve perguntar se o servico estah atendendo)
@servico.route("/isalive/")
def is_alive():
    return IS_ALIVE


# rota que retorna informacoes basicas sobre o servico e o autor do servico
@servico.route("/info/")
def get_info():
    info = jsonify(
        version = VERSION,
        description = DESCRIPTION, 
        author = AUTHOR,
        email = EMAIL
    )

    return info

# rota que retorna noticias sobre jogos eletronicos
@servico.route("/noticias/")
def get_jogatina():
    noticias = jsonify(
        JOGATINA
    )

    return noticias

if __name__ == "__main__":
    servico.run(
        host = "0.0.0.0",
        debug=True
    )