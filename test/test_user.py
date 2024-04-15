import model.package_model.User as User
obj_user = User.User()
lista_users = obj_user.obtener_users()

if lista_users!=None:
    for x in lista_users:
        print(x[0],x[1])
else:
    print("No se encontraron datos de user")


lista_users_id = obj_user.obtener_user_por_id(1)
if lista_users_id!=None:
    print("si")
    print(lista_users_id[0], lista_users_id[1])
else:
    print("no")
    
#Insertar
# obj_user=User.User("","Yop","yyy2","user")
# result_ins=obj_user.insertar_user(obj_user)
# if result_ins=="1":
#     print("El user fue registrado con exito")
# else:
#     print("No se pudo registrar el user")
    
#Update
# obj_user_upd=User.User(1,"ABere","bbb3","admin")
# result_upd=obj_user_upd.update_user(obj_user_upd)
# if result_upd=="1":
#     print("El user fue actualizado con exito")
# else:
#     print("No se pudo actualizar el user")
    
    #ctl+k+c
    
#Delete
#borra_user_id=obj_user.eliminar_user(2)
#if borra_user_id==1:
#    print("El user fue borrado con exito")
#else:
#    print("No se pudo borrar el user")