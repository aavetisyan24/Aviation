adult = [1,2,3,4,5,6,7,8,9]
child = [0,1,2,3,4,5]
infant = [0,1,2,3,4,5]




def customers(a):
    lst1 = [0, 1, 2, 3, 4]
    maximumadult = list(range(1, 10))
    maxchild = list(range(9))
    maxinf = list(range(6))
    if a in lst1:
        maxchild=list(range(6))
        maxinf=a
    elif a not in lst1:
        maxinf=list(range(6))
        maxchild = list(range(10 - a))
    print(maximumadult, maxchild, maxinf)
    return [maximumadult, maxchild, maxinf]

print(customers())