from faker  import Faker

myfake = Faker('ko_KR')
myfake.seed(1)

print(myfake.name())
print(myfake.address())
#print(myfake.text())
#print(myfake.state())
#print(myfake.sentence())
print(myfake.random_number())