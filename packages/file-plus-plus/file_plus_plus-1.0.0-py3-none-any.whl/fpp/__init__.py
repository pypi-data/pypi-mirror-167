def get_file(*args, **kwargs):
	f = open(*args, **kwargs)
	data = f.read()
	f.close()
	f = None
	return data
def put_file(*args, data=""):
	f = open(*args)
	f.write(data)
	f.close()
	f = None
