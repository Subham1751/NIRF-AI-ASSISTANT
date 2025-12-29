import tkinter as tk
from tkinter import ttk, messagebox

class QPCalculatorFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="QP Calcullator", padding=10)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        
        style = ttk.Style()
        style.configure("Docs.TButton", 
                       background="#4A90E2", 
                       foreground="#FFFFFF",
                       font=("Arial", 10, "bold"),
                       padding=5)
        
        btn_docs = ttk.Button(self, text="📘 QP Docs", style="Docs.TButton")
        btn_docs.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        # Row 1: Total fac, Total Stu, Total Cit Count
        ttk.Label(self, text="Total Fac:").grid(row=1, column=0, sticky="w", padx=2, pady=5)
        self.tot_fac = ttk.Entry(self, width=10)
        self.tot_fac.grid(row=1, column=1, padx=2, pady=5, sticky="ew")
        
        ttk.Label(self, text="Total Stu(UG+PG):").grid(row=1, column=2, sticky="w", padx=2, pady=5)
        self.tot_stu = ttk.Entry(self, width=10)
        self.tot_stu.grid(row=1, column=3, sticky="ew", padx=2, pady=5)
        
        ttk.Label(self, text="Total CitCount:").grid(row=1, column=4, sticky="w", padx=2, pady=5)
        self.tot_ccount = ttk.Entry(self, width=10)
        self.tot_ccount.grid(row=1, column=5, sticky="ew", padx=2, pady=5)
        
        # Row 2: Total Weighted Pubs, Top25% CitCount, Total Retracted Pubs
        ttk.Label(self, text="Total WPubs:").grid(row=2, column=0, sticky="w", padx=2, pady=5)
        self.tot_wpubs = ttk.Entry(self, width=10)
        self.tot_wpubs.grid(row=2, column=1, sticky="ew", padx=2, pady=5)
        
        ttk.Label(self, text="Top 25% CitCount:").grid(row=2, column=2, sticky="w", padx=2, pady=5)
        self.top_citcount = ttk.Entry(self, width=10)
        self.top_citcount.grid(row=2, column=3, sticky="ew", padx=2, pady=5)
        
        ttk.Label(self, text="Total RPubs:").grid(row=2, column=4, sticky="w", padx=2, pady=5)
        self.tot_rpubs = ttk.Entry(self, width=10)
        self.tot_rpubs.grid(row=2, column=5, sticky="ew", padx=2, pady=5)
        
        # Row 3: Buttons
        predict_btn = ttk.Button(self, text="Predict QP")
        clear_btn = ttk.Button(self, text="Clear")
        
        clear_btn.grid(row=3, column=0, columnspan=3, sticky="ew", padx=2, pady=5)
        predict_btn.grid(row=3, column=3, columnspan=3, sticky="ew", padx=2, pady=5)
        
        # Row 4: Output and recommendation
        self.output_entry = ttk.Entry(self, width=15, font=("Ariel", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=4, column=0, columnspan=3, sticky="ew", padx=2, pady=(0, 15))
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "PU Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get PU Recommendation")
        recommend_btn.grid(row=4, column=3, columnspan=3, sticky="ew", padx=2, pady=(0, 15))
        
        