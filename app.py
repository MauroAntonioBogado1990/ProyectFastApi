from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Text
from datetime  import datetime
from typing import Optional

class Users(BaseModel):
    id: int
    name: str
    lastname: str    
    create: int 
    age: int
    address: str
    description: Optional[Text]

class Elements(BaseModel):
    id: int
    name: str
    create: int 
    size: Optional[str]
    description: Optional[Text]



app =  FastAPI()
 
elements = []
usuarios = []


@app.get('/')
def root_route():
    return ('welcome to page')

@app.get('/posts')
def retornar_post():
    print('Esta es la ruta de post')
    return elements

@app.post('/posts')
def guardar_post(element: Elements):
    print(element.dict())
    elements.append(element.dict())
    print('received post')
    print(element)
    return elements[-1]

@app.get('/posts/{post_id}')
def devolver_post(post_id: int):
    for p in elements:
        if p["id"] == post_id:
            return  p           
    raise HTTPException(status_code=404, detail='No existe el elemento')  

@app.delete('/posts/{post_id}')
def eliminate_post(post_id: int):
    for i, p in enumerate(elements):
        if p["id"] == post_id:
            elements.pop(i)
            return  "han sido eliminados"           
    raise HTTPException(status_code=404, detail='No existe el elemento')  

###Así se agregan los usuarios en la lista de usuarios
@app.post('/user')
def crear_users(user: Users):
    usuario = user.dict()
    print (usuario)
    
    #print(usuario.dict())
    usuarios.append(usuario)
    print('Usuarios recibidos')
    print(usuario)
    return usuarios     
    
### Se retorna la lista completa de los usuarios     
@app.get('/user')
def obtener_usuarios():
    print('Se retorna la lista de usuarios ')
    return usuarios

### Retornar el usuario por ID
@app.get('/user/{user_id}')
def devolver_usuario(user_id: int):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            return {'usuario':usuario}
    return ('No se encontro el usuario')