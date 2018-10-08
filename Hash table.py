# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 18:26:59 2018

@author: johor
"""
import math
import random

class HashData:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        

class SeparateChainingHash:
    def __init__(self, size, hashToUse):
        self.size = size
        self.table = [None] * self.size
        self.hashToUse = hashToUse

    def hashDivision(self,key):
        return hash(key) % self.size

    def hashMultiplication(self, key):
        A = 0.13
        return hash(math.floor(self.size*((key*A)%1)))

    def hashUniversalInt(self, key):
        p = 100003
        a = 10321
        b = 4993
        return hash((((a*key)+b)% p)% self.size)
    
    def wichHash(self,key):
        
        if(self.hashToUse == 1):
            return self.hashDivision(key)
        elif(self.hashToUse == 2):
            return self.hashMultiplication(key)
        elif(self.hashToUse == 3):
            return self.hashUniversalInt(key)
 

    def reHash(self, entry, key, value):
        while entry and entry.key != key:
            prev, entry = entry, entry.next
        if(entry):
            entry.value = value
        else:
            prev.next = HashData(key, value)

    def set(self, key, value):
        slot = self.wichHash(key)
        entry = self.table[slot]
        if(not entry):
            self.table[slot] = HashData(key, value)
        else:
            self.reHash(entry,key, value)

    def get(self, key):
        hash = self.wichHash(key)
        if(not self.table[hash]):
            raise KeyError
        else:
            entry = self.table[hash]
            while(entry and entry.key != key):
                entry = entry.next
            return entry.value
        

    
test1 = SeparateChainingHash(100,1)
    
for i in range(100):
    key = random.randint(0,999)
    value = random.randint(0,999)
    test1.set(key,value)
    print(key)
    

    
        
