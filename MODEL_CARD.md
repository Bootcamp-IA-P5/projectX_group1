# Model card — Proyecto: Detección de Lenguaje de Odio

Nombre del modelo
- Nombre: projectx-xxx (ejemplo)

Resumen
- Tarea: Clasificación de textos para detectar lenguaje de odio / toxicidad en español e inglés
- Arquitectura: (p. ej. DistilBERT / transformer fine-tuned)
- Fecha de entrenamiento: YYYY-MM-DD
- Datos usados: nombre/dominio del dataset (descríbelo y las condiciones de uso)

Métricas
- Métrica principal: F1-macro (u otra)
- Resultados en test set:
  - Precision: X
  - Recall: Y
  - F1: Z

Limitaciones
- Sesgos posibles: (describir)
- Casos en los que el modelo falla: lenguaje muy irónico, regionalismos, contexto multimodal.

Consideraciones éticas
- No usar para decisiones legales o médicas.
- Requiere revisión humana en casos críticos.
- Riesgo de false positives que pueden afectar a usuarios.

Uso y despliegue
- Input: texto plano (string)
- Output: etiqueta + probabilidad
- Ejemplo:
  ```python
  from transformers import AutoTokenizer, AutoModelForSequenceClassification
  # cargar y predecir...
  ```

Mantenimiento
- Fecha de la última actualización del modelo.
- Instrucciones para reproducir el entrenamiento (comandos, seeds y hardware).

Licencia
- Indica licencia de uso del modelo y restricciones.
