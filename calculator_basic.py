#somple calculator
print("calculate")
n1 = float(input("enter no 1: "))
n2 = float(input("enter no 2: "))
operator = input("enter operator +,-,*,/: ")
if operator == '+':
  print(n1,'+',n2,'=',n1+n2)
  result = n1+n2
elif operator == '-':
  print(n1,'-',n2,'=',n1-n2)
  result = n1-n2
elif operator == '*':
  print(n1,'*',n2,'=',n1*n2)
  result = n1*n2
elif operator == '/':
  print(n1,'/',n2,'=',n1/n2)
  result = n1/n2
else:
  print('invalid')
print("result : ",result)
i=3
while(True):
    operator = input("enter operator +,-,*,/: ")
    
    
    #print(ni,'=','ni')
    if operator == '+':
        ni = float(input(""))
        print(result,'+',ni,'=',result+ni)
        result = result+ni
    elif operator == '-':
        ni = float(input(""))
        print(result,'-',ni,'=',result-ni)
        result = result-ni
    elif operator == '*':
        ni = float(input(""))
        print(result,'*',ni,'=',result*ni)
        result = result*ni
    elif operator == '/':
        ni = float(input(""))
        print(result,'/',ni,'=',result/ni)
        result = result/ni
    else:
        break

print("result : ",result)


