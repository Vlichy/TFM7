"""Pruebas locales reproducibles. Los dobles no llaman a Gemini."""
import json
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from langchain_core.messages import AIMessage
import nbformat
from streamlit.testing.v1 import AppTest

import rag


class EmbeddingsDePrueba:
    def __init__(self, **kwargs):
        pass

    def embed_documents(self, passages):
        return [[1.0, 0.0] for _ in passages]

    def embed_query(self, question):
        return [1.0, 0.0]


class ModeloDePrueba:
    def invoke(self, messages):
        payload = json.loads(messages[-1].content)
        if "history" in payload:
            return AIMessage(content=payload["history"][-1][0] + " " + payload["question"])
        if "paella" in payload["question"]:
            return AIMessage(content="Cita incorrecta [99]")
        return AIMessage(content="Respuesta de prueba [1, 2]")


class TestProyecto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = list(rag.chunks())
        cls.workdir = TemporaryDirectory(ignore_cleanup_errors=True)
        cls.addClassCleanup(cls.workdir.cleanup)
        cls.root = Path(cls.workdir.name)
        shutil.copytree(rag.ROOT / "corpus", cls.root / "corpus")
        with patch.object(rag, "ROOT", cls.root), patch.object(
            rag, "settings", return_value=("clave-ficticia", "", "test")
        ), patch.object(rag, "GoogleGenerativeAIEmbeddings", EmbeddingsDePrueba), patch.object(rag.time, "sleep"):
            cls.index = rag.open_index()
            reopened = rag.open_index()
            assert reopened[0].count() == cls.index[0].count()
        print(f"{len(cls.entries)} fragmentos de {len({(m['file'],m['page']) for _,m in cls.entries})} páginas con texto.")

    def test_corpus_e_indice(self):
        self.assertEqual(len({m["file"] for _, m in self.entries}), 3)
        self.assertGreaterEqual(len({(m["file"], m["page"]) for _, m in self.entries}), 20)
        self.assertEqual(len(self.entries), self.index[0].count())
        hits = rag.retrieve(self.index, "Zero Trust")
        self.assertEqual(len(hits), 5)
        self.assertTrue(all(h["page"] > 0 and h["url"].startswith("https://") for h in hits))

    def test_memoria_citas_y_abstencion(self):
        agent = rag.build_agent(self.index, ModeloDePrueba())
        first = rag.converse(agent, "¿Qué significa Zero Trust?", "demo")
        self.assertEqual([source["number"] for source in first["sources"]], [1, 2])
        followup = rag.converse(agent, "¿Y cómo se aplica?", "demo")
        self.assertIn("Zero Trust", followup["query"])
        self.assertEqual(len(followup["history"]), 2)
        other = rag.converse(agent, "¿Cómo se cocina paella?", "otro")
        self.assertEqual(len(other["history"]), 1)
        self.assertEqual(other["answer"], rag.UNKNOWN)
        self.assertEqual(other["sources"], [])

    def test_error_api_sin_exponer_detalles(self):
        with patch.object(rag, "open_index", side_effect=RuntimeError("detalle reservado")):
            app = AppTest.from_file(str(rag.ROOT / "app.py")).run()
        self.assertFalse(app.exception)
        self.assertIn("No se pudo iniciar", app.error[0].value)

    def test_notebook(self):
        notebook = nbformat.read(rag.ROOT / "TFM7.ipynb", as_version=4)
        nbformat.validate(notebook)

    def test_streamlit(self):
        agent = rag.build_agent(self.index, ModeloDePrueba())
        with patch.object(rag, "open_index", return_value=self.index), patch.object(
            rag, "build_agent", return_value=agent
        ):
            app = AppTest.from_file(str(rag.ROOT / "app.py"), default_timeout=15).run()
            self.assertFalse(app.exception)
            app.chat_input[0].set_value("¿Qué significa Zero Trust?").run()
            self.assertFalse(app.exception)
            self.assertEqual(len(app.session_state.history), 1)
            self.assertTrue(app.expander)
            app.sidebar.button[0].click().run()
            self.assertFalse(app.exception)
            self.assertEqual(app.session_state.history, [])


if __name__ == "__main__":
    unittest.main()
