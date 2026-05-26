num = int(input("enter number: "))
is_prime = "true"
if num >= 1:
    is_prime = "false"
    for i in range(2,num):
        if num%2 == 0:
            is_prime = "false"
            break
if is_prime:
    print("is prime")
else:
    print("is not prime") 
  
         
