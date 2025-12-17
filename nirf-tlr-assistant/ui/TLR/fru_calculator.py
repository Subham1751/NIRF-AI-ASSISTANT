import tkinter as tk
from tkinter import ttk, messagebox
from loaders.stats_loader import load_fru_medians
from helpers.SS_prompts.fru_prompt import build_prompt
from input_scripts.SS.predict_fru import load_model, predict_fru

class FRUCalculatorFrame(ttk.LabelFrame):
    def set_gemini_frame(self, gemini_frame):
        self.gemini_frame = gemini_frame
    
    def __init__(self, parent):
        super().__init__(parent, text="FRU Calculator", padding=10)
        self.model = load_model()
        self.gemini_frame = None
        self.medians = load_fru_medians()
        
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
    
        btn_docs = ttk.Button(self, text="📘 FRU Docs", style="Docs.TButton")
        btn_docs.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        # Row 1: TS1, TS2, TS3 in same row
        ttk.Label(self, text="TS1(23-24):").grid(row=1, column=0, sticky="w", pady=5, padx=2)
        self.ts1_entry = ttk.Entry(self, width=10)
        self.ts1_entry.grid(row=1, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="TS2(22-23):").grid(row=1, column=2, sticky="w", pady=5, padx=2)
        self.ts2_entry = ttk.Entry(self, width=10)
        self.ts2_entry.grid(row=1, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="TS3(21-22):").grid(row=1, column=4, sticky="w", pady=5, padx=2)
        self.ts3_entry = ttk.Entry(self, width=10)
        self.ts3_entry.grid(row=1, column=5, pady=5, sticky="ew", padx=2)
        
        # Row 2: CE1, CE2, CE3 in same row
        ttk.Label(self, text="CE1(23-24):").grid(row=2, column=0, sticky="w", pady=5, padx=2)
        self.ce1_total_entry = ttk.Entry(self, width=10)
        self.ce1_total_entry.grid(row=2, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="CE2(22-23):").grid(row=2, column=2, sticky="w", pady=5, padx=2)
        self.ce2_total_entry = ttk.Entry(self, width=10)
        self.ce2_total_entry.grid(row=2, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="CE3(21-22):").grid(row=2, column=4, sticky="w", pady=5, padx=2)
        self.ce3_total_entry = ttk.Entry(self, width=10)
        self.ce3_total_entry.grid(row=2, column=5, pady=5, sticky="ew", padx=2)
        
        # Row 3: OE1, OE2, OE3 in same row
        ttk.Label(self, text="OE1(23-24):").grid(row=3, column=0, sticky="w", pady=5, padx=2)
        self.oe1_total_entry = ttk.Entry(self, width=10)
        self.oe1_total_entry.grid(row=3, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="OE2(22-23):").grid(row=3, column=2, sticky="w", pady=5, padx=2)
        self.oe2_total_entry = ttk.Entry(self, width=10)
        self.oe2_total_entry.grid(row=3, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="OE3(21-22):").grid(row=3, column=4, sticky="w", pady=5, padx=2)
        self.oe3_total_entry = ttk.Entry(self, width=10)
        self.oe3_total_entry.grid(row=3, column=5, pady=5, sticky="ew", padx=2)
        
        predict_btn = ttk.Button(self, text="Predict FRU", command=self.predict_score)
        clear_btn = ttk.Button(self, text="Clear", command=self.clear_fields)
        
        clear_btn.grid(row=4, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
        predict_btn.grid(row=4, column=3, columnspan=3, sticky="ew", padx=10, pady=5)
        
        self.output_entry = ttk.Entry(self, width=15, font=("Arial", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=5, column=0, columnspan=3, sticky="ew", padx=2)
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "FRU Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get FRU Recommendation", command=self.get_recommendation)
        recommend_btn.grid(row=5, column=3, columnspan=3, sticky="ew", padx=2)
        
    def predict_score(self):
        try:
            ts1 = float(self.ts1_entry.get())
            ts2 = float(self.ts2_entry.get())
            ts3 = float(self.ts3_entry.get())
            ce1 = float(self.ce1_total_entry.get())
            ce2 = float(self.ce2_total_entry.get())
            ce3 = float(self.ce3_total_entry.get())
            o1 = float(self.oe1_total_entry.get())
            o2 = float(self.oe2_total_entry.get())
            o3 = float(self.oe3_total_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Enter valid numbers.")
            return
        
        if self.model is None:
            messagebox.showerror("Model Error", "FRU Model not found.")
            return
            
        try:
            fru_score, bc, bo = predict_fru(self.model,ts1, ts2, ts3, ce1, ce2, ce3, o1, o2, o3)
            self.fru_score = fru_score
            self.bc = bc
            self.bo = bo
            self.output_entry.config(state="normal", foreground="white")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, str(fru_score))
            self.output_entry.config(state="readonly")
        except Exception as e:
            messagebox.showerror("Prediction Error", str(e))
    
    def get_recommendation(self):
        try:
            ts1 = float(self.ts1_entry.get())
            ts2 = float(self.ts2_entry.get())
            ts3 = float(self.ts3_entry.get())
            ce1 = float(self.ce1_total_entry.get())
            ce2 = float(self.ce2_total_entry.get())
            ce3 = float(self.ce3_total_entry.get())
            o1 = float(self.oe1_total_entry.get())
            o2 = float(self.oe2_total_entry.get())
            o3 = float(self.oe3_total_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Enter valid numbers.")
            return
        
        if not self.gemini_frame:
            messagebox.showerror("Gemini Error", "Gemini frame not conencted.")
            return
        
        fru_score_text = self.output_entry.get().strip()
        try:
            fru_score = float(fru_score_text)
        except ValueError:
            messagebox.showerror("Error", "Please predict FRU Score first.")
            return
        
        values = {
            # Predicted & derived metrics
            "fru_score": self.fru_score,
            "bc": self.bc,
            "bo": self.bo,
            
            # Median benchmarks (from stats_loader)
            "medians": {
                "median_fru": self.medians["median_FRU"],
                "median_bc": self.medians["median_BC"],
                "median_bo": self.medians["median_BO"],
                
                "median_library_share": self.medians["median_library_share"],
                "median_lab_share": self.medians["median_lab_share"],
                "median_workshop_share": self.medians["median_workshop_share"],
                "median_other_capex_share": self.medians["median_other_capex_share"],
                
                "median_salary_share": self.medians["median_salary_share"],
                "median_infra_share": self.medians["median_infra_share"],
                "median_seminar_share": self.medians["median_seminar_share"],
            },
            
            # Student counts
            "students": {
                "2023-24": ts1,
                "2022-23": ts2,
                "2021-22": ts3,
            },
            
            # Capital expenditur (year wise)
            "capital_expenditure": {
                "total": {
                    "2023-24": ce1,
                    "2022-23": ce2,
                    "2021-22": ce3,
                },
            },
            
            # Operational expenditure (year-wise)
            "operational_expenditure": {
                "total": {
                    "2023-24": o1,
                    "2022-23": o2,
                    "2021-22": o3,
                }
            }
        }
        
        prompt = build_prompt(values)
        self.gemini_frame.generate_recommendation(prompt)
            
    def clear_fields(self):
        self.ce1_total_entry.delete(0, tk.END)
        self.ce2_total_entry.delete(0, tk.END)
        self.ce3_total_entry.delete(0, tk.END)
        self.oe1_total_entry.delete(0, tk.END)
        self.oe2_total_entry.delete(0, tk.END)
        self.oe3_total_entry.delete(0, tk.END)
        self.ts1_entry.delete(0, tk.END)
        self.ts2_entry.delete(0, tk.END)
        self.ts3_entry.delete(0, tk.END)
        self.output_entry.config(state="normal", foreground="gray")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, "FRU Score will appear here")
        self.output_entry.config(state="readonly")