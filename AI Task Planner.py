import customtkinter as ctk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class TaskDependencyPlannerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AI Task Dependency Planner")
        self.geometry("1420x860")
        self.minsize(1280, 780)

        self.tasks = set()
        self.dependencies = []

        self.configure(fg_color=("#f5f5f5", "#171717"))

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_main_area()
        self.update_stats_and_lists()

    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(
            self,
            width=240,
            corner_radius=0,
            fg_color=("#e5e7eb", "#202020")
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        self.sidebar.grid_rowconfigure(7, weight=1)

        self.sidebar_title = ctk.CTkLabel(
            self.sidebar,
            text="AI Task\nPlanner",
            justify="left",
            font=ctk.CTkFont(size=30, weight="bold"),
            text_color=("#111827", "#f9fafb")
        )
        self.sidebar_title.grid(row=0, column=0, padx=24, pady=(28, 10), sticky="w")

        self.sidebar_subtitle = ctk.CTkLabel(
            self.sidebar,
            text="Discrete Mathematics\nApplication using\nDirected Graphs",
            justify="left",
            font=ctk.CTkFont(size=14),
            text_color=("#374151", "#d1d5db")
        )
        self.sidebar_subtitle.grid(row=1, column=0, padx=24, pady=(0, 24), sticky="w")

        btn_cfg = dict(height=46, corner_radius=12, font=ctk.CTkFont(size=15, weight="bold"))

        self.sample_btn = ctk.CTkButton(
            self.sidebar, text="Load Sample Data", command=self.load_sample_data,
            fg_color="#2563eb", hover_color="#1d4ed8", **btn_cfg
        )
        self.sample_btn.grid(row=2, column=0, padx=22, pady=10, sticky="ew")

        self.plan_btn = ctk.CTkButton(
            self.sidebar, text="Generate Plan", command=self.generate_plan,
            fg_color="#7c3aed", hover_color="#6d28d9", **btn_cfg
        )
        self.plan_btn.grid(row=3, column=0, padx=22, pady=10, sticky="ew")

        self.graph_btn = ctk.CTkButton(
            self.sidebar, text="Visualize Graph", command=self.visualize_graph,
            fg_color="#f97316", hover_color="#ea580c", **btn_cfg
        )
        self.graph_btn.grid(row=4, column=0, padx=22, pady=10, sticky="ew")

        self.clear_btn = ctk.CTkButton(
            self.sidebar, text="Clear All", command=self.clear_all,
            fg_color="#ef4444", hover_color="#dc2626", **btn_cfg
        )
        self.clear_btn.grid(row=5, column=0, padx=22, pady=10, sticky="ew")

        self.mode_label = ctk.CTkLabel(
            self.sidebar,
            text="Appearance Mode",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=("#111827", "#f9fafb")
        )
        self.mode_label.grid(row=6, column=0, padx=24, pady=(24, 8), sticky="w")

        self.mode_menu = ctk.CTkOptionMenu(
            self.sidebar,
            values=["Dark", "Light", "System"],
            command=self.change_appearance_mode,
            height=42,
            corner_radius=10,
            font=ctk.CTkFont(size=14),
            dropdown_font=ctk.CTkFont(size=14)
        )
        self.mode_menu.set("Dark")
        self.mode_menu.grid(row=7, column=0, padx=22, pady=(0, 18), sticky="ew")

        self.sidebar_footer = ctk.CTkLabel(
            self.sidebar,
            text="Topological Sorting\nCycle Detection\nDAG Validation",
            justify="left",
            font=ctk.CTkFont(size=13),
            text_color=("#4b5563", "#9ca3af")
        )
        self.sidebar_footer.grid(row=8, column=0, padx=24, pady=24, sticky="sw")

    def create_main_area(self):
        self.main = ctk.CTkFrame(self, fg_color="transparent")
        self.main.grid(row=0, column=1, sticky="nsew", padx=18, pady=18)
        self.main.grid_columnconfigure(0, weight=1)
        self.main.grid_rowconfigure(3, weight=1)

        self.create_header()
        self.create_input_row()
        self.create_stats_row()
        self.create_bottom_row()

    def create_header(self):
        self.header = ctk.CTkFrame(
            self.main,
            corner_radius=18,
            fg_color=("#ffffff", "#232323")
        )
        self.header.grid(row=0, column=0, sticky="ew", pady=(0, 16))

        self.header_content = ctk.CTkFrame(self.header, fg_color="transparent")
        self.header_content.pack(fill="both", expand=True, padx=28, pady=22)

        self.header_title = ctk.CTkLabel(
            self.header_content,
            text="Task Dependency Planner Dashboard",
            font=ctk.CTkFont(size=30, weight="bold"),
            text_color=("#111827", "#f9fafb")
        )
        self.header_title.pack(anchor="w")

        self.header_subtitle = ctk.CTkLabel(
            self.header_content,
            text='Build task flows like "Design → Development → Testing → Deployment"',
            font=ctk.CTkFont(size=16),
            text_color=("#4b5563", "#bdbdbd")
        )
        self.header_subtitle.pack(anchor="w", pady=(8, 0))

    def create_input_row(self):
        self.input_row = ctk.CTkFrame(self.main, fg_color="transparent")
        self.input_row.grid(row=1, column=0, sticky="ew", pady=(0, 16))
        self.input_row.grid_columnconfigure((0, 1), weight=1)

        self.task_card = ctk.CTkFrame(
            self.input_row,
            corner_radius=18,
            fg_color=("#ffffff", "#232323")
        )
        self.task_card.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        self.dep_card = ctk.CTkFrame(
            self.input_row,
            corner_radius=18,
            fg_color=("#ffffff", "#232323")
        )
        self.dep_card.grid(row=0, column=1, sticky="nsew", padx=(10, 0))

        self.build_task_card()
        self.build_dependency_card()

    def build_task_card(self):
        container = ctk.CTkFrame(self.task_card, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=24, pady=22)

        title = ctk.CTkLabel(
            container,
            text="Add Task",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=("#111827", "#f9fafb")
        )
        title.pack(anchor="w", pady=(0, 14))

        self.task_entry = ctk.CTkEntry(
            container,
            placeholder_text="Enter task name",
            height=46,
            corner_radius=12,
            font=ctk.CTkFont(size=15)
        )
        self.task_entry.pack(fill="x", pady=(0, 16))

        self.add_task_btn = ctk.CTkButton(
            container,
            text="Add Task",
            command=self.add_task,
            height=46,
            corner_radius=12,
            font=ctk.CTkFont(size=15, weight="bold"),
            fg_color="#2563eb",
            hover_color="#1d4ed8"
        )
        self.add_task_btn.pack(fill="x")

    def build_dependency_card(self):
        container = ctk.CTkFrame(self.dep_card, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=24, pady=22)

        title = ctk.CTkLabel(
            container,
            text="Add Dependency",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=("#111827", "#f9fafb")
        )
        title.pack(anchor="w", pady=(0, 14))

        self.from_entry = ctk.CTkEntry(
            container,
            placeholder_text="From task",
            height=46,
            corner_radius=12,
            font=ctk.CTkFont(size=15)
        )
        self.from_entry.pack(fill="x", pady=(0, 12))

        self.to_entry = ctk.CTkEntry(
            container,
            placeholder_text="To task",
            height=46,
            corner_radius=12,
            font=ctk.CTkFont(size=15)
        )
        self.to_entry.pack(fill="x", pady=(0, 12))

        self.dep_note = ctk.CTkLabel(
            container,
            text='Meaning: "A → B" means A must be completed before B',
            font=ctk.CTkFont(size=12),
            text_color=("#4b5563", "#bdbdbd")
        )
        self.dep_note.pack(anchor="w", pady=(0, 14))

        self.add_dep_btn = ctk.CTkButton(
            container,
            text="Add Dependency",
            command=self.add_dependency,
            height=46,
            corner_radius=12,
            font=ctk.CTkFont(size=15, weight="bold"),
            fg_color="#16a34a",
            hover_color="#15803d"
        )
        self.add_dep_btn.pack(fill="x")

    def create_stats_row(self):
        self.stats_row = ctk.CTkFrame(self.main, fg_color="transparent")
        self.stats_row.grid(row=2, column=0, sticky="ew", pady=(0, 16))
        self.stats_row.grid_columnconfigure((0, 1, 2), weight=1)

        self.task_stat = self.create_stat_card(self.stats_row, "Total Tasks", "0", 0)
        self.dep_stat = self.create_stat_card(self.stats_row, "Dependencies", "0", 1)
        self.status_stat = self.create_stat_card(self.stats_row, "Status", "Ready", 2)

    def create_stat_card(self, parent, title, value, col):
        card = ctk.CTkFrame(
            parent,
            corner_radius=16,
            fg_color=("#ffffff", "#232323")
        )
        card.grid(row=0, column=col, sticky="ew", padx=8)

        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=20, pady=18)

        title_lbl = ctk.CTkLabel(
            inner,
            text=title,
            font=ctk.CTkFont(size=15),
            text_color=("#4b5563", "#d1d5db")
        )
        title_lbl.pack(anchor="w")

        value_lbl = ctk.CTkLabel(
            inner,
            text=value,
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color=("#111827", "#f9fafb")
        )
        value_lbl.pack(anchor="w", pady=(10, 0))

        card.value_label = value_lbl
        return card

    def create_bottom_row(self):
        self.bottom_row = ctk.CTkFrame(self.main, fg_color="transparent")
        self.bottom_row.grid(row=3, column=0, sticky="nsew")
        self.bottom_row.grid_columnconfigure((0, 1), weight=1)
        self.bottom_row.grid_rowconfigure(0, weight=1)

        self.output_panel = ctk.CTkFrame(
            self.bottom_row,
            corner_radius=18,
            fg_color=("#ffffff", "#232323")
        )
        self.output_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        self.right_panel = ctk.CTkFrame(
            self.bottom_row,
            corner_radius=18,
            fg_color=("#ffffff", "#232323")
        )
        self.right_panel.grid(row=0, column=1, sticky="nsew", padx=(10, 0))

        self.build_output_panel()
        self.build_right_panel()

    def build_output_panel(self):
        container = ctk.CTkFrame(self.output_panel, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=20, pady=18)

        title = ctk.CTkLabel(
            container,
            text="Planner Output",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=("#111827", "#f9fafb")
        )
        title.pack(anchor="w", pady=(0, 12))

        self.output_box = ctk.CTkTextbox(
            container,
            corner_radius=14,
            font=("Consolas", 14),
            fg_color=("#f9fafb", "#121212"),
            text_color=("#111827", "#f9fafb"),
            border_width=1,
            border_color=("#d1d5db", "#323232")
        )
        self.output_box.pack(fill="both", expand=True)

    def build_right_panel(self):
        container = ctk.CTkFrame(self.right_panel, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=20, pady=18)

        task_title = ctk.CTkLabel(
            container,
            text="Task List",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=("#111827", "#f9fafb")
        )
        task_title.pack(anchor="w", pady=(0, 12))

        self.task_list_box = ctk.CTkTextbox(
            container,
            height=170,
            corner_radius=14,
            font=("Consolas", 13),
            fg_color=("#f9fafb", "#121212"),
            text_color=("#111827", "#f9fafb"),
            border_width=1,
            border_color=("#d1d5db", "#323232")
        )
        self.task_list_box.pack(fill="x", pady=(0, 18))

        dep_title = ctk.CTkLabel(
            container,
            text="Dependency List",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=("#111827", "#f9fafb")
        )
        dep_title.pack(anchor="w", pady=(0, 12))

        self.dep_list_box = ctk.CTkTextbox(
            container,
            corner_radius=14,
            font=("Consolas", 13),
            fg_color=("#f9fafb", "#121212"),
            text_color=("#111827", "#f9fafb"),
            border_width=1,
            border_color=("#d1d5db", "#323232")
        )
        self.dep_list_box.pack(fill="both", expand=True)

    def log_output(self, text):
        self.output_box.insert("end", text + "\n")
        self.output_box.see("end")

    def set_status(self, text):
        self.status_stat.value_label.configure(text=text)

    def update_stats_and_lists(self):
        self.task_stat.value_label.configure(text=str(len(self.tasks)))
        self.dep_stat.value_label.configure(text=str(len(self.dependencies)))

        self.task_list_box.delete("1.0", "end")
        self.dep_list_box.delete("1.0", "end")

        if self.tasks:
            for i, task in enumerate(sorted(self.tasks), start=1):
                self.task_list_box.insert("end", f"{i}. {task}\n")
        else:
            self.task_list_box.insert("end", "No tasks added yet.\n")

        if self.dependencies:
            for i, (a, b) in enumerate(self.dependencies, start=1):
                self.dep_list_box.insert("end", f"{i}. {a} → {b}\n")
        else:
            self.dep_list_box.insert("end", "No dependencies added yet.\n")

    def add_task(self):
        task = self.task_entry.get().strip()

        if not task:
            messagebox.showwarning("Input Error", "Please enter a task name.")
            return

        if task in self.tasks:
            messagebox.showinfo("Duplicate Task", f'Task "{task}" already exists.')
            return

        self.tasks.add(task)
        self.task_entry.delete(0, "end")
        self.log_output(f"✓ Task added: {task}")
        self.set_status("Updated")
        self.update_stats_and_lists()

    def add_dependency(self):
        from_task = self.from_entry.get().strip()
        to_task = self.to_entry.get().strip()

        if not from_task or not to_task:
            messagebox.showwarning("Input Error", "Please enter both tasks.")
            return

        if from_task == to_task:
            messagebox.showwarning("Invalid Dependency", "A task cannot depend on itself.")
            return

        if from_task not in self.tasks:
            self.tasks.add(from_task)
            self.log_output(f"✓ Auto-added task: {from_task}")

        if to_task not in self.tasks:
            self.tasks.add(to_task)
            self.log_output(f"✓ Auto-added task: {to_task}")

        if (from_task, to_task) in self.dependencies:
            messagebox.showinfo("Duplicate Dependency", "This dependency already exists.")
            return

        self.dependencies.append((from_task, to_task))
        self.from_entry.delete(0, "end")
        self.to_entry.delete(0, "end")

        self.log_output(f"✓ Dependency added: {from_task} → {to_task}")
        self.set_status("Updated")
        self.update_stats_and_lists()

    def generate_plan(self):
        if not self.tasks:
            messagebox.showwarning("No Data", "Please add tasks first.")
            return

        graph = nx.DiGraph()
        graph.add_nodes_from(self.tasks)
        graph.add_edges_from(self.dependencies)

        self.log_output("\n" + "=" * 48)
        self.log_output("TASK EXECUTION PLAN ANALYSIS")
        self.log_output("=" * 48)

        try:
            order = list(nx.topological_sort(graph))
            self.log_output("Status      : Valid dependency structure")
            self.log_output("Cycle Check : No cycle detected\n")
            self.log_output("Execution Order:")

            for i, task in enumerate(order, start=1):
                self.log_output(f"{i}. {task}")

            self.log_output("\nInterpretation:")
            self.log_output("The task dependency system forms a DAG.")
            self.log_output("Therefore, a valid topological ordering exists.\n")
            self.set_status("Valid DAG")

        except nx.NetworkXUnfeasible:
            self.log_output("Status      : Invalid dependency structure")
            self.log_output("Cycle Check : Cycle detected\n")
            self.log_output("A valid execution plan cannot be generated.")

            try:
                cycle = nx.find_cycle(graph, orientation="original")
                self.log_output("\nCycle Path:")
                for edge in cycle:
                    self.log_output(f"{edge[0]} → {edge[1]}")
            except Exception:
                pass

            self.log_output("\nPlease remove cyclic dependencies.\n")
            self.set_status("Cycle Found")

    def visualize_graph(self):
        if not self.tasks:
            messagebox.showwarning("No Data", "Please add tasks first.")
            return

        graph = nx.DiGraph()
        graph.add_nodes_from(self.tasks)
        graph.add_edges_from(self.dependencies)

        mode = ctk.get_appearance_mode()

        if mode == "Light":
            bg_color = "#ffffff"
            title_color = "#111827"
            label_color = "#111827"
            node_main = "#60a5fa"
            node_isolated = "#d1d5db"
            edge_color = "#f59e0b"
            border_color = "#1e3a8a"
        else:
            bg_color = "#171717"
            title_color = "#f9fafb"
            label_color = "#f9fafb"
            node_main = "#60a5fa"
            node_isolated = "#6b7280"
            edge_color = "#f59e0b"
            border_color = "#1e3a8a"

        plt.figure(figsize=(13, 8), facecolor=bg_color)
        ax = plt.gca()
        ax.set_facecolor(bg_color)

        pos = {}
        try:
            topo_order = list(nx.topological_sort(graph))

            levels = {}
            for node in topo_order:
                preds = list(graph.predecessors(node))
                if not preds:
                    levels[node] = 0
                else:
                    levels[node] = max(levels[p] for p in preds) + 1

            layer_nodes = {}
            for node, level in levels.items():
                layer_nodes.setdefault(level, []).append(node)

            for level, nodes in layer_nodes.items():
                for i, node in enumerate(nodes):
                    pos[node] = (level * 3, -i * 2)

        except nx.NetworkXUnfeasible:
            pos = nx.spring_layout(graph, seed=42, k=1.5)

        isolated_nodes = list(nx.isolates(graph))
        connected_nodes = [n for n in graph.nodes if n not in isolated_nodes]

        if connected_nodes:
            nx.draw_networkx_nodes(
                graph, pos,
                nodelist=connected_nodes,
                node_size=2600,
                node_color=node_main,
                edgecolors=border_color,
                linewidths=2
            )

        if isolated_nodes:
            # place isolated nodes to the far right if using layered DAG layout
            if pos:
                max_x = max(x for x, _ in pos.values()) if pos else 0
                for idx, node in enumerate(isolated_nodes):
                    if node not in pos:
                        pos[node] = (max_x + 3, -idx * 2)

            nx.draw_networkx_nodes(
                graph, pos,
                nodelist=isolated_nodes,
                node_size=2600,
                node_color=node_isolated,
                edgecolors=border_color,
                linewidths=2
            )

        nx.draw_networkx_edges(
            graph, pos,
            arrows=True,
            arrowstyle="-|>",
            arrowsize=24,
            width=2.4,
            edge_color=edge_color,
            connectionstyle="arc3,rad=0.05"
        )

        nx.draw_networkx_labels(
            graph, pos,
            font_size=10,
            font_weight="bold",
            font_color=label_color
        )

        plt.title("Task Dependency Graph", fontsize=18, color=title_color, pad=16)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def clear_all(self):
        self.tasks.clear()
        self.dependencies.clear()

        self.output_box.delete("1.0", "end")
        self.task_list_box.delete("1.0", "end")
        self.dep_list_box.delete("1.0", "end")

        self.task_entry.delete(0, "end")
        self.from_entry.delete(0, "end")
        self.to_entry.delete(0, "end")

        self.set_status("Ready")
        self.update_stats_and_lists()
        self.log_output("All data cleared.")

    def load_sample_data(self):
        self.tasks = {
            "Requirement Analysis",
            "UI Design",
            "Backend Development",
            "Model Integration",
            "Testing",
            "Deployment"
        }

        self.dependencies = [
            ("Requirement Analysis", "UI Design"),
            ("Requirement Analysis", "Backend Development"),
            ("UI Design", "Model Integration"),
            ("Backend Development", "Model Integration"),
            ("Model Integration", "Testing"),
            ("Testing", "Deployment")
        ]

        self.output_box.delete("1.0", "end")
        self.log_output("Sample project data loaded.")
        self.set_status("Sample Loaded")
        self.update_stats_and_lists()

    def change_appearance_mode(self, mode):
        ctk.set_appearance_mode(mode)


if __name__ == "__main__":
    app = TaskDependencyPlannerApp()
    app.mainloop()