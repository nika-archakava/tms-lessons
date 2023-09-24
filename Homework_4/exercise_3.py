for i in range(101):
    print(i)
    answer = input("Should we break? ")
    if answer == 'Yes':
        break
    elif answer == 'No':
        continue
    else:
        while True:
            print("Don't understand you")
            answer = input("Should we break? ")
            if answer == 'Yes' or answer == 'No':
                break
        if answer == 'Yes':
            break
        elif answer == 'No':
            continue
