## Insertion sort - without duplicates

import pdb

l = [1,2,3,4,5,6,7,8,9,10]
#1,0,10,9,100,-1,9,0,100,-1,3,4,2,4,5,6,7,2,3]

i = 0

while i < len(l)-1:
        pop_value = min(l[i:i+2])
      # with duplicates sorting
        index = l[i:i+2].index(pop_value)
        l.pop(i+index)
        
        print "minimum value.. ",pop_value
        # traverse and keep the element ele < x < ele1
        j = 0
        while j < len(l[:i+1]):
#            pdb.set_trace()
#       To remove duplicates: l[j] == pop_value means break the loop and do nothing 
#       so element will not be insert in the list
            if (l[j] >= pop_value or l[j] == pop_value ):
              l.insert(j,pop_value)
              break
            elif (l[j] <= pop_value and pop_value <= l[j+1] ):
              l.insert(j+1,pop_value)
              break
            j = j+1
        print l
        i = i+1


print l
