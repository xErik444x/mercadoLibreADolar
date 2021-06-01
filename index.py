from flask import Flask, render_template, request, jsonify, make_response
from webScrap import calcular,verificarURL


app = Flask(__name__) #Confirmar que es el prinicpal
@app.route("/create-entry", methods=["POST"])
def create_entry():
    req = request.get_json()
    valores = calcular(req["url"])
    res = make_response(jsonify(valores), 200)
    return res
@app.route("/", methods=["GET","POST"]) #pagina principal
def home():
    return(render_template("home.html"))

@app.route("/about")
def about():
    return("About page")


if __name__ == "__main__":
    app.run(debug=True)
