MichaelCash = int(input())
IvanCash = int(input())
minimumInvestment = int(input())

if (MichaelCash >= minimumInvestment) and (IvanCash >= minimumInvestment):
    print(2)
elif (MichaelCash >= minimumInvestment) and (IvanCash < minimumInvestment):
    print('Mike')
elif (IvanCash >= minimumInvestment) and (MichaelCash < minimumInvestment):
    print('Ivan')
elif (MichaelCash < minimumInvestment) and (IvanCash < minimumInvestment) and (MichaelCash + IvanCash >= minimumInvestment):
    print(1)
else:
    print(0)
