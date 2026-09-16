from flask import Flask, request
from models.instituicaoensino import InstituicaoEnsino
from helpers.file.json import read


def listar():
    # Ler o arquivo json.
    dataset = read("instituicoes.json")
    # Converter o json -> InsitituicaoEnsino.
    instituicoesEnsino = [InstituicaoEnsino(
        row["id"], row["no_entidade"], row["co_entidade"], row["qt_mat_bas"]) for row in dataset]
    # Retorna a lista de InstituicoesEnsino.
    return instituicoesEnsino


app = Flask(__name__)


@app.route("/")
def index():
    return {"versao": "0.0.1"}, 200


@app.route("/health")
def health():
    return {"health": "ok"}, 200

# /instituicoesensino?co_inep=123456


@app.get("/instituicoesensino")
def getAllInstituicoes():
    insituicoesEnsino = listar()
    print("Entrou na requisição")
    coEntidade = request.args.get("co_entidade")
    print(f'Valor do co_entidade do request: {coEntidade}')
    print(f'Itens da lista de instituições:{len(insituicoesEnsino)}')
    if coEntidade is not None:
        insituicoesEnsinoReponse = [
            insituicaoEnsino.toDict() for insituicaoEnsino in insituicoesEnsino if insituicaoEnsino.co_entidade == coEntidade]
    else:
        insituicoesEnsinoReponse = [
            insituicaoEnsino.toDict() for insituicaoEnsino in insituicoesEnsino]

    return insituicoesEnsinoReponse, 200


@app.get("/instituicoesensino/<int:id>")
def getByIdInstituicoes(id):
    instituicoesensino = listar()

    for item in instituicoesensino:
     if int(item.id) == id:
        instituicaoEncontrada = item
        break 
    return instituicaoEncontrada.toDict(), 200


@app.post("/instituicoesensino")
def postInstituicoes():
    data = request.get_json()
    instituicoesensino = listar()


    nova_instituicao = InstituicaoEnsino(
        id=31,
        no_entidade=data.get("no_entidade"),
        co_entidade=data.get("co_entidade"),
        qt_mat_bas=data.get("qt_mat_bas")
    )
    
    instituicoesensino.append(nova_instituicao)
    return nova_instituicao.toDict(), 200


@app.put("/instituicoesensino/<int:id>")
def putInstituicoes(id):
    data = request.get_json()

    instituicoesensino = listar()

   
    for item in instituicoesensino:
     if int(item.id) == id:
        
            
      item.no_entidade=data.get("no_entidade"),
      item.co_entidade=data.get("co_entidade"),
      item.qt_mat_bas=data.get("qt_mat_bas")
     
      break 
    return item.toDict(), 200




@app.delete("/instituicoesensino/<int:id>")
def deleteInstituicoes(id):
      instituicoesensino = listar()
      for item in  instituicoesensino:
         if int(item.id) == id:
              Encontrei = item
              break

      instituicoesensino.remove(Encontrei)
      return {"foi deletado": "teste"}



def main(arg=[]):
    app.run(debug=True)


if __name__ == '__main__':
    main()
