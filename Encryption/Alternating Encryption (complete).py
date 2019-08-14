#this is some ridiculously convoluted code that encrypts a string n amount of times
#and then can decrypt it n amount of times 
#could do with cleaning up but I'm just proud that it works

def decrypt(encrypted_text,n):
    n_count = 0
    if n <= 0:
        return(encrypted_text)
    else:
        #splitting the string that needs decrypting in half
        length = (len(encrypted_text))
                
        half_length = int(length/2)
               
        first_half = encrypted_text[:half_length]
        second_half = encrypted_text[half_length:]
        first_half = list(first_half)
        second_half = list(second_half)

        #combining 1st of second_half, then 1st of first_half, etc into 1 string
        decrypted = []
        my_counter = 0
        
        while my_counter < half_length:
            decrypted.append(second_half[my_counter])
            decrypted.append(first_half[my_counter])
            my_counter += 1
            
        if length % 2 == 0:
            #print('the inputted string was even!')
            pass
        else:
            decrypted.append(second_half[half_length])
            
        decrypted = ''.join(decrypted)
        n_count+=1
        if n_count == n:
            return(decrypted)
        
        else:
            while n_count != n:
            #now decrypted is a string, and it needs to go through it again
                first_half = decrypted[:half_length]
                second_half = decrypted[half_length:]
                first_half = list(first_half)
                second_half = list(second_half)

                #combining 1st of second_half, then 1st of first_half, etc into 1 string
                decrypted = []
                my_counter = 0

                while my_counter < half_length:
                    decrypted.append(second_half[my_counter])
                    decrypted.append(first_half[my_counter])
                    my_counter += 1
                
                if length % 2 != 0:
                    decrypted.append(second_half[-1]) 
                
                decrypted = ''.join(decrypted)
            
                n_count+=1
                if n_count == n:
                    return(decrypted)
                else:
                    continue
        
def encrypt(text,n):
    evens=[]
    odds=[]
    
    counter = 0
    
    if counter == n:
        return(text)
    
    if n < counter:
        return(text)
    
    while counter != 1:
        for i, c in enumerate(text):
            if i % 2 == 0:
                evens.append(c)
            else:
                odds.append(c)
    
        even_str = ''.join(evens)
        odd_str = ''.join(odds)
    
        answer = (odd_str + even_str)
        counter +=1
        
    if counter == n:
        return(answer)
    else:
        while counter != n:
            evens = []
            odds = []
            for i, c in enumerate(answer):

                if i % 2 == 0:
                    evens.append(c)
                else:
                    odds.append(c)
        
            even_str = ''.join(evens)
            odd_str = ''.join(odds)
    
            answer = (odd_str + even_str)
            counter +=1
    
    return(answer)