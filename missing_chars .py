def missing_chars(s: str):


    digits = ["0","1","2","3","4","5","6","7","8","9"]
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

    digits_s = ''
    letters_s = ''

    for i in s:
        if i not in characters:
            digits_s += i
        elif i in characters:
            letters_s += i
    
    fault_digits = set(digits)- set(digits_s)
    l_fault_digits = list(sorted(fault_digits))
    fault_letters = set(characters)- set(letters_s)
    l_fault_letters = list(sorted(fault_letters))



    final = ''.join(l_fault_digits)+''.join(l_fault_letters)
    print(final)


    



missing_chars(input())