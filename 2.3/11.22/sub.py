class MyList(list):

    def __init__(self, *args, **kwargs):
        list.__init__(self, *args, **kwargs)

    def __sub__(self, other):
        a = self
        r = []
        for i in range(len(other)):
            r.append(a[i]-other[i])
        return r


a = MyList([1, 2, 3])
print(a-[2,3])
