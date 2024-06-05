Password = "ABCD1234"

def NewCheckPassword(user_input):
    password = True
    for i in range(len(Password)):
        if user_input[i] != Password[i]:
            password = False
    return password

user_input = input()
if NewCheckPassword(user_input):
    print("Correct")
