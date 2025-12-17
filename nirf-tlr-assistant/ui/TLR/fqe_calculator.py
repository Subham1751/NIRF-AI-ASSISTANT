import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from helpers.SS_prompts.fqe_prompt import build_prompt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from parameter_docs.SS.FQE.fqe_doc_content import get_fqe_doc_content
from parameter_docs.SS.FQE.fqe_graph_exp import create_experience_graph
from parameter_docs.SS.FQE.fqe_graph_primary import create_primary_graph

class FQECalculatorFrame(ttk.LabelFrame):
    def set_gemini_frame(self, gemini_frame):
        self.gemini_frame = gemini_frame
    
    def __init__(self, parent):
        super().__init__(parent, text="FQE Calculator", padding=10)
        self.gemini_frame = None
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        
        style = ttk.Style()
        style.configure("Docs.TButton", 
                       background="#4A90E2", 
                       foreground="#FFFFFF",
                       font=("Arial", 10, "bold"),
                       padding=5)
        
        btn_docs = ttk.Button(self, text="📘 FQE Docs", style="Docs.TButton", command=self.show_docs)
        btn_docs.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        ttk.Label(self, text="Tot Fac: ").grid(row=1, column=0, sticky="w", pady=5, padx=2)
        self.f_total_entry = ttk.Entry(self, width=10)
        self.f_total_entry.grid(row=1, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="PhD Fac: ").grid(row=1, column=2, sticky="w", pady=5, padx=2)
        self.phd_faculty_entry = ttk.Entry(self, width=10)
        self.phd_faculty_entry.grid(row=1, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Tot Stu(UG+PG): ").grid(row=1, column=4, sticky="w", pady=5, padx=2)
        self.total_students = ttk.Entry(self, width=10)
        self.total_students.grid(row=1, column=5, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Fac exp ≤ 8: ").grid(row=2, column=0, sticky="w", pady=5, padx=2)
        self.exp1_entry = ttk.Entry(self, width=10)
        self.exp1_entry.grid(row=2, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Fac exp 8–15: ").grid(row=2, column=2, sticky="w", pady=5, padx=2)
        self.exp2_entry = ttk.Entry(self, width=10)
        self.exp2_entry.grid(row=2, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Fac exp > 15: ").grid(row=2, column=4, sticky="w", pady=5, padx=2)
        self.exp3_entry = ttk.Entry(self, width=10)
        self.exp3_entry.grid(row=2, column=5, pady=5, sticky="ew", padx=2)
        
        predict_btn = ttk.Button(self, text="Predict FQE", command=self.predict_fqe)
        clear_btn = ttk.Button(self, text="Clear", command=self.clear_fields)
        
        clear_btn.grid(row=3, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
        predict_btn.grid(row=3, column=3, columnspan=3, sticky="ew", padx=10, pady=5)
        
        self.output_entry = ttk.Entry(self, width=15, font=("Arial", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=4, column=0, columnspan=3, sticky="ew", padx=2)
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "FQE Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get FQE Recommendation", command=self.get_recommendation)
        recommend_btn.grid(row=4, column=3, columnspan=3, sticky="ew", padx=2)
    
    def calculate_fqe_metrics(self, total_faculty, phd_faculty, total_students, exp1, exp2, exp3):
        required_faculty = total_students / 15
        faculty_base = max(total_faculty, required_faculty)
        FRA = (phd_faculty / faculty_base) * 100
        
        if FRA < 95:
            FQ = 10 * (FRA / 95)
        else:
            FQ = 10
        
        F1 = exp1 / total_faculty
        F2 = exp2 / total_faculty
        F3 = exp3 / total_faculty
        
        part1 = 3 * min(3 * F1, 1)
        part2 = 3 * min(3 * F2, 1)
        part3 = 4 * min(3 * F3, 1)
        
        FE = part1 + part2 + part3
        FQE = FQ + FE
        
        return {
            "fqe_score": FQE,
            "required_faculty": required_faculty,
            "faculty_base": faculty_base,
            "FRA": FRA,
            "FQ": FQ,
            "FE": FE
        }
        
    def predict_fqe(self):
        try:
            total_faculty = float(self.f_total_entry.get())
            phd_faculty = float(self.phd_faculty_entry.get())
            total_students = float(self.total_students.get())
            exp1 = float(self.exp1_entry.get())
            exp2 = float(self.exp2_entry.get())
            exp3 = float(self.exp3_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return
        
        try:    
            metrics = self.calculate_fqe_metrics(
                total_faculty, phd_faculty, total_students, 
                exp1, exp2, exp3
            )
            
            self.output_entry.config(state="normal", foreground="white")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, f"{metrics['fqe_score']:.2f}")
            self.output_entry.config(state="readonly")
        except Exception as e:
            messagebox.showerror("Prediction Error", str(e))
            return
    
    def get_recommendation(self):
        try:
            total_faculty = float(self.f_total_entry.get())
            phd_faculty = float(self.phd_faculty_entry.get())
            total_students = float(self.total_students.get())
            fe1 = float(self.exp1_entry.get())
            fe2 = float(self.exp2_entry.get())
            fe3 = float(self.exp3_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Enter valid numbers.")
            return
        
        if not self.gemini_frame:
            messagebox.showerror("Gemini Error", "Gemini frame not connected.")
            return
        
        fqe_score_text = self.output_entry.get().strip()
        try:
            fqe_score = float(fqe_score_text)
        except ValueError:
            messagebox.showerror("Error", "Please predict FQE Score first.")
            return

        metrics = self.calculate_fqe_metrics(
            total_faculty, phd_faculty, total_students,
            fe1, fe2, fe3
        )
        
        values = {
            "tf": total_faculty,
            "pf": phd_faculty,
            "ts": total_students,
            "fe1": fe1,
            "fe2": fe2,
            "fe3": fe3,
            "fqe_score": fqe_score,
            "req_fac": metrics["required_faculty"],
            "fra": metrics["FRA"],
            "fq": metrics["FQ"],
            "fe": metrics["FE"]
        }
        
        prompt = build_prompt(values)
        self.gemini_frame.generate_recommendation(prompt)
            
    def show_docs(self):
        doc_window = tk.Toplevel(self)
        doc_window.title("FQE - Documentation")
        doc_window.geometry("900x700")
        
        notebook = ttk.Notebook(doc_window)
        notebook.pack(expand=True, fill="both")
        
        text_frame = ttk.Frame(notebook)
        notebook.add(text_frame, text="Explanation")
        
        text = tk.Text(text_frame, wrap="word")
        text.pack(expand=True, fill="both", padx=10, pady=10)
        
        text.insert("1.0", get_fqe_doc_content())
        text.config(state="disabled")
        
        graph_frame = ttk.Frame(notebook)
        notebook.add(graph_frame, text="Example Graph")

        fig = create_primary_graph()
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both", padx=10, pady=10)

        fig2 = create_experience_graph()
        canvas2 = FigureCanvasTkAgg(fig2, master=graph_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(expand=True, fill="both", padx=10, pady=10)
        
        text.configure(font=("TkDefaultFont", 20))
        
        doc_content = get_fqe_doc_content()
        text.insert("1.0", doc_content)
        text.config(state="disabled")
        
        close_btn = ttk.Button(doc_window, text="Close", command=doc_window.destroy)
        close_btn.pack(pady=(0, 10))
    
    def clear_fields(self):
        self.f_total_entry.delete(0, tk.END)
        self.phd_faculty_entry.delete(0, tk.END)
        self.total_students.delete(0, tk.END)
        self.exp1_entry.delete(0, tk.END)
        self.exp2_entry.delete(0, tk.END)
        self.exp3_entry.delete(0, tk.END)
        self.output_entry.config(state="normal", foreground="gray")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, "FQE Score appear here")
        self.output_entry.config(state="readonly")