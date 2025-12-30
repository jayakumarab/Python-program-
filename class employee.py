class employee:
	def __init__(self,em_id, em_Name,em_age,em_Role):
		self.em_id = em_id
		self.em_Name=em_Name
		self.em_age = em_age
		self.em_Role = em_Role
		
	def employees (self):
		return self.em_id, self.em_Name

detail = employee (1,"jai",20,"enginner")

print (detail. employees())