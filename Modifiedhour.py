#Python program to get all  
# sublist from a given list  
# function to generate all the sub lists 
def getsublist(A): 
   # store all the sublists  
   B = [[ ]] 
      
   # first loop  
   for i in range(len(A) + 1):   
      # second loop  
      for j in range(i + 1, len(A) + 1):         
         # slice the subarray  
         sub = A[i:j] 
         B.append(sub) 
   return B 

c=getsublist([[1,2,3],[2,3,4],[1,2,4],[2,3,5]])
#print(c)

def onlysubmulti(c):
    k=[]
	   for i in c:
    	   if type(i)==list and len(i)==3:
        	   #print(i)
			          l=0
			          for p in i:
    			          for j in p:
        			          l+=p.count(j)
			              if l==9:
    			              print(i)
				                 k.append(i)	
	   return k

print(onlysubmulti(c))#print all 3x3 matrix	

h=onlysubmulti(c)

def gethour_glass(h):
    dic=[i for i in range(1,len(h)+1)]#create a dictionary
    final_dic=dict(zip(dic,h))
    print(final_dic)
    for item in final_dic.items():
        item[1].pop(0)
        item[1].pop(1)
        
    print(final_dic)

gethour_glass()    
        

		
