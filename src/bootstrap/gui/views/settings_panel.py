import customtkinter as ctk
from bootstrap.gui.config import AppConfig, UserSettings
from bootstrap.gui.i18n import I18n

class SettingsPanel(ctk.CTkFrame):
    def __init__(self, master, log_callback=None, on_back_click=None):
        super().__init__(
            master,
            corner_radius=AppConfig.RADIUS_LG,
            fg_color=AppConfig.RS_SURFACE,
            border_width=1,
            border_color=AppConfig.RS_BORDER
        )
        self.log_callback = log_callback
        self.on_back_click = on_back_click
        self.settings = UserSettings()
        
        # Responsive Layout (Centered Content)
        self.grid_columnconfigure(0, weight=1) # Spacer Left
        self.grid_columnconfigure(1, weight=3) # Main Content
        self.grid_columnconfigure(2, weight=1) # Spacer Right
        self.grid_rowconfigure(0, weight=0) # Title
        self.grid_rowconfigure(1, weight=1) # Form

        # Title Header
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=1, padx=0, pady=(30, 20), sticky="ew")
        self.header_frame.grid_columnconfigure(0, weight=1)

        self.title = ctk.CTkLabel(
            self.header_frame,
            text=I18n.get("title_settings"),
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=AppConfig.RS_ORANGE,
            anchor="w"
        )
        self.title.grid(row=0, column=0, sticky="w")
        
        # Back Button
        if self.on_back_click:
            self.back_btn = ctk.CTkButton(
                self.header_frame,
                text="Volver",
                width=100,
                height=32,
                fg_color=AppConfig.RS_BG_INPUT,
                text_color=AppConfig.RS_TEXT_PRIMARY,
                hover_color=AppConfig.RS_ORANGE_DARK,
                command=self.on_back_click
            )
            self.back_btn.grid(row=0, column=1, sticky="e")

        # Settings Form (Scrollable)
        self.form_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.form_frame.grid(row=1, column=1, padx=0, pady=10, sticky="nsew")
        self.form_frame.grid_columnconfigure(1, weight=1)

        # 1. Author Name
        self.author_label = self._create_label(I18n.get("lbl_author"), 0)
        self.author_entry = self._create_entry(self.settings.author_name, 0)
        
        # 2. GitHub Username
        self.github_label = self._create_label(I18n.get("lbl_github"), 1)
        self.github_entry = self._create_entry(self.settings.github_username, 1)

        # 3. Branding Theme (Project)
        self.branding_label = self._create_label(I18n.get("lbl_branding"), 2)
        self.branding_combo = ctk.CTkComboBox(
            self.form_frame,
            values=["RS Dark", "RS Light"],
            fg_color=AppConfig.RS_BG_INPUT,
            border_color=AppConfig.RS_ORANGE_DARK,
            button_color=AppConfig.RS_ORANGE,
            button_hover_color=AppConfig.RS_ORANGE_DARK,
            text_color=AppConfig.RS_TEXT_PRIMARY,
            dropdown_fg_color=AppConfig.RS_BG_MAIN,
            dropdown_text_color=AppConfig.RS_TEXT_PRIMARY,
            height=40
        )
        self.branding_combo.set(self.settings.branding_theme)
        self.branding_combo.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        # 4. App Theme (GUI) - Moved here and changed to SegmentedButton
        self.theme_label = self._create_label(I18n.get("switch_theme"), 3)
        self.theme_seg = ctk.CTkSegmentedButton(
            self.form_frame,
            values=["Dark", "Light"],
            fg_color=AppConfig.RS_BG_INPUT,
            selected_color=AppConfig.RS_ORANGE,
            selected_hover_color=AppConfig.RS_ORANGE_DARK,
            unselected_color=AppConfig.RS_BG_INPUT,
            unselected_hover_color=AppConfig.RS_ORANGE_DARK,
            text_color=AppConfig.RS_TEXT_PRIMARY,
            height=40,
            command=self._on_theme_change
        )
        self.theme_seg.set(self.settings.app_theme_mode)
        self.theme_seg.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        # 5. Language Selector
        self.lang_label = self._create_label(I18n.get("lbl_lang"), 4)
        self.lang_seg = ctk.CTkSegmentedButton(
            self.form_frame,
            values=["Español", "English"],
            fg_color=AppConfig.RS_BG_INPUT,
            selected_color=AppConfig.RS_ORANGE,
            selected_hover_color=AppConfig.RS_ORANGE_DARK,
            unselected_color=AppConfig.RS_BG_INPUT,
            unselected_hover_color=AppConfig.RS_ORANGE_DARK,
            text_color=AppConfig.RS_TEXT_PRIMARY,
            height=40,
            command=self._on_language_change
        )
        self.lang_seg.set("Español" if self.settings.language == "es" else "English")
        self.lang_seg.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        # 6. Automation Defaults (Moved to bottom, cleaned up)
        self.defaults_label = ctk.CTkLabel(
            self.form_frame,
            text="Defaults:",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=AppConfig.RS_TEXT_SECONDARY,
            anchor="w"
        )
        self.defaults_label.grid(row=5, column=0, padx=10, pady=(20, 10), sticky="nw")

        self.toggle_frame = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        self.toggle_frame.grid(row=5, column=1, pady=10, sticky="ew")
        
        self.git_var = ctk.BooleanVar(value=self.settings.auto_git_init)
        self.git_switch = self._create_switch(I18n.get("switch_git"), self.git_var)
        self.git_switch.pack(side="left", padx=(10, 20))
        
        self.venv_var = ctk.BooleanVar(value=self.settings.create_venv)
        self.venv_switch = self._create_switch(I18n.get("switch_venv"), self.venv_var)
        self.venv_switch.pack(side="left", padx=10)

        # Save Button Container
        self.save_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.save_frame.grid(row=2, column=1, padx=0, pady=30, sticky="ew")
        self.save_frame.grid_columnconfigure(0, weight=1)

        # Save Button
        self.save_btn = ctk.CTkButton(
            self.save_frame,
            text=I18n.get("btn_save"),
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=AppConfig.RS_ORANGE,
            hover_color=AppConfig.RS_ORANGE_DARK,
            height=50,
            corner_radius=AppConfig.RADIUS_LG,
            command=self._save_settings
        )
        self.save_btn.grid(row=0, column=0, sticky="ew")
        
        # Toast Label
        self.toast_label = ctk.CTkLabel(
            self.save_frame,
            text="",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=AppConfig.RS_SUCCESS
        )
        self.toast_label.grid(row=1, column=0, pady=(5, 0))

    def refresh_strings(self):
        """Actualiza los textos al cambiar el idioma."""
        self.title.configure(text=I18n.get("title_settings"))
        self.author_label.configure(text=I18n.get("lbl_author"))
        self.github_label.configure(text=I18n.get("lbl_github"))
        self.branding_label.configure(text=I18n.get("lbl_branding"))
        self.lang_label.configure(text=I18n.get("lbl_lang"))
        self.theme_label.configure(text=I18n.get("switch_theme"))
        self.git_switch.configure(text=I18n.get("switch_git"))
        self.venv_switch.configure(text=I18n.get("switch_venv"))
        self.save_btn.configure(text=I18n.get("btn_save"))

    def _on_theme_change(self, value):
        ctk.set_appearance_mode(value)
        self._log(f"Theme switched to {value}", "INFO")

    def _on_language_change(self, value):
        """Maneja el cambio de idioma."""
        lang_code = "es" if value == "Español" else "en"
        I18n.set_language(lang_code)
        
        # Actualizar configuración
        self.settings.language = lang_code
        
        # Notificar a la App principal para refrescar toda la UI
        # Esto requiere que la App tenga un mecanismo para propagar el evento
        if self.master.master.master: # Hacky way to reach App, better use a callback or event
             try:
                 # App is self.master.master.master usually in this structure: App -> MainContainer -> SettingsPanel
                 # But safer to assume 'App' passed 'self.console.log' from 'self'
                 # We need a reference to 'app' instance.
                 # For now, we will rely on the save button or implement a callback injection.
                 pass
             except:
                 pass
        
        # Refrescar este panel inmediatamente
        self.refresh_strings()
        
        # Intentar refrescar la app completa si es posible
        app_instance = self.winfo_toplevel()
        if hasattr(app_instance, "refresh_all_views"):
            app_instance.refresh_all_views()
            
        self._log(I18n.get("success_lang"), "INFO")

    def _create_label(self, text, row):
        lbl = ctk.CTkLabel(
            self.form_frame,
            text=text,
            font=ctk.CTkFont(size=14),
            text_color=AppConfig.RS_TEXT_SECONDARY,
            anchor="w"
        )
        lbl.grid(row=row, column=0, padx=10, pady=10, sticky="w")
        return lbl

    def _create_entry(self, default_val, row):
        entry = ctk.CTkEntry(
            self.form_frame,
            fg_color=AppConfig.RS_BG_INPUT,
            border_color=AppConfig.RS_ORANGE_DARK,
            text_color=AppConfig.RS_TEXT_PRIMARY,
            height=40
        )
        entry.insert(0, default_val)
        entry.grid(row=row, column=1, padx=10, pady=10, sticky="ew")
        return entry

    def _create_switch(self, text, variable):
        return ctk.CTkSwitch(
            self.toggle_frame,
            text=text,
            variable=variable,
            onvalue=True,
            offvalue=False,
            progress_color=AppConfig.RS_ORANGE,
            text_color=AppConfig.RS_TEXT_SECONDARY,
            font=ctk.CTkFont(size=14)
        )

    def _toggle_theme(self):
        mode = self.theme_var.get()
        ctk.set_appearance_mode(mode)
        self._log(f"Theme switched to {mode}", "INFO")

    def _on_branding_change(self, value):
        """Sincroniza el tema de la app con el branding seleccionado si el usuario lo cambia."""
        mode = "Light" if "Light" in value else "Dark"
        
        # Actualizar el switch visual
        self.theme_var.set(mode)
        
        # Aplicar el tema
        ctk.set_appearance_mode(mode)
        self._log(f"App Theme synchronized with Branding: {mode}", "INFO")

    def _save_settings(self):
        # En una app real, esto se guardaría en un archivo config.yaml o JSON
        self.settings.author_name = self.author_entry.get()
        self.settings.github_username = self.github_entry.get()
        self.settings.branding_theme = self.branding_combo.get()
        self.settings.auto_git_init = self.git_var.get()
        self.settings.create_venv = self.venv_var.get()
        self.settings.app_theme_mode = self.theme_var.get()
        
        self._log(I18n.get("success_save"), "SUCCESS")
        self._show_toast(I18n.get("success_save"))

    def _show_toast(self, message):
        """Muestra un mensaje temporal de éxito."""
        self.toast_label.configure(text=message)
        self.after(3000, lambda: self.toast_label.configure(text=""))

    def _log(self, msg, level):
        if self.log_callback:
            self.log_callback(msg, level)
