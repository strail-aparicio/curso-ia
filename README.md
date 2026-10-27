# Curso de Inteligencia Artificial desde cero

Hoja de ruta personal para aprender IA partiendo de experiencia en programación.

- **Lenguaje principal:** Python. Más adelante se conecta con Java, Kotlin, Swift, C#, Rust y C++.
- **Método de cada lección:** concepto → intuición (analogías y dibujos) → código → ejercicio.
- **Ritmo orientativo:** 5 a 8 horas por semana, entre 6 y 9 meses en total. Las fases 1 y 2 son la base; no conviene saltarlas.

## Cómo usar este proyecto

1. Instala [uv](https://docs.astral.sh/uv/), el gestor de Python que usaremos:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2. Dentro de la carpeta del curso, crea el entorno e instala las dependencias:
   ```bash
   uv sync
   ```
3. Abre la carpeta en VSCodium (`codium .`) y acepta instalar las extensiones recomendadas.
4. Elige el intérprete de `.venv` (`Ctrl+Shift+P` → *Python: Select Interpreter*).
5. Abre cualquier `.py` con celdas `# %%` y pulsa **Run Cell**, o ejecuta el archivo completo:
   ```bash
   uv run modulos/00-mapa-del-terreno/codigo/filtro_spam.py
   ```

Para ver el Markdown renderizado usa `Ctrl+Shift+V`. Con *Markdown All in One* puedes marcar una casilla con `Alt+C`.

## Estructura

```
curso-ia/
├── README.md          ← este temario
├── pyproject.toml     ← dependencias (uv)
├── modulos/
│   └── NN-nombre/
│       ├── README.md      ← la lección
│       ├── ejercicios.md  ← enunciados y tus respuestas
│       └── codigo/        ← scripts con celdas # %%
├── datos/             ← datasets (no se suben a Git)
└── notas/
    ├── glosario.md    ← términos aprendidos
    └── diario.md      ← diario de sesiones
```

## Registro de avance

| Fase | Módulos | Estado | Inicio | Fin |
|------|---------|--------|--------|-----|
| 1. Fundamentos | 0 – 2 | En curso | | |
| 2. Machine Learning clásico | 3 – 6 | Pendiente | | |
| 3. Deep Learning | 7 – 10 | Pendiente | | |
| 4. La IA moderna | 11 – 15 | Pendiente | | |
| 5. Del notebook al mundo real | 16 – 18 | Pendiente | | |

---

## Fase 1: Fundamentos

### [Módulo 0. El mapa del terreno](modulos/00-mapa-del-terreno/README.md)

- [ ] Qué es la IA y en qué se diferencia del ML, el Deep Learning y la IA generativa
- [ ] Breve historia: de los sistemas de reglas a los asistentes actuales
- [ ] Los tres tipos de aprendizaje: supervisado, no supervisado y por refuerzo
- [ ] Qué puede hacer la IA hoy y qué no puede hacer

### [Módulo 1. Caja de herramientas](modulos/01-caja-de-herramientas/README.md)

- [ ] Python para quien ya programa (sintaxis, listas, diccionarios, funciones, clases)
- [ ] Entornos: uv, celdas `# %%` en VSCodium y Google Colab (GPU gratis)
- [ ] NumPy (cálculo con matrices)
- [ ] pandas (manejo de datos)
- [ ] matplotlib (gráficas)
- [ ] **Práctica:** analizar un dataset real y graficarlo

### [Módulo 2. Las matemáticas necesarias, explicadas de forma intuitiva](modulos/02-matematicas/README.md)

- [ ] Álgebra lineal: vectores, matrices y producto punto
- [ ] Cálculo: derivadas, gradiente y la idea de "bajar la montaña"
- [ ] Probabilidad y estadística: distribuciones, media, varianza y teorema de Bayes
- [ ] Todo con código, sin demostraciones formales

## Fase 2: Machine Learning clásico

### [Módulo 3. IA "antigua" (breve pero útil)](modulos/03-ia-clasica/README.md)

- [ ] Búsqueda: BFS, DFS y A* (el GPS de los videojuegos)
- [ ] Sistemas basados en reglas y por qué no escalan

### [Módulo 4. Aprendizaje supervisado](modulos/04-aprendizaje-supervisado/README.md)

- [ ] Regresión lineal: el primer modelo, implementado desde cero
- [ ] Regresión logística y clasificación
- [ ] k-NN
- [ ] Árboles de decisión y Random Forest
- [ ] SVM
- [ ] scikit-learn
- [ ] **Proyecto:** predecir precios de viviendas o detectar spam

### [Módulo 5. Evaluar modelos](modulos/05-evaluar-modelos/README.md)

- [ ] Conjuntos de entrenamiento, validación y prueba
- [ ] Overfitting y underfitting
- [ ] Métricas: accuracy, precision, recall, F1 y matriz de confusión
- [ ] Validación cruzada
- [ ] Ingeniería de características

### [Módulo 6. Aprendizaje no supervisado](modulos/06-aprendizaje-no-supervisado/README.md)

- [ ] Clustering con k-means
- [ ] Reducción de dimensionalidad con PCA
- [ ] **Proyecto:** segmentar clientes

## Fase 3: Deep Learning

### [Módulo 7. Redes neuronales desde cero](modulos/07-redes-neuronales/README.md)

- [ ] La neurona artificial y el perceptrón
- [ ] Funciones de activación
- [ ] Backpropagation paso a paso
- [ ] **Proyecto clave:** red neuronal en NumPy puro que reconoce dígitos escritos a mano

### [Módulo 8. PyTorch](modulos/08-pytorch/README.md)

- [ ] Tensores, autograd y el ciclo de entrenamiento
- [ ] Optimizadores: SGD y Adam
- [ ] Regularización: dropout y batch normalization
- [ ] Uso de GPU

### [Módulo 9. Visión por computadora](modulos/09-vision-por-computadora/README.md)

- [ ] Redes convolucionales (CNN)
- [ ] Transfer learning: reutilizar modelos preentrenados
- [ ] **Proyecto:** clasificador de imágenes propio

### [Módulo 10. Secuencias](modulos/10-secuencias/README.md)

- [ ] RNN y LSTM: la memoria en las redes
- [ ] Por qué fueron reemplazadas por los Transformers

## Fase 4: La IA moderna

### [Módulo 11. Lenguaje natural y Transformers](modulos/11-transformers/README.md)

- [ ] Tokenización
- [ ] Embeddings: palabras convertidas en vectores
- [ ] El mecanismo de atención
- [ ] La arquitectura Transformer pieza por pieza
- [ ] **Proyecto:** mini-GPT entrenado sobre textos en español

### [Módulo 12. Modelos de lenguaje grandes (LLMs)](modulos/12-llms/README.md)

- [ ] Cómo se entrenan: preentrenamiento, fine-tuning y RLHF
- [ ] Ingeniería de prompts
- [ ] Uso de APIs de modelos comerciales
- [ ] Modelos locales (Ollama, llama.cpp)
- [ ] Fine-tuning eficiente con LoRA
- [ ] Hugging Face

### [Módulo 13. Construir aplicaciones con IA](modulos/13-aplicaciones-con-ia/README.md)

- [ ] RAG: que la IA responda usando tus propios documentos
- [ ] Bases de datos vectoriales (pgvector, Chroma)
- [ ] Agentes y tool use: IA que ejecuta acciones
- [ ] **Proyecto:** asistente que responde preguntas sobre tu documentación

### [Módulo 14. IA generativa de imágenes y audio](modulos/14-ia-generativa-multimedia/README.md)

- [ ] Modelos de difusión: cómo nace una imagen a partir de ruido
- [ ] Modelos multimodales

### [Módulo 15. Aprendizaje por refuerzo](modulos/15-aprendizaje-por-refuerzo/README.md)

- [ ] Agente, entorno y recompensa
- [ ] Q-learning
- [ ] **Proyecto:** una IA que aprende a jugar un juego sencillo

## Fase 5: Del notebook al mundo real

### [Módulo 16. IA en producción (MLOps)](modulos/16-mlops/README.md)

- [ ] Servir modelos con una API (FastAPI)
- [ ] Empaquetar con Docker
- [ ] ONNX: ejecutar modelos desde Java, C#, Rust o C++
- [ ] IA en móviles: Core ML (Swift/iOS) y LiteRT (Kotlin/Android)
- [ ] Monitoreo, versionado y evaluación continua

### [Módulo 17. Ética, seguridad y límites](modulos/17-etica-y-seguridad/README.md)

- [ ] Sesgos en los datos
- [ ] Alucinaciones
- [ ] Privacidad y prompt injection
- [ ] Regulación (EU AI Act, entre otras)

### [Módulo 18. Proyecto final](modulos/18-proyecto-final/README.md)

- [ ] Elegir el problema
- [ ] Datos y preparación
- [ ] Modelo y evaluación
- [ ] Despliegue
- [ ] Presentación y documentación

---

📓 [Glosario](notas/glosario.md) · [Diario](notas/diario.md) · [Datos](datos/README.md)
