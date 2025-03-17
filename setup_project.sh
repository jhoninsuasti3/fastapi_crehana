#!/bin/bash

# Nombre del proyecto
PROJECT_ROOT="app"

# Crear la estructura de directorios
mkdir -p $PROJECT_ROOT/{api/routes,core,domain,infrastructure,services,schemas,tests/{unit,integration}}

# Crear los archivos dentro de cada directorio
touch $PROJECT_ROOT/api/{dependencies.py,error_handlers.py,__init__.py}
touch $PROJECT_ROOT/api/routes/task_routes.py
touch $PROJECT_ROOT/core/{config.py,database.py,__init__.py}
touch $PROJECT_ROOT/domain/{task.py,__init__.py}
touch $PROJECT_ROOT/infrastructure/{task_repository.py,__init__.py}
touch $PROJECT_ROOT/services/{task_service.py,__init__.py}
touch $PROJECT_ROOT/schemas/{task_schema.py,__init__.py}
touch $PROJECT_ROOT/tests/{__init__.py}
touch $PROJECT_ROOT/tests/unit/{__init__.py}
touch $PROJECT_ROOT/tests/integration/{__init__.py}
touch $PROJECT_ROOT/main.py
touch $PROJECT_ROOT/__init__.py

# Crear archivos de configuración en la raíz del proyecto
touch Dockerfile docker-compose.yml requirements.txt .flake8 pytest.ini README.md

# Mensaje de éxito
echo "📁 Estructura del proyecto creada correctamente."
