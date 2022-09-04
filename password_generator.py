import random
import string

def pas_generator():
    character = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    password = []
    
    while len(password) < 16:
        characters = random.choice(character)
        password.append(characters)
    
    new_pass = "".join(password)
    print("Your password is: ", new_pass)
    
if __name__ == '__main__':
    pas_generator() 