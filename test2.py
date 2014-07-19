with file("treasure_map.txt","r") as text:
#text=file("Hello world.txt","r")
	for line in text:
		no=[]
		line = line.lower()
		for c in line:
			if c.isdigit():
				no.append(c)
		no="".join(no)
		print line[int(no)],

	

	for line in text:
		number=line.find("!@#$%")
		if number>0:
			print line[number+len('!@#$%')]
