import webbrowser as w 
import math as m
from statistics import *

def PIZZA():
    w.open("https://www.youtube.com/watch?v=I85R9Uyxt18")

def L(num): #lines
    print("-"*num)
    
def rect(l,h,x): #rectangle length, height, material
    for i in range(h):
        print(str(x)*l)
    
def mean(lst):
    s = 0
    for i in lst:
        s+=i
        
    l = len(lst)
    d = s/l
    return d


def median(lst):
    l = len(lst)
    d = 0
    m = int(l/2)
    
    if l%2==1:
        n1, n2 = lst[m-1], lst[m]
        d = (n1+n2)/2
    
    else:
        d = lst[m-1]
    
    return d


def Range(lst):
    n1, n2 = lst[0], lst[len(lst)-1]
    m = n2 - n1
    return m

def quad(a,b,c): #quadratic formula
    
    x1 = str((-(b) + m.sqrt((b**2)-4*a*c))/(2*a))
    x2 = str((-(b) - m.sqrt((b**2)-4*a*c))/(2*a))
    return x1, x2


def Wcount(st): #word count in string
    g = st.split(" ")
    lst = []
    for i in g:
        count = 0
        for f in range(0, len(g)):
            if (i == g[f]):
                count = count + 1
                
        final = (f"{i}: {count}")
        if final not in lst:
            lst.append(final)
        
    for p in lst:
        print(p)
        

def mth(f,l,d,nm): #something
    ls = []
    
    for num in range(f,l+1):
        if num % d == 0 and num % nm != 0:
            ls.append(str(num))
            
    return ls

def Pascal(n): #pascal Triangle n lines
  for i in range(n):
    # adjust space
    print(' '*(n-i), end='')
 
    # compute power of 11
    print(' '.join(map(str, str(11**i))))


def triangle(n,x,s,t): #center triangle, n lines, x material, s angle in quotation spaces, t boolean
     
    # number of spaces
    k = n - 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=s)
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
            if t is True:
                print(f"{i+1} " , end="")
            # printing stars
            else:
                print(f"{x} " , end="")
     
        # ending line after each row
        print("\r")
 
def revtri(n,x,s,t): # upside down center triangle, same same
     
    # number of spaces
    for i in range(n, 1, -1):
        for space in range(0, n-i):
            print("  ", end=s)
            
        for j in range(i, 2*i-1):
            if t is True:
                print(f"{i+1} " , end="")
            # printing stars
            else:
                print(f"{x} " , end="")
            
        for j in range(1, i-1):
            if t is True:
                print(f"{i+1} " , end="")
            # printing stars
            else:
                print(f"{x} " , end="")
        print()
        
def rightri(x,n,t): #right triangle, same same
    for i in range(1,n+1):
        if t is True:
            x=i
        print(str(x)*i)
        
def leftri(x,n,t): #opposite right triangle, same same
    for i in range(n, 0,-1):
        if t is True:
            x=i
        print(str(x)*i)
        
def triside(x,n,t): #half crystal, same same
    rightri(x,n,t)
    leftri(x,n-1,t)
        
def numtri(r): #number triangle
    k = 0
    count=0
    count1=0

    for i in range(1, r+1):
        for space in range(1, (r-i)+1):
            print("  ", end="")
            count+=1
    
        while k!=((2*i)-1):
            if count<=r-1:
                print(i+k, end=" ")
                count+=1
            else:
                count1+=1
                print(i+k-(2*count1), end=" ")
            k += 1
    
        count1 = count = k = 0
        print()

def Floyd(r): #Floyd's triangle (search it up)

    number = 1

    for i in range(1, r+1):
        for j in range(1, i+1):
            print(number, end=" ")
            number += 1
        print()


def Fibonacci(n): #Fibonacci Sequence
 
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
 
def edit(dirc, wrt): #edits file with given string and directroy
    file = open(dirc, "w")
    file.write(wrt)
    file.close()


def substring(strg, start, end): #Substring from AP CSP
    start = int(start)
    end = int(end)
    string = strg[start-1:(start+end)-1]
    return  string

def concat(str1, str2): #Concat from AP CSP
    str1 = str(str1)
    str2 = str(str2)
    string = (str1+str2)
    return string

def reverse(strg): #reverse from AP CSP
    string = strg[::-1]
    return string
 
def prefix(strg, length): #Prefix from AP CSP
    string = strg[:length]
    return string


def lcd(x,y): #Least common denominator
    z = x*y
    g=m.gcd(x,y)
    a = g/z
    return a

    
def encrypt(text, shift): #Encrypts string
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift

            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26

            encrypted_text += chr(shifted)
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(encrypted_text, shift): #Decrypts string
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - shift

            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26

            decrypted_text += chr(shifted)
        else:
            decrypted_text += char

    return decrypted_text


def CO(elements, target): #COUNT OCCURENCES
    count = 0
    for element in elements:
        if element == target:
            count += 1
    return count


def GeN(start, end): #generate even numbers
    even_numbers = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def GoN(start, end): #generate odd numbers
    odd_numbers = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            odd_numbers.append(num)
    return odd_numbers

