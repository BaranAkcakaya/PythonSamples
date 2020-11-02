# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:28:52 2019

@author: lenovoz
"""
"""
x='05464'
dosya=open('aaa.txt','a')
with open("ödev.txt","r+") as file:
    file.read()
    for i in range(0,1000):
        a=file.seek(66*i)
        if(file.readline(5)==x):
            file.seek(66*i)
            file.write('*****:***************:********************:**********:**********')
            dosya.write(str(a)+'\n')
            break
dosya.close()
file.close()
"""
class node:
        def __init__(self,data):
            self.data=data
            self.next=None 
class linkedList:
    def __init__(self):
        self.start=None
    def deleteFirst(self):
        if(self.start==None):
            print("Liste Boş.")
        else:
            self.start=self.start.next   
    def insert(self,value):
        newNood=node(value)
        if(self.start==None):
            self.start=newNood
        else:
            temp=self.start
            while(temp.next!=None):
                temp=temp.next
            temp.next=newNood
    def viewList(self):
        if(self.start==None):
            print("Liste Boş.")
        else:
            temp=self.start
            while(temp!=None):
                print(temp.data,end='')
                temp=temp.next
    def firstData(self):
        if(self.start==None):
            print("Liste Boş.")
        else:
            return self.start.data
            
            
mylist=linkedList()
mylist.insert(10)
mylist.insert(20)
mylist.insert(30)
a=mylist.firstData()
print(a)
if(mylist.start==None):
    print("sada")

            
            
            
            
            