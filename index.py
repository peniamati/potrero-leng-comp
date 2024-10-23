from flask import Flask, render_template  # Llamar a la librería Flask

app = Flask(__name__)  # Crear una instancia de Flask


@app.route('/')  # Ruta inicial
def home():  # Crear una función
    return render_template('home.html')  # Llamar a la plantilla home.html

@app.route('/about')  # Ruta about
def about():  # Crear una función
    return render_template('about.html')  # Llamar a la plantilla about.html

@app.route('/courses')  # Ruta courses
def courses():  # Crear una función
    return render_template('courses.html')  # Llamar a la plantilla courses.html


@app.route('/contact')  # Ruta contact
def contact():  # Crear una función
    return render_template('contact.html')  # Llamar a la plantilla contact.html


# validamos si estamos en el archivo principal para que siempre se quede
# escuchando una peticion del usuario y si se cumple ejecuta el app.run
if __name__ == '__main__':
    app.run(debug=True)  # Ejecutar la aplicación en modo depuración  