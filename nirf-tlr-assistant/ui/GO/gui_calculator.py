import tkinter as tk
from tkinter import ttk, messagebox
from input_scripts.GO.predict_gue import predict_gue
from helpers.GO_prompts.GUE_prompt import build_gue_prompt

class GUICalculatorFrame(ttk.LabelFrame):
    def set_gemini_frame(self, gemini_frame):
        self.gemini_frame = gemini_frame
        
    def __init__(self, parent):
        super().__init__(parent, text="GUI Calculator", padding=10)
        
        # Configure 12 columns for 6 label-entry pairs
        for i in range(12):
            self.grid_columnconfigure(i, weight=1)
        
        style = ttk.Style()
        style.configure("Docs.TButton", 
                       background="#4A90E2", 
                       foreground="#FFFFFF",
                       font=("Arial", 10, "bold"),
                       padding=5)
        
        btn_docs = ttk.Button(self, text="📘 GUI Docs", style="Docs.TButton")
        btn_docs.grid(row=0, column=0, columnspan=12, sticky="ew")
        
        # Row 1: All 6 fields alternating Intake and Graduated (UG4)
        ttk.Label(self, text="IN-18:").grid(row=1, column=0, sticky="e", pady=5, padx=(2,1))
        self.total_ug4_intake1 = ttk.Entry(self, width=4)
        self.total_ug4_intake1.grid(row=1, column=1, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="GRAD-22:").grid(row=1, column=2, sticky="e", pady=5, padx=(2,1))
        self.total_ug4_passed1 = ttk.Entry(self, width=4)
        self.total_ug4_passed1.grid(row=1, column=3, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="IN-19:").grid(row=1, column=4, sticky="e", pady=5, padx=(2,1))
        self.total_ug4_intake2 = ttk.Entry(self, width=4)
        self.total_ug4_intake2.grid(row=1, column=5, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="GRAD-23:").grid(row=1, column=6, sticky="e", pady=5, padx=(2,1))
        self.total_ug4_passed2 = ttk.Entry(self, width=4)
        self.total_ug4_passed2.grid(row=1, column=7, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="IN-20:").grid(row=1, column=8, sticky="e", pady=5, padx=(2,1))
        self.total_ug4_intake3 = ttk.Entry(self, width=4)
        self.total_ug4_intake3.grid(row=1, column=9, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="GRAD-24:").grid(row=1, column=10, sticky="e", pady=5, padx=(2,1))
        self.total_ug4_passed3 = ttk.Entry(self, width=4)
        self.total_ug4_passed3.grid(row=1, column=11, pady=5, sticky="ew", padx=(1,2))
        
        # Row 2: All 6 fields alternating Intake and Graduated (UG5)
        ttk.Label(self, text="IN-17:").grid(row=2, column=0, sticky="e", pady=5, padx=(2,1))
        self.total_ug5_intake1 = ttk.Entry(self, width=4)
        self.total_ug5_intake1.grid(row=2, column=1, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="GRAD-22:").grid(row=2, column=2, sticky="e", pady=5, padx=(2,1))
        self.total_ug5_passed1 = ttk.Entry(self, width=4)
        self.total_ug5_passed1.grid(row=2, column=3, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="IN-18:").grid(row=2, column=4, sticky="e", pady=5, padx=(2,1))
        self.total_ug5_intake2 = ttk.Entry(self, width=4)
        self.total_ug5_intake2.grid(row=2, column=5, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="GRAD-23:").grid(row=2, column=6, sticky="e", pady=5, padx=(2,1))
        self.total_ug5_passed2 = ttk.Entry(self, width=4)
        self.total_ug5_passed2.grid(row=2, column=7, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="IN-19:").grid(row=2, column=8, sticky="e", pady=5, padx=(2,1))
        self.total_ug5_intake3 = ttk.Entry(self, width=4)
        self.total_ug5_intake3.grid(row=2, column=9, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="GRAD-24:").grid(row=2, column=10, sticky="e", pady=5, padx=(2,1))
        self.total_ug5_passed3 = ttk.Entry(self, width=4)
        self.total_ug5_passed3.grid(row=2, column=11, pady=5, sticky="ew", padx=(1,2))
        
        # Row 3: All 6 fields alternating Intake and Graduated (PG-2)
        ttk.Label(self, text="IN-20:").grid(row=3, column=0, sticky="e", pady=5, padx=(2,1))
        self.total_pg2_intake1 = ttk.Entry(self, width=4)
        self.total_pg2_intake1.grid(row=3, column=1, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="GRAD-22:").grid(row=3, column=2, sticky="e", pady=5, padx=(2,1))
        self.total_pg2_passed1 = ttk.Entry(self, width=4)
        self.total_pg2_passed1.grid(row=3, column=3, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="IN-21:").grid(row=3, column=4, sticky="e", pady=5, padx=(2,1))
        self.total_pg2_intake2 = ttk.Entry(self, width=4)
        self.total_pg2_intake2.grid(row=3, column=5, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="GRAD-23:").grid(row=3, column=6, sticky="e", pady=5, padx=(2,1))
        self.total_pg2_passed2 = ttk.Entry(self, width=4)
        self.total_pg2_passed2.grid(row=3, column=7, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="IN-22:").grid(row=3, column=8, sticky="e", pady=5, padx=(2,1))
        self.total_pg2_intake3 = ttk.Entry(self, width=4)
        self.total_pg2_intake3.grid(row=3, column=9, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="GRAD-24:").grid(row=3, column=10, sticky="e", pady=5, padx=(2,1))
        self.total_pg2_passed3 = ttk.Entry(self, width=4)
        self.total_pg2_passed3.grid(row=3, column=11, pady=5, sticky="ew", padx=(1,2))
        
        # Row 1: All 6 fields alternating Intake and Graduated (PG-3)
        ttk.Label(self, text="IN-19:").grid(row=4, column=0, sticky="e", pady=5, padx=(2,1))
        self.total_pg3_intake1 = ttk.Entry(self, width=4)
        self.total_pg3_intake1.grid(row=4, column=1, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="GRAD-22:").grid(row=4, column=2, sticky="e", pady=5, padx=(2,1))
        self.total_pg3_passed1 = ttk.Entry(self, width=4)
        self.total_pg3_passed1.grid(row=4, column=3, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="IN-20:").grid(row=4, column=4, sticky="e", pady=5, padx=(2,1))
        self.total_pg3_intake2 = ttk.Entry(self, width=4)
        self.total_pg3_intake2.grid(row=4, column=5, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="GRAD-23:").grid(row=4, column=6, sticky="e", pady=5, padx=(2,1))
        self.total_pg3_passed2 = ttk.Entry(self, width=4)
        self.total_pg3_passed2.grid(row=4, column=7, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="IN-21:").grid(row=4, column=8, sticky="e", pady=5, padx=(2,1))
        self.total_pg3_intake3 = ttk.Entry(self, width=4)
        self.total_pg3_intake3.grid(row=4, column=9, pady=5, sticky="ew", padx=(1,2))
        
        ttk.Label(self, text="GRAD-24:").grid(row=4, column=10, sticky="e", pady=5, padx=(2,1))
        self.total_pg3_passed3 = ttk.Entry(self, width=4)
        self.total_pg3_passed3.grid(row=4, column=11, pady=5, sticky="ew", padx=(1,2))
        
        predict_btn = ttk.Button(self, text="Predict_GUI", command=self.predict_score)
        clear_btn = ttk.Button(self, text="Clear")
        
        clear_btn.grid(row=5, column=0, columnspan=6, sticky="ew", padx=10, pady=5)
        predict_btn.grid(row=5, column=6, columnspan=6, sticky="ew", padx=10, pady=5)
        
        self.output_entry = ttk.Entry(self, width=15, font=("Arial", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=6, column=0, columnspan=6, sticky="ew", padx=2)
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "GUI Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get GUI Recommendation", command=self.get_recommendation)
        recommend_btn.grid(row=6, column=6, columnspan=6, sticky="ew", padx=2)
        
    def predict_score(self):
        try:
            total_ug4_intake1 = float(self.total_ug4_intake1.get())
            total_ug4_passed1 = float(self.total_ug4_passed1.get())
            total_ug4_intake2 = float(self.total_ug4_intake2.get())
            total_ug4_passed2 = float(self.total_ug4_passed2.get())
            total_ug4_intake3 = float(self.total_ug4_intake3.get())
            total_ug4_passed3 = float(self.total_ug4_passed3.get())
            
            total_ug5_intake1 = float(self.total_ug5_intake1.get())
            total_ug5_passed1 = float(self.total_ug5_passed1.get())
            total_ug5_intake2 = float(self.total_ug5_intake2.get())
            total_ug5_passed2 = float(self.total_ug5_passed2.get())
            total_ug5_intake3 = float(self.total_ug5_intake3.get())
            total_ug5_passed3 = float(self.total_ug5_passed3.get())
            
            total_pg2_intake1 = float(self.total_pg2_intake1.get())
            total_pg2_passed1 = float(self.total_pg2_passed1.get())
            total_pg2_intake2 = float(self.total_pg2_intake2.get())
            total_pg2_passed2 = float(self.total_pg2_passed2.get())
            total_pg2_intake3 = float(self.total_pg2_intake3.get())
            total_pg2_passed3 = float(self.total_pg2_passed3.get())
            
            total_pg3_intake1 = float(self.total_pg3_intake1.get())
            total_pg3_passed1 = float(self.total_pg3_passed1.get())
            total_pg3_intake2 = float(self.total_pg3_intake2.get())
            total_pg3_passed2 = float(self.total_pg3_passed2.get())
            total_pg3_intake3 = float(self.total_pg3_intake3.get())
            total_pg3_passed3 = float(self.total_pg3_passed3.get())
            
            self.gue_score, self.total_intake, self.total_graduated, self.ng_percentage = predict_gue(
                total_ug4_intake1, total_ug4_passed1, total_ug4_intake2,
                total_ug4_passed2, total_ug4_intake3, total_ug4_passed3,
                total_ug5_intake1, total_ug5_passed1, total_ug5_intake2,
                total_ug5_passed2, total_ug5_intake3, total_ug5_passed3,
                total_pg2_intake1, total_pg2_passed1, total_pg2_intake2,
                total_pg2_passed2, total_pg2_intake3, total_pg2_passed3,
                total_pg3_intake1, total_pg3_passed1, total_pg3_intake2,
                total_pg3_passed2, total_pg3_intake3, total_pg3_passed3
            )
            
            # Store year-wise aggregations for recommendation
            self.intake_y1 = total_ug4_intake1 + total_ug5_intake1 + total_pg2_intake1 + total_pg3_intake1
            self.intake_y2 = total_ug4_intake2 + total_ug5_intake2 + total_pg2_intake2 + total_pg3_intake2
            self.intake_y3 = total_ug4_intake3 + total_ug5_intake3 + total_pg2_intake3 + total_pg3_intake3
            
            self.graduated_y1 = total_ug4_passed1 + total_ug5_passed1 + total_pg2_passed1 + total_pg3_passed1
            self.graduated_y2 = total_ug4_passed2 + total_ug5_passed2 + total_pg2_passed2 + total_pg3_passed2
            self.graduated_y3 = total_ug4_passed3 + total_ug5_passed3 + total_pg2_passed3 + total_pg3_passed3
            
            self.output_entry.config(state="normal")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, f"{self.gue_score}")
            self.output_entry.config(state="readonly")
        
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    def get_recommendation(self):
        # Check if prediction has been run
        if not hasattr(self, 'gue_score'):
            messagebox.showerror("Error", "Please predict GUE Score first.")
            return
        
        # Values dict for prompt - using stored instance variables
        values = {
            "gue_score": self.gue_score,
            "total_intake": self.total_intake,
            "total_graduated": self.total_graduated,
            "ng_percentage": round(self.ng_percentage, 2),
            "year_wise_intake": {
                "y1": self.intake_y1,
                "y2": self.intake_y2,
                "y3": self.intake_y3
            },
            "year_wise_graduated": {
                "y1": self.graduated_y1,
                "y2": self.graduated_y2,
                "y3": self.graduated_y3
            }
        }
        
        prompt = build_gue_prompt(values)
        self.gemini_frame.generate_recommendation(prompt)
            
            
            