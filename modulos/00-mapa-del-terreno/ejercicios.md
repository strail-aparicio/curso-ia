# Módulo 0 · Ejercicios

[⬅ Volver a la lección](README.md)

## Ejercicio 1: Reglas o aprendizaje

Piensa en tres problemas de sistemas que hayas programado o que conozcas. Para cada uno, responde:

1. ¿Se resuelve mejor con reglas escritas a mano o con aprendizaje a partir de datos? ¿Por qué?
2. Si fuera con ML, ¿qué tipo de aprendizaje sería: supervisado, no supervisado o por refuerzo?

| # | Problema | ¿Reglas o ML? | ¿Por qué? | Tipo de aprendizaje |
|---|----------|---------------|-----------|---------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

## Ejercicio 2: Experimenta con el código

Abre [`codigo/filtro_spam.py`](codigo/filtro_spam.py) y resuelve los tres experimentos del final del archivo. Anota aquí lo que descubriste:

- **Experimento 1 (añadir ejemplos):**
- **Experimento 2 (mayúsculas):**
- **Experimento 3 (frase desconocida):**

---

## Autoevaluación

Responde primero y después despliega la solución.

**1. ¿Cuál es la relación correcta entre IA, Machine Learning, Deep Learning e IA generativa?**

<details><summary>Ver respuesta</summary>

Están anidados: IA ⊃ ML ⊃ Deep Learning ⊃ IA generativa. La IA es el paraguas, el ML es la IA que aprende de datos, el Deep Learning es ML con redes neuronales profundas y la IA generativa es Deep Learning que crea contenido.
</details>

**2. En Machine Learning, ¿qué le das al sistema y qué obtienes?**

<details><summary>Ver respuesta</summary>

Le das datos y respuestas, y obtienes las reglas. Es el proceso inverso a la programación clásica, donde das datos y reglas para obtener respuestas.
</details>

**3. Tienes miles de clientes sin etiqueta y quieres descubrir grupos con hábitos parecidos. ¿Qué tipo de aprendizaje usas?**

<details><summary>Ver respuesta</summary>

No supervisado (clustering). No hay respuestas previas, así que el modelo debe encontrar la estructura por sí mismo.
</details>

**4. Deep Blue venció a Kasparov en 1997. ¿Qué técnica usaba principalmente?**

<details><summary>Ver respuesta</summary>

Búsqueda y evaluación con fuerza bruta. Exploraba millones de jugadas por segundo con funciones de evaluación diseñadas por expertos. Es IA, pero no aprendía de datos.
</details>

**5. ¿Por qué un modelo de lenguaje puede "alucinar" datos falsos?**

<details><summary>Ver respuesta</summary>

Porque genera la respuesta más probable según los patrones que aprendió, no necesariamente la verdadera. Una respuesta puede sonar plausible y aun así ser falsa.
</details>

**6. (Del código) ¿Por qué `predecir("PREMIO GRATIS")` no da el resultado esperado?**

<details><summary>Ver respuesta</summary>

Devuelve `False` porque `"PREMIO"` y `"premio"` son cadenas distintas: el modelo solo vio las palabras en minúsculas, así que no reconoce ninguna y la puntuación queda en 0. Se arregla normalizando el texto con `.lower()` tanto al entrenar como al predecir. Preparar los datos así se llama **preprocesamiento**, y lo verás en todos los proyectos de ML.
</details>
