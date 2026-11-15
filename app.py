import uuid

import streamlit as st

from rag import build_agent, converse, open_index

st.set_page_config(page_title="TFM7 · Ciberseguridad")
st.title("Asistente de ciberseguridad")
st.caption("Consulta guías NIST y comprueba las páginas citadas.")


@st.cache_resource
def knowledge_base():
    return open_index()


def show_answer(answer, sources):
    st.markdown(answer)
    if sources:
        with st.expander("Fuentes"):
            for source in sources:
                st.markdown(f'[{source["number"]}] [{source["title"]}]'
                            f'({source["url"]}#page={source["page"]})'
                            f' · PDF, pág. {source["page"]}')
                st.caption(source["text"])


reset = st.sidebar.button("Reiniciar conversación")
if reset or "history" not in st.session_state:
    st.session_state.history = []
    st.session_state.thread_id = str(uuid.uuid4())
    st.session_state.pop("agent", None)


if "agent" not in st.session_state:
    try:
        with st.spinner("Preparando la base documental…"):
            st.session_state.agent = build_agent(knowledge_base())
    except Exception as error:
        st.error(f"No se pudo iniciar el sistema ({type(error).__name__}).")
        st.info("Comprueba la clave de Gemini, la conectividad y la disponibilidad de los PDF.")
        st.stop()


for question, answer, sources in st.session_state.history:
    with st.chat_message("user"):
        st.write(question)
    with st.chat_message("assistant"):
        show_answer(answer, sources)

if question := st.chat_input("Escribe tu consulta"):
    with st.chat_message("user"):
        st.write(question)
    with st.chat_message("assistant"):
        try:
            with st.spinner("Consultando las fuentes…"):
                result = converse(st.session_state.agent, question, st.session_state.thread_id)
        except Exception as error:
            st.error(f"Falló la consulta ({type(error).__name__}). "
                     "Comprueba la conectividad, la cuota y el modelo configurado.")
        else:
            show_answer(result["answer"], result["sources"])
            st.session_state.history.append((question, result["answer"], result["sources"]))
