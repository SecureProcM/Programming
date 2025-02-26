# The program simulates a simple menu system that asks the user to choose an option
# from a list of choices. The program uses a while loop to keep displaying the
# menu until the user chooses to exit.

# Declaring variable to handle user input (initially invalid to trigger the menu display)
choice = 0

while True:  # I Corrected loop to continuously display the menu until the user exits
    # Display the menu options
    print("\nMenu:")
    print("1. Print Hello")
    print("2. Print Goodbye")
    print("3. Exit")

    # Prompt the user to input a choice from the menu
  
    choice = int(input("Enter your choice (1, 2, or 3): "))
    

    # Perform the corresponding actions based on user choice
    if choice == 1:
        # If the choice is 1, print "Hello!"
        print("Hello!")
    elif choice == 2:
        # If the choice is 2, print "Goodbye!"
        print("Goodbye!")
    elif choice == 3:
        # If the choice is 3, print exit message and break the loop
        print("Exiting the program...")
        print("Excellent choice")  # Print this only when exiting correctly
        break
    else:
        # If the user enters an invalid choice, display an error message
        print("Invalid choice, please try again.")

# all the fixes
# 1. The original `while choice == 1 or choice == 2 or choice == 3:` condition
#    was incorrect because it relied on `choice` having a valid  value.
#    This was changed to `while True` to ensure the menu displays 
#    until the user explicitly chooses to exit.


# 3. In the original code, when the user entered an invalid choice, the loop
#    would  break. This was changed to allow the menu to display again
#    after an invalid input.

# 4. Removed the unnecessary `pass` statement in the `elif choice == 3` block
#    since it added no functionality.

# 5. I Ensured  "Excellent choice" is only printed when the user exits the program
#    by moving it into the `elif choice == 3` block.
