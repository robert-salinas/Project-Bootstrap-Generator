from dataclasses import dataclass

@dataclass(frozen=True)
class AppConfig:
    """Configuración central de la interfaz gráfica siguiendo el sistema de diseño RS."""
    
    # Nombre de la aplicación
    APP_NAME: str = "Project Bootstrap Generator"
    APP_SIZE: str = "1100x700"
    
    # Paleta de Colores (RS Design System)
    # Color Primario (Acción) - (Light, Dark)
    RS_ORANGE: tuple = ("#E86A2A", "#FF7A3D")
    RS_ORANGE_LIGHT: tuple = ("#FF7A3D", "#FFA566")
    RS_ORANGE_DARK: tuple = ("#D65A1A", "#E86A2A")
    
    # Superficies y Fondos
    # RS_DARK_PRIMARY -> Surface/Card (Light: White, Dark: #2D3142)
    RS_SURFACE: tuple = ("#FFFFFF", "#2D3142")
    # RS_DARK_SECONDARY -> Main Background (Light: #F9FAFB, Dark: #1A1F2E)
    RS_BG_MAIN: tuple = ("#F9FAFB", "#1A1F2E")
    # RS_DARK_TERTIARY -> Inputs/Deep (Light: #E5E7EB, Dark: #0F1419)
    RS_BG_INPUT: tuple = ("#E5E7EB", "#0F1419")
    
    # Bordes para profundidad (Light: #E5E7EB, Dark: #4B5563)
    RS_BORDER: tuple = ("#E5E7EB", "#4B5563")
    
    # Textos
    # RS_TEXT_WHITE -> Primary Text (Light: #111827, Dark: #FFFFFF)
    RS_TEXT_PRIMARY: tuple = ("#111827", "#FFFFFF")
    # RS_TEXT_LIGHT -> Secondary Text (Light: #374151, Dark: #F3F4F6)
    RS_TEXT_SECONDARY: tuple = ("#374151", "#F3F4F6")
    # RS_TEXT_MUTED -> Muted Text (Light: #6B7280, Dark: #9CA3AF)
    RS_TEXT_MUTED: tuple = ("#6B7280", "#9CA3AF")
    
    # Semánticos
    RS_SUCCESS: tuple = ("#059669", "#10B981")
    RS_ERROR: tuple = ("#DC2626", "#EF4444")
    
    # Espaciado y Radios
    RADIUS_LG: int = 12
    SPACING_MD: int = 16
    
    # CustomTkinter Theme Defaults
    THEME_MODE: str = "Dark"
    COLOR_THEME: str = "blue"  # Base, pero sobrescribiremos colores

@dataclass
class UserSettings:
    """Configuración persistente del usuario."""
    author_name: str = "Robert Salinas"
    github_username: str = "robert-salinas"
    auto_git_init: bool = True
    create_venv: bool = False
    branding_theme: str = "RS Dark"  # "RS Dark" or "RS Light"
    app_theme_mode: str = "Dark" # "Dark" or "Light"
    language: str = "es" # "es" or "en"

class SettingsStore:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SettingsStore, cls).__new__(cls)
            cls._instance.settings = UserSettings()
        return cls._instance
