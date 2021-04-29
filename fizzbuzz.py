import time
starttime = time.clock()
a = []
for i in range(1,100):
    if  i % 3 ==0 and i % 5 == 0 :
        a.append("fizzbuzz")
    if  i % 3 == 0 :
        a.append("fizz")
    elif  i% 5 ==0 :
        a.append("buzz")
    else:
        a.append(i)
        
print(a)
endtime = time.clock()
print("Duration {}".format(endtime - starttime))