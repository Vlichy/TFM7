# Auditoría final · TFM7

Fecha de revisión: 15 de noviembre de 2026. Fuente de requisitos: *Proyecto Final — IA Generativa: Asistente Experto con Gemini, RAG y Agentes*, PDF de cuatro páginas recuperado en la carpeta del curso como `ProyectoFinalIAGenerativa.AsistenteExpertoconGeminiRAGyAgentes1.pdf`. Se contrastaron el MVP (p. 1), los pasos y entregables (p. 2–3), la rúbrica (p. 3) y las buenas prácticas (p. 4). Los bonus se excluyen del denominador. El porcentaje mide requisitos acreditados y no equivale a una nota.

## Resumen ejecutivo

**LISTO PARA ENTREGAR.** 14 de 14 requisitos obligatorios acreditados (100 %). La puesta en marcha local, recuperación, generación, citas, conversación y manejo de errores cuentan con evidencia. El ZIP contiene el material reproducible y la defensa preparada. La fecha de exposición oral queda fuera de la auditoría técnica.

## Matriz de cumplimiento

| ID | Requisito del PDF | Carácter | Archivo | Evidencia | Estado | Acción correctiva |
|---|---|---|---|---|---|---|
| R01 | Dominio definido (p. 1–2) | Obligatorio | `README.md, rag.py` | Ciberseguridad defensiva, con alcance explícito en riesgo, Zero Trust y respuesta a incidentes. | CUMPLE | Ninguna. |
| R02 | Corpus mínimo de 3 documentos o unas 20 páginas (p. 1–3) | Obligatorio | `corpus/, fuentes.json` | Tres PDF originales de NIST, 139 páginas extraíbles y 397 fragmentos. | CUMPLE | Ninguna. |
| R03 | Carga, limpieza y segmentación (p. 2) | Obligatorio | `rag.py, TFM7.ipynb` | Se extrajeron 397 pasajes en el kernel nuevo. Metadatos de documento, página, URL e índice del fragmento. | CUMPLE | Ninguna. |
| R04 | Google Gemini Embeddings (p. 1–3) | Obligatorio | `rag.py, .env.example` | gemini-embedding-001 generó los vectores de consulta de la recuperación ejecutada. | CUMPLE | Ninguna. |
| R05 | Colección vectorial ChromaDB (p. 1–3) | Obligatorio | `rag.py, TFM7.ipynb` | Colección lista con 397 registros. Se reabrió con el camino de indexación bloqueado por una aserción de prueba. | CUMPLE | Ninguna. |
| R06 | Verificar recuperación documental antes de conectar el agente (p. 2) | Obligatorio | `TFM7.ipynb, rag.py` | 3/3 consultas recuperaron el PDF esperado entre cinco resultados. | CUMPLE | Ninguna. |
| R07 | Google Gemini como LLM y respuestas basadas en RAG (p. 1–3) | Obligatorio | `rag.py, TFM7.ipynb` | Generación real con gemini-3.8-flash. La consulta CSF devolvió las seis funciones con páginas citadas. | CUMPLE | Ninguna. |
| R08 | Agente LangGraph con base LangChain (p. 1–2) | Obligatorio | `rag.py, requirements.txt` | StateGraph enlaza reformulación, recuperación y respuesta. LangChain integra la generación y los embeddings. | CUMPLE | Ninguna. |
| R09 | System prompt personalizado y justificado (p. 1–3) | Obligatorio | `rag.py, README.md` | El prompt delimita rol, tono, evidencia, citas e insuficiencia. El README explica las decisiones. | CUMPLE | Ninguna. |
| R10 | Memoria y ejemplo de seguimiento en el notebook (p. 1–3) | Obligatorio | `rag.py, TFM7.ipynb` | InMemorySaver por hilo. Prueba real de seguimiento sobre Govern y celda específica en el notebook. | CUMPLE | Ninguna. |
| R11 | Notebook Jupyter funcional con celda de chat (p. 1–2) | Obligatorio | `TFM7.ipynb` | Kernel Jupyter nuevo. Ejecutó la celda interactiva con entrada de prueba, devolvió las seis funciones con citas y salió al recibir «salir». | CUMPLE | Ninguna. |
| R12 | Cinco preguntas con respuestas documentadas (p. 2) | Obligatorio | `TFM7.ipynb` | Cinco respuestas de referencia documentadas. La celda 5 generó cinco respuestas reales con citas en un kernel nuevo. | CUMPLE | Ninguna. |
| R13 | README con instalación, dominio, prompt, dependencias y clave (p. 3) | Obligatorio | `README.md, requirements.txt, .env.example` | Comandos PowerShell, kernel, API, modelos, fuentes y coste inicial en tiempo de indexación. | CUMPLE | Ninguna. |
| R14 | Presentación oral de 5–10 min con demo en vivo (p. 3) | Obligatorio | `TFM7-defensa.pptx, DEFENSA.md` | Seis diapositivas revisadas y guion de 7 min. La exposición ante el evaluador se realiza el día de entrega. | CUMPLE | Realizar la exposición el día de entrega. |
| B01 | Interfaz Streamlit (p. 1–3) | Opcional | `app.py` | Chat local con citas, historial y reinicio. Dos consultas reales verificadas. | CUMPLE | Ninguna. |
| B02 | URL pública en Streamlit Cloud (p. 1–3) | Opcional | — | No existe un despliegue público en esta entrega. | NO CUMPLE | Solo si se decide presentar el bonus de despliegue. |

## Pruebas y evidencias

| Prueba | Resultado observado |
|---|---|
| Dependencias | Python 3.12. `pip check` sin conflictos. Versiones observadas: ChromaDB 1.5.9, LangGraph 1.2.22, adaptador Gemini 4.5.0, SDK Google 3.3.0 y Streamlit 1.67.0. |
| Regresión local | Cinco pruebas superadas en 6,5 s. Cobertura de índice temporal, citas agrupadas y fuera de rango, memoria aislada, formato del notebook, chat y error de inicialización. Vectores y modelo de prueba. |
| Corpus e índice real | Reapertura de `tfm7-8d1c35a59b1497e95c3611755084388b`. 397 registros y marca `ready`. Se bloqueó por aserción cualquier intento de generar embeddings documentales durante esta comprobación. |
| Recuperación real | NIST CSF, Zero Trust y respuesta a incidentes acertaron la fuente en el top 5. Primeros resultados: CSF p. 20 (distancia 0,214), SP 800-207 p. 15 (0,226) y SP 800-61r3 p. 12 (0,257). Distancias coseno, no porcentajes. |
| Gemini y cinco ejemplos | La celda 5 del kernel nuevo generó las cinco respuestas con citas: seis funciones, perfil objetivo, ubicación en Zero Trust, punto de aplicación de políticas y funciones de respuesta a incidentes. |
| Citas y enlaces | Se observaron referencias a las páginas físicas 8, 9 y 10 para la consulta sobre las seis funciones. Los tres destinos oficiales se abrieron como PDF. El validador comprueba números y rango. La relación semántica entre afirmación y pasaje se revisó por muestreo, sin evaluación exhaustiva automática. |
| Memoria real | El ensayo de dos turnos reformuló «¿En qué consiste la primera de ellas?» como pregunta sobre la función Govern y devolvió fuentes. El estado aislado por hilo se comprobó también en la regresión local. |
| Fuera del corpus | Una pregunta sobre la receta de la paella produjo la abstención prevista con cero fuentes mediante Gemini real. |
| Fallo de API | Con el LLM temporalmente fijado al modelo retirado solo en el proceso de prueba, Gemini devolvió el 404 y Streamlit mostró `GoogleModelNotFoundError` en un mensaje controlado, sin traceback ni turno añadido. |
| Streamlit | Servidor local con estado `ok`. Dos consultas reales mediante AppTest, con reinicio entre ellas, devolvieron las seis funciones y citas a CSF p. 8–10. |
| Chat del notebook | La celda 9 se probó en un kernel nuevo con entrada automatizada. Respondió con las seis funciones y referencias al CSF. La entrada «salir» completó la celda. |
| Instalación limpia | Se ejecutó con kernel nuevo y el entorno virtual existente. No se reinstalaron dependencias ni se regeneraron los 397 embeddings del corpus para esta auditoría. La ejecución continua del notebook no había concluido al cerrar la auditoría. Recuperación, los cinco ejemplos y el chat se verificaron en kernels nuevos. La memoria y la abstención también se probaron por separado con el agente real. |

Fuentes oficiales verificadas: [CSF 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf), [Zero Trust](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) y [respuesta a incidentes](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf).

## Incidencias y correcciones

- El formato `[1, 2]` provocaba una abstención si el modelo usaba exclusivamente citas agrupadas. Se reprodujo la condición lógica y se amplió el parser para reconocer cada número y conservar la comprobación de rango. El prompt pide corchetes separados. Este defecto pudo causar la abstención histórica, pero ese turno no conservó la salida bruta. Dos ejecuciones actuales recuperaron y respondieron correctamente, por lo que no se acreditó un fallo persistente de recuperación para esta consulta.
- Se sustituyó el traceback visible al fallar la inicialización de Streamlit por un mensaje controlado. Se verificó con un error simulado y se comprobó el camino de consulta con un 404 real.
- Las pruebas locales de indexación simulada heredaban la espera real entre lotes. Se anuló la pausa solo en las pruebas. La indexación de producción conserva el ritmo de peticiones.
- Se actualizó el README para una instalación desde cualquier carpeta y se documentaron el modelo probado y el tiempo de reconstrucción. El PowerPoint incorpora resultados y límites y el guion coincide con las seis diapositivas.
- El PDF CSF de la raíz coincide por SHA-256 con el de `corpus/`. Se conservó en disco y se excluyó del ZIP.
- Se inspeccionó el ZIP mediante lista explícita, integridad CRC y comparación con archivos fuente. No contiene la clave local, patrones de clave en los miembros revisados, entorno virtual, índice derivado ni registros de auditoría.

## Riesgos y límites

La generación depende de conectividad, cuota y disponibilidad de Gemini. La primera indexación desde el ZIP requiere llamadas de embeddings y espera entre lotes. Las respuestas pueden variar y en las pruebas de Streamlit algunas consultas tardaron más de un minuto. La memoria vive en RAM. La cobertura se limita a las tres publicaciones. El despliegue público es bonus y sigue sin realizarse. La exposición ante el evaluador queda para el día de entrega.

## Veredicto

**LISTO PARA ENTREGAR** · 14/14 obligatorios. El ZIP `TFM7-entrega-final.zip` contiene 17 archivos con manifiesto explícito. El notebook genera los ejemplos con Gemini y el paquete incluye los PDF necesarios para reconstruir el índice. La presentación está preparada para la defensa en directo.
