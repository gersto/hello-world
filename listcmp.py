#!/usr/bin/python

l1=(1,2,3)
l2=(1,2,3)

ll1=len(l1)
ll2=len(l2)

if ll1 == ll2:
	for le1 in l1:
		z=0
		for le2 in l2:
			if le1 == le2:
				break
			else:
				if z == ll2-1:
					print("Listen ungleich")
			z=z+1
else:
	print("Listenlaenge ungleich")
