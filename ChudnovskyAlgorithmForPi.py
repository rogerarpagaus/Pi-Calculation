from decimal import Decimal as Dec, getcontext as gc

def PI(maxK: int = 200, prec: int = 20010, disp: int = 2000):  # Parameter defaults chosen to gain 1000+ digits within a few seconds
    gc().prec = prec
    K, M, L, X, S = 6, 1, 13591409, 1, 13591409
    for k in range(1, maxK + 1):
        M = (K**3 - 16*K) * M // k**3 
        L += 545140134
        X *= -262537412640768000
        S += Dec(M * L) / X
        K += 12
    pi = 426880 * Dec(10005).sqrt() / S
    pi = Dec(str(pi)[:disp])  # Drop few digits of precision for accuracy
    print("PI(maxK={} iterations, gc().prec={}, disp={} digits) =\n{}".format(maxK, prec, disp, pi))
    return pi

print("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")
Pi = PI()
#print("\nFor greater precision and more digits (takes a few extra seconds) - Try")
#print("Pi = PI(317, 4501, 4500)") 
#print("Pi = PI(353, 5022, 5020)")
