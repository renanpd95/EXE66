import os,random,time

par = 0
impar = 0

for i in range(5):
  n = random.randint (0,500)
  print(n)
  time.sleep(0.1)
  
  if(n % 2 == 0):
    par = par+1
  elif(n % 2 == 1):
    impar = impar+1
    
else:
  os.system('clear')
  print("Pares: ",par)
  print("Impar: ",impar)
  
  
    
  

