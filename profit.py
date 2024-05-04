print("Trading Profit and Loss account")

def calculate_gross_profit(Salesamount, Openingstockamount, Purchasesamount, Purchasesreturnsamount, Closingstock, Discountreceived):
    return Salesamount - Openingstockamount + Purchasesamount - Purchasesreturnsamount - Closingstock + Discountreceived

user = int(input("Enter the Sales amount: "))
user1 = int(input("Enter the Opening stock amount: "))
user2 = int(input("Enter the Purchases amount: "))
user3 = int(input("Enter the Purchases returns amount: "))
user4 = int(input("Enter the Closing stock: "))
user5 = int(input("Enter the Discount received: "))

Salesamount = user
Openingstockamount = user1
Purchasesamount = user2
Purchasesreturnsamount = user3
Closingstock = user4
Discountreceived = user5

result = calculate_gross_profit(Salesamount, Openingstockamount, Purchasesamount, Purchasesreturnsamount, Closingstock, Discountreceived)

def calculate_net_profit_or_loss(gross_profit, Expensesamount, Accruedexpensesamount, Prepaidexpensesamount):
    return gross_profit - Expensesamount + Accruedexpensesamount - Prepaidexpensesamount

answer = input("Enter the Expenses amount separated by a comma: ")
answer1 = int(input("Enter the Accrued expenses amount: "))
answer2 = int(input("Enter the Prepaid expenses amount: "))

answer_list = answer.split(',')
answer_user = [int(num) for num in answer_list]

Expensesamount = sum(answer_user)
Accruedexpensesamount = answer1
Prepaidexpensesamount = answer2

net_result = calculate_net_profit_or_loss(result, Expensesamount, Accruedexpensesamount, Prepaidexpensesamount)

if net_result > 0:
    print("The Net profit is:", net_result)
else:
    print("The Net loss is:", net_result)
