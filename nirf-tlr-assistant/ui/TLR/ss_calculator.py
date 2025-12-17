import tkinter as tk
from tkinter import ttk, messagebox
from helpers.SS_prompts.ss_prompt import build_prompt
from input_scripts.SS.predict_ss import load_model, predict_ss
from loaders.stats_loader import load_medians
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from parameter_docs.SS.SS.ss_doc_content import get_ss_doc_content
from parameter_docs.SS.SS.ss_graph_phd import create_phd_graph
from parameter_docs.SS.SS.ss_graph_score import create_ss_score_graph
from parameter_docs.SS.SS.ss_graph_capacity import create_capacity_graph

class SSCalculatorFrame(ttk.LabelFrame):
    def set_gemini_frame(self, gemini_frame):
        self.gemini_frame = gemini_frame
        
    def __init__(self, parent):
        super().__init__(parent, text="SS Calculator", padding=10)
        self.model = load_model()
        self.gemini_frame = None
        self.medians = load_medians()
        
        # Configure 6 columns for buttons/output
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        
        # Create styled documentation button at the top center
        style = ttk.Style()
        style.configure("Docs.TButton", 
                       background="#4A90E2", 
                       foreground="#FFFFFF",
                       font=("Arial", 10, "bold"),
                       padding=5)
        
        btn_docs = ttk.Button(self, text="📘 SS Docs", command=self.show_docs, style="Docs.TButton")
        btn_docs.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        ttk.Label(self, text="Total Sanctioned Seats (NT_total): ").grid(row=1, column=0, columnspan=2, sticky="w", pady=5, padx=2)
        self.nt_entry = ttk.Entry(self)
        self.nt_entry.grid(row=1, column=2, columnspan=4, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Total Enrolled Seats (NE_total): ").grid(row=2, column=0, columnspan=2, sticky="w", pady=5, padx=2)
        self.ne_entry = ttk.Entry(self)
        self.ne_entry.grid(row=2, column=2, columnspan=4, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Total Enrolled PhD Seats (NP_total): ").grid(row=3, column=0, columnspan=2, sticky="w", pady=5, padx=2)
        self.np_entry = ttk.Entry(self)
        self.np_entry.grid(row=3, column=2, columnspan=4, pady=5, sticky="ew", padx=2)
        
        predict_btn = ttk.Button(self, text="Predict_SS", command=self.predict_score)
        clear_btn = ttk.Button(self, text="Clear", command=self.clear_fields)
        
        clear_btn.grid(row=4, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
        predict_btn.grid(row=4, column=3, columnspan=3, sticky="ew", padx=10, pady=5)
        
        self.output_entry = ttk.Entry(self, width=15, font=("Arial", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=5, column=0, columnspan=3, pady=(0, 15), sticky="ew", padx=2)
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "SS Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get SS Recommendation", command=self.get_recommendation)
        recommend_btn.grid(row=5, column=3, columnspan=3, pady=(0, 15), sticky="ew", padx=2)

    def predict_score(self):
        try:
            nt = float(self.nt_entry.get())
            ne = float(self.ne_entry.get())
            np = float(self.np_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return
        
        if self.model is None:
            messagebox.showerror("Model Error", "SS Model not found")
            return
        
        try:
            score = predict_ss(self.model, nt, ne, np)
            self.output_entry.config(state="normal", foreground="white")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, str(score))
            self.output_entry.config(state="readonly")
        except Exception as e:
            messagebox.showerror("Prediction Error", str(e))
    
    def get_recommendation(self):
        try:
            nt = float(self.nt_entry.get())
            ne = float(self.ne_entry.get())
            np = float(self.np_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Enter valid numbers")
            return
            
        if not self.gemini_frame:
            messagebox.showerror("Gemini Error", "Gemini frame not connected.")
            return
        
        ss_score_text = self.output_entry.get().strip()
        try:
            ss_score = float(ss_score_text)
        except ValueError:
            messagebox.showerror("Error", "Please predict SS Score first.")
            return
        
        values = {
            "nt": nt,
            "ne": ne,
            "np": np,
            "ss_score": ss_score,
            "median_NT": self.medians["median_NT"],
            "median_NE": self.medians["median_NE"],
            "median_NP": self.medians["median_NP"],
            "median_SS": self.medians["median_SS"]
        }
        
        prompt = build_prompt(values)
        self.gemini_frame.generate_recommendation(prompt)
    
    def show_docs(self):
        doc_window = tk.Toplevel(self)
        doc_window.title("SS - Documentation")
        doc_window.geometry("1200x800")
        
        notebook = ttk.Notebook(doc_window)
        notebook.pack(expand=True, fill="both")
        
        text_frame = ttk.Frame(notebook)
        notebook.add(text_frame, text="Explanation")
        
        text = tk.Text(text_frame, wrap="word")
        text.pack(expand=True, fill="both", padx=10, pady=10)
        
        text.insert("1.0", get_ss_doc_content())
        text.config(state="disabled")
        
        scroll_frame = ttk.Frame(notebook)
        notebook.add(scroll_frame, text="Example Graph")
        
        canvas = tk.Canvas(scroll_frame)
        canvas.pack(side="left", fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        graph_container = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=graph_container, anchor="nw")
        
        fig1 = create_capacity_graph(2186, 2160)
        canvas1 = FigureCanvasTkAgg(fig1, master=graph_container)
        canvas1.draw()
        canvas1.get_tk_widget().pack(expand=True, fill="both", padx=10, pady=10)

        fig2 = create_phd_graph(1)
        canvas2 = FigureCanvasTkAgg(fig2, master=graph_container)
        canvas2.draw()
        canvas2.get_tk_widget().pack(expand=True, fill="both", padx=10, pady=10)

        fig3 = create_ss_score_graph(10.8)
        canvas3 = FigureCanvasTkAgg(fig3, master=graph_container)
        canvas3.draw()
        canvas3.get_tk_widget().pack(expand=True, fill="both", padx=10, pady=10)
        
        text.configure(font=("TkDefaultFont", 20))
                
        close_btn = ttk.Button(doc_window, text="Close", command=doc_window.destroy)
        close_btn.pack(pady=(0, 10))
    
    def clear_fields(self):
        self.nt_entry.delete(0, tk.END)
        self.ne_entry.delete(0, tk.END)
        self.np_entry.delete(0, tk.END)
        self.output_entry.config(state="normal", foreground="gray")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, "SS Score will appear here")
        self.output_entry.config(state="readonly")