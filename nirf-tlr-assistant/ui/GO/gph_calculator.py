import tkinter as tk
from tkinter import ttk, messagebox

class GPHCalculatorFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="GPH Calculator", padding=10)
        
        # Configure 6 columns for buttons/output
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
        
        btn_docs = ttk.Button(self, text="📘 GPH Docs", style="Docs.TButton")
        btn_docs.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        ttk.Label(self, text="Total Graduates(UG+PG) [last 3 years]: ").grid(row=1, column=0, columnspan=2, sticky="w", pady=5, padx=2)
        self.tgrad1_total_entry = ttk.Entry(self, width=20)
        self.tgrad1_total_entry.grid(row=1, column=2, columnspan=4, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Total Placed(UG+PG) [last 3 years]: ").grid(row=2, column=0, columnspan=2, sticky="w", pady=5, padx=2)
        self.tplaced1_total_entry = ttk.Entry(self, width=20)
        self.tplaced1_total_entry.grid(row=2, column=2, columnspan=4, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Total Higher Grads(UG+PG) [last 3 years]: ").grid(row=3, column=0, columnspan=2, sticky="w", pady=5, padx=2)
        self.tplaced1_total_entry = ttk.Entry(self, width=20)
        self.tplaced1_total_entry.grid(row=3, column=2, columnspan=4, pady=5, sticky="ew", padx=2)
        
        predict_btn = ttk.Button(self, text="Predict GPH")
        clear_btn = ttk.Button(self, text="Clear")
        
        clear_btn.grid(row=4, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
        predict_btn.grid(row=4, column=3, columnspan=3, sticky="ew", padx=10, pady=5)
        
        self.output_entry = ttk.Entry(self, width=15, font=("Arial", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=5, column=0, columnspan=3, sticky="ew", padx=2)
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "GPH Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get GPH Recommendation")
        recommend_btn.grid(row=5, column=3, columnspan=3, sticky="ew", padx=2)