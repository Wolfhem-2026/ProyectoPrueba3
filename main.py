
# Importamos las herramientas necesarias de Flaskc
from flask import Flask, render_template, request

# Creamos la aplicación
app = Flask(__name__)


# Página principal
@app.route("/")
def inicio():
    return render_template("index.html")


# Ejercicio 1: cálculo de notas y asistencia
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():

    resultado = None
    error = None

    # Comprobamos si el usuario envió el formulario
    if request.method == "POST":

        try:
            # Recibimos los datos del formulario
            nota1 = int(request.form["nota1"])
            nota2 = int(request.form["nota2"])
            nota3 = int(request.form["nota3"])
            asistencia = int(request.form["asistencia"])

            # Validamos los rangos permitidos
            if not all(10 <= nota <= 70
                       for nota in [nota1, nota2, nota3]):
                error = "Las notas deben estar entre 10 y 70."

            elif not 0 <= asistencia <= 100:
                error = "La asistencia debe estar entre 0 y 100."

            else:
                # Calculamos el promedio
                promedio = (nota1 + nota2 + nota3) / 3

                # Verificamos ambas condiciones
                if promedio >= 40 and asistencia >= 75:
                    estado = "APROBADO"
                else:
                    estado = "REPROBADO"

                # Preparamos los datos para HTML
                resultado = {
                    "promedio": round(promedio, 2),
                    "asistencia": asistencia,
                    "estado": estado
                }

        except (ValueError, KeyError):
            error = "Debes ingresar valores numéricos válidos."

    # Mostramos el formulario y su resultado
    return render_template(
        "ejercicio1.html",
        resultado=resultado,
        error=error
    )



# Ejercicio 2: comparación de nombres
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():

    resultado = None
    error = None

    # Comprobamos si se envió el formulario
    if request.method == "POST":

        # Recibimos los tres nombres
        nombre1 = request.form.get("nombre1", "").strip()
        nombre2 = request.form.get("nombre2", "").strip()
        nombre3 = request.form.get("nombre3", "").strip()

        nombres = [nombre1, nombre2, nombre3]

        # Validamos que no existan campos vacíos
        if not all(nombres):
            error = "Debes ingresar los tres nombres."

        # Validamos que sean diferentes
        elif len(set(nombre.casefold() for nombre in nombres)) != 3:
            error = "Los tres nombres deben ser diferentes."

        else:
            # Identificamos el nombre más largo
            nombre_mayor = max(nombres, key=len)

            # Contamos sus caracteres
            cantidad = len(nombre_mayor)

            # Preparamos el resultado
            resultado = {
                "nombre": nombre_mayor,
                "cantidad": cantidad
            }

    # Enviamos el resultado a la página HTML
    return render_template(
        "ejercicio2.html",
        resultado=resultado,
        error=error
    )

# Iniciamos el servidor
if __name__ == "__main__":
    app.run(debug=True)

