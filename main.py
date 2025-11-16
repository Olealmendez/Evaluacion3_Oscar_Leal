from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            nota1 = float(request.form.get('nota1', 0))
            nota2 = float(request.form.get('nota2', 0))
            nota3 = float(request.form.get('nota3', 0))
            asistencia = float(request.form.get('asistencia', 0))

            promedio = (nota1 + nota2 + nota3) / 3

            if promedio >= 40 and asistencia >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"

            return redirect(url_for('ejercicio1', promedio=promedio, estado=estado))

        except (ValueError, TypeError):
            return redirect(url_for('ejercicio1', error="Datos inválidos"))

    promedio = request.args.get('promedio')
    estado = request.args.get('estado')
    error = request.args.get('error')

    return render_template('ejercicio1.html', promedio=promedio, estado=estado, error=error)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form.get('nombre1', '').strip()
        nombre2 = request.form.get('nombre2', '').strip()
        nombre3 = request.form.get('nombre3', '').strip()

        nombres = [nombre1, nombre2, nombre3]

        nombre_mayor = ""
        longitud_mayor = -1

        for nombre in nombres:
            longitud_actual = len(nombre)

            if longitud_actual > longitud_mayor:
                longitud_mayor = longitud_actual
                nombre_mayor = nombre

        return redirect(url_for('ejercicio2', nombre_mayor=nombre_mayor, longitud_mayor=longitud_mayor))

    nombre_mayor = request.args.get('nombre_mayor')
    longitud_mayor = request.args.get('longitud_mayor')

    return render_template('ejercicio2.html', nombre_mayor=nombre_mayor, longitud_mayor=longitud_mayor)


if __name__ == '__main__':
    app.run(debug=True)