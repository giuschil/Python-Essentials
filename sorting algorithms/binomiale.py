# base case: triangol dyagonals
def binomial(m, k):
    if m==k or k==0:
        return 1
    return binomial(m-1, k-1) + binomial(m-1, k)
    