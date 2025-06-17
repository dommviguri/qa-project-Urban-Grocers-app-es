import sender_stand_request
import data

#cambiar el nombre del kit en el diccioanrio
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body['name'] = name
    return current_body

#####enviar una solicitud para crear un nuevo kit

def test_create_kit_1_char_get_201():
    kit_body = get_kit_body('a')
    kit_response = sender_stand_request.post_new_kit(kit_body)

    assert kit_response.status_code == 201
    print(kit_response.status_code)


#Evitar repetición, se sintetiza lo anterior, se deja la variable: kit_body
def positive_assert(kit_body):
    kit_body = get_kit_body(kit_body)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201

def negative_assert_code_400(kit_body):
    kit_body = get_kit_body(kit_body)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400

##########################
####pruebas###############

#prueba 1. Creación de un nuevo kit
# El parámetro 'name' contiene un caracter
def test_create_kit_1_char_get_201():
        positive_assert(data.kit_body["name_1"])

#prueba 2. Creación de un nuevo kit
# El parámetro 'name' contiene 511 caracteres
def test_create_kit_511_char_get_201():
        positive_assert(data.kit_body['name_2'])

#prueba 3. Creación de un nuevo kit
# El parámetro 'name' contiene 0 caracteres
def test_create_kit_0_char_get_400():
        negative_assert_code_400(data.kit_body['name_3'])

#prueba 4. Creación de un nuevo kit
# El parámetro 'name' contiene 512
def test_create_kit_511_char_get_400():
        negative_assert_code_400(data.kit_body['name_4'])

#prueba 5. Creación de un nuevo kit
# El parámetro 'name' contiene caracteres especiales
def test_create_kit_special_char_get_201():
        positive_assert(data.kit_body['name_5'])

# prueba 6. Creación de un nuevo kit
# El parámetro 'name' permite espacios
def test_create_kit_with_spaces_get_201():
        positive_assert(data.kit_body['name_6'])

# prueba 7. Creación de un nuevo kit
# El parámetro 'name' permite números
def test_create_kit_with_nums_get_201():
        positive_assert(data.kit_body['name_7'])

# prueba 8. Creación de un nuevo kit
# El parámetro 'name' ni se pasa en la solicitud
def test_create_kit_empty_get_400():
        negative_assert_code_400(data.kit_body['name_8'])

# prueba 9. Creación de un nuevo kit
# El parámetro 'name' entra un param diferente (número)
def test_create_kit_dif_param_get_400():
        negative_assert_code_400(data.kit_body['name_9'])



