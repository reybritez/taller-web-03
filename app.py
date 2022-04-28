from flask import Flask, escape, request, render_template, url_for
import requests #Importar la libreria

app = Flask(__name__) #Inicializamos la app con el nombre.

@app.route('/')
def hola():
    return 'Hi Penguins!' #Retorna Hi Penguins!

@app.route('/coach') #Creamos la ruta coach
def hola_coaches(): #Definimos la funcion que sera devuelta
    nombre = 'Stevencin' #Inicializamos un dato
    devolver = request.args.get('nombre',nombre) #Definimos que sera devuelto y renderizado 
    return f'Hola, {escape(devolver)} ' #Retornamos al html

@app.route('/inicio') #Creamos la ruta inicio
def inicio(): 
    return render_template('inicio.html')

@app.route('/contacto') #Creamos la ruta contacto
def contacto():
    API_KEY= "595695c3" # API key que se consigue en ombdapi.com tras registro
    titulo = "Harry Potter" 
    basic_call= "http://www.omdbapi.com/?apikey=" + API_KEY +"&t="+titulo # Concatenación de URL a la que se realizará la búsqueda
    datos= requests.get(basic_call) # Se ingresa en datos los datos de respuests
    datos=datos.json() # Se convierte a JSON
    titulo_de_pelicula = datos['Title'] # Extraigo el título
    director_de_pelicula = datos['Director'] # Extraigo el director

    datos_filtrados = {'titulo':titulo_de_pelicula, 'director':director_de_pelicula } # Creo el diccionario datos filtrados en el que alojo clave,valor
    return render_template('contacto.html',  datos = datos_filtrados  )
    #return jsonify(datos_filtrados = datos_filtrados)

@app.route('/curriculum') #Creamos la ruta inicio
def cv(): 
    return render_template('cv.html')

if __name__ == "__main__":
    app.run(debug=True) #Para ejecutar


