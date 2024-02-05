# Take input from the user
email = input("Enter your email: ")  # ashut@gmail.com

# Initialize variables
k = 0
j = 0
d = 0

# Check length of the email
if len(email) >= 6:
    # Check if the first character is an alphabet
    if email[0].isalpha():
        # Check for the presence of '@' and only one '@'
        if "@" in email and email.count("@") == 1:
            # Check the position of '.' in the domain and top-level domain
            if email[-4] == "." or email[3] == ".":
                # Loop through each character in the email
                for i in email:
                    # Check for spaces
                    if i.isspace():
                        k = 1
                    # Check for uppercase alphabets
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    # Check for digits
                    elif i.isdigit():
                        continue
                    # Check for allowed special characters
                    elif i in ["_", ".", "@"]:
                        continue
                    else:
                        d = 1

                  # Check the flags and print appropriate message
                if k == 1 or j == 1 or d == 1:
                  print("Wrong email 5")
                else:
                    print("Email is valid")
            else:
                print("Wrong email 4")
        else:
            print("Wrong email 3")
    else:
        print("Wrong email 2")
else:
    print("Wrong email 1")
