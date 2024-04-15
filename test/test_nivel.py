import model.package_model.Nivel as Nivel
obj_nivel = Nivel.Nivel()
lista_niveles = obj_nivel.obtener_niveles()

if lista_niveles!=None:
    for x in lista_niveles:
        print(x[0],x[1])
else:
    print("No se encontraron datos de nivel")


lista_niveles_id = obj_nivel.obtener_nivel_por_id(1)
if lista_niveles_id!=None:
    print("si")
    print(lista_niveles_id[0], lista_niveles_id[1])
else:
    print("no")
    
#Insertar
# obj_nivel=Nivel.Nivel("","Doctorado")
# result_ins=obj_nivel.insertar_nivel(obj_nivel)
# if result_ins=="1":
#     print("El nivel fue registrado con exito")
# else:
#     print("No se pudo registrar el nivel")
    
#Update
# obj_nivel_upd=Nivel.Nivel(1,"Preeescolar")
# result_upd=obj_nivel_upd.update_nivel(obj_nivel_upd)
# if result_upd=="1":
#     print("El nivel fue actualizado con exito")
# else:
#     print("No se pudo actualizar el nivel")
    
    #ctl+k+c
    
#Delete
#borra_nivel_id=obj_nivel.eliminar_nivel(2)
#if borra_nivel_id==1:
#    print("El nivel fue borrado con exito")
#else:
#    print("No se pudo borrar el nivel")