import tkinter as tk
from tkinter import ttk

class GUICalculatorFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="GUI Calculator", padding=10)
        
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
        
        btn_docs = ttk.Button(self, text="📘 GUI Docs", style="Docs.TButton")
        btn_docs.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        # Row 1: All three Intake fields
        ttk.Label(self, text="Intake21-22: ").grid(row=1, column=0, sticky="w", pady=5, padx=2)
        self.total_intake1 = ttk.Entry(self, width=10)
        self.total_intake1.grid(row=1, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Intake22-23: ").grid(row=1, column=2, sticky="w", pady=5, padx=2)
        self.total_intake2 = ttk.Entry(self, width=10)
        self.total_intake2.grid(row=1, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Intake23-24: ").grid(row=1, column=4, sticky="w", pady=5, padx=2)
        self.total_intake3 = ttk.Entry(self, width=10)
        self.total_intake3.grid(row=1, column=5, pady=5, sticky="ew", padx=2)
        
        # Row 2: All three Passed fields
        ttk.Label(self, text="Passed21-23: ").grid(row=2, column=0, sticky="w", pady=5, padx=2)
        self.total_passed1 = ttk.Entry(self, width=10)
        self.total_passed1.grid(row=2, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Passed22-23: ").grid(row=2, column=2, sticky="w", pady=5, padx=2)
        self.total_passed2 = ttk.Entry(self, width=10)
        self.total_passed2.grid(row=2, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Passed23-24: ").grid(row=2, column=4, sticky="w", pady=5, padx=2)
        self.total_passed3 = ttk.Entry(self, width=10)
        self.total_passed3.grid(row=2, column=5, pady=5, sticky="ew", padx=2)
        
        predict_btn = ttk.Button(self, text="Predict_GUI")
        clear_btn = ttk.Button(self, text="Clear")
        
        clear_btn.grid(row=3, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
        predict_btn.grid(row=3, column=3, columnspan=3, sticky="ew", padx=10, pady=5)
        
        self.output_entry = ttk.Entry(self, width=15, font=("Arial", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=4, column=0, columnspan=3, sticky="ew", padx=2)
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "GUI Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get GUI Recommendation")
        recommend_btn.grid(row=4, column=3, columnspan=3, sticky="ew", padx=2)