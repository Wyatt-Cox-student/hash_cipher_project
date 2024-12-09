## Function for user to input a message
def get_user_input(prompt):
    while True:
        
        message = input(prompt)
        if message.isalpha() == True:
            
            return message.upper()
        else:
            print(f"Invalid message'{message}', message cannot have numbers or spaces.")
        

## Function that produce a shift number
def get_shift_calculation(message):
    # Array to hold each letter.
    Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'
                , 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'
                , 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    len(Alphabet)
    
    # Maps the posision of each letter.
    letter_position = {letter: idx + 1 for idx, letter in enumerate(Alphabet)}
    
    # Count the number of times a letter appears.
    letter_amount = {letter: message.count(letter) for letter in set(message)}

    # Calculate the sum of the letters posisions
    letter_sum = sum(letter_position[letter] * count for letter, count in letter_amount.items())
    
    # Calculate the shif value
    shift_amount = (letter_sum - 1) % 25 + 1
    
    return shift_amount

## Function that will produce a hash string
def hash_string(message):
    
    Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'
                , 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'
                , 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    
    # Count the amout of numbers that reapear.
    letter_amount = {letter: message.count(letter) for letter in Alphabet}

    # Creates a hash string.
    hash_string_def = ''.join(f'{count}{letter}' for letter, count in letter_amount.items())
    
    return hash_string_def

## Function that encrypts the message given from the user
def encrypt_message(message, shift):
    
    Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'
                , 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'
                , 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    # Define the encrypted message
    encrypted_message = ''

    # Encrypt the message, array.index should work.
    for letter in message:
        # Find the position of the letter.
        original_position = Alphabet.index(letter)
        # Define a new position with wrapping.
        new_position = (original_position + shift) % 26
        # Append to the result
        encrypted_message += Alphabet[new_position]
    return encrypted_message

## Don't forget to output the hash and encrypted message.

## Basic main function
def main():
    
    # Get the users input.
    message = get_user_input('Enter a message to encrypt: ')
    
    # Get the shift value
    shift = get_shift_calculation(message)
    
    # Get the hash string
    Hash = hash_string(message)

    # Encrypt the message itself
    encrypted_msg = encrypt_message(message, shift)
    
    ## Outputs for the final test
        ## Delete the '#' behind the print statement for the shift if you need to know 
        ## the shift number. 
    print(f'(DEBUG ONLY!) Shift number: {shift}')
    print(Hash)
    print(encrypted_msg)



main()