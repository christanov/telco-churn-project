[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/christanov/telco-churn-project/blob/main/notebooks/churn_dual_source.ipynb)

# 📊 Telco Churn Project

Este proyecto aplica técnicas de aprendizaje automático para analizar y predecir la tasa de abandono de clientes (churn) en empresas de telecomunicaciones, utilizando datos de comportamiento y facturación.

## 🚀 Objetivos

- Predecir qué clientes podrían abandonar el servicio.
- Identificar las características más influyentes en la decisión de abandono.
- Visualizar patrones en los datos para apoyar la toma de decisiones comerciales.

## 📂 Estructura del repositorio

```text
telco-churn-project/
├── data/
│ ├── telco_customer.csv # Dataset original
│ ├── telco_dataset_final.csv # Dataset procesado con columnas nuevas
│ └── telco_churn.db # Base de datos SQLite generada
│
├── notebooks/
│ ├── churn_from_csv_with_viz.ipynb # Análisis completo desde CSV
│ ├── churn_from_sqlite_with_viz.ipynb# Análisis completo desde SQLite
│
├── scripts/
│ └── create_sql_db.py # Script para generar .db desde CSV
│
└── README.md

```


## 🧠 Tecnologías utilizadas

- **Python 3**
- **Google Colab**
- **Pandas** para manipulación de datos
- **Matplotlib y Seaborn** para visualizaciones
- **Scikit-learn** para el modelo predictivo
- **SQLite** como sistema de base de datos relacional

## 📊 Modelos y Visualizaciones

- Entrenamiento con `RandomForestClassifier`.
- Métricas de evaluación: *Precisión, Recall, F1-score*.
- Visualizaciones clave:
  - Matriz de Confusión
  - Importancia de características
  - Distribución por categorías de cliente
  - ARPU vs Total de servicios

## 📝 Wiki del proyecto

Consulta el análisis completo y la documentación técnica en la [Wiki del Repositorio](https://github.com/christanov/telco-churn-project/wiki).

## 📎 Archivos útiles para análisis

| Tipo de análisis | Notebook |  
|------------------|----------|
| Desde CSV        | [churn_from_csv_with_viz.ipynb](notebooks/churn_from_csv_with_viz.ipynb) |
| Desde SQLite     | [churn_from_sqlite_with_viz.ipynb](notebooks/churn_from_sqlite_with_viz.ipynb) |

## 📌 Cómo ejecutar en Google Colab

Abre directamente en Colab:

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/christanov/telco-churn-project/blob/main/notebooks/churn_from_csv_with_viz.ipynb)

## 📚 Referencias

- [Scikit-learn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [SQLite](https://www.sqlite.org/index.html)

---
