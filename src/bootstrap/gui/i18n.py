"""
Módulo de Internacionalización (i18n) para Project Bootstrap Generator.
"""
from typing import Dict, Any

class I18n:
    # Idioma por defecto
    current_lang: str = "es"

    _STRINGS: Dict[str, Dict[str, str]] = {
        "es": {
            # Sidebar
            "menu_create": "Crear Proyecto",
            "menu_settings": "Configuración",
            
            # Main Panel
            "title_create": "Crear Nuevo Proyecto",
            "lbl_name": "Nombre del Proyecto:",
            "lbl_type": "Tipo de Proyecto:",
            "lbl_path": "Ruta de Salida:",
            "ph_name": "mi-proyecto-increible",
            "ph_path": "./proyectos",
            "btn_browse": "Explorar",
            "btn_create": "GENERAR PROYECTO",
            "btn_zip": "EXPORTAR COMO ZIP",
            
            # Settings Panel
            "title_settings": "Configuración Global",
            "lbl_author": "Autor por Defecto:",
            "lbl_github": "Usuario de GitHub:",
            "lbl_branding": "Tema de Branding:",
            "lbl_lang": "Idioma / Language:",
            "switch_git": "Inicializar repositorio Git",
            "switch_venv": "Crear Entorno Virtual (.venv)",
            "switch_theme": "Tema de la App (Oscuro/Claro)",
            "btn_save": "GUARDAR CONFIGURACIÓN",
            
            # Logs & Messages
            "log_ready": "Listo para crear proyectos.",
            "log_settings_open": "Configuración abierta.",
            "log_start": "Iniciando bootstrap para {name} ({type})...",
            "log_zip_start": "Generando ZIP para {name} ({type})...",
            "log_git_init": "Inicializando repositorio Git...",
            "log_venv_init": "Creando entorno virtual (.venv)...",
            
            "success_project": "¡Proyecto '{name}' creado exitosamente en {path}!",
            "success_zip": "ZIP creado exitosamente: {path}",
            "success_git": "Repositorio Git inicializado.",
            "success_venv": "Entorno virtual creado.",
            "success_save": "¡Configuración guardada exitosamente!",
            "success_lang": "Idioma cambiado a Español.",
            
            "err_name_req": "Error: El nombre del proyecto es obligatorio",
            "err_project": "Fallo al crear proyecto: {error}",
            "err_zip": "Fallo al crear ZIP: {error}",
            "warn_git": "Fallo al inicializar git: {error}",
            "warn_venv": "Fallo al crear venv: {error}",
            
            "lbl_logs": "Registros del Sistema"
        },
        "en": {
            # Sidebar
            "menu_create": "Create Project",
            "menu_settings": "Settings",
            
            # Main Panel
            "title_create": "Create New Project",
            "lbl_name": "Project Name:",
            "lbl_type": "Project Type:",
            "lbl_path": "Output Path:",
            "ph_name": "my-awesome-project",
            "ph_path": "./projects",
            "btn_browse": "Browse",
            "btn_create": "BOOTSTRAP PROJECT",
            "btn_zip": "EXPORT AS ZIP",
            
            # Settings Panel
            "title_settings": "Global Configuration",
            "lbl_author": "Default Author Name:",
            "lbl_github": "GitHub Username:",
            "lbl_branding": "Branding Theme:",
            "lbl_lang": "Language / Idioma:",
            "switch_git": "Auto-init Git repository",
            "switch_venv": "Create Virtual Environment (.venv)",
            "switch_theme": "App Theme Mode (Dark/Light)",
            "btn_save": "SAVE SETTINGS",
            
            # Logs & Messages
            "log_ready": "Ready to create projects.",
            "log_settings_open": "Settings opened.",
            "log_start": "Starting bootstrap for {name} ({type})...",
            "log_zip_start": "Generating ZIP for {name} ({type})...",
            "log_git_init": "Initializing Git repository...",
            "log_venv_init": "Creating virtual environment (.venv)...",
            
            "success_project": "Project '{name}' created successfully at {path}!",
            "success_zip": "ZIP created successfully: {path}",
            "success_git": "Git repository initialized.",
            "success_venv": "Virtual environment created.",
            "success_save": "Settings saved successfully!",
            "success_lang": "Language switched to English.",
            
            "err_name_req": "Error: Project Name is required",
            "err_project": "Failed to create project: {error}",
            "err_zip": "Failed to create ZIP: {error}",
            "warn_git": "Failed to init git: {error}",
            "warn_venv": "Failed to create venv: {error}",
            
            "lbl_logs": "System Logs"
        }
    }

    @classmethod
    def get(cls, key: str, **kwargs) -> str:
        """Obtiene una cadena traducida, formateándola si es necesario."""
        lang_dict = cls._STRINGS.get(cls.current_lang, cls._STRINGS["es"])
        text = lang_dict.get(key, key)
        if kwargs:
            try:
                return text.format(**kwargs)
            except KeyError:
                return text
        return text

    @classmethod
    def set_language(cls, lang_code: str):
        """Cambia el idioma actual (es, en)."""
        if lang_code in cls._STRINGS:
            cls.current_lang = lang_code
