print("Welcome to self medical care")
print("How are you doing")
case = input("Please enter how you are feeling ")
print(case)
case_malaria ={"Headache","Stomach pains","Naususe","Dizzeness","Feverish"}
print(f"{case_malaria}")
case_breastcancer= {"Breast lump","Rash around nipple","Swelling in armpit","Discharge from nipple","Change in structure of breast"}
print(f"{case_breastcancer}")
case_diabetes ={"Feeling very thirsty","Feeling very tired","Blurred vision","Itching around private parts","Slow healing of wounds"}
print(f"{case_diabetes}")
case_foodpoisoning ={"Nauseous","Vomiting","Diarrhoea","Chills","Weakness","Abdominal pain","High temperature"}
print(f"{case_foodpoisoning}")
case_prostatecancer ={"Pain in testicles","Frequent urinating","Difficulty in urinating","Feeling of bladder not emptied after urinating"}
print(f"{case_prostatecancer}")
case_stomachulcer ={"Stomach pains","Weight loss","Indigestion","Feeling sick","Loss of appetite"}
print(f"{case_stomachulcer}")
user_case = input("Enter the number in which your symptoms fall under ")
if user_case == "1":
    print("You may have malaria, go to the nearest pharmacy or medical center")
elif user_case == "2":
    print("You may have breastcancer, seek immediate medical attention")
elif user_case == "3":
    print("You may have diabetes, check your diet and consult a medical officer")
elif user_case == "4":
    print("You may have foodpoisoning, consult a medical officer for help")
elif user_case == "5": 
    print("You may have prostatecancer, find the nearest suitable medical center for help")
else:
    print("You need to go to the nearest healthcare center for more details about your condition")