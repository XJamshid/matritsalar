
import random 
from math import pow
def fact(n):
    s=1
    i=1
    while i<=n:
        s=s*i
        i+=1
    return s
def inv(nums):
    k=0
    i=0
    while i<len(nums):
        j=len(nums)-1
        while j>i:
            if nums[i]>nums[j]:
                k+=1
            j-=1
        i+=1
    return k
'''print(f"n-tartibli determinantning qiymatini topish dasturi")
n=int(input(' n ni kiriting>>'))
nums=[]
i=0
while i<n:
    j=0
    nums4=[]
    while j<n:
        a=float(input(f'a{i+1}{j+1}='))
        nums4.append(a)
        j+=1
    nums.append(nums4)
    i+=1
i=0
while i<n:
    j=0
    while j<n:
        print(f'{nums[i][j]}  ',end="")
        j+=1
    print('\n')
    i+=1
a=len(nums)
nums1=list(range(1,a+1))
nums2=nums1[:]
sonlar=[]
b=0
s=0
while True:
    k=pow(-1,inv(nums2))
    
    if nums2 not in sonlar:
        j=0
        #print(nums2,"orinlashtirish")
        while j<a:
            k=k*nums[nums1[j]-1][nums2[j]-1]
            #print(k,"inversiya a")
            j+=1
        s+=k
        #print(s,"yigindi")
        b+=1
    
    nums3=nums2[:]
    sonlar.append(nums3)
   # print(sonlar)
    random.shuffle(nums2)
    if b==fact(a):
        break
print(f'Determinantning qiymati {s}')'''

def matritsa(A):
    i=0
    n=len(A)
    while i<n:
        j=0
        while j<n:
            print(f'{A[i][j]}  ',end="")
            j+=1
        print('\n')
        i+=1

'''A=[[1,2,3],[4,5,6],[7,8,9]]
boshqa_matritsa=[[3,5,6],[1,2,3],[7,8,9]]
i=0
a=len(A)
while i<a:
    j=0
    while j<a:
        A[i][j]+=boshqa_matritsa[i][j]
        j+=1
    i+=1'''

'''if len(A[0])==len(B):
    i=0
    C=[]
    while i<len(A):
        j=0
        while j<len(B[0]):
            k=0
            #cij=1
            c=0
            while k<len(A):
                cij=A[i][k]*B[k][j]
                c+=cij
                k+=1
            C.append(c)
            j+=1
        i+=1'''
'''def a_toldiruvchi(E,i,j):
    A=E[:]
    pass
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[3,5,6],[1,2,3],[7,8,9]]
M=A[:]
del M[0]
#print(A)
#print(M)'''
def transp(A):
    n=len(A[0])
    C=[]
    k=len(A)
    i=0
    while i<n:
        D=[]
        j=0
        while j<k:
           D.append(A[j][i])
           j+=1
        C.insert(i,D)
        i+=1
    return C
def a_toldiruvchi(A,i,j):
    B=A[:]
    del B[i]
    B=transp(B)
    del B[j]
    B=transp(B)
    return B
aij=[[2,-3,1],[4,-5,2],[5,-7,3]]
C=aij[:]
aij=tuple(aij)
C[0][0]=1
print(aij)
print(C)

        
        
        
            