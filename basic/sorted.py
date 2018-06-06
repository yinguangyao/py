L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_age(a):
    return a[1]
print(sorted(L, key=by_name))
print(sorted(L, key=by_age))