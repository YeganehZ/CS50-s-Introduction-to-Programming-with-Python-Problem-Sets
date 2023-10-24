'''
Check out the link here for description:
https://cs50.harvard.edu/python/2022/psets/8/jar/

'''

class Jar:
    
    def __init__(self, capacity=12):
    
        if type(capacity) != int :
            raise ValueError("Invalid capacity value")  
             
        self._capacity=capacity
        self._size=4
       # self.capacity=int(capacity)
       # self.n=int(n)
       # self.numofcookies=int(numofcookies)

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Exceeds capacity")
          
        if self.size + n > self.capacity:
            raise ValueError("Exceeds capacity")
        self._size +=  n
        return self._size * "🍪"

      
    def withdraw(self, n):
        if n > self.size:
           raise ValueError("Not enough cookies in jar")
        self._size -=  n 
        return self._size * "🍪"
   
    @property
    def capacity(self):
        return self._capacity  

    @property
    def size(self):
        return self._size

    



#Capacity= input("capacity: ")
#Number=input("Number of cookies: ")
#Num_cookie_injar = input("Number of cookies in jar: ")
s=Jar(15)
print(s)
print(s.deposit(11))
print(s.withdraw(1))








