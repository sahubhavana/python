## program to print a nth term of series
a=int(input(" enter a first term"))
n=int(input(" enter element which we want to find"))
d=int(input(" enter a comma diffrenec"))
# TN=a+(n-1)d
tn=a+(n-1)*d
sum_n = (n * (2 * a + (n - 1) * d)) / 2
print(" nth term of seris",tn)
print("sum of nth element",sum_n)