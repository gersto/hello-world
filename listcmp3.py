#!/usr/bin/python

l1=(1,2,3)
l2=(1,2,3)

ll1=len(l1)
ll2=len(l2)

if ll1 == ll2:
	count=0
	while(count < ll1):
		le1=l1[count]
		count2=0
		while(count2 < ll2):
			le2=l2[count2]
			print(le1,le2)
			count2+=1
			if le2 == 2:
				break
		count+=1
#		if le1 == 2:
#			break
else:
	print("Listenlaenge ungleich")