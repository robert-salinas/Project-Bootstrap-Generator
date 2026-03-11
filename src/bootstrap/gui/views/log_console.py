import customtkinter as ctk
from bootstrap.gui.config import AppConfig
from bootstrap.gui.i18n import I18n

class LogConsole(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            height=150,
            corner_radius=AppConfig.RADIUS_LG,
            fg_color=AppConfig.RS_BG_INPUT
        )
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        self.label = ctk.CTkLabel(
            self,
            text=I18n.get("lbl_logs"),
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=AppConfig.RS_TEXT_MUTED,
            anchor="w"
        )
        self.label.grid(row=0, column=0, padx=15, pady=(10, 5), sticky="ew")

        # Text Area
        self.log_text = ctk.CTkTextbox(
            self,
            font=ctk.CTkFont(family="Consolas", size=11),
            text_color=AppConfig.RS_SUCCESS,
            fg_color="transparent",
            activate_scrollbars=True
        )
        self.log_text.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")
        self.log_text.configure(state="disabled")

    def refresh_strings(self):
        """Actualiza los textos al cambiar el idioma."""
        self.label.configure(text=I18n.get("lbl_logs"))

    def log(self, message: str, level: str = "INFO"):
        self.log_text.configure(state="normal")
        color = AppConfig.RS_TEXT_PRIMARY
        if level == "ERROR":
            color = AppConfig.RS_ERROR
        elif level == "SUCCESS":
            color = AppConfig.RS_SUCCESS
        elif level == "WARNING":
            color = AppConfig.RS_ORANGE
        
        # Resolver color basado en el modo (Light/Dark) ya que tag_config es de Tkinter
        mode = ctk.get_appearance_mode()
        color_idx = 0 if mode == "Light" else 1
        resolved_color = color[color_idx] if isinstance(color, tuple) else color

        tag_name = f"tag_{level}"
        self.log_text.tag_config(tag_name, foreground=resolved_color)
        
        prefix = f"[{level}] "
        self.log_text.insert("end", f"{prefix}{message}\n", tag_name)
        self.log_text.see("end")
        self.log_text.configure(state="disabled")
