import tkinter as tk
from tkinter import ttk, messagebox
from helpers.SS_prompts.fsr_prompt import build_fsr_prompt
from loaders.stats_loader import load_fsr_medians
from parameter_docs.SS.FSR.fsr_doc_content import get_fsr_doc_content

class FSRCalculatorFrame(ttk.LabelFrame):
    def set_gemini_frame(self, gemini_frame):
        self.gemini_frame = gemini_frame
        self.medians = load_fsr_medians()
        
    def __init__(self, parent):
        super().__init__(parent, text="FSR Calculator", padding=10)
        
        # Configure 2 columns for inputs, but 6 columns for buttons/output
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
        
        btn_docs = ttk.Button(self, text="📘 FSR Docs", style="Docs.TButton", command=self.show_docs)
        btn_docs.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        ttk.Label(self, text="Total Sanctioned Seats (NT_total): ").grid(row=1, column=0, columnspan=2, sticky="w", pady=5, padx=2)
        self.nt_entry = ttk.Entry(self, width=20)
        self.nt_entry.grid(row=1, column=2, columnspan=4, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Permanen Enrolled PhD Seats (NP_total): ").grid(row=2, column=0, columnspan=2, sticky="w", pady=5, padx=2)
        self.ne_entry = ttk.Entry(self, width=20)
        self.ne_entry.grid(row=2, column=2, columnspan=4, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Total Faculties (F_total): ").grid(row=3, column=0, columnspan=2, sticky="w", pady=5, padx=2)
        self.f_entry = ttk.Entry(self, width=20)
        self.f_entry.grid(row=3, column=2, columnspan=4, pady=5, sticky="ew", padx=2)
        
        predict_btn = ttk.Button(self, text="Predict_FSR", command=self.predict_fsr)
        clear_btn = ttk.Button(self, text="Clear", command=self.clear_fields)
        
        clear_btn.grid(row=4, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
        predict_btn.grid(row=4, column=3, columnspan=3, sticky="ew", padx=10, pady=5)
        
        self.output_entry = ttk.Entry(self, width=15, font=("Arial", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=5, column=0, columnspan=3, sticky="ew", padx=2)
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "FSR Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get FSR Recommendation", command=self.get_fsr_recommendation)
        recommend_btn.grid(row=5, column=3, columnspan=3, sticky="ew", padx=2)
    
    def predict_fsr(self):
        try:
            nt_total = float(self.nt_entry.get())
            np_total = float(self.ne_entry.get())
            f_total = float(self.f_entry.get())
            
            n_total = nt_total + np_total
            
            if n_total == 0:
                messagebox.showerror("Calculation Error", "Total students cannot be zero.")
                return
            
            fsr_ratio = f_total / n_total
            if fsr_ratio < (.02):
                fsr_score = 0
            else:
                fsr_score = 450 * fsr_ratio
                
                if fsr_score > 30:
                    fsr_score = 30
            
            self.output_entry.config(state="normal", foreground="white")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, f"{fsr_score: .3f}")
            self.output_entry.config(state="readonly")
                        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return
    
    def get_fsr_recommendation(self):
        try:
            nt = float(self.nt_entry.get())
            np = float(self.ne_entry.get())
            f = float(self.f_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please calculate FSR first.")
            return
        if not self.gemini_frame:
            messagebox.showerror("Gemini Error", "Gemini frame not connected.")
            return
        
        fsr_score_text = self.output_entry.get().strip()
        try:
            fsr_score = float(fsr_score_text)
        except ValueError:
            messagebox.showerror("Error", "Please predict FSR Score first.")
            return
        
        values = {
            "nt": nt,
            "np": np,
            "f": f,
            "fsr_score": fsr_score,
            "median_F": self.medians["median_F"],
            "median_N": self.medians["median_N"],
            "median_FSR": self.medians["median_FSR"]
        }
        
        prompt = build_fsr_prompt(values)
        self.gemini_frame.generate_recommendation(prompt)
    
    def show_docs(self):
        doc_window = tk.Toplevel(self)
        doc_window.title("FSR - Documentation")
        doc_window.geometry("900x700")
        
        notebook = ttk.Notebook(doc_window)
        notebook.pack(expand=True, fill="both")
        
        text_frame = ttk.Frame(notebook)
        notebook.add(text_frame, text="Explanation")
        
        text = tk.Text(text_frame, wrap="word")
        text.pack(expand=True, fill="both", padx=10, pady=10)
        
        text.insert("1.0", get_fsr_doc_content())
        text.config(state="disabled")
    
    def clear_fields(self):
        self.nt_entry.delete(0, tk.END)
        self.ne_entry.delete(0, tk.END)
        self.f_entry.delete(0, tk.END)
        self.output_entry.config(state="normal")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, "")
        self.output_entry.config(state="readonly")