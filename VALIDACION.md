# Validación y rúbrica del PDF

| Criterio | Evidencia y comprobación |
|---|---|
| Base de conocimiento | Tres publicaciones NIST. El notebook cuenta páginas y fragmentos y comprueba el tamaño de la colección. |
| RAG con Gemini | Consultas de recuperación con fuente esperada, cinco preguntas de referencia y prueba de abstención. Ejecución real pendiente de credenciales. |
| Ingeniería de prompts | Prompt personalizado y justificación en el README. |
| Agente con memoria | Guardado por hilo, reformulación contextual y aserciones de seguimiento y aislamiento. Validación con Gemini pendiente de credenciales. |
| Código y documentación | Módulo compartido, notebook, interfaz local, requisitos y guía de ejecución. |
| Presentación y demo | Guion de siete minutos en DEFENSA.md. La demo en directo requiere credenciales. |
| Bonus Streamlit | Interfaz local con historial, citas y reinicio. Despliegue público opcional. |

## Resultados observados · 15 de noviembre de 2026

- **Superado.** Los tres PDF se abrieron y produjeron 397 fragmentos de 139 páginas con texto.
- **Superado.** Las dependencias se instalaron en Python 3.12. `pip check` no detectó incompatibilidades.
- **Superado localmente.** Cuatro pruebas de `test_local.py` verificaron la persistencia y consulta de ChromaDB con vectores controlados, la estructura del notebook, el estado por hilo y el chat de Streamlit con un modelo de prueba. Se comprobó el rechazo de una cita fuera de rango.
- **Superado.** Se renderizaron e inspeccionaron las seis diapositivas de la defensa.
- **Bloqueado por credenciales.** Quedan por verificar la generación de embeddings con Gemini, la precisión de la recuperación semántica, las cinco respuestas generadas, la abstención ante preguntas fuera del corpus y la calidad del seguimiento. Las respuestas de referencia son síntesis de NIST.
- **Pendiente.** Ensayo de la demo con una clave válida. El despliegue público es opcional.

Desde la terminal de VS Code, una vez instaladas las dependencias, repite la validación local con:

```powershell
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m unittest -v test_local
```

## Corrección de Gemini · 15 de noviembre de 2026

La configuración efectiva de Streamlit seleccionaba `gemini-2.5-flash` desde `.env`. Al consultar con LangChain se reprodujo `GoogleModelNotFoundError` (HTTP 404, `NOT_FOUND`). El identificador que recibe LangChain era el mismo que figuraba en `.env`.

Se cambió a `gemini-3.8-flash` en `.env`, `.env.example` y el valor por defecto de `rag.py`. Se verificó byte a byte que en `.env` solo cambiaba el identificador del modelo. El mismo adaptador generó la respuesta con la configuración nueva. El SDK oficial también confirmó la versión `gemini-3.8-flash`. `pip check` pasó con `langchain-google-genai 4.5.0` y `google-genai 3.3.0`, por lo que no se requirieron cambios de dependencias.

La colección existente `tfm7-8d1c35a59b1497e95c3611755084388b` conservó sus 397 fragmentos y su estado listo. La consulta de prueba devolvió las seis funciones y referencias al PDF oficial en las páginas 8, 9, 10 y 26 en una ejecución directa del agente. Los embeddings de consulta se generaron con `gemini-embedding-001`.

La prueba de dos turnos verificó que «¿En qué consiste la primera de ellas?» se reformuló como una pregunta sobre la función Govern, mantuvo el hilo y devolvió citas cuyos números coincidían con sus fuentes. Se comprobó también que abrir la colección no entraba en el flujo de reindexación.

Streamlit se inició en http://127.0.0.1:8517. En el navegador, el primer intento devolvió la abstención prevista por el agente. Tras reiniciar el chat y repetir la misma pregunta, aparecieron las seis funciones con citas y el desplegable Fuentes. En ambos intentos desapareció el error de modelo no encontrado.

## Auditoría de entrega

Los resultados vigentes y la matriz completa quedan en [AUDITORIA_FINAL.md](AUDITORIA_FINAL.md). El [checklist](CHECKLIST_ENTREGA.md) enumera los archivos y pasos de entrega. El informe conserva arriba los resultados históricos para trazar lo que cambió entre ejecuciones.
