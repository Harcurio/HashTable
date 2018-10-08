# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 18:26:59 2018

@author: johor
"""
import math

class HashData:
    def __init__(self, key, value, hashToUse):
        self.key = key
        self.value = value
        self.next = None
        self.hashToUse = hashToUse

class SeparateChainingHash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hashDivision(self,key):
        return hash(key) % self.size

    def hashMultiplication(self, key):
        A = 0.13
        return hash(math.floor(self.size*((key*A)%1)))

    def hashUniversalInt(size, key):
        p = 100003
        a = 10321
        b = 4993
        return hash((((a*key)+b)% p)% size)


    def reHash(self, entry, key, value):
        while entry and entry.key != key:
            prev, entry = entry, entry.next
        if(entry):
            entry.value = value
        else:
            prev.next = HashData(key, value)

    def set(self, key, value):
        slot = self.hashDivision(key)
        entry = self.table[slot]
        if(not entry):
            self.table[slot] = HashData(key, value)
        else:
            self.reHash(entry,key, value)

    def get(self, key):
        hash = self.hashDivision(key)
        if(not self.table[hash]):
            raise KeyError
        else:
            entry = self.table[hash]
            while(entry and entry.key != key):
                entry = entry.next
            return entry.value
