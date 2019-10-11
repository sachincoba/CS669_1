'''
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):# used from any function in class
		#super(ClassName, self).__init__()
		self.element = arg
	def superdry(self):
		print(self.element)
		print('dsfd')

m=ClassName(5)#  m is object 

m.superdry()
		




class Boy:
	gender='Male'
	def __init__(self,name):
		self.name=name

r=Male('vijay')
s=Male('raju')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)
'''




class parent():
	def fn(self):
		print('firstname')

class child(parent):
	def ln(self):
		print('lastname')

	def fn(self):
		print('this is overriding')

x=child()
x.ln()
x.fn()




class class3(class1,class2):
	pass

dm=class3()


