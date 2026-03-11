import pytest
from bootstrap.gui.config import AppConfig

def test_app_config_colors():
    """Verifica que la configuración de colores coincida con el RS Design System."""
    assert AppConfig.RS_ORANGE == "#FF7A3D"
    assert AppConfig.RS_DARK_SECONDARY == "#1A1F2E"
    assert AppConfig.THEME_MODE == "Dark"

def test_gui_imports():
    """Verifica que los módulos de la GUI se puedan importar correctamente."""
    try:
        from bootstrap.gui.app import App
        from bootstrap.gui.views.sidebar import Sidebar
        from bootstrap.gui.views.main_panel import MainPanel
        from bootstrap.gui.views.log_console import LogConsole
    except ImportError as e:
        pytest.fail(f"Error al importar módulos GUI: {e}")
