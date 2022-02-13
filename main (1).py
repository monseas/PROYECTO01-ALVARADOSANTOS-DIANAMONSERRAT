# -*- coding: utf-8 -*-
# _*_ coding:utf-8 _*_
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

"""
Login
credenciales:

usuario:
    Monse
contraseña:
    MonseFQ
"""
usuarioAccedio = False
intentos = 0
# Bienvenida!
mensaje_bienvenida = 'Bienvenidos a Lifestore Market!\nAccede con tus credenciales'
print(mensaje_bienvenida)

# Recibo constantemente sus intentos
while not usuarioAccedio:
    # Primero ingresa Credenciales
    usuario = input('Usuario: ')
    contras = input('Contrase;a: ')
    intentos += 1
    # Reviso si el par coincide
    if usuario == 'Monse' and contras == 'MonseFQ':
        usuarioAccedio = True
        print('Hola de nuevo!')
    else:
        # print('Tienes', 3 - intentos, 'intentos restantes')
        print(f'Tienes {3 - intentos} intentos restantes')
        if usuario == 'jimmy':
            print('Te equivocaste en la contrase;a')
        else:
            print(f'El usuario: "{usuario}" no esta registrado')
            
    if intentos == 3:
        exit()

print('A continuación los resultados del análisis')


"""
continuacion ...
"""

############################################################
print('Los productos mas vendidos son los siguientes: ')
#De lifestore_sales los 5 productos con mayores ventas#

#De lista de ventas selecciono el id_product, exceptuando las devoluciones 
lista_venta=[sale[1] for sale in lifestore_sales if sale[4]==0]
#Creo un diccionario vacío donde almacenaré cada elemento en la lista
mas_vendido={}
for venta in lista_venta:
  if venta in mas_vendido:
   mas_vendido[venta]+=1
  else:
   mas_vendido[venta]=1 
#print(mas_vendido)

#Ordenar el diccionario por valor, se utiliza operator para odernar el valor del numero de veces repetidas y sorted ordena de mayor a menor 
import operator
mas_vendido_sort = sorted(mas_vendido.items(), key=operator.itemgetter(1), reverse=True)
for n in enumerate(mas_vendido_sort):
    print('El producto',n[1][0], 'tiene', mas_vendido[n[1][0]],'articulos vendidos')
print('---------------------------------------------------')
############################################################
print('Los productos con mayores busquedas es la siguiente: ')
#__________________________________________________________
#De lifestore_searches los 10 productos con mayores busquedas#

#De lista de busqueda selecciono el id_product
lista_searches=[search[1] for search in lifestore_searches] 
#Creo un diccionario vacío donde almacenaré cada elemento en la lista

mas_buscado={}
for busqueda in lista_searches:
  if busqueda in mas_buscado:
   mas_buscado[busqueda]+=1
  else:
   mas_buscado[busqueda]=1

#Ordenar el diccionario por valor, se utiliza operator para odernar el valor del numero de veces repetidas y sorted ordena de mayor a menor 
import operator
mas_buscado_sort = sorted(mas_buscado.items(), key=operator.itemgetter(1), reverse=True)
for n in enumerate(mas_buscado_sort):
    print('El producto',n[1][0], 'tiene', mas_buscado[n[1][0]],'busquedas')

print('------------------------------------------')
print('Los menos vendidos y buscados por categoria son: ')
# Diccionario de busquedas por id
prods_busquedas = {}
for search in lifestore_searches:
    prod_id = search[1]
    busqueda = search[0]
    if busqueda not in prods_busquedas.keys():
        prods_busquedas[busqueda] = []
    prods_busquedas[busqueda].append(prod_id)

# Diccionario de ids por categoria
cat_prods = {}
for prod in lifestore_products:
    prod_id = prod[0]
    cat = prod[3]
    if cat not in cat_prods.keys():
        cat_prods[cat] = []
    cat_prods[cat].append(prod_id)

# Ventas por categorias
cat_ventas = {}
for cat in cat_prods.keys():
    # La lista de productos de la categoria
    prods_list = cat_prods[cat]

    # Lista vacía para las busquedas por categoria inciando ganancias y ventas en cero
    busquedas_cat = []
    ganancias = 0
    ventas = 0

    # Por cada producto de esa categoria
    for prod_id in prods_list:
        # Obtengo las reviews, precio y cantidad de ventas del producto
        if prod_id not in prods_busquedas.keys():
            continue
        searches = prods_busquedas[prod_id]
        precio = lifestore_products[prod_id-1][2]
        total_sales = len(searches)
        # Guardo las ganancias y total de ventas en los datos de la categoria
        ganancias += precio * total_sales
        ventas += total_sales
        busquedas_cat += searches

    # Calculo la busqueda promedio de la categoria
    busq_prom_cat = sum(busquedas_cat)/len(busquedas_cat)
    # Guardo todo en mi diccionario
    cat_ventas[cat] = {
        'Busquedas promedio': busq_prom_cat,
        'Ganancias totales': ganancias,
        'ventas_totales': ventas
    }

f'string'

for key in cat_ventas.keys():
    print(key)
    for llave, valor in cat_ventas[key].items():
        print(f'\t {llave}: {valor}')

print('--------------------------------')
print('Los productos con mejores reseñas son: ')
ranking=[]
#Iteramos sobre cada uno de los productos
for product in lifestore_products:
  #Primero voy a ir guardando unicamente las puntuaciones de las diferentes ventas
  score_products=[]
  for sale in lifestore_sales:
    #Si el idproduct=idproduct las puntuaciones se añaden a la lista existente con append
    if product[0] == sale[1]:
      score_products.append(sale[2])
  #Descarto los productos sin reseñas    
  if len(score_products) != 0:
  #Evaluo el promedio como la suma/longitud
    score_promedio=(sum(score_products))/(len(score_products))
    ranking.append([product[0],score_promedio])

#Con sorted ordené de mayor a menor el promedio de las puntuaciones
ranking_orden=sorted(ranking, key=lambda score:score[1], reverse=True)
#Ordeno los productos por puntuación
for i,j in ranking_orden:
    print('El producto',i, 'tiene una puntuación de',j)

print('-------------------------------------')
print('El análisis de ingresos es: ')
id_fecha=[[sale[0], sale[3]] for sale in lifestore_sales if sale[4]==0]

#Categorizar en un diccionario
ventas_mensuales={}
for par in id_fecha:
  id=par[0]
  _,mes,_=par[1].split('/')
  #El mes se crea si no existe con una llave
  if mes not in ventas_mensuales.keys():
    ventas_mensuales[mes]=[]
  ventas_mensuales[mes].append(id)

#Calculo por mes:
suma_anual=0
for key in ventas_mensuales.keys():
  lista_mes=ventas_mensuales[key]
  suma_venta=0
  for id_venta in lista_mes:
    indice=id_venta-1
    info_venta=lifestore_sales[indice]
    id_product=info_venta[1]
    precio=lifestore_products[id_product-1][2]
    suma_venta+=precio
  

  suma_anual+=suma_venta
  print('El mes',key,'tiene $',suma_venta, 'en ventas, con ',len(lista_mes),'articulos vendidos')
  print('Ventas acumuladas: $',suma_anual)
print('-------------------------------------')