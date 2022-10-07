def run(phrase_for_check):
    
    phrase_for_check = phrase_for_check.replace(' ', '')

    for i in range (1, len(phrase_for_check) // 2 + 1):
        if(phrase_for_check[i - 1] != phrase_for_check[-i]):
            print(False)
            return

    print(True)