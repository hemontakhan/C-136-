from flask import Flask,jsonify,request
from info import info 

app = Flask(__name__)

@app.route("/")
def greet():
   return jsonify({
       "info":info,
       "message" : "Success"
   }),200

@app.route("/planet")
def planet_info():
    name = request.args.get("name")
    planet_data = next(crux for crux in info if crux["name"]==name)
    return jsonify({
        "data" : planet_data,
        "message":"Succces"
    }),200

if __name__ == "__main__":
    app.run()