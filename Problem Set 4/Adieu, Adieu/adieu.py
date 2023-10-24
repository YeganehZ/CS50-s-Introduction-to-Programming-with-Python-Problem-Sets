'''
In a file called adieu.py, implement a program that 
prompts the user for names, one per line, until the 
user inputs control-d. Assume that the user will input 
at least one name. Then bid adieu to those names, 
separating two names with one and, three names with 
two commas and one and, n and n-1 names with commas and one and, as in the below:

    Adieu, adieu, to Liesl
    Adieu, adieu, to Liesl and Friedrich
    Adieu, adieu, to Liesl, Friedrich, and Louisa
    Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl


'''
list_names=[]
sentence=""
while True:
    try:
        names=input("Name: ")
        list_names.append(names.replace("Name:","") )
        pass

    except EOFError:
        break

if len(list_names)==1:
    print("Adieu, adieu, to " + list_names[0])
elif len(list_names)==2:
    print("Adieu, adieu, to " + list_names[0] + " and " + list_names[1])
else:
    for i in range(len(list_names)):
        if i==len(list_names)-1:
            sentence= sentence + "and " + list_names[i]
        else:
            sentence= sentence + list_names[i] + ", "
       
    print("Adieu, adieu, to " + sentence)