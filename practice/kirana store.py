sum=0
i=1
while True:
    price=input()
    if price=="q":
        break
    
    print(f"Enter the price of item{i}: Rs.{price}")
    with open("Recipt.txt","a") as f:   
        f.write(f"Price of item{i}: Rs.{price}\n") 
        
    i=i+1
    sum=sum+int(price)

with open("Recipt.txt","a") as f:   
        f.write(f"Total bill: Rs.{sum}\n\n")
print(f"Total bill: Rs.{sum}")