def variable_argument( arg, *vari):
    print ("Out-put is",arg)
    for var in vari:
        print (var)
variable_argument(60)
variable_argument("Hari",100,90,40,50,60)