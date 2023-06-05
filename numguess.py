import random
def main():
    rand_num = random.randint(1, 100)
    guess_num = int(input("Enter a number: "))

    if guess_num == rand_num:
        outp = f"You guessed it right. The number is {rand_num}"
        print(outp)
    else:
        print(f"Incorrect!!The number is {rand_num}")
        
    ask_user = input("Do you want to play again?Y/N: ")
    if ask_user == "Y":
        main()
    else:
        print("Game ended.")
        
if __name__ == "__main__":
    main()
    
    
    
