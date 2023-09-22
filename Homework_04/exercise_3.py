print(0)
for i in range(1, 101):
    answer = input("Should we break? ")
    if answer == 'Yes':
        break
    elif answer == 'No':
        print(i)
        continue
    else:
        print("Don't undestand you")
