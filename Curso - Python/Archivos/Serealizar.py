import pickle

inf =[35,88,3.14,16]
with open("ArchivoSerial","wb") as binFile:
    pickle.dump(inf,binFile)

print("Archivo binario escrito")

with open("ArchivoSerial","rb") as binFile:
    lista = pickle.load(binFile)
    print(lista)

print("Archivo binario leido y reconstruido.")