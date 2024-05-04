user_response = input("Hello, how are you doing? ")
print(user_response)

print("I'm doing well myself also")

print("What Bible fact do you want to know?")

user_question = input("Enter your question here ")
print(user_question)

Bible_facts1 = ("The longest living person was Methusaleh ")
Bible_facts2 = ("The sister of Moses was Miriam")
Bible_facts3 = ("The brother of Moses was Aaron")
Bible_facts4 = ("The mother of Moses was Jochebed")
Bible_facts5 = ("The total number of plagues that occured in Egypt was 10")
Bible_facts6 = ("The father of John the baptist was Zechariah")
Bible_facts7 = ("The mother of John the baptist was Elizabeth")
Bible_facts8 = ("John the baptist was the cousin of Jesus Christ")
Bible_facts9 = ("There were 13 apostles in the New Testament")
Bible_facts10 = ("The church first began at Jerusalem")


if user_question == "Who was the oldest person in the Bible":
    print(Bible_facts1)
elif user_question == "Who was the sister of Moses":
    print(Bible_facts2)
elif user_question == "Who was the brother of Moses":
    print(Bible_facts3)
elif user_question == "Who was the mother of Moses":
    print(Bible_facts4)
elif user_question == "How many plagues occured in Egypt":
    print(Bible_facts5)
elif user_question == "Who was the father of John the baptist":
    print(Bible_facts6)
elif user_question == "Who was the mother of John the baptist":
    print(Bible_facts7)
elif user_question == "Who was John the baptist to Jesus Christ":
    print(Bible_facts8)
elif user_question == "How many apostles were there in the New Testament":
    print(Bible_facts9)
elif user_question == "Where did the church first begin":
    print(Bible_facts10)
else:
    print("I don't have what you're looking for")