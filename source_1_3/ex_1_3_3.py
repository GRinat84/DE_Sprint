def get_rome_letter(cur_symb, letter_1, letter_5, letter_10):

    cur_dec = int(cur_symb)
    str_symb = ''

    if (cur_symb == '4'):
        str_symb = letter_1 + letter_5
    elif (cur_symb == '9'):
        str_symb = letter_1 + letter_10
    elif (cur_symb == '5'):
        str_symb = letter_5
    elif (cur_dec >= 1 and cur_dec <= 4):
        for i2 in range(1, cur_dec + 1):
            str_symb = letter_1 + str_symb 
    elif (cur_dec >= 6 and cur_dec <= 8):
        for i2 in range(6, cur_dec + 1):
            str_symb = letter_1 + str_symb 
        str_symb = letter_10 + str_symb     

    return str_symb

def run(decimal_for_transform):
    
    str_for_transform = str(decimal_for_transform)
    str_transformed = ''

    for i in range (1, len(str_for_transform) + 1):
        cur_symb = str_for_transform[-i]
        cur_dec = int(cur_symb)

        if (i == 1): # можно сократить через компоновки 3 одинаковых в отдельную функцию
            str_transformed = get_rome_letter(cur_symb, 'I', 'V', 'X') + str_transformed    
            '''
            if (cur_symb == '4'):
                str_transformed = 'IV' + str_transformed
            elif (cur_symb == '9'):
                str_transformed = 'IX' + str_transformed 
            elif (cur_symb == '5'):
                str_transformed = 'V' + str_transformed 
            elif (cur_dec >= 1 and cur_dec <= 4):
                for i2 in range(1, cur_dec + 1):
                    str_transformed = 'I' + str_transformed 
            elif (cur_dec >= 6 and cur_dec <= 8):
                for i2 in range(6, cur_dec + 1):
                    str_transformed = 'I' + str_transformed 
                str_transformed = 'V' + str_transformed 
            '''                
        elif (i == 2):
            str_transformed = get_rome_letter(cur_symb, 'X', 'L', 'C') + str_transformed   
            '''
            if (cur_symb == '4'):
                str_transformed = 'XL' + str_transformed
            elif (cur_symb == '9'):
                str_transformed = 'XC' + str_transformed 
            elif (cur_symb == '5'):
                str_transformed = 'L' + str_transformed 
            elif (cur_dec >= 1 and cur_dec <= 4):
                for i2 in range(1, cur_dec + 1):
                    str_transformed = 'X' + str_transformed 
            elif (cur_dec >= 6 and cur_dec <= 8):
                for i2 in range(6, cur_dec + 1):
                    str_transformed = 'X' + str_transformed 
                str_transformed = 'L' + str_transformed 
            '''
        elif (i == 3):
            str_transformed = get_rome_letter(cur_symb, 'C', 'D', 'M') + str_transformed   
            '''
            if (cur_symb == '4'):
                str_transformed = 'CD' + str_transformed
            elif (cur_symb == '9'):
                str_transformed = 'CM' + str_transformed 
            elif (cur_symb == '5'):
                str_transformed = 'D' + str_transformed 
            elif (cur_dec >= 1 and cur_dec <= 4):
                for i2 in range(1, cur_dec + 1):
                    str_transformed = 'C' + str_transformed 
            elif (cur_dec >= 6 and cur_dec <= 8):
                for i2 in range(6, cur_dec + 1):
                    str_transformed = 'C' + str_transformed 
                str_transformed = 'D' + str_transformed 
            '''
        elif (i > 3):
            for i2 in range(1, cur_dec + 1):
                str_transformed = 'M' + str_transformed 


    print(str_transformed)