import pickle

ruta = 'high_score'
file = open(ruta, 'wb')

pickle.dump([ (-1,'') ], file)

file. close()

