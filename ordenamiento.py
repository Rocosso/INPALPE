from Indice import *
def Ordenamiento(p):
	for i in range(len(p)):
		for j in range(i+1,len(p)):		
			if(p[i].get_fv()>p[j].get_fv()):
				temp=p[i]
				p[i]=p[j]
				p[j]=temp
	

			

	