def Convert_Text(_string):
    integer_list = []
    for s in _string:
        integer_list.append(ord(s))
    return integer_list #this integer list is used in the encode function as part of the encoding process

def Convert_Num(_list):
    _string = ''
    for i in _list:
        _string += chr(i)
    return _string    #this is used in the decode function as part of the decoding process

def FME(b, n, m):
    result = 1  #this will become the return value
    sq = b  #assigning this as square makes this easier to read and follow the math
    while n > 0: #loop converts n to binary
        k = n % 2   # extracts the least significant bit
        if k == 1:  #this checks if the least significant bit is 1
            result = (result * sq) % m
        sq = (sq * sq) % m
        n = n // 2  #this makes sure that we do not have an infinite loop
    return result  #returns result of b^n mod m

def Euclidean_Alg(a, b):
    while b > 0:     #loop returns when b = 0
        k = a % b    #k will get smaller after each loop
        a = b          
        b = k         
    return a         #returns the GCD

def Find_Public_Key_e(p, q):
    if(p*q < 150): #this check is here to make sure n > 150 to avoid ASCII issues
        print("Please reselect your prime numbers, the product of the primes needs to be more than 150")
    n = p * q
    e = 3 
    
    if not(Euclidean_Alg(e, (p-1)*(q-1)) == 1): #determines if e and (p-1)(q-1) are relatively prime
        print("Please choose different primes whose product is more than 150 and not the number 3.")
    return n, e

def Find_Private_Key_d(e, p, q):
    #Find Euler's totient function, phi, given that p and q are prime numbers
    phi = (p-1)*(q-1)
    
    #the eea() will give the value for s, one of the Bezout coeffs.
    def eea(m, n):
    #m0 = m, n0 = n
        s1, t1 = 1, 0  #initial values for s1 and t1 - used to find bezout coeffs.
        s2, t2 = 0, 1   #initial values for s2 and t2 - used to find bezout coeffs.
        while n > 0:     #loop returns when n = 0
            k = m % n
            q = m//n
            m = n          
            n = k          
            s1_hat, t1_hat = s2, t2
            s2_hat, t2_hat = s1-q*s2, t1-q*t2
            s1, t1 = s1_hat, t1_hat
            s2, t2 = s2_hat, t2_hat
        return m, s1, t1      #returns the GCD, and the s1, t1 used to find it (bezout)
    
    s = eea(e, phi)[1]  
    if s < 1:
        s = s % phi #this ensures that s is positive
    d = s
    return d  

def Encode(n, e, message):
    cipher_text = [] #the encoded message will be added to this empty list
    
    int_list = Convert_Text(message) #takes text string and converts it to the corresponding list of integers (ascii)
    
    for num in int_list:
        cipher_text.append(FME(num,e,n)) #this finds the num^e mod n, goes to the next number each time the loop executes
        
    return cipher_text

def Decode(n, d, cipher_text):
    message = ''
    decode_list = [] #the decoded message will be added to this empty list
    
    for item in cipher_text:  
        decode_list.append(FME(item,d,n)) #item=integer in the list, this finds the integer^d mod n
        
    message = Convert_Num(decode_list)  #this converts the decoded integers back to text as a string  
    
    return message
