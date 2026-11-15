# Checklist de entrega · TFM7

## Contenido del ZIP

- [x] `TFM7.ipynb`: configuración, carga, prueba de recuperación, ejemplos, seguimiento y chat.
- [x] `rag.py` y `app.py`: agente compartido e interfaz local opcional.
- [x] `requirements.txt`, `.env.example` y `.gitignore`: dependencias, configuración sin clave y exclusiones.
- [x] `fuentes.json` y los tres PDF de `corpus/`: CSF 2.0, SP 800-207 y SP 800-61 Rev. 3.
- [x] `README.md`, `VALIDACION.md`, `AUDITORIA_FINAL.md` y este checklist.
- [x] `test_local.py`: pruebas reproducibles sin uso de cuota.
- [x] `TFM7-defensa.pptx` y `DEFENSA.md`: diapositivas y guion de siete minutos.

El ZIP se genera con una lista explícita de archivos. El duplicado de CSF que existe en la raíz queda fuera. El agente lee la copia de `corpus/`. La colección ChromaDB se reconstruye desde los PDF y Gemini Embeddings al abrir el proyecto por primera vez. El ZIP excluye la configuración privada, el entorno virtual, la colección generada, los ensayos y los archivos temporales.

## Comprobación en el equipo de entrega

- [ ] Abrir el ZIP en una carpeta nueva y seguir el README con Python 3.12.
- [ ] Crear un `.env` local a partir de la plantilla y configurar la clave privada de Gemini.
- [ ] Ejecutar `pip check` y `python -m unittest -v test_local`.
- [ ] Verificar que ChromaDB termina la primera indexación con 397 fragmentos.
- [ ] Ejecutar el notebook y comprobar las tres fuentes esperadas, los cinco ejemplos, el seguimiento y el chat.
- [ ] Ensayar la defensa de 5 a 10 minutos con una pregunta, una fuente abierta y un seguimiento.
- [ ] Entregar el ZIP y realizar la demostración oral el día de la evaluación.

Streamlit local es un bonus. El despliegue público queda fuera de esta entrega.
