# GROWTREND Análisis de tendencia de inversiones: Un estudio de acciones en el mercado financiero.

![banner](https://github.com/JuanPabloNieto24/Encriptador/assets/64119342/b6a15679-8455-4e1b-abde-0cdeed84fdc0)

## Índice
* [Introducción](#introducción)
* [Resumen](#resumen)
* [Conceptos Claves](#conceptos-claves)
* [Público Objetivo](#público-objetivo)
* [Metodología](#metodología)
    * [Datos](#datos)
    * [Herramientas y Técnicas](#herramientas-y-técnicas)
* [Deploy](#deploy)
* [Contacto](#contacto)

## Introducción

En el dinámico y complejo mundo de las inversiones, la capacidad de tomar decisiones informadas es clave para el éxito financiero. GROWTREND emerge como una herramienta integral para analizar tendencias en el mercado accionario de Estados Unidos. Este proyecto se sumerge en la vasta cantidad de datos financieros, utilizando técnicas avanzadas de Extracción, Transformación y Carga (ETL), Análisis Exploratorio de Datos (EDA), Visualización de Datos (DV) y Machine Learning para proporcionar insights valiosos a inversores, analistas financieros y estudiantes.

## Resumen

Este proyecto se enfoca en identificar patrones y oportunidades de inversión, presentando una cartera destacada por su rendimiento sólido y riesgo moderado. Utilizamos datos extraídos de Yahoo Finance a través de su API, garantizando la fiabilidad y actualización constante de la información. La metodología abarca desde la extracción y almacenamiento de datos hasta el uso de herramientas como PowerBI para el análisis exploratorio y Python para implementar modelos de Machine Learning.

## Conceptos Claves:

- ETL (Extracción, Transformación y Carga): Proceso integral para adquirir, transformar y cargar datos desde diversas fuentes.

- EDA (Análisis Exploratorio de Datos): Técnica para comprender la estructura y distribución de los datos mediante estadísticas descriptivas y visualizaciones.

- DV (Visualización de Datos): Utilización de gráficos para comunicar patrones, relaciones y tendencias de manera efectiva.

- Machine Learning (Aprendizaje Automático): Integración de algoritmos para análisis predictivo y modelado de tendencias, mejorando las capacidades de predicción.

## Público Objetivo:

- Inversores: Personas interesados en maximizar rendimientos y gestionar riesgos en sus inversiones.

- Analistas Financieros: Profesionales que buscan herramientas para análisis exhaustivos de las tendencias del mercado.

- Estudiantes: Recurso educativo para comprender y aplicar técnicas avanzadas de análisis de datos en el contexto financiero.

Este proyecto se presenta como una herramienta accesible y valiosa, beneficiando a una amplia audiencia, desde aquellos que buscan mejorar sus decisiones de inversión hasta profesionales que requieren un enfoque analítico sólido en el ámbito financiero.

## Metodología:

### Datos:

- Fuente: La información se extrajo de la página [![Static Badge](https://img.shields.io/badge/Yahoo%20Finance-black?style=for-the-badge&color=%238421f3)
](https://finance.yahoo.com/) mediante el uso de su [API](https://github.com/ranaroussi/yfinance), garantizando datos financieros confiables y actualizados.

- Características: Incluyen variables clave para el análisis de inversiones, como precios de acciones, volumen de transacciones y otros indicadores relevantes.

- Período de Tiempo: Los datos abarcan un período específico desde Diciembre del 2017 hasta la actualidad.

### Herramientas y Técnicas:

- Extracción y Almacenamiento de Datos: Utilizamos la API de Yahoo Finance para extraer datos en tiempo real. Estos datos se almacenaron en una base de datos [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/) mediante el orquestador de flujos de [![Render](https://img.shields.io/badge/Render-black?style=for-the-badge)](https://render.com/).

- Análisis Exploratorio de Datos (EDA): [![PowerBI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=Power%20BI&logoColor=white)](https://powerbi.microsoft.com/es-es/desktop/) se empleó para conectarse a la base de datos y realizar un EDA detallado, visualizando gráficamente los datos extraídos.

- Aprendizaje Automático: se utilizó [![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/) para implementar modelos de machine learning, específicamente para prever el precio de las acciones y evaluar posibles tendencias futuras.

## Deploy

API Machine Learning [![FASTAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)](https://proyectonocountryml.onrender.com/docs)

Documentacion de la API [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Tato2013/ProyectoNoCountryML)

## Contacto

| Integrantes | Rol | Contacto
|------------|------------|------------|
| [Gabriel Fernandez](https://github.com/gabfer1896) | ![Data Engineer](https://img.shields.io/badge/Data%20Engineer-black?style=for-the-badge&color=%2384b6f4) | [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gabfer1896) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabriel-fernandez-635096222/)
| [Hugo Terrile](https://github.com/hterril) | ![Data Engineer](https://img.shields.io/badge/Data%20Engineer-black?style=for-the-badge&color=%2384b6f4) | [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/hterril) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hugo-terrile-it/)
| [Pablo Chail](https://github.com/Pablochail) | ![Data Engineer](https://img.shields.io/badge/Data%20Engineer-black?style=for-the-badge&color=%2384b6f4) | [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Pablochail) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pablochail/)
| [Marcelo Peralta](https://github.com/Tato2013) | ![Data Scientist](https://img.shields.io/badge/Data%20Scientist-black?style=for-the-badge&color=%2377dd77) | [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Tato2013) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marcelo-peralta2/)
| [Alvaro Rodrigo Soria](https://github.com/Alvarosc90) | ![Data Analyst](https://img.shields.io/badge/Data%20Analyst-black?style=for-the-badge&color=%23fdfd96) | [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Alvarosc90) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alvaro-rodrigo-soria-casali-60422a135/)
| [Juan Pablo Nieto](https://github.com/JuanPabloNieto24) | ![Data Analyst](https://img.shields.io/badge/Data%20Analyst-black?style=for-the-badge&color=%23fdfd96) | [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JuanPabloNieto24) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/juan-pablo-nieto-perfil/)
