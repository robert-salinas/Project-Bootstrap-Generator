import customtkinter as ctk
from bootstrap.gui.config import AppConfig
from bootstrap.gui.i18n import I18n
from tkinter import filedialog
from bootstrap.generator import ProjectGenerator

class MainPanel(ctk.CTkFrame):
    def __init__(self, master, log_callback=None):
        super().__init__(
            master,
            corner_radius=AppConfig.RADIUS_LG,
            fg_color=AppConfig.RS_SURFACE
        )
        self.log_callback = log_callback
        self.settings = None  # Will be injected by App
        
        # Responsive Layout (Centered Content)
        self.grid_columnconfigure(0, weight=1) # Spacer Left
        self.grid_columnconfigure(1, weight=3) # Main Content (~60% width)
        self.grid_columnconfigure(2, weight=1) # Spacer Right
        self.grid_rowconfigure(0, weight=1) # Form

        # Form Container (Scrollable)
        self.form_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            orientation="vertical"
        )
        self.form_frame.grid(row=0, column=1, padx=0, pady=10, sticky="nsew")
        self.form_frame.grid_columnconfigure(1, weight=1)

        # 1. Project Name
        self._create_row(I18n.get("lbl_name"), 
                         ctk.CTkEntry(self.form_frame, placeholder_text=I18n.get("ph_name"), height=32,
                                      fg_color=AppConfig.RS_BG_INPUT, border_color=AppConfig.RS_ORANGE_DARK, text_color=AppConfig.RS_TEXT_PRIMARY),
                         0, bind_key_release=True)

        # 2. Project Type
        self.type_combo = ctk.CTkComboBox(
            self.form_frame,
            values=[
                "python_cli", "python_web", "node_cli", "hardware_esp32",
                "python_pro", "web_frontend", "cpp_engineering",
                "full_stack_fastapi", "data_science"
            ],
            fg_color=AppConfig.RS_BG_INPUT, border_color=AppConfig.RS_ORANGE_DARK,
            button_color=AppConfig.RS_ORANGE, button_hover_color=AppConfig.RS_ORANGE_DARK,
            text_color=AppConfig.RS_TEXT_PRIMARY, dropdown_fg_color=AppConfig.RS_BG_MAIN,
            dropdown_text_color=AppConfig.RS_TEXT_PRIMARY, height=32,
            command=self._on_input_change
        )
        self.type_combo.set("python_pro")
        self._create_row(I18n.get("lbl_type"), self.type_combo, 1)

        # 3. Output Path
        self.path_frame = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        self.path_frame.grid_columnconfigure(0, weight=1)
        self.path_entry = ctk.CTkEntry(
            self.path_frame, placeholder_text=I18n.get("ph_path"), height=32,
            fg_color=AppConfig.RS_BG_INPUT, border_color=AppConfig.RS_ORANGE_DARK, text_color=AppConfig.RS_TEXT_PRIMARY
        )
        self.path_entry.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        self.path_entry.bind("<KeyRelease>", self._on_input_change)
        
        self.browse_btn = ctk.CTkButton(
            self.path_frame, text="...", width=40, height=32,
            fg_color=AppConfig.RS_BG_MAIN, hover_color=AppConfig.RS_ORANGE_DARK,
            text_color=AppConfig.RS_TEXT_PRIMARY, command=self._browse_folder
        )
        self.browse_btn.grid(row=0, column=1)
        self._create_row(I18n.get("lbl_path"), self.path_frame, 2)

        # 4. License
        self.license_combo = ctk.CTkComboBox(
            self.form_frame,
            values=["None", "MIT", "Apache 2.0", "GNU GPLv3", "BSD 3-Clause"],
            fg_color=AppConfig.RS_BG_INPUT, border_color=AppConfig.RS_ORANGE_DARK,
            button_color=AppConfig.RS_ORANGE, button_hover_color=AppConfig.RS_ORANGE_DARK,
            text_color=AppConfig.RS_TEXT_PRIMARY, dropdown_fg_color=AppConfig.RS_BG_MAIN,
            dropdown_text_color=AppConfig.RS_TEXT_PRIMARY, height=32,
            command=self._on_input_change
        )
        self.license_combo.set("None")
        self._create_row("Licencia:", self.license_combo, 3)

        # 5. Initial Libraries
        self.libs_entry = ctk.CTkEntry(
            self.form_frame, placeholder_text="ej: pandas, requests", height=32,
            fg_color=AppConfig.RS_BG_INPUT, border_color=AppConfig.RS_ORANGE_DARK, text_color=AppConfig.RS_TEXT_PRIMARY
        )
        self.libs_entry.bind("<KeyRelease>", self._on_input_change)
        self._create_row("Librerías:", self.libs_entry, 4)

        # 6. Engineering Options (Compact Grid)
        self.options_label = ctk.CTkLabel(
            self.form_frame, text="Ingeniería", font=ctk.CTkFont(size=14, weight="bold"),
            text_color=AppConfig.RS_TEXT_SECONDARY, anchor="w"
        )
        self.options_label.grid(row=5, column=0, padx=10, pady=(10, 5), sticky="nw")

        self.options_frame = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        self.options_frame.grid(row=5, column=1, padx=10, pady=5, sticky="ew")
        self.options_frame.grid_columnconfigure((0, 1), weight=1)

        self.git_switch = self._create_switch("Git 🐙", 0, 0)
        self.venv_switch = self._create_switch("Venv 🐍", 0, 1)
        self.docker_switch = self._create_switch("Docker 🐳", 1, 0)
        self.tests_switch = self._create_switch("Tests 🧪", 1, 1)
        self.actions_switch = self._create_switch("Actions 🤖", 2, 0)
        self.tests_switch.select()

        # 7. Preview Panel (Compact)
        self.preview_label = ctk.CTkLabel(
            self.form_frame, text="Preview:", font=ctk.CTkFont(size=14, weight="bold"),
            text_color=AppConfig.RS_TEXT_SECONDARY, anchor="w"
        )
        self.preview_label.grid(row=6, column=0, padx=10, pady=(10, 5), sticky="nw")

        self.preview_text = ctk.CTkTextbox(
            self.form_frame, height=80, fg_color=AppConfig.RS_BG_INPUT,
            text_color=AppConfig.RS_TEXT_SECONDARY, wrap="word"
        )
        self.preview_text.grid(row=6, column=1, padx=10, pady=(10, 5), sticky="ew")
        self.preview_text.configure(state="disabled")

        # 8. Action Buttons Container (Fixed Bottom in grid row 2 of MainPanel, moved OUT of Scrollable)
        self.actions_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.actions_frame.grid(row=2, column=1, padx=0, pady=20, sticky="ew")
        self.actions_frame.grid_columnconfigure((0, 1), weight=1)

        self.create_btn = ctk.CTkButton(
            self.actions_frame, text=I18n.get("btn_create"), font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=AppConfig.RS_ORANGE, hover_color=AppConfig.RS_ORANGE_DARK, height=40,
            corner_radius=AppConfig.RADIUS_LG, command=self._on_create
        )
        self.create_btn.grid(row=0, column=0, padx=(0, 5), sticky="ew")

        self.zip_btn = ctk.CTkButton(
            self.actions_frame, text=I18n.get("btn_zip"), font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=AppConfig.RS_BG_INPUT, hover_color=AppConfig.RS_ORANGE_DARK, border_width=2,
            border_color=AppConfig.RS_ORANGE, height=40, text_color=AppConfig.RS_TEXT_PRIMARY,
            corner_radius=AppConfig.RADIUS_LG, command=self._on_create_zip
        )
        self.zip_btn.grid(row=0, column=1, padx=(5, 0), sticky="ew")
        
        # Initial validation/preview
        self._update_preview()

    def _create_row(self, label_text, widget, row, bind_key_release=False):
        lbl = ctk.CTkLabel(self.form_frame, text=label_text, font=ctk.CTkFont(size=14),
                           text_color=AppConfig.RS_TEXT_SECONDARY, anchor="w")
        lbl.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        widget.grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        if bind_key_release and isinstance(widget, ctk.CTkEntry):
             self.name_entry = widget # Hack to keep ref
             widget.bind("<KeyRelease>", self._on_input_change)

    def _create_switch(self, text, r, c):
        sw = ctk.CTkSwitch(self.options_frame, text=text, progress_color=AppConfig.RS_ORANGE,
                           font=ctk.CTkFont(size=12), command=self._on_input_change)
        sw.grid(row=r, column=c, padx=5, pady=5, sticky="w")
        return sw



    def refresh_strings(self):
        """Actualiza los textos al cambiar el idioma."""
        self.title.configure(text=I18n.get("title_create"))
        self.name_label.configure(text=I18n.get("lbl_name"))
        self.name_entry.configure(placeholder_text=I18n.get("ph_name"))
        self.type_label.configure(text=I18n.get("lbl_type"))
        self.path_label.configure(text=I18n.get("lbl_path"))
        self.path_entry.configure(placeholder_text=I18n.get("ph_path"))
        self.browse_btn.configure(text=I18n.get("btn_browse"))
        self.create_btn.configure(text=I18n.get("btn_create"))
        self.zip_btn.configure(text=I18n.get("btn_zip"))

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

    def _create_entry(self, placeholder, row):
        entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text=placeholder,
            fg_color=AppConfig.RS_BG_INPUT,
            border_color=AppConfig.RS_ORANGE_DARK,
            text_color=AppConfig.RS_TEXT_PRIMARY,
            height=40
        )
        entry.grid(row=row, column=1, padx=10, pady=10, sticky="ew")
        return entry

    def _browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_entry.delete(0, "end")
            self.path_entry.insert(0, folder)

    def _get_context(self):
        """Obtiene el contexto para la generación basado en la configuración."""
        context = {}
        if self.settings:
            context["author_name"] = self.settings.author_name
            context["github_username"] = self.settings.github_username
            context["branding_theme"] = self.settings.branding_theme
        return context

    def _post_process(self, output_path):
        """Ejecuta acciones post-generación como git init o venv."""
        if not self.settings:
            return

        import subprocess
        
        if self.settings.auto_git_init:
            try:
                self._log(I18n.get("log_git_init"), "INFO")
                subprocess.run(["git", "init"], cwd=output_path, check=True, capture_output=True)
                self._log(I18n.get("success_git"), "SUCCESS")
            except Exception as e:
                self._log(I18n.get("warn_git", error=str(e)), "WARNING")

        if self.settings.create_venv:
            try:
                self._log(I18n.get("log_venv_init"), "INFO")
                subprocess.run(["python", "-m", "venv", ".venv"], cwd=output_path, check=True, capture_output=True)
                self._log(I18n.get("success_venv"), "SUCCESS")
            except Exception as e:
                self._log(I18n.get("warn_venv", error=str(e)), "WARNING")

    def _log(self, msg, level):
        if self.log_callback:
            self.log_callback(msg, level)

    def _on_input_change(self, event=None):
        # Dynamic switch logic
        p_type = self.type_combo.get()
        is_web = "web" in p_type or "node" in p_type or "fastapi" in p_type
        is_python = "python" in p_type or "fastapi" in p_type or "data" in p_type
        is_cpp = "cpp" in p_type
        
        # Venv: Only for Python projects
        if is_python:
            self.venv_switch.configure(state="normal")
        else:
            self.venv_switch.deselect()
            self.venv_switch.configure(state="disabled")
            
        # Update UI
        self._validate_path()
        self._update_preview()

    def _validate_path(self):
        path_str = self.path_entry.get()
        if not path_str:
            self.path_entry.configure(border_color=AppConfig.RS_ORANGE_DARK)
            return

        from pathlib import Path
        path = Path(path_str)
        if path.exists() and path.is_dir():
            self.path_entry.configure(border_color=AppConfig.RS_SUCCESS)
        else:
            self.path_entry.configure(border_color=AppConfig.RS_ERROR)

    def _update_preview(self):
        name = self.name_entry.get() or "[Project Name]"
        p_type = self.type_combo.get()
        path_str = self.path_entry.get()
        license_type = self.license_combo.get()
        libs = self.libs_entry.get()
        
        from pathlib import Path
        base_path = Path(path_str) if path_str else Path.cwd()
        full_path = base_path / name
        
        preview = f"Project: {name}\nType: {p_type}\nLocation: {full_path}\n"
        preview += f"License: {license_type}\n"
        if libs:
            preview += f"Libs: {libs}\n"
        preview += "\n"
        
        # Engineering Options
        opts = []
        if self.git_switch.get(): opts.append("Git Repo")
        if self.venv_switch.get(): opts.append("Virtual Env")
        if self.docker_switch.get(): opts.append("Docker Support")
        if self.tests_switch.get(): opts.append("Test Suite")
        if self.actions_switch.get(): opts.append("GitHub Actions")
        
        if opts:
            preview += "Included: " + ", ".join(opts) + "\n\n"
        
        if p_type == "python_pro":
            preview += "• Includes standard .gitignore\n• Python src structure"
        elif p_type == "web_frontend":
            preview += "• Includes Header/Footer with branding\n• RS Design System assets"
        elif p_type == "cpp_engineering":
            preview += "• Includes main.cpp with Hello World\n• Makefile & include structure"
        
        self.preview_text.configure(state="normal")
        self.preview_text.delete("1.0", "end")
        self.preview_text.insert("1.0", preview)
        self.preview_text.configure(state="disabled")

    def _on_create(self):
        name = self.name_entry.get().strip()
        p_type = self.type_combo.get()
        path = self.path_entry.get().strip()

        if not name:
            self._log(I18n.get("err_name_req"), "ERROR")
            return
            
        from pathlib import Path
        output_path = Path(path) if path else Path.cwd() / name
        
        self._log(I18n.get("log_start", name=name, type=p_type), "INFO")
        
        try:
            generator = ProjectGenerator()
            context = self._get_context()
            
            # Capture options
            opts = {
                "with_git": bool(self.git_switch.get()),
                "with_venv": bool(self.venv_switch.get()),
                "with_docker": bool(self.docker_switch.get()),
                "with_tests": bool(self.tests_switch.get()),
                "with_github_actions": bool(self.actions_switch.get()),
                "license": self.license_combo.get(),
                "initial_libs": self.libs_entry.get()
            }
            
            # En una app real, esto debería ir en un hilo aparte para no congelar la GUI
            generator.generate(p_type, name, output_path, context=context, **opts)
            self._log(I18n.get("success_project", name=name, path=output_path), "SUCCESS")
            
        except Exception as e:
            self._log(I18n.get("err_project", error=str(e)), "ERROR")

    def _on_create_zip(self):
        name = self.name_entry.get().strip()
        p_type = self.type_combo.get()
        path = self.path_entry.get().strip()

        if not name:
            self._log(I18n.get("err_name_req"), "ERROR")
            return

        from pathlib import Path
        output_path = Path(path) if path else Path.cwd() / name

        self._log(I18n.get("log_zip_start", name=name, type=p_type), "INFO")

        try:
            generator = ProjectGenerator()
            context = self._get_context()
            
            # Capture options
            opts = {
                "with_git": bool(self.git_switch.get()),
                "with_venv": bool(self.venv_switch.get()),
                "with_docker": bool(self.docker_switch.get()),
                "with_tests": bool(self.tests_switch.get()),
                "with_github_actions": bool(self.actions_switch.get()),
                "license": self.license_combo.get(),
                "initial_libs": self.libs_entry.get()
            }
            
            # 1. Generar proyecto temporalmente
            generator.generate(p_type, name, output_path, context=context, **opts)
            
            # 2. Comprimir
            zip_path = generator.compress_project(output_path)
            self._log(I18n.get("success_zip", path=zip_path), "SUCCESS")
        except Exception as e:
            self._log(I18n.get("err_zip", error=str(e)), "ERROR")
