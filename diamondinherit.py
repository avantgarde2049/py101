class A():
  def met(self):
    print("The mthod of class A")
class B(A):
  def met(self):
    print("The mthod of class B")

class C(A):
  def met(self):
    print("The mthod of class C")

class D(B,C):
  pass#we commented the method for D to get multilevel inheritance ,orderwise B
  #def met(self):
   # print("The mthod of class D")


a=A()
b=B()
c=C()
d=D()

print(d.met())