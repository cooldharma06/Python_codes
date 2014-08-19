########
## Author Dharmalingam S <cooldharma06@gmail.com>
## Compiler program
## Found any error means kindly mail me; with output screen ..:)
#########

#! /usr/bin/python

print "kindly enter your program as string - contains { } ( ) < > p..."
print "example inputs are ... {<>(p)}.."
list = str(raw_input())
temp = []
result = []
pcount,lt,gt,brac,brkt = 0,0,0,0,0


for i in list:
     temp.append(i)
     if i=="<":
       lt=lt+1
       print lt
     elif i==">":
       gt=gt+1
       print gt
     elif i=="{":
       brac=brac+1
     elif i=="}":
       brac=brac-1
     elif i=="(":
       brkt=brkt+1
     elif i==")":
       brkt=brkt-1
     else:
       continue

print lt,"..",gt,"..",brac,"...",brkt

if (gt==1 and lt ==1 and brac == 0 and brkt==0):
     if (temp[0]!="{" and temp[-1]!="}"):
        print "condition failed seems errors"
        exit()
     print "condition 1 passed continue..."
else:
     print "invalid strings"
     exit()

temp.reverse()


while len(temp) != 0:
   ele = temp.pop()
   try:
     if (ele == "{"):
        result.append(ele)
     elif ele == "(":
        if (temp[-1]=="("):
           print "condition failed () user defined function"
           break
        result.append(ele)
        while (temp[-1] == "p"):
          temp.pop()
          pcount = pcount+1
          if (pcount > 100):
             print "Sorry instruction limit exceeds.."
             break
     elif ele == "<":
        if (result[-1]=="("):
           print "condition failed () user defined function"
           break
        result.append(ele)
        if temp[-1] != ">":
           break
     elif ele == "}":
        if (result[-1]=="{"):
           result.pop()
        else:
           break
     elif ele == ")":
        if (result[-1]=="("):
           result.pop()
           pcount =0
        else:
           break
     elif ele==">":
        if (result[-1]=="<"):
           result.pop()
        else:
           break
     else:
        continue  # p things have not written
     print result
   except:
     print "Compilation errors"
     break


if len(temp)==0:
    print "Great ...No compilation errors"
else:
    print "i think some errors"
