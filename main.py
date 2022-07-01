# Importing Modules
import jason as js
from fastapi import FastAPI


# Creating FastAPI app object

app=FastAPI()


@app.get('/stockdata')
def stockdata():
    return js.object_Data.Data()


@app.get('/symbol')
def symbol():
    return js.obj_symbol.SymbolData()