def run(input_str):
    
    square_count = 0; # {}
    brackets_count = 0; # []
    round_count = 0; # ()


    for i in range (1, len(input_str) + 1):
        cur_symb = input_str[i - 1]

        if (cur_symb == '{'):
            square_count += 1
        elif (cur_symb == '}'):
            square_count -= 1
        elif (cur_symb == '['):
            brackets_count += 1
        elif (cur_symb == ']'):
            brackets_count -= 1
        elif (cur_symb == '('):
            round_count += 1
        elif (cur_symb == ')'):
            round_count -= 1
        
    print (square_count == 0 and brackets_count == 0 and round_count == 0)