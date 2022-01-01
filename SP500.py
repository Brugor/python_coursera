"""Read in the contents of the file SP500.txt which
has monthly data for 2016 and 2017 about the S&P 500
closing prices as well as some other financial indicators,
including the “Long Term Interest Rate”, which is interest
rate paid on 10-year U.S. government bonds. Write a program
that computes the average closing price (the second column,
labeled SP500) and the highest long-term interest rate.
Both should be computed only for the period from June 2016
through May 2017. Save the results in the variables mean_SP
and max_interest.
"""

from statistics import mean

with open("SP500.txt") as file:
    data = file.readlines()[6:18]
    
    mean_SP = mean([float(d.split(",")[1]) for d in data])
    max_interest = max([float(d.split(",")[5]) for d in data])
