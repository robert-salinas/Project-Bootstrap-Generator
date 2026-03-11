import customtkinter as ctk
from bootstrap.gui.config import AppConfig
from bootstrap.gui.i18n import I18n

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, on_create_click=None, on_settings_click=None):
        super().__init__(
            master,
            width=250,
            corner_radius=0,
            fg_color=AppConfig.RS_SURFACE
        )
        self.on_create_click = on_create_click
        self.on_settings_click = on_settings_click

        self.grid_rowconfigure(4, weight=1)
        
        # Logo / Title
        self.logo_label = ctk.CTkLabel(
            self,
            text="PROJECT\nBOOTSTRAP",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=AppConfig.RS_ORANGE
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # Menu Buttons
        self.create_btn = self._create_menu_button(I18n.get("menu_create"), "Home", row=1, command=self.on_create_click)
        self.settings_btn = self._create_menu_button(I18n.get("menu_settings"), "Settings", row=2, command=self.on_settings_click)
        
        # Footer
        self.version_label = ctk.CTkLabel(
            self,
            text="v0.1.0\nRS Design System",
            text_color=AppConfig.RS_TEXT_MUTED,
            font=ctk.CTkFont(size=10)
        )
        self.version_label.grid(row=5, column=0, padx=20, pady=20)

    def refresh_strings(self):
        """Actualiza los textos al cambiar el idioma."""
        self.create_btn.configure(text=I18n.get("menu_create"))
        self.settings_btn.configure(text=I18n.get("menu_settings"))

    def _create_menu_button(self, text, icon_name, row, command=None):
        btn = ctk.CTkButton(
            self,
            text=text,
            fg_color="transparent",
            text_color=AppConfig.RS_TEXT_SECONDARY,
            hover_color=AppConfig.RS_ORANGE_DARK,
            anchor="w",
            height=40,
            corner_radius=AppConfig.RADIUS_LG,
            font=ctk.CTkFont(size=14),
            command=command
        )
        btn.grid(row=row, column=0, padx=20, pady=10, sticky="ew")
        return btn
