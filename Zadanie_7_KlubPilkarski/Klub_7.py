import os

class KlubPilkarski():

	def __init__(self,klub,exist):
		self.klub = klub
		self.exist = exist


	def create_klubPilkarski(self):
		f = open("klub.txt", "w")
		f.write(self.klub)
		f.close()

	def delete_klubPilkarski(self):
		if(self.exist == True):
			os.remove("klub.txt")
		else:
			print("Plik nie istnieje");