def remove_duplicates(lista):
        lista2=[]
        if lista:
            for item in lista:
                if item not in lista2:
                    lista2.append(item)
        else:
            return
