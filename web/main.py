from flask import Flask
from sqlalchemy import create_engine
from faker import Faker 

app = Flask(__name__)

connection_db= "postgresql://postgres_user:postgrespwd@db:5432/postgresdb"

app.config["SQLALCHEMY_DATABASE_URI"] = connection_db
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
engine = create_engine(connection_db)


@app.route('/insertar_datos', methods=["POST"])
def insertar_datos():
    fake = Faker()
    try:
        for i in range(10):
            nombre = fake.name()
            telefono = fake.phone_number()

            engine.execute(f"""Insert into usuarios(nombre,telefono) values ('{nombre}','{telefono}')""")
    except:
        return jsonify({"Respuesta":"no se inserto"})
    return jsonify({"Rspuesta":"Datos insertados"})

@app.route('/creartabla',methods=["POST"])
def crear_tabla():
    try:
        engine.execute("create table if not exists usuarios(id serial, nombre varchar(200),telefono varchar(200))")
    except:
        return jsonify({"Respuesta":"FALLE"})
    return jsonify({"Respuesta": "Base de datos creada"})
        
if __name__=="__main__":
    app.run(host="0.0.0.0", port=80)