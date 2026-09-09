from flask import Flask, request

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
    insituicoesEnsino = [{"co_inep": "123456"}, {"co_inep": "654321"}]
    coInep = request.args.get("co_inep")
    if coInep is not None:
        insituicoesEnsino = [
            insituicaoEnsino for insituicaoEnsino in insituicoesEnsino if insituicaoEnsino["co_inep"] == coInep]
    return insituicoesEnsino, 200


@app.get("/instituicoesensino/<int:id>")
def getByIdInstituicoes(id):
    return {"id": "1", "co_inep": "123456"}, 200


@app.post("/instituicoesensino")
def postInstituicoes():
    data = request.get_json()
    coInep = data.get("co_inep")
    return {"id": 1, "co_inep": coInep}, 201


@app.put("/instituicoesensino/<int:id>")
def putInstituicoes():
    pass


@app.delete("/instituicoesensino/<int:id>")
def deleteInstituicoes():
    pass


def main(arg=[]):
    app.run(debug=True)


if __name__ == '__main__':
    main()
