import tkinter as tk
from tkinter import ttk

class PCSCalculatorFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="PCS Calculator", padding=10)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        style = ttk.Style()
        style.configure("Docs.TButton", 
                       background="#4A90E2", 
                       foreground="#FFFFFF",
                       font=("Arial", 10, "bold"),
                       padding=5)
        
        btn_docs = ttk.Button(self, text="📘 PCS Docs", style="Docs.TButton")
        btn_docs.grid(row=0, column=0, columnspan=2)
        
        label1 = ttk.Label(self, text="Do your institution buildings have Lifts/Ramps?:", wraplength=300, justify="left")
        label1.grid(row=1, column=0, sticky="w", pady=5)
        self.total_ramps = ttk.Entry(self, width=20)
        self.total_ramps.grid(row=1, column=1, pady=5, sticky="ew", padx=(0, 10))
        
        label2 = ttk.Label(self, text="Do your institution have provision for walking aids, including wheelchairs and transportation from one building to another for handicapped students?:", wraplength=300, justify="left")
        label2.grid(row=2, column=0, sticky="w", pady=5)
        self.total_walking_aids = ttk.Entry(self, width=20)
        self.total_walking_aids.grid(row=2, column=1, pady=5, sticky="ew", padx=(0, 10))
        
        label3 = ttk.Label(self, text="Do your institution buildings have specially designed toilets for handicapped students?:", wraplength=300, justify="left")
        label3.grid(row=3, column=0, sticky="w", pady=5)
        self.total_toilets_handicapped = ttk.Entry(self, width=20)
        self.total_toilets_handicapped.grid(row=3, column=1, pady=5, sticky="ew", padx=(0, 10))
        
        predict_btn = ttk.Button(self, text="Predict_PCS")
        clear_btn = ttk.Button(self, text="Clear")
        
        clear_btn.grid(row=4, column=0, sticky="w", padx=10)
        predict_btn.grid(row=4, column=1, sticky="e", padx=10)
        
        self.output_entry = ttk.Entry(self, width=15, font=("Ariel", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=5, column=0, columnspan=1, sticky="ew")
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "PSCS Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get PSCS Recommendation")
        recommend_btn.grid(row=5, column=1, columnspan=1, sticky="ew", padx=(0, 10))