while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break
if age >= 18: 
    print("You are able to vote in the United States!")
else:
    print("You are not able to vote in the United States.")

input()



