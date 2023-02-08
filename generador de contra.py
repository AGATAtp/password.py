import random 
mayusculas = "abcdefghijklmnñopqrstuvwxyz"
minusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "1234567890"
simbolos = "!@#$%^&*/?"

ancho_banda= 8
uso_para = mayusculas + minusculas + simbolos + numeros
contraseña = "".join(random.sample(uso_para,ancho_banda))

print("tu contraseña es:"+ contraseña)