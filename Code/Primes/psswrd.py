a = "de9f8caa7ea6fe56830925a124d605d4"
p = ""
for i in range (0,20):
	p += a.substring((i%3),(i%5)+(i%3))

print p
