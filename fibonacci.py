
n = input("Type a real number from 1 to 40: ")
def fibonachi(n):
    F = [0, 1]
    if n == 1:
        print "Answer for n = " + str(n) + " is "+ str(F[i])
        return F[1]
    else:
        for i in range(2,n+1):
            F.append(F[i-1] + F[i-2])
            print str(F[i])
            if i == n:
                print "Answer for n = " + str(n) + " is "+ str(F[i])
                return F[i]

fibonachi(n)
