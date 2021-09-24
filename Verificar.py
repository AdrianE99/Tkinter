import re

def Validar(campo):
	"""
	En este método validamos 
	los datos recibidos en título
	según un patron
	"""
	patron="^[A-Za-z]+(?:[_-][A-Za-z]+)*$"
	if re.search(patron,campo)is None:
		return False
	else:
		return True


