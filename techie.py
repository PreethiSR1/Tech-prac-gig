import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here
T = int(input())

        

if (T < 11 and T > 0):
    N,M = input().split()
    N = int(N)
    M = int(M)   
    for l in range(T):
        if N < 1001 and N > 0: 
            cp = list(map(int, input().strip().split()))[:N]
            sp = list(map(int, input().strip().split()))[:N]  
            cpt = 0
            spt = 0
            total = 0
            for i in cp:
                if(i < 1000001):
                    cpt = cpt + i
                
                
            for j in sp:
                if(j < 1000001):
                    spt = spt + j
            
            total = cpt + spt
            print(total)
            if( M > 0 and M <= 10^15):
                if total <= M and total > 0:
                    print ("YES")
                else:
                    print ("NO")
                    
            

