Aqui vamos a poner cada una persona, un conflicto enfrentado durante el trabajo colaborativo:
1. No se tenia el conocimiento previo de la plataforma GitHub, por lo que fue un poco dificil al momento de usar dicha plataforma.
2. Debido a que no existe un compilador en el propio github, hubieron problemas al ver si el código iba a funcionar, sin embargo, al añadir una extensión en el repositorio, fue posible ver si los códigos tienen algún error de typeo.
3. Dificultades al momento de pasar los códigos del idioma C a Python.
4. Hubo problemas al momento de entender de forma correcta el sistema de Branches.
5. Al ser la primera vez trabajando en un entorno colaborativo con control de versiones, hubo confusión sobre cómo coordinar los cambios realizados por cada integrante del equipo sin generar conflictos en el código.
6. Al tratar de buscar soluciones a problemas técnicos, fue complicado comprender la documentación oficial de GitHub y otras herramientas, ya que muchas veces está escrita en un lenguaje avanzado o en inglés.

# Simulador de Cajero Automático

Este proyecto es una simulación de un sistema de cajero automático que permite a los usuarios realizar diversas operaciones financieras de manera interactiva, como consultar el saldo, depositar dinero, retirar dinero, transferir fondos y ver un historial de transferencias. El programa está diseñado en Python y utiliza un enfoque orientado a objetos para gestionar las operaciones y los usuarios registrados.

## Funcionalidades Principales

- **Registro de usuarios**: Los usuarios pueden registrarse proporcionando un número de identificación, una contraseña y se les asigna un número de cuenta único.
- **Inicio de sesión**: Los usuarios deben iniciar sesión con sus credenciales para acceder al sistema.
- **Operaciones financieras**:
  - Consultar saldo.
  - Depositar dinero.
  - Retirar dinero.
  - Transferir fondos a otra cuenta.
  - Ver historial de transferencias realizadas.
- **Interfaz de menú**: Un menú interactivo permite a los usuarios navegar entre las distintas opciones del sistema.

## Estructura del Proyecto

El código está estructurado de la siguiente manera:

- **`CajeroAutomatico`**: Clase principal que gestiona las operaciones financieras y el historial.
- **Funciones auxiliares**: Funciones como el registro de usuarios, inicio de sesión, y validación de datos.
- **`menu_principal`**: Punto de entrada del programa que ofrece un menú interactivo para ejecutar las funcionalidades.

## Uso del Proyecto

### Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

### Crear una nueva rama

Antes de realizar cambios, es recomendable trabajar en una nueva rama:

```bash
git checkout -b nueva-rama
```

### Realizar cambios

Realiza las modificaciones necesarias al código y verifica que todo funcione correctamente.

### Comprobar cambios

Usa `git status` para verificar los archivos modificados y `git diff` para revisar los cambios.

### Hacer un commit

Guarda tus cambios con un mensaje claro:

```bash
git add .
git commit -m "Descripción breve del cambio realizado"
```

### Fusionar los cambios (Merge)

Primero, cambia a la rama principal y actualízala:

```bash
git checkout main
git pull origin main
```

Luego, fusiona tu rama con la principal:

```bash
git merge nueva-rama
```

### Subir los cambios al repositorio remoto

Envía los cambios a GitHub:

```bash
git push origin main
```

## Conclusión

Este proyecto es una herramienta educativa para comprender cómo funciona un cajero automático en un entorno seguro y simulado. La estructura modular y el uso de clases permiten la fácil escalabilidad y modificación del sistema. Siéntete libre de contribuir al proyecto y sugerir mejoras.

¡Gracias por explorar este simulador de cajero automático! 🚀


