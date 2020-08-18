from dataclasses import dataclass
import sys
import pprint

@dataclass
class Hi :
	
	name: str

	def fn(self, a: int) -> bool :
		if(a == 2) :
			return True

	def print_name(self) :
		print(self.name)

	def get_natural(self, b):
			n = 0
			while b == 1:
				n += 1
				yield n

			while True :
				yield "hi"
				yield "cae"
				yield "krue"


class cae:
	__name = ""

	def __init__(self, b):
		self.__name = b

	def get_name(self):
		print(self.__name)



hi = Hi("sungyu")
cae = cae("gyu")
hi.print_name()
print(hi.get_natural(1))

cae.get_name()
g = hi.get_natural(2)

#for _ in range(0, 100):
#	print(next(g), end= ' ')
#print('\n')

b = range(100000) #b = [n for n in range(1000000)]
print(type(b)) 
print(sys.getsizeof(b))
#print(b[98749754])
#enumerate

lover = ['hi','im','sun','lover']

for i, v in enumerate(lover):
	print(str(i),"v",v, sep= ",", end= " ")

print('|'.join(["str","btr","ktr"]))
print(type(divmod(5, 3)))

for i, v in enumerate(lover):
	print(f'{i} {v}')# {} == str()

##PASS
@dataclass
class Sayes(object):
	sayes: int
	

	def method_a(self):
		pass
	def method_b(self):
		print(self.sayes)

sayes = Sayes(0)
sayes.method_b()

#pprint.pprint(locals())

def foo(a, b=None):
	if b is None :
		b = []


#예외처리
try:
	print([1,2,3,4,5,6][7])
except IndexError:
	print("순구루루루")

