try:
    hrs = raw_input("Enter Hours:")
    h = float(hrs)
    rate = raw_input("Enter Rate:")
    r = float(rate)
except:
    print "Please enter a numeric number"
    quit()

def computepay(h,r):
    if h <= 40:
        pay = h * r
    else:
        pay = 40 * r + (h - 40) * (r * 1.5)
    return pay
    
print computepay(h,r)