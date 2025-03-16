P=int(input("Enter principal value: "))
R=float(input("Enter rate (in %): "))
T=int(input("Enter time: "))
n=int(input("Enter number of compounding periods per year: "))
PMT=int(input("Enter annuity payment: "))

def simple_interest(P,R,T):
    A = P * (1 + (R / 100) * T)
    return A
def compound_interest(P,R,T,n):
    A = P * ((1 + R / n) ** n * T)
    return A
def annuity_plan(PMT,R,n,T):
    A = PMT * ((1 + R / n) ** (n * T) - 1) / (R / n) 
    return A
print("Simple interest:", simple_interest(P,R,T)) 
print("Compound interest:", compound_interest(P,R/100,n,T)) 
print("annuity plan:", annuity_plan(PMT,R/100, n,T))    
