import re
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "https://fastapi.polverini.com.ar",
    "http://localhost:3000",
    "http://localhost:3080",
    "https://rpolverini.github.io",

]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Transposicion(BaseModel):
    texto: str
    semitonos: int


class Translate(BaseModel):
    texto: str

@app.post("/transpose/oneNote")
def transpose_one_note(transposicion: Transposicion):
    transponer_semitonos = transposicion.semitonos
    lista_notas_do = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    transposicion.texto = transposicion.texto.upper()
    try:
        posicion = lista_notas_do.index(transposicion.texto)
        posicion_transp = posicion + transponer_semitonos
        if posicion_transp > 11:
            posicion_transp = posicion_transp - 12
        return {"entro": transposicion.texto, "transp": lista_notas_do[posicion_transp]}

    except ValueError:
        raise HTTPException(status_code=404, detail="a este recurso deberias enviar solamente de a una nota en cifrado americano (ejemplo DO=C Fa# = F#")

# C a Bb son 2 semitonos--- C a Eb son 9 semitonos
# Eb a Bb son 5 semitonos- de alto a tenor
@app.post("/transpose/string/")
def transpose_string(transposicion: Transposicion):
    transposicion.texto = transposicion.texto.upper()
    notas_a_transponer = re.sub(' +', ' ', transposicion.texto)
    notas_a_transponer = notas_a_transponer.split(" ")

    transponer_semitonos = transposicion.semitonos
    lista_notas_do = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    lista_transpuesta = []
    for nota in notas_a_transponer:
        try:
            posicion = lista_notas_do.index(nota)
            posicion_transp = posicion + transponer_semitonos
            if posicion_transp > 11:
                posicion_transp = posicion_transp - 12
            lista_transpuesta.append(lista_notas_do[posicion_transp])
        except ValueError:
            raise HTTPException(status_code=404, detail="Alguna No es una nota correcta che...")

    return {"entro": transposicion.texto, "transp": lista_transpuesta}

@app.post("/translate/popularToAmericano/")
def translate_song_doremi_cde(translate: Translate):
    translate.texto = translate.texto.upper()
    notas_a_transponer = re.sub(' +', ' ', translate.texto)
    notas_a_transponer = notas_a_transponer.split(" ")

    lista_notas_do = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    lista_notas_Popular = ["DO", "DO#", "RE", "RE#", "MI", "FA", "FA#", "SOL", "SOL#", "LA", "LA#", "SI"]

    lista_transpuesta = []
    for nota in notas_a_transponer:
        try:
            posicion = lista_notas_Popular.index(nota)
            posicion_transp = posicion
            if posicion_transp > 11:
                posicion_transp = posicion_transp - 12
            lista_transpuesta.append(lista_notas_do[posicion_transp])
        except ValueError:
            raise HTTPException(status_code=404, detail="Alguna No es una nota correcta che...")

    return {"entro": translate.texto, "transp": lista_transpuesta}


@app.post("/translate/americanoToPopular/")
def translate_song_cde_doremi(translate: Translate):
    translate.texto = translate.texto.upper()
    notas_a_transponer = re.sub(' +', ' ', translate.texto)
    notas_a_transponer = notas_a_transponer.split(" ")

    lista_notas_do = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    lista_notas_Popular = ["DO", "DO#", "RE", "RE#", "MI", "FA", "FA#", "SOL", "SOL#", "LA", "LA#", "SI"]

    lista_transpuesta = []
    for nota in notas_a_transponer:
        try:
            posicion = lista_notas_do.index(nota)
            posicion_transp = posicion
            if posicion_transp > 11:
                posicion_transp = posicion_transp - 12
            lista_transpuesta.append(lista_notas_Popular[posicion_transp])
        except ValueError:
            raise HTTPException(status_code=404, detail="Alguna No es una nota correcta che...")

    return {"entro": translate.texto, "transp": lista_transpuesta}

