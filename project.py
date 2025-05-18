test_dic={'codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'coding' : 1}
print("the original dictionary is : " +str(test_dic))
a=int(input("enter value you want to check: "))
res=0
for key in test_dic:
    if test_dic[key]==a:
        res=res+1
        print("frequency for a is: "+ str(res))