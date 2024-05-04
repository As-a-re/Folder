print("Hello, Welcome to the HillTop Church of Christ")
church_user = {
    "Atta Boateng",
    "Bismark",
    "Obeng",
    "Bekoe",
    "Stephen"
}
church_name = input("Enter your full name ")
if church_name in church_user:
    print(f"You have been marked present today: {church_name}")
else:
    print("You are not a recognised member")   