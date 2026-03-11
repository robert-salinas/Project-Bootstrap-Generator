import customtkinter as ctk
from bootstrap.gui.config import AppConfig
from bootstrap.gui.views.sidebar import Sidebar
from bootstrap.gui.views.main_panel import MainPanel
from bootstrap.gui.views.settings_panel import SettingsPanel
from bootstrap.gui.views.log_console import LogConsole

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title(AppConfig.APP_NAME)
        self.geometry(AppConfig.APP_SIZE)
        
        # Theme configuration
        ctk.set_appearance_mode(AppConfig.THEME_MODE)
        ctk.set_default_color_theme(AppConfig.COLOR_THEME)
        
        # Grid layout (Sidebar + Main Content)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Background color hack (CTk doesn't support direct bg on root sometimes easily)
        self.configure(fg_color=AppConfig.RS_BG_MAIN)

        # 1. Sidebar
        self.sidebar = Sidebar(self, on_create_click=self.show_create, on_settings_click=self.show_settings)
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew")

        # 2. Main Content Area (Stack of frames)
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="nsew")
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

        # 3. Log Console (Bottom)
        self.console = LogConsole(self)
        self.console.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

        # Initialize Views
        self.views = {}
        self._init_views()
        
        # Share settings between panels
        self.views["create"].settings = self.views["settings"].settings
        
        # Show default view
        self.show_create()

    def _init_views(self):
        self.views["create"] = MainPanel(self.main_container, log_callback=self.console.log)
        self.views["settings"] = SettingsPanel(self.main_container, log_callback=self.console.log)

    def show_view(self, name):
        # Hide all views
        for view in self.views.values():
            view.grid_forget()
        
        # Show selected view
        if name in self.views:
            self.views[name].grid(row=0, column=0, sticky="nsew")
        else:
            self.console.log(f"View '{name}' not found", "ERROR")

    def show_create(self):
        self.show_view("create")
        # No log here to avoid spamming when switching views, handled by button clicks mostly

    def show_settings(self):
        self.show_view("settings")

    def refresh_all_views(self):
        """Llama al método refresh_strings de todas las vistas secundarias."""
        self.sidebar.refresh_strings()
        self.console.refresh_strings()
        for view in self.views.values():
            if hasattr(view, "refresh_strings"):
                view.refresh_strings()

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
