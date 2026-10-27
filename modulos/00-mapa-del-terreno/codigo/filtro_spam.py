"""
Módulo 0 · Reglas escritas a mano frente a reglas aprendidas de datos.

Ejecuta este archivo completo:
    uv run modulos/00-mapa-del-terreno/codigo/filtro_spam.py

O celda a celda en VSCodium: cada bloque que empieza con "# %%" es una
celda. Pulsa "Run Cell" encima de ella (o Shift+Enter).
"""

# %% [markdown]
# ## 1. Enfoque clásico: tú escribes las reglas
#
#     datos + reglas  →  respuestas

# %%
def es_spam_por_reglas(correo: str) -> bool:
    palabras_sospechosas = ["gratis", "premio", "urgente"]
    return any(p in correo.lower() for p in palabras_sospechosas)


print("Reglas →", es_spam_por_reglas("Has ganado un PREMIO"))   # True
print("Reglas →", es_spam_por_reglas("Te envío el informe"))    # False

# %% [markdown]
# ## 2. Enfoque Machine Learning: el programa deduce las reglas
#
#     datos + respuestas  →  reglas
#
# Nadie le dice qué palabras son sospechosas. Las descubre contando
# en qué tipo de correo aparece cada una.

# %%
from collections import Counter

# Datos de entrenamiento: (texto, ¿es spam?)
ejemplos = [
    ("gana un premio gratis ya", True),
    ("reunión mañana a las 10", False),
    ("premio urgente haz clic", True),
    ("te envío el informe", False),
]

# "Entrenamiento": contar palabras por categoría
spam, normal = Counter(), Counter()
for texto, etiqueta in ejemplos:
    (spam if etiqueta else normal).update(texto.split())

print("Palabras en spam:  ", dict(spam))
print("Palabras en normal:", dict(normal))

# %%
# "Predicción": las palabras de spam suman puntos y las normales restan
def predecir(texto: str) -> bool:
    puntos = sum(spam[p] - normal[p] for p in texto.split())
    return puntos > 0


print("Aprendido →", predecir("premio gratis"))          # True
print("Aprendido →", predecir("el informe de mañana"))   # False

# %% [markdown]
# ## 3. Experimenta
#
# 1. Añade ejemplos a la lista `ejemplos` y vuelve a ejecutar las celdas.
#    El comportamiento cambia sin tocar la función `predecir`.
# 2. Prueba `predecir("PREMIO GRATIS")`. ¿Por qué falla?
#    (Pista: mayúsculas. ¿Cómo lo arreglarías?)
# 3. Prueba una frase sin ninguna palabra conocida. ¿Qué devuelve y por qué?
