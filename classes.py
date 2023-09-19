class MyClass(object):
    i = 345
    def __init__(self):
        self.i = 200
a = MyClass()
print(a.i)
print(MyClass.i)

#200
#345


class Bill():
    def __init__(self,apples,figs,dates):
        self.apples = apples
        self.figs = figs
        self.dates = dates
        self.bill = apples + figs + dates
        print ("Buy",self.apples,"apples", self.figs,"figs and",self.dates,"dates Total fruitty bill is",self.bill," pieces of fruit :)")


purchase = Bill(5, 6, 7)
#Buy 5 apples 6 figs and 7 dates. Total fruitty bill is 18  pieces of> fruit :)



