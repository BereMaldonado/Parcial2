import model.package_model.Persona as Persona
obj_persona = Persona.Persona()
lista_personas = obj_persona.obtener_personas()

if lista_personas!=None:
    for x in lista_personas:
        print(x[0],x[1])
else:
    print("No se encontraron datos de persona")


lista_personas_id = obj_persona.obtener_persona_por_id(1)
if lista_personas_id!=None:
    print("si")
    print(lista_personas_id[0], lista_personas_id[1])
else:
    print("no")
    
#Insertar
# obj_persona=Persona.Persona("","MAFL001122MCLLRDA8","Alexis","Maldonado","Garcia","8444444444","8444444444","correo@correo.com")
# result_ins=obj_persona.insertar_persona(obj_persona)
# if result_ins=="1":
#     print("La persona fue registrado con exito")
# else:
#     print("No se pudo registrar la persona")
    
#Update
# obj_persona_upd=Persona.Persona(1, 'MAGA031200MCLLRDA5', 'BERENICE ', 'MALDONADO', 'GARCIA', '12345678910', '8441554061', 'abere@gmail.com')
# result_upd=obj_persona_upd.update_persona(obj_persona_upd)
# if result_upd=="1":
#     print("El persona fue actualizado con exito")
# else:
#     print("No se pudo actualizar el persona")
    
    #ctl+k+c
    
#Delete
#borra_persona_id=obj_persona.eliminar_persona(2)
#if borra_persona_id==1:
#    print("El persona fue borrado con exito")
#else:
#    print("No se pudo borrar el persona")