import pandas as pd


class PercentageCalculator:

  def __init__(self, income, bill):
    self.income = income
    self.bill = bill

  def calculate_percentage(self):
    return (self.bill / self.income) * 100


income = input('Enter you income: ')
while not income.isnumeric():
  print(f"Invalid Integer . '{income}'' Not Defined")
  income = input('Enter you income: ')
income = int(income)
inp = input('''Enter the spendings (Sperate them with ','):  ''')
while inp.isnumeric():
  print(f"Invalid String. '{inp}' Not Defined")
  inp = input('''Enter the spendings (Sperate them with ','):  ''')
temp_list = inp.split(",")
list = []
spend = []
for element in temp_list:
  bill = input(f"Enter the bill for {element}: ")
  while not bill.isnumeric():
    print(f"Enter a Valid Number . '{bill}' Not Defined")
    bill = input(f"Enter the bill for {element}: ")
  list.append([element, bill])
  spend.append(int(bill))
spend = sum(spend)

for i in range(len(list)):
  bill = int(list[i][1])
  calculator = PercentageCalculator(income, bill)
  percentage = calculator.calculate_percentage()
  list[i].append(str(percentage) + "%")
file = []
print(list)
for spending1 in list:
  spending = spending1[0]
  percentage = spending1[1]

  bill = spending1[1]
  df = file.append([spending, bill, percentage])

df = pd.DataFrame(file,
                  columns=['Spendings', 'Bill', 'Percentage from income'])
print('''Total Income:''', income, '''
Total Bill:{spend}
Savings   :''', income - spend)

df.to_excel('export.xlsx', index=False)
print(pd.read_excel('export.xlsx'))
