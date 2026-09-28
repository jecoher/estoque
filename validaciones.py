
# FUNC VALIDACION, TRATAMIENTO, CARGA Y DESCAGAR
########################################################
def tratamiento_float(entrada_user):
    """
    devuelve float si el numero esta correcto
    None >>> si hay valor diferente de float
    """
    try:
        cambio_para_float = float(entrada_user)
        return cambio_para_float
    except ValueError:
        return None

    
def validar_opcion_menu(int_user):
    """
    Devuelve la opc del menu principal\n
    None -> si no es ninguna de las seleccionadads
    """
    if int_user == "v":
        return 'v'
    elif int_user == "e":
            return 'e'
    elif int_user == "a":
            return 'a'
    elif int_user == "s":
            return 's'
    elif int_user == 'r':
        return 'r'
    else:
         return None


def validacion_id_user(id_user):
    try:
        id_validado = int(id_user)
        return id_validado
    except ValueError:
        return None




