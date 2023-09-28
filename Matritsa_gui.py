# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 17:00:58 2023

@author: Xudoyberdiyev Jamshid
"""
from tkinter import *
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
'''def list_entrys():
    entrys=[]
    n=int(row_entry.get())
    m=int(column_entry.get())
    for i in range(n):
        d=[]
        for j in range(m):
            entry=Entry(frame2,width=3)
            d.append(entry)
            #entry.grid(row=i,column=j)
        entrys.append(d)
    return entrys
def create():
    n=int(row_entry.get())
    m=int(column_entry.get())
    entrys=[]
    i=0
    while i<n:
        j=0
        d=[]
        while j<m:
            entry=Entry(frame2,width=3)
            d.append(entry)
            entry.grid(row=i,column=j)
            j+=1
        entrys.append(d)
        i+=1
    #button_send=Button(frame2,text='Send')
    #button_send.grid(row=n,column=0,columnspan=m)
    button_determinant=Button(frame2,text='Determinant',command=determinant)
    button_determinant.grid(row=n,column=0,columnspan=m)
    label_result=Label(frame2,text='Result')
    label_result.grid(row=n+1,column=0,columnspan=m)
def determinant(enrtys):
    entrys2=[]
    n=int(row_entry.get())
    m=int(column_entry.get())
    row=0
    while row< n:
        d=[]
        column=0
        while column<m:
            entry=entrys[row][column].get()
            d.append(entry)
            column+=1
        entrys2.append(d)
        row+=1
    a=len(entrys2)
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
                k=k*entrys2[nums1[j]-1][nums2[j]-1]
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
    label_result.config(text=str(s))'''
def determinant():
    entrys2=[]
    n=3
    m=3
    row=0
    while row< n:
        d=[]
        column=0
        while column<m:
            entry=float(entrys[row][column].get())
            d.append(entry)
            column+=1
        entrys2.append(d)
        row+=1
    a=len(entrys2)
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
                k=k*entrys2[nums1[j]-1][nums2[j]-1]
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
    label_result.config(text=str(s))

window=Tk()
window.geometry('420x420')
frame=Frame(window)
frame.pack()
frame2=Frame(window)
frame2.pack()
title_label=Label(frame,
                  text='Matritces',
                  font=('Times New Roman',20),
                  fg='#00FF00',
                  bg='black',
                  relief=RAISED,
                  bd=1,
                  padx=1,
                  pady=0.5
                  )
row_label=Label(frame,
                text='3',
                width=3,
                font=('Times New Roman',20),
                fg='#00FF00',
                bg='black',
                relief=RAISED,
                bd=1,
                padx=1,
                pady=0.5
                )
column_label=Label(frame,
                   text='3',
                   width=3,
                   font=('Times New Roman',20),
                   fg='#00FF00',
                   bg='black',
                   relief=RAISED,
                   bd=1,
                   padx=1,
                   pady=0.5
                   )
title_label.grid(row=0,column=0,columnspan=2)
row_label.grid(row=1,column=0)
column_label.grid(row=1,column=1)
#insert_button=Button(frame,text='Insert',command=insert)
#insert_button.grid(row=2,column=0,columnspan=2)
#n=insert()[0]
#m=insert()[1]
m=3
n=3
entrys=[]
i=0
while i<n:
    j=0
    d=[]
    while j<m:
        entry=Entry(frame2,
                    width=3,
                    font=('Times New Roman',20),
                    fg='#00FF00',
                    bg='black',
                    relief=RAISED,
                    bd=5,
                    )
        d.append(entry)
        entry.grid(row=i,column=j)
        j+=1
    entrys.append(d)
    i+=1
button_determinant=Button(frame2,text='Determinant',command=determinant,
                          font=('Times New Roman',20),
                          fg='#00FF00',
                          bg='black',
                          relief=RAISED,
                          bd=5,)
button_determinant.grid(row=n+1,column=0,columnspan=m)
label_result=Label(frame2,text='Result',
                  font=('Times New Roman',20),
                  fg='#00FF00',
                  bg='black',
                  relief=RAISED,
                  bd=1,
                  padx=1,
                  pady=0.5 )
label_result.grid(row=n+2,column=0,columnspan=m)
#create_button=Button(frame,text='Create',command=create)
#create_button.grid(row=2,column=0,columnspan=2)
window.mainloop()