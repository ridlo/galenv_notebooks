#!/home/ridlo/anaconda2/bin/python

import galenv

obj = ["3C 273", "3C 454.3", "PKS J2232+1143", "PKS J1924-2914", "3C 279", "PKS J1058+0133"]

dirname = "./images/"

for objname in obj:
	try:
		galenv.run(objname, 10.0, 5000.0, show=False, savefig=True, imgname=dirname+objname+"_10_5000.png")
	except Exception as e:
		print str(e)
		continue