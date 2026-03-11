import customtkinter as ctk
import os
from bootstrap.gui.config import AppConfig
from bootstrap.gui.views.main_panel import MainPanel
from bootstrap.gui.views.settings_panel import SettingsPanel
from bootstrap.gui.views.log_console import LogConsole


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title(AppConfig.APP_NAME)
        self.geometry(AppConfig.APP_SIZE)
        
        # Set Icon
        try:
            icon_path = os.path.join("assets", "icon.ico")
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)
        except Exception:
            pass
        
        # Theme configuration
        ctk.set_appearance_mode(AppConfig.THEME_MODE)
        ctk.set_default_color_theme(AppConfig.COLOR_THEME)
        
        # Grid layout (Single Column)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0) # Header
        self.grid_rowconfigure(1, weight=1) # Main Content
        self.grid_rowconfigure(2, weight=0) # Logs
        
        # Background color hack
        self.configure(fg_color=AppConfig.RS_BG_MAIN)

        # 1. Header
        self.header = ctk.CTkFrame(self, fg_color="transparent", height=60)
        self.header.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        self.header.grid_columnconfigure(0, weight=1)

        # Header Title & Subtitle Container
        self.title_frame = ctk.CTkFrame(self.header, fg_color="transparent")
        self.title_frame.grid(row=0, column=0, sticky="w")
        
        self.app_title = ctk.CTkLabel(
            self.title_frame,
            text=AppConfig.APP_NAME,
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=AppConfig.RS_ORANGE,
            anchor="w"
        )
        self.app_title.pack(anchor="w")
        
        self.app_subtitle = ctk.CTkLabel(
            self.title_frame,
            text="By Robert Salinas", # Could be dynamic from settings but hardcoded per request
            font=ctk.CTkFont(size=12),
            text_color=AppConfig.RS_TEXT_SECONDARY,
            anchor="w"
        )
        self.app_subtitle.pack(anchor="w")

        # Header Button (Settings)
        self.settings_btn = ctk.CTkButton(
            self.header,
            text="Configuración",
            width=120,
            height=32,
            fg_color=AppConfig.RS_BG_INPUT,
            text_color=AppConfig.RS_TEXT_PRIMARY,
            hover_color=AppConfig.RS_ORANGE_DARK,
            command=self.toggle_settings
        )
        self.settings_btn.grid(row=0, column=1, sticky="e")

        # 2. Main Content Area (Stack of frames)
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

        # 3. Log Console (Bottom)
        self.console = LogConsole(self)
        self.console.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        # Initialize Views
        self.views = {}
        self._init_views()
        
        # Share settings
        self.views["create"].settings = self.views["settings"].settings
        
        # Show default view
        self.current_view = "create"
        self.show_create()

    def _init_views(self):
        self.views["create"] = MainPanel(self.main_container, log_callback=self.console.log)
        # Pass callback to return to main
        self.views["settings"] = SettingsPanel(
            self.main_container, 
            log_callback=self.console.log,
            on_back_click=self.show_create
        )

    def show_view(self, name):
        # Hide all views
        for view in self.views.values():
            view.grid_forget()
        
        # Show selected view
        if name in self.views:
            self.views[name].grid(row=0, column=0, sticky="nsew")
            self.current_view = name
            
            # Update Header Button based on view
            if name == "create":
                self.settings_btn.configure(text="Configuración", command=self.toggle_settings, state="normal")
                self.settings_btn.grid(row=0, column=1, sticky="e") # Ensure visible
            elif name == "settings":
                # In settings view, we might hide the top button because SettingsPanel has its own "Volver"
                # Or we can keep it as a toggle. The reference shows a "Volver" button inside the panel header.
                # Let's hide the main header button when in settings to avoid redundancy if SettingsPanel has one.
                self.settings_btn.grid_remove() 
        else:
            self.console.log(f"View '{name}' not found", "ERROR")

    def show_create(self):
        self.show_view("create")

    def show_settings(self):
        self.show_view("settings")

    def toggle_settings(self):
        if self.current_view == "create":
            self.show_settings()
        else:
            self.show_create()

    def refresh_all_views(self):
        """Llama al método refresh_strings de todas las vistas secundarias."""
        self.console.refresh_strings()
        for view in self.views.values():
            if hasattr(view, "refresh_strings"):
                view.refresh_strings()

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
