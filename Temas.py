def EleccionTemas(miFrame,TemaOpcion):
	"""
	Con este método nos permite
	 realizar el cambio de color 
	 en la ventana de la interfaz.

	"""
	
	if TemaOpcion==1:
		miFrame.config(bg='#68EB0D')
	elif TemaOpcion==2:
		miFrame.config(bg='#CF0DEB')
	else:
		miFrame.config(bg='#0DDBEB')