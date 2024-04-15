import model.package_model.Asunto as Asunto
obj_asunto = Asunto.Asunto()
lista_asuntos = obj_asunto.obtener_asuntos()

if lista_asuntos!=None:
    for x in lista_asuntos:
        print(x[0],x[1])
else:
    print("No se encontraron datos de asuntos")

#Obtener
# lista_asuntos_id = obj_asunto.obtener_asunto_por_id(1)
# if lista_asuntos_id!=None:
#     print("si")
#     print(lista_asuntos_id[0], lista_asuntos_id[1])
# else:
#     print("no")
    
#Insertar
# obj_asunto=Asunto.Asunto("","Baja")
# result_ins=obj_asunto.insertar_asunto(obj_asunto)
# if result_ins=="1":
#     print("El asunto fue registrado con exito")
# else:
#     print("No se pudo registrar el asunto")
    
#Update
# obj_asunto_upd=Asunto.Asunto(1,"Reinscripciones")
# result_upd=obj_asunto_upd.update_asunto(obj_asunto_upd)
# if result_upd=="1":
#     print("El asunto fue actualizado con exito")
# else:
#     print("No se pudo actualizar el asunto")
    
    #ctl+k+c
    
#Delete
# borra_asunto_id=obj_asunto.eliminar_asunto(2)
# if borra_asunto_id==1:
#     print("El asunto fue borrado con exito")
# else:
#     print("No se pudo borrar el asunto")