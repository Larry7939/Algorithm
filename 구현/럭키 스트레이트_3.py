N = list(map(int, input()))
length = len(N)
half_length =len(N)//2   
if sum(N[half_length:length])== sum(N[:half_length]):
    print("LUCKY")
  
else: 
    print("READY")
