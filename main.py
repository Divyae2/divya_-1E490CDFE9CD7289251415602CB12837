# factorial of tha given number
def fact_rec(n):
  if n==0 or n==1:
    return 1
  else : return n*fact_rec
number=2
res=fact_rec(number)
print("the factorial or {}is{}.".format(number,res)