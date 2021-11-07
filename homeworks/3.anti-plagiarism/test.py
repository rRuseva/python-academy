from formatting import format_msg
# fdsfdsf

def send(name, website=None, verbose=False):
	if website is not None:
		msg = format_msg(my_name=name,my_website=website)
	else:
		msg = format_msg(my_name=name)
	if verbose:
		print(name, website)

	r = requests.get

	if r.status_code = 200: 
		return r.json()
	else:
		print("There was an error!")


if __name__ ==  "__main":
	print(sys.arg)
	name = "uknown"
	if len(sys.argv) > 1:
		name = sys.argv[1]

	response = send(name, verbose=True)
	print(response)