
import pickle
ruta = 'high_score'
file = open(ruta,'rb')
lista = pickle.load(file)
file.close()

print(lista)
