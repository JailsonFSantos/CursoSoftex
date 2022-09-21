import time 

def bomb(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⠛⠙⠛⢿⣟⢙⣿⣿⠙⣿⠟⢙⣿⣿⣟⠙⢿⣿⠙⣿⡟⢹⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⠄⣷⡄⢸⣗⢐⣿⣿⠄⣿⠄⡄⢽⣿⠁⠄⢽⣿⢐⣿⣗⢸⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⠄⢙⠑⢼⣗⢐⣿⣿⠄⣿⠄⣗⢸⣟⢰⠅⢽⣿⢐⣿⣗⢸⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⠄⣿⣗⢘⣗⢐⣿⣿⠄⣿⠄⣿⠐⠇⢼⠅⢽⣿⣐⣿⣗⣸⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⠄⠙⢁⣰⣿⡀⠙⠁⢰⣿⠄⣿⡇⢀⣿⠅⢽⣿⠙⣿⡟⢹⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣷⣷⣿⣿⣿⣿⣷⣿⣿⣿⣷⣿⣿⣿⣿⣷⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")    
  
  
t = input("Com quanto tempo a bomba deve explodir?:\n ")
print("iniciando contagem regressiva:")
bomb(int(t)) 