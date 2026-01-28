full_name = input("Full Name:")
letters = full_name.count(" ")
email = input("Email:")
mobile_num = input("Mobile:")
age = int(input("Age:"))
if len(letters) >= 1 and full_name[0] != "" and full_name[-1] != "" and "@" in email and "." in email and email[0] != "@" and len(mobile_num) == 10 and mobile_num.isdigit() == True and mobile_num[0] != "0" and age >= 18 and age <= 60:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")


