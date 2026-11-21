# ProyectoPrueba3 - Programación Web

## Descripción del proyecto

Aplicación web desarrollada utilizando Python, Flask, HTML5 y CSS3, como parte de las actividades prácticas de Programación Web.

El proyecto contiene un menú principal que permite acceder a dos ejercicios, desarrollados mediante formularios HTML y procesamiento de datos con Python.

## Tecnologías utilizadas

- Python 3.14
- Flask 3.1.3
- HTML5
- CSS3
- Visual Studio Code
- Git y GitHub

## Ejercicio 1: Formulario de Notas

Permite ingresar tres notas y el porcentaje de asistencia de un estudiante.

**Funcionalidades:**
- Ingreso de tres notas.
- Validación de los valores permitidos.
- Cálculo del promedio.
- Verificación del porcentaje de asistencia.
- Determinación del estado APROBADO o REPROBADO.
- Visualización del resultado en pantalla.

## Ejercicio 2: Formulario de Nombres

Permite ingresar tres nombres y determinar cuál tiene la mayor cantidad de caracteres.

**Funcionalidades:**
- Ingreso de tres nombres.
- Validación de campos obligatorios.
- Verificación de que los nombres sean diferentes.
- Comparación de la longitud de los nombres.
- Presentación del nombre más largo y su cantidad de caracteres.

## Estructura del proyecto

```text
ProyectoPrueba3/
|
|-- main.py
|-- requirements.txt
|-- .gitignore
|
|-- static/
|   |-- style.css
|
|-- templates/
|   |-- index.html
|   |-- ejercicio1.html
|   |-- ejercicio2.html
|
|-- README.md
```

## Instalación y ejecución

**1. Clonar el repositorio:**

```bash
git clone https://github.com/Wolfhem-2026/ProyectoPrueba3.git
```

**2. Ingresar al directorio:**

```bash
cd ProyectoPrueba3
```

**3. Crear el entorno virtual:**

```bash
python -m venv .venv
```

**4. Activar el entorno virtual en PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**5. Instalar las dependencias:**

```bash
python -m pip install -r requirements.txt
```

**6. Ejecutar la aplicación:**

```bash
python main.py
```

**7. Abrir el navegador:**

http://127.0.0.1:5000

## Pruebas realizadas

Se realizaron pruebas funcionales de los formularios, incluyendo:

- Cálculo de promedios y validación de asistencia.
- Resultados de aprobación y reprobación.
- Validación de notas fuera del rango permitido.
- Identificación del nombre con mayor cantidad de caracteres.
- Validación de nombres repetidos.
- Validación de campos obligatorios.

## Observaciones

La aplicación utiliza el servidor de desarrollo de Flask para su ejecución local.

El entorno virtual `.venv` no se incluye en el repositorio, ya que las dependencias pueden instalarse utilizando el archivo `requirements.txt`.

## Repositorio

https://github.com/Wolfhem-2026/ProyectoPrueba3