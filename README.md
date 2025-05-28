# 🧠 Test de Lógica de Programación

Aplicación web desarrollada con **Flask** que simula un examen de lógica de programación y resolución de problemas con código en **Python**, dividido en tres fases: **Básico**, **Intermedio** y **Avanzado**. Cada fase contiene 10 preguntas, y al finalizar el test se guardan los resultados en una base de datos SQLite.

> 📌 **Nota:** El módulo encargado de analizar los resultados, calcular el puntaje final y detectar fallos por categoría se encuentra actualmente **en desarrollo**.

---

## 🎯 Objetivo

El propósito de esta aplicación es ofrecer una herramienta interactiva de evaluación de habilidades de lógica de programación y conocimientos de Python, ideal para procesos de selección, autoevaluación o formación académica.

---

## 🚀 Características principales

- ✅ Cuestionarios divididos por nivel: Básico, Intermedio y Avanzado
- 🧪 Cada fase contiene 10 preguntas únicas
- ⌨️ Preguntas con código Python y lógica algorítmica
- 🧾 Persistencia de resultados en base de datos **SQLite**
- 🧩 Interfaz dinámica usando **Fetch API**
- 🧠 Módulo de análisis de resultados en desarrollo (cálculo de puntaje y retroalimentación)

---

## 🧱 Tecnologías utilizadas

- **Python 3**
- **Flask** (Backend)
- **Jinja2** (Frontend server-side)
- **Fetch API** (Interacción dinámica)
- **SQLite** (Base de datos local)

---


---

## 🧪 Cómo ejecutar la aplicación

```bash
# Clonar el repositorio
git clone https://github.com/D4n13L-CSTL/Test_partipation.git
cd Test_partipation

# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
flask run  # o python app.py si está configurado
