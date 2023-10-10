a=int(input("Enter jug A capacity:"))
b=int(input("Enter jug B capacity:"))
ai=int(input("Initially water in jug A:"))
bi=int(input("Initially water in jug B:"))
af=int(input("Final state of jug A:"))
bf=int(input("Final state of jug B:"))
print("List of operations you can Do\n")
print("1.Fill jug A completely\n")
print("2.Fill jug B completely\n")
print("3.Empty jug A completely\n")
print("4.Empty jug B completely\n")
print("5.Pour from jug A till jug B filled completely or A becomes empty\n")
print("6.Pour from jug B till jug A filled completely or B becomes empty\n")
print("7.Pour all from jug B to jug A\n")
print("8.Pour all from jug A to jug B\n")
while((ai!=af or bi!=bf)):
	op=int(input("Enter the operation:"))
	if (op==1):
		ai=a
	elif op==2:
		bi=b
	elif op==3:
		ai=0
	elif op==4:
		bi=0
	elif op==5:
		if (b-bi>ai):
			bi=ai+bi
			ai=0
		else:
			ai=ai-(b-bi)
			bi=b
	elif op==6:
		if (a-ai>bi):
			ai=ai+bi
			bi=0
		else:
			bi=bi-(a-ai)
			print("***",ai)
			ai=a
	elif op==7:
		if ai+bi>a:
			print("Jug A Overflown")
			break;
		else:
			ai=ai+bi
			bi=0
	elif op==8:
		if ai+bi>b:
			print("Jug B Overflown")
			break;
		else:
			bi=bi+ai
			ai=0
	print(ai,bi)