import Product

inp=Product.inputsp
it1=inp.item1()
it2=inp.item2()
it3=inp.item3()
it4=inp.item4()
it5=inp.item5()

comp=Product.computation
v1=comp.variance1(it1)
v2=comp.variance2(it2)
v3=comp.variance3(it3)
v4=comp.variance4(it4)
v5=comp.variance5(it5)

total=comp.total(it1,it2,it3,it4,it5)
vt=comp.variance(total)
# print(vt)

k=3
nr=comp.net_reliability(k,v1,v2,v3,v4,v5,vt)
print(nr)

print(comp.check_reliability(nr))
print(comp.check_reliabilityq(nr))