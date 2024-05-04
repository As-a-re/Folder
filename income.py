def calc(theConsumptionamount, theInvestmentamount, theGovernmentamount, theExportamount, theImportamount):
    
    return theConsumptionamount + theInvestmentamount + theGovernmentamount + theExportamount - theImportamount

print("National Income Calculator (Expenditure Approach)")

user_info1 = int(input("Enter the Consumption amount "))
user_info2 = int(input("the Investment amount ")) 
user_info3 = int(input("the Government amount "))
user_info4 = int(input("the Export amount ")) 
user_info5 = int(input("the Import amount "))

theConsumptionamount = user_info1
theInvestmentamount = user_info2
theGovernmentamount = user_info3
theExportamount = user_info4
theImportamount = user_info5

results = calc(theConsumptionamount, theInvestmentamount, theGovernmentamount, theExportamount, theImportamount)

def ans(results, theNetFactorIncomeAbroad):
    return results + theNetFactorIncomeAbroad

print("Provide the Net Factor Income Abroad which is Income received less Income paid")
user_info6 = int(input("Enter the Net Factor Income Abroad "))

theNetFactorIncomeAbroad = user_info6 

answer = ans(results, theNetFactorIncomeAbroad)

def add(answer, Depreciationamount):
    return answer - Depreciationamount

user_info7 = int(input("Enter the Depreciation amount "))
Depreciationamount = user_info7

solution = add(answer, Depreciationamount)

def less(solution, Subsidiesamount, Indirecttaxamount):
    return solution + Subsidiesamount - Indirecttaxamount

user_info8 = int(input("Enter the Subsidies amount "))
user_info9 = int(input("Enter the Indirect tax amount "))

Subsidiesamount = user_info8
Indirecttaxamount = user_info9

attempt = less(solution, Subsidiesamount, Indirecttaxamount)

def final(attempt, thetotalpopulation):
    return attempt / thetotalpopulation

user_info10 = int(input("Enter the total population "))

thetotalpopulation = user_info10

percapitaincome = final(attempt, thetotalpopulation)
print("The Per capita income is ", percapitaincome)
