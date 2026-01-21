#Program 1 | "11" in base 2 = 3 in decimal
a=int("11",2)
print(a)

#Program 2 | Medium
x=10
if x>5:
    if x>15:
        print("Big")
    else:
        print("Medium")

#Program 3 | No
x=0
if x>3:
    print("Yes")
else:
    print("No")

#Program 4 | A
x=5
if x>3:
    print("A")
else:
    print("b")

#Program 5 (True+1*2) (1+2)
print(True+True*2)

#Program 6 | Python treats them as the same value in a set. True==1 & list skips dublicate values {1,1,}
s={1, True, 1.0}
print(len(s))

#Program 7 | str=(old,new,Count)
s="python programming program"
print(s.replace("p","T",3))

#Program 8 | Python treats them as the same value in a set. True==1 & list skips dublicate values
d={}
d[1]="A"
d[True]="B"
print(d)

#Program 9 | Python allows negative indices to access elements from the end of a list
a=[10,20,30,40]
print(a[-3])

#Program 10 | chained comparisons. 5 > 3 and 3 > 1, True and True, True
print(5>3>1)

#Program 11 | 2
d={1:"one", "1":"one"}
print(len(d))

#Program 12 | [1,9,4]
x=[1,2,3,4]
x[1:3]=[9]
print(x)

#Program 13 | Python
text="Python"
text.lower().replace("p","X")
print(text)

#Program 14 | Error
#s="python"
#s[0]="P"
#print(s)

#Program 15 | 
nums = [3,8,2,6]
i = nums[0] + nums[2]
print(i)
j=nums[i%4]
print(j)