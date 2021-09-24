import re

def Validar(campo):
	"""
	En este método validamos 
	dos datos recividos en título
	segun un cierto patron
	"""
	patron="^[A-Za-z]+(?:[_-][A-Za-z]+)*$"
	if re.search(patron,campo)is None:
		return False
	else:
		return True


