import model.package_model.Municipio as Municipio
obj_municipio = Municipio.Municipio()
lista_municipios = obj_municipio.obtener_municipios()

if lista_municipios!=None:
    for x in lista_municipios:
        print(x[0],x[1])
else:
    print("No se encontraron datos de municipio")


lista_municipios_id = obj_municipio.obtener_municipio_por_id(1)
if lista_municipios_id!=None:
    print("si")
    print(lista_municipios_id[0], lista_municipios_id[1])
else:
    print("no")
    
#Insertar
# obj_municipio=Municipio.Municipio("","Conchita del Oro")
# result_ins=obj_municipio.insertar_municipio(obj_municipio)
# if result_ins=="1":
#     print("El municipio fue registrado con exito")
# else:
#     print("No se pudo registrar el municipio")
    
#Update
# obj_municipio_upd=Municipio.Municipio(1,"Abasole")
# result_upd=obj_municipio_upd.update_municipio(obj_municipio_upd)
# if result_upd=="1":
#     print("El municipio fue actualizado con exito")
# else:
#     print("No se pudo actualizar el municipio")
    
    #ctl+k+c
    
#Delete
#borra_municipio_id=obj_municipio.eliminar_municipio(2)
#if borra_municipio_id==1:
#    print("El municipio fue borrado con exito")
#else:
#    print("No se pudo borrar el municipio")