class A(object):
    def __init__(self, s,p):
        self.s = s
        self.price = p

    def __eq__(self, other):
        return self.price <= other.price

a = A('aaaa',10)
b = A('AAAA',12)
print (a == b) # prints True
