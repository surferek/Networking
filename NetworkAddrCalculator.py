#!/usr/bin/python
#coding: utf-8

import random
import math

number1=random.randint(0,255)
number2=random.randint(0,255)

IP=[172,23,number1,number2]
MASK=[255,255,254,0]


def decToBin(IPaddr):
    wynik=[]
    for i in IPaddr:
        #print(i)
        liczbaDziesietna=i
        bin=""
        while liczbaDziesietna > 0:
            bin = str(liczbaDziesietna % 2) + bin
            liczbaDziesietna = liczbaDziesietna / 2
        if len(bin)==8:
            wynik.append(bin)
        else:
            while len(bin)<8:
                bin = str(0)+ bin
            wynik.append(bin)
        #print wynik

    return "".join(wynik)


def binToDec(binaryString):

    wynik=[]
    toList = map(''.join, zip(*[iter(binaryString)] * 8))

    for i in toList:
        wynik.append(int(i,2))
    return wynik


def SumAND(IPaddr, MASKaddr):

    wynik=[]
    for i,j in zip(IPaddr,MASKaddr):
        #print i, j
        if i == str(1) and j==str(1):
            wynik.append(str(1))
        else:
            wynik.append(str(0))

    return "".join(wynik)


def SumNOT(MASKaddr):
    #print MASKaddr
    wynik = []

    for i in MASKaddr:
        #print i
        if not i != str(0):
            wynik.append(str(1))
        else:
            wynik.append(str(0))

    return "".join(wynik)


def broadcastAddr(localIP,binMASK):
    #print(localIP)
    revMASK= binToDec(binMASK)

    wynik=[]
    for i,j in zip(localIP,revMASK):
        wynik.append(i+int(j))

    return wynik

def maxHOST(IPaddr,MASK):
    binIP=decToBin(IPaddr)
    binMask=decToBin(MASK)
    shortMask = 0
    binIP=len(binIP)

    for i in binMask:

        if i == str(1):
            shortMask+=1
        else: pass
    wynik=math.pow(2,(binIP-shortMask))-2

    return wynik


print "Binarne IP: \n"+ decToBin(IP)
print "Binarna Maska: \n"+decToBin(MASK)
print "Wynik obliczenia AND (Adres sieci binarny): \n"+SumAND(decToBin(IP),decToBin(MASK))


BinStr=SumAND(decToBin(IP),decToBin(MASK))
print "Asres sieci: ",binToDec(BinStr)


MaskNOT=SumNOT(decToBin(MASK))
print "Adres rozgloszeniowy sieci: ", broadcastAddr(binToDec(BinStr),MaskNOT)


print "Maksymalna liczba hostow: ",maxHOST(IP,MASK)