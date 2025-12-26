import tkinter as tk
from tkinter import ttk, messagebox

class FPPPCalculatorFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="FPPP Calculator", padding=10)
        
        # Configure 6 columns for consistent layout
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
        
        btn_docs = ttk.Button(self, text="📘 FPPP Docs", style="Docs.TButton")
        btn_docs.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        # Row 1: Total Fac, SAmt_24-23, SAmt_23-22
        ttk.Label(self, text="Total Fac:").grid(row=1, column=0, sticky="w", pady=5, padx=2)
        self.tot_fac = ttk.Entry(self, width=10)
        self.tot_fac.grid(row=1, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="SAmt_24-23:").grid(row=1, column=2, sticky="w", pady=5, padx=2)
        self.spon_amt_24_23 = ttk.Entry(self, width=10)
        self.spon_amt_24_23.grid(row=1, column=3, sticky="ew", padx=2, pady=5)
        
        ttk.Label(self, text="SAmt_23-22:").grid(row=1, column=4, sticky="w", pady=5, padx=2)
        self.spon_amt_23_22 = ttk.Entry(self, width=10)
        self.spon_amt_23_22.grid(row=1, column=5, sticky="ew", padx=2, pady=5)
        
        # Row 2: SAmt_22-21, CAmt_24-23, CAmt_23-22
        ttk.Label(self, text="SAmt_22-21:").grid(row=2, column=0, sticky="w", pady=5, padx=2)
        self.spon_amt_22_21 = ttk.Entry(self, width=10)
        self.spon_amt_22_21.grid(row=2, column=1, sticky="ew", padx=2, pady=5)
        
        ttk.Label(self, text="CAmt_24-23:").grid(row=2, column=2, sticky="w", pady=5, padx=2)
        self.consul_amt_24_23 = ttk.Entry(self, width=10)
        self.consul_amt_24_23.grid(row=2, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="CAmt_23-22:").grid(row=2, column=4, sticky="w", pady=5, padx=2)
        self.consul_amt_23_22 = ttk.Entry(self, width=10)
        self.consul_amt_23_22.grid(row=2, column=5, pady=5, sticky="ew", padx=2)
        
        # Row 3: CAmt_22-21
        ttk.Label(self, text="CAmt_22-21:").grid(row=3, column=0, sticky="w", pady=5, padx=2)
        self.consul_amt_22_21 = ttk.Entry(self, width=10)
        self.consul_amt_22_21.grid(row=3, column=1, pady=5, sticky="ew", padx=2)
        
        # Row 4: Buttons
        predict_btn = ttk.Button(self, text="Predict FPPP")
        clear_btn = ttk.Button(self, text="Clear")
        
        clear_btn.grid(row=4, column=0, columnspan=3, sticky="ew", padx=2, pady=5)
        predict_btn.grid(row=4, column=3, columnspan=3, sticky="ew", padx=2, pady=5)
        
        # Row 5: Output and recommendation
        self.output_entry = ttk.Entry(self, width=15, font=("Arial", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=5, column=0, columnspan=3, sticky="ew", padx=2, pady=(0, 15))
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "FPPP Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get FPPP Recommendation")
        recommend_btn.grid(row=5, column=3, columnspan=3, sticky="ew", padx=2, pady=(0, 15))