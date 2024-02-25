
import random,getpass,os

declaration = ["te amo",'te quiero','te adoro','te deseo','simpre vale la pena luchar por ti','te escojeria mil veses mas','te extraño','me encantaria verte pronto','verte sonreir es lo mejor','todavia recuerdo la primera ves que te vi','me haces felis','eres mi inspiracion para segir adelante','puedo vivir sin ti pero elijo vivir contigo',]

k:str= getpass.getpass('ingresa el nombre de la persona a la que te quieres declararte: ')
responsable:str = input("ingresa tu nombre: ").upper()

dec=random.choice(declaration) 
declarate:str = '*' *len(k)  

os.system("clear")

print(f'{dec}, solo queria desir eso {declarate} \n con amor {responsable}')

