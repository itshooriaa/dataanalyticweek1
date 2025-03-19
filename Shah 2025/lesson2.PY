print("***Welcome***")
name=input("Please tell me your name sir=")
age=int(input("please mention your age:"))
price=int(input("input your budget:"))
color=input("enter your color:")
market=input("enter market name:")
if(price>=100 and color=="red",market=="A"):
    print("2kg" ,"apple" ,"&" ,"bananas")
elif(price>=80 and color=="black",market=="B"):
    print("4kg" ,"apple" , "&" "Bananas")
elif(price>=60 and color=="blue",market=="C"):
    print("6kg" ,"apple" , "&" "Bananas")
elif(price>=40 and color=="white",market=="D"):
    print("8kg" , "apple" , "&" "Bananas")
elif(price>=10 and color=="brown",market=="E"):
    print("10kg","apple" , "&" "Bananas")    
else:
    print("out of budget","apple" , "&" "Bananas")
