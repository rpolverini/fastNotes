<p align="center">
  <img src="NotesLogo.png" alt="NotesAPI">
</p>
<p align="center">
    <em>FastNotes, musical notes transposition Api, specially for saxophonists but free for all friendly musicians :D</em>
</p>


# Api para transposición de notas musicales

En principio la idea es tener algunos endpoints que permitan transponer notas musicales de a una, y en "conjunto", para poder pasar los arreglos que tenia para saxofon Alto, para poder practicar con el Soprano y Tenor.

# Lanzar localmente
 Se recomienda crear entorno limpio de python3 con virtualenv 

 git clone https://github.com/rpolverini/fastNotes.git

 pip install -r requirements.txt 

 uvicorn main:app

# Lanzar Con Docker
sudo docker build -t fast_notes_image .

sudo docker run -d --name fastNotesContainer -p 80:80 fast_notes_image



# Documentación
Podes verificar la documentación en swagger, gracias a FastAPI 
http://127.0.0.1:8000/docs


#### Roadmap / Todo List
- Deploy en docker container u otra forma serverless.
- Realizar tests unitarios


Al enviar un objeto json con los semitonos a transponer, con esta herramienta los músicos podrán (entre otras):


* **De Piano (Do/C) a saxo Tenor/Soprano **: Transponer de Tonalidad C a Bb son 2 semitonos ("/transpose/string/") 

``` 
 {"semitonos": 2,
 "texto": "a"}
``` 

* **De Piano (Do/C) a saxo Alto **: Transponer de Tonalidad C a Eb son 9 semitonos ("/transpose/string/")

``` 
 {"semitonos": 9,
 "texto": "a"}
``` 

* **De Saxo Alto a saxo Tenor/Soprano  **: Transponer de Tonalidad Eb a Bb son 5 semitonos- de alto a tenor ("/transpose/string/")
``` 
 {"semitonos": 5,
 "texto": "a"}
``` 

* **Traducir**: de cifrado tradicional a cifrado Americano ("/translate/popularToAmericano/"):
``` 
{
 "texto": "LA SI DO"
}
``` 


* **Traducir**: de cifrado Americano a cifrado tradicional ("/translate/americanoToPopular/"):

``` 
{
 "texto": "C D f#"
}
``` 

Pueden verificar cada endpoint gracias a la documentación automatica de FastAPI en localhost/docs


Ver info adicional

https://cdn.shopify.com/s/files/1/1069/0122/files/NOMBRE-DE-ACORDES-ESPANOL-E-INGLES-II_large.jpg

https://thevisualsoundmethod.com/wp-content/uploads/2016/02/tabla-de-transposicion-do-mi-bemol-si-bemol.png
