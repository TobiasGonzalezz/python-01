import os
import unittest
from logger_singleton import Logger, singleton


class TestLoggerSingleton(unittest.TestCase):

    def setUp(self):
        """Antes de cada test, borra el archivo de log si existe."""
        self.log_file = "app.log"
        if os.path.exists(f"Singleton/{self.log_file}"):
            os.remove(self.log_file)

    def test_singleton_instance(self):
        """Verifica que solo haya una instancia de Logger."""
        logger1 = Logger()
        logger2 = Logger()
        self.assertIs(logger1, logger2, "Logger no es singleton")

    def test_log_writing(self):
        """Verifica que los mensajes se escriban correctamente."""
        logger = Logger()
        logger.log("Inicio del sistema")
        logger.log("Nueva conexión")

        with open(self.log_file, "r") as f:
            content = f.read()

        self.assertIn("Inicio del sistema", content)
        self.assertIn("Nueva conexión", content)
        self.assertTrue(content.startswith("Logger iniciado"))

    def test_log_persists_single_instance(self):
        """Verifica que la segunda instancia use el mismo archivo."""
        logger1 = Logger()
        logger1.log("Primera entrada")

        logger2 = Logger()
        logger2.log("Segunda entrada")

        with open(self.log_file, "r") as f:
            lines = f.readlines()

        # Solo una cabecera de inicialización
        init_lines = [line for line in lines if "Logger iniciado" in line]
        self.assertEqual(len(init_lines), 1, "Se creó un segundo logger")
        self.assertIn("Primera entrada", "".join(lines))
        self.assertIn("Segunda entrada", "".join(lines))


if __name__ == "__main__":
    unittest.main()
