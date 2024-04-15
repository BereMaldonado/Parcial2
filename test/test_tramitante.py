import model.package_model.Tramitante as Tramitante
obj_tramitante = Tramitante.Tramitante()
lista_tramitantes = obj_tramitante.obtener_tramitantes()

if lista_tramitantes!=None:
    for x in lista_tramitantes:
        print(x[0],x[1])
else:
    print("No se encontraron datos de tramitante")


lista_tramitantes_id = obj_tramitante.obtener_tramitante_por_id(1)
if lista_tramitantes_id!=None:
    print("si")
    print(lista_tramitantes_id[0], lista_tramitantes_id[1])
else:
    print("no")
    
#Insertar
# obj_tramitante=Tramitante.Tramitante("","Elohim de la Rosa García")
# result_ins=obj_tramitante.insertar_tramitante(obj_tramitante)
# if result_ins=="1":
#     print("El tramitante fue registrado con exito")
# else:
#     print("No se pudo registrar el tramitante")
    
#Update
# obj_tramitante_upd=Nivel.Nivel(1,"Adriana Maldonado García")
# result_upd=obj_tramitante_upd.update_tramitante(obj_tramitante_upd)
# if result_upd=="1":
#     print("El tramitante fue actualizado con exito")
# else:
#     print("No se pudo actualizar el tramitante")
    
    #ctl+k+c
    
#Delete
#borra_tramitante_id=obj_tramitante.eliminar_tramitante(2)
#if borra_tramitante_id==1:
#    print("El tramitante fue borrado con exito")
#else:
#    print("No se pudo borrar el tramitante")