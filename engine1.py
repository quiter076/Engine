import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

ENGINE_DATA = {
    "2 ":  { "Полная темп. ":  "288,15 K ",  "Стат. темп. ":  "274,41 K ",  "Полное давл. ":  "100,31 kPa ",  "Стат. давл. ":  "84,56 kPa ",  "Скорость ":  "166,05 m/s "},
    "21 ": { "Полная темп. ":  "423,62 K ",  "Стат. темп. ":  "403,83 K ",  "Полное давл. ":  "300,94 kPa ",  "Стат. давл. ":  "253,84 kPa ",  "Скорость ":  "201,05 m/s "},
    "25 ": { "Полная темп. ":  "423,62 K ",  "Стат. темп. ":  "403,83 K ",  "Полное давл. ":  "297,93 kPa ",  "Стат. давл. ":  "251,30 kPa ",  "Скорость ":  "201,05 m/s "},
    "3 ":  { "Полная темп. ":  "737,06 K ",  "Стат. темп. ":  "731,80 K ",  "Полное давл. ":  "1787,56 kPa ", "Стат. давл. ":  "1739,74 kPa ", "Скорость ":  "106,93 m/s "},
    "31 ": { "Полная темп. ":  "737,06 K ",  "Стат. темп. ":  "731,80 K ",  "Полное давл. ":  "1787,56 kPa ", "Стат. давл. ":  "1739,74 kPa ", "Скорость ":  "106,93 m/s "},
    "4 ":  { "Полная темп. ":  "1250 K ",    "Стат. темп. ":  "1232,74 K ", "Полное давл. ":  "1733,93 kPa ", "Стат. давл. ":  "1635,21 kPa ", "Скорость ":  "204,46 m/s "},
    "41 ": { "Полная темп. ":  "1250 K ",    "Стат. темп. ":  "1232,74 K ", "Полное давл. ":  "1733,93 kPa ", "Стат. давл. ":  "1635,21 kPa ", "Скорость ":  "204,46 m/s "},
    "44 ": { "Полная темп. ":  "916,05 K ",  "Стат. темп. ":  "885,92 K ",  "Полное давл. ":  "473,63 kPa ",  "Стат. давл. ":  "414,59 kPa ",  "Скорость ":  "262,45 m/s "},
    "45 ": { "Полная темп. ":  "916,05 K ",  "Стат. темп. ":  "892,15 K ",  "Полное давл. ":  "464,16 kPa ",  "Стат. давл. ":  "417,68 kPa ",  "Скорость ":  "234,05 m/s "},
    "5 ":  { "Полная темп. ":  "722,58 K ",  "Стат. темп. ":  "691,92 K ",  "Полное давл. ":  "168,51 kPa ",  "Стат. давл. ":  "142,74 kPa ",  "Скорость ":  "259,63 m/s "},
    "6 ":  { "Полная темп. ":  "722,58 K ",  "Стат. темп. ":  "716,65 K ",  "Полное давл. ":  "165,14 kPa ",  "Стат. давл. ":  "159,98 kPa ",  "Скорость ":  "114,56 m/s "},
    "13 ": { "Полная темп. ":  "359,67 K ",  "Стат. темп. ":  "348,57 K ",  "Полное давл. ":  "200,62 kPa ",  "Стат. давл. ":  "179,72 kPa ",  "Скорость ":  "149,58 m/s "},
    "16 ": { "Полная темп. ":  "359,67 K ",  "Стат. темп. ":  "354,15 K ",  "Полное давл. ":  "194,60 kPa ",  "Стат. давл. ":  "184,31 kPa ",  "Скорость ":  "105,53 m/s "},
    "163 ": { "Полная темп. ": "359,67 K ",  "Стат. темп. ":  "354,15 K ",  "Полное давл. ":  "194,60 kPa ",  "Стат. давл. ":  "184,31 kPa ",  "Скорость ":  "105,53 m/s "},
    "64 ": { "Полная темп. ":  "555,97 K ",  "Стат. темп. ":  "549,65 K ",  "Полное давл. ":  "170,05 kPa ",  "Стат. давл. ":  "163,10 kPa ",  "Скорость ":  "115,14 m/s "},
    "7 ":  { "Полная темп. ":  "546,42 K ",  "Стат. темп. ":  "473,66 K ",  "Полное давл. ":  "170,05 kPa ",  "Стат. давл. ":  "101,33 kPa ",  "Скорость ":  "389,16 m/s "},
    "8 ":  { "Полная темп. ":  "546,42 K ",  "Стат. темп. ":  "473,66 K ",  "Полное давл. ":  "170,05 kPa ",  "Стат. давл. ":  "101,33 kPa ",  "Скорость ":  "389,16 m/s "},
    "63 ": { "Полная темп. ":  "722,58 K ",  "Стат. темп. ":  "716,65 K ",  "Полное давл. ":  "165,14 kPa ",  "Стат. давл. ":  "159,98 kPa ",  "Скорость ":  "114,56 m/s "}
}

BUTTON_COORDS = {
    "2 ":  (116, 42),  "21 ": (254, 42),  "25 ": (292, 42),
    "3 ":  (374, 42),  "31 ": (392, 98),  "4 ":  (420, 42),
    "41 ": (430, 98),  "44 ": (454, 42),  "45 ": (475, 98),
    "5 ":  (502, 42),  "6 ":  (590, 361), "13 ": (330, 42),
    "16 ": (591, 42),  "163 ": (627, 42), "64 ": (688, 42),
    "7 ":  (759, 42),  "8 ":  (800, 42),  "63 ": (628, 362)
}

class EngineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ТРДД: Параметры рабочего тела | Тарасов Д.А. | ТЭД-223Б")
        self.root.geometry("1400x900")
        self.root.state('zoomed')
        self.root.configure(bg="#2c3e50")

        style = ttk.Style()
        style.theme_use('clam')

        main_frame = tk.Frame(root, bg="#2c3e50")
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(main_frame, bg="#34495e", highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#34495e")

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.scroll_position = 0
        self.scroll_step = 100
        self.max_position = 2000

        nav_frame = tk.Frame(main_frame, bg="#1abc9c", width=80)
        nav_frame.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Button(nav_frame, text="▲\nВВЕРХ", command=self.scroll_up, bg="#16a085", fg="white",
                 font=("Arial", 9, "bold"), width=8, height=2, relief=tk.FLAT).pack(pady=5)
        tk.Button(nav_frame, text="▼\nВНИЗ", command=self.scroll_down, bg="#16a085", fg="white",
                 font=("Arial", 9, "bold"), width=8, height=2, relief=tk.FLAT).pack(pady=5)

        self.create_header()
        self.create_engine_section()
        self.create_graphs_section()
        self.create_footer()

        self.scrollable_frame.bind("<Configure>", lambda e: self.update_scroll_region())

    def update_scroll_region(self):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def scroll_up(self):
        self.scroll_position = max(0, self.scroll_position - self.scroll_step)
        self.canvas.yview_moveto(self.scroll_position / self.max_position)

    def scroll_down(self):
        self.scroll_position = min(self.max_position, self.scroll_position + self.scroll_step)
        self.canvas.yview_moveto(self.scroll_position / self.max_position)

    def create_header(self):
        header_frame = tk.Frame(self.scrollable_frame, bg="#3498db", relief=tk.RAISED, bd=2)
        header_frame.pack(fill=tk.X, padx=20, pady=15)

        tk.Label(header_frame, text="КУРСОВАЯ РАБОТА", font=("Arial", 20, "bold"),
                bg="#3498db", fg="white").pack(pady=5)
        tk.Label(header_frame, text="по дисциплине «Языки программирования»",
                font=("Arial", 14), bg="#3498db", fg="white").pack()
        tk.Label(header_frame, text="Тема: Моделирование изменения параметров рабочего тела\nпо тракту двухконтурного турбореактивного двигателя (ТРДД)",
                font=("Arial", 12), bg="#3498db", fg="white", justify=tk.CENTER).pack(pady=5)
        tk.Label(header_frame, text="Студент: Тарасов Д.А. | Группа: ТЭД-223Б",
                font=("Arial", 12, "bold"), bg="#3498db", fg="#ecf0f1").pack(pady=5)

    def create_engine_section(self):
        section_frame = tk.Frame(self.scrollable_frame, bg="#ecf0f1", relief=tk.RAISED, bd=2)
        section_frame.pack(fill=tk.X, padx=20, pady=10)

        title_bar = tk.Frame(section_frame, bg="#e74c3c")
        title_bar.pack(fill=tk.X)
        tk.Label(title_bar, text="🔧 ИНТЕРАКТИВНАЯ СХЕМА ДВИГАТЕЛЯ (ТРДД)",
                font=("Arial", 14, "bold"), bg="#e74c3c", fg="white", pady=8).pack()

        self.engine_canvas = tk.Canvas(section_frame, bg="white", highlightthickness=0)
        self.engine_canvas.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        self.load_image()

        info_bar = tk.Frame(section_frame, bg="#f39c12")
        info_bar.pack(fill=tk.X)
        tk.Label(info_bar, text="💡 Нажмите на номер сечения для просмотра параметров",
                font=("Arial", 10), bg="#f39c12", fg="white").pack(pady=5)

    def load_image(self):
        try:
            img = Image.open("engine_scheme2.png")
            screen_width = self.root.winfo_screenwidth()
            target_width = screen_width - 250
            wpercent = (target_width / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((target_width, hsize), Image.Resampling.LANCZOS)

            self.photo = ImageTk.PhotoImage(img)
            self.engine_canvas.config(width=target_width, height=hsize)
            self.engine_canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.draw_buttons(target_width, hsize)
        except Exception:
            self.engine_canvas.config(width=900, height=560)
            self.engine_canvas.create_text(450, 280, text="Поместите файл 'engine_scheme.png' в папку с программой",
                                          fill="#e74c3c", font=("Arial", 14, "bold"))

    def draw_buttons(self, current_width, current_height):
        if current_width == 0: current_width = 900
        if current_height == 0: current_height = 560

        scale_x = current_width / 900.0
        scale_y = current_height / 560.0

        for section_id, (x, y) in BUTTON_COORDS.items():
            clean_id = section_id.strip()
            group_tag = f"btn_group_{clean_id}"

            new_x = x * scale_x
            new_y = y * scale_y

            circle_id = self.engine_canvas.create_oval(new_x - 27, new_y - 27, new_x + 27, new_y + 27,
                                                       fill="#3498db", outline="#2c3e50", width=2, tags=group_tag)
            text_id = self.engine_canvas.create_text(new_x, new_y, text=clean_id,
                                                    font=("Arial", 10, "bold"), fill="white", tags=group_tag)

            self.engine_canvas.tag_bind(group_tag, "<Enter>", lambda e, cid=circle_id: self.on_hover(cid))
            self.engine_canvas.tag_bind(group_tag, "<Leave>", lambda e, cid=circle_id: self.on_leave(cid))
            self.engine_canvas.tag_bind(group_tag, "<Button-1>", lambda e, sid=section_id: self.show_params(sid))

    def on_hover(self, circle_id):
        self.engine_canvas.itemconfig(circle_id, fill="#e74c3c")

    def on_leave(self, circle_id):
        self.engine_canvas.itemconfig(circle_id, fill="#3498db")

    def show_params(self, section_id):
        if section_id not in ENGINE_DATA:
            return

        data = ENGINE_DATA[section_id]
        popup = tk.Toplevel(self.root)
        popup.title(f"📊 Параметры сечения {section_id.strip()}")
        popup.geometry("380x350")
        popup.configure(bg="#ecf0f1")
        popup.resizable(False, False)

        header = tk.Frame(popup, bg="#9b59b6")
        header.pack(fill=tk.X)
        tk.Label(header, text=f"Сечение {section_id.strip()}", font=("Arial", 16, "bold"),
                bg="#9b59b6", fg="white", pady=10).pack()

        frame = tk.Frame(popup, bg="#ecf0f1")
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)

        colors = ["#3498db", "#e74c3c", "#2ecc71", "#f39c12", "#9b59b6"]
        idx = 0
        for param, value in data.items():
            row = tk.Frame(frame, bg="white", relief=tk.RAISED, bd=1)
            row.pack(fill=tk.X, pady=3)

            color_bar = tk.Frame(row, bg=colors[idx % len(colors)], width=8)
            color_bar.pack(side=tk.LEFT, fill=tk.Y)

            tk.Label(row, text=f" {param} ", font=("Arial", 11, "bold"),
                    bg="white", width=18, anchor="w").pack(side=tk.LEFT, padx=5)
            tk.Label(row, text=f" {value}  ", font=("Arial", 11),
                    bg="#ecf0f1", fg="#2c3e50").pack(side=tk.LEFT, padx=5)
            idx += 1

        tk.Button(popup, text="✖ Закрыть", command=popup.destroy, bg="#e74c3c",
                 fg="white", font=("Arial", 11, "bold"), pady=5).pack(pady=10)

    def create_graphs_section(self):
        graphs_frame = tk.Frame(self.scrollable_frame, bg="#ecf0f1", relief=tk.RAISED, bd=2)
        graphs_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        title_bar = tk.Frame(graphs_frame, bg="#27ae60")
        title_bar.pack(fill=tk.X)
        tk.Label(title_bar, text=" ГРАФИКИ ИЗМЕНЕНИЯ ПАРАМЕТРОВ",
                font=("Arial", 14, "bold"), bg="#27ae60", fg="white", pady=8).pack()

        self.create_graphs(graphs_frame)

    def create_graphs(self, parent):
        # Сечения для внутреннего контура (ядро)
        internal_sections = ["2 ", "21 ", "3 ", "31 ", "4 ", "41 ", "44 ", "45 ", "5 ", "6 ", "64 ", "7 ", "8 "]
        # Сечения для внешнего контура (обвод)
        external_sections = ["2 ", "21 ", "25 ", "13 ", "16 ", "163 ", "63 ", "64 ", "7 ", "8 "]

        # Сетка 5 строк × 2 столбца = 10 графиков
        fig, axes = plt.subplots(5, 2, figsize=(14, 18))
        fig.suptitle('Параметры рабочего тела по контурам ТРДД', fontsize=16, fontweight='bold', color='#2c3e50')

        params = [
            ("Полная темп. ", "Температура (K)", "Полная температура"),
            ("Стат. темп. ", "Статическая температура (K)", "Статическая температура"),
            ("Полное давл. ", "Давление (kPa)", "Полное давление"),
            ("Стат. давл. ", "Статическое давление (kPa)", "Статическое давление"),
            ("Скорость ", "Скорость (m/s)", "Скорость")
        ]

        for i, (key, ylabel, param_name) in enumerate(params):
            # --- Внутренний контур (левый столбец) ---
            ax_int = axes[i, 0]
            y_int, x_int = [], []
            for sec in internal_sections:
                if sec in ENGINE_DATA:
                    val = ENGINE_DATA[sec][key].replace(" K ", "").replace(" kPa ", "").replace(" m/s ", "").replace(",", ".")
                    y_int.append(float(val))
                    x_int.append(sec)

            ax_int.plot(x_int, y_int, marker='o', linestyle='-', color='#003366', linewidth=2.5, markerfacecolor='#003366', markersize=6)
            ax_int.set_title(f'Внутренний контур: {param_name}', fontsize=10, color='#003366')
            ax_int.set_ylabel(ylabel)
            ax_int.grid(True, alpha=0.4)
            ax_int.tick_params(axis='x', rotation=45)

            # --- Внешний контур (правый столбец) ---
            ax_ext = axes[i, 1]
            y_ext, x_ext = [], []
            for sec in external_sections:
                if sec in ENGINE_DATA:
                    val = ENGINE_DATA[sec][key].replace(" K ", "").replace(" kPa ", "").replace(" m/s ", "").replace(",", ".")
                    y_ext.append(float(val))
                    x_ext.append(sec)

            ax_ext.plot(x_ext, y_ext, marker='D', linestyle='--', color='#e67e22', linewidth=2.5, markerfacecolor='#d35400', markersize=6)
            ax_ext.set_title(f'Внешний контур: {param_name}', fontsize=10, color='#e67e22')
            ax_ext.set_ylabel(ylabel)
            ax_ext.grid(True, alpha=0.4)
            ax_ext.tick_params(axis='x', rotation=45)

        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

    def create_footer(self):
        footer_frame = tk.Frame(self.scrollable_frame, bg="#34495e")
        footer_frame.pack(fill=tk.X, padx=20, pady=10)

        tk.Label(footer_frame, text="Уфимский университет науки и технологий | Кафедра авиационных двигателей | 2026",
                font=("Arial", 10), bg="#34495e", fg="#bdc3c7", justify=tk.CENTER).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = EngineApp(root)
    root.mainloop()
