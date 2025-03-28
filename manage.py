#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv

def main():
    """Run administrative tasks."""
    # Cargar variables de entorno
    load_dotenv()
    
    # Configurar puerto personalizado si se ejecuta `runserver`
    if len(sys.argv) >= 2 and sys.argv[1] == "runserver":
        port = os.getenv("RUNSERVER_PORT", "8080")  # Puerto por defecto 8080
        if len(sys.argv) == 2:  # Solo 'runserver' sin puerto
            sys.argv.append(f"127.0.0.1:{port}")  # Añadir IP y puerto
    
    # Configuración de Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PoliApuestas.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
