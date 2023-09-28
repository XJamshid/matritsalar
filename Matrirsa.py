# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 18:07:22 2023

@authorr:XUdoyberdiyev Jamshid
Matritsa va matritsalar ustida amallar
"""
#Kerakli funksiyalar
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
def det(A):
    a=len(A)
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
                k=k*A[nums1[j]-1][nums2[j]-1]
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
    return s
#Matritsa
class Matritsa:
    def __init__(self,A):
        self.A=A
    def __call__(self):
       matritsa(self.A)
    def det(self):
        return det(self.A)
    def __add__(self,boshqa_matritsa):
        i=0
        a=len(self.A)
        while i<a:
            j=0
            while j<a:
                self.A[i][j]=self.A[i][j]+boshqa_matritsa.A[i][j]
                j+=1
            i+=1
        matritsa(self.A)
    def __len__(self):
        return len(self.A)
    def __getitem__(self,index):
        return self.A[index]
    def __setitem__(self,index,qiymat):
        self.A[index]=qiymat
    
    def __sub__(self,boshqa_matritsa):
        i=0
        a=len(self.A)
        while i<a:
            j=0
            while j<a:
                self.A[i][j]=self.A[i][j]-boshqa_matritsa.A[i][j]
                j+=1
            i+=1
        matritsa(self.A)
    def t_matr(self):
       n=len(self.A[0])
       C=[]
       k=len(self.A)
       i=0
       while i<n:
           D=[]
           j=0
           while j<k:
              D.append(self.A[j][i])
              j+=1
           C.insert(i,D)
           i+=1
       matritsa(C)
    def __mul__(self,boshqa_matritsa):
        if isinstance(boshqa_matritsa,Matritsa):
            if len(self.A[0])==len(boshqa_matritsa.A):
                i=0
                C=[]
                while i<len(self.A):
                    D=[]
                    j=0
                    while j<len(boshqa_matritsa.A[0]):
                        k=0
                        #cij=1
                        c=0
                        while k<len(self.A):
                            cij=self.A[i][k]*boshqa_matritsa.A[k][j]
                            c+=cij
                            k+=1
                        D.insert(j,c)
                        j+=1
                    C.insert(i,D)
                    i+=1
            matritsa(C)
        else:
            i=0
            K=self.A[:]
            while i<len(self.A):
                j=0
                while j<len(self.A):
                    K[i][j]*=boshqa_matritsa
                    j+=1
                i+=1
            matritsa(K)
    def teskarisi(self):
        C=[]
        l=1/det(self.A)
        m=len(self.A)
        i=0
        while i<m:
            j=0
            D=[]
            while j<m:
                dij=a_toldiruvchi(self.A, i, j)
                d=det(dij)
                toldiruvchi=pow(-1,i+j)*d*l
                D.insert(j,toldiruvchi)
                j+=1
            C.append(D)
            i+=1
        C=transp(C)
        matritsa(C)
aij=[[2,-3,1],[4,-5,2],[5,-7,3]]
bij=[[3,5,6],[1,2,3],[7,8,9]]
A=Matritsa(aij)
B=Matritsa(bij)
A.t_matr()
