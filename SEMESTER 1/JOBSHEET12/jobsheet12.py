# -*- coding: utf-8 -*-
"""Jobsheet12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cz-sr8GEQBIvsU88bk74AiGnHJu0pUvx
"""

def rekursif(n):
  if n <= 0:
    print("Zero!")
  else:
    print(n,"A"*n)
    rekursif(n-2)

def main():
  n = eval(input("Masukan nilai n : "))
  rekursif(n)

main()