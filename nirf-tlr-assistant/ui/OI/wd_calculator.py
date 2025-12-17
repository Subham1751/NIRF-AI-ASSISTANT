import tkinter as tk
from tkinter import ttk, messagebox
from input_scripts.OI.predict_wd import predict_wd
from helpers.OI_prompts.wd_prompt import build_prompt

class WDCalculatorFrame(ttk.LabelFrame):
    def set_gemini_frame(self, gemini_frame):
        self.gemini_frame = gemini_frame
    
    def __init__(self, parent):
        super().__init__(parent, text="WD Calculator", padding=10)
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
        
        btn_docs = ttk.Button(self, text="📘 WD Docs", style="Docs.TButton")
        btn_docs.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        # UG4 row - all three entries
        ttk.Label(self, text="UG4 Male:").grid(row=1, column=0, sticky="w", pady=5, padx=2)
        self.ug4_male_students = ttk.Entry(self, width=10)
        self.ug4_male_students.grid(row=1, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Female:").grid(row=1, column=2, sticky="w", pady=5, padx=2)
        self.ug4_female_students = ttk.Entry(self, width=10)
        self.ug4_female_students.grid(row=1, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Total:").grid(row=1, column=4, sticky="w", pady=5, padx=2)
        self.ug4_total_students = ttk.Entry(self, width=10)
        self.ug4_total_students.grid(row=1, column=5, pady=5, sticky="ew", padx=2)
        
        # UG5 row - all three entries
        ttk.Label(self, text="UG5 Male:").grid(row=2, column=0, sticky="w", pady=5, padx=2)
        self.ug5_male_students = ttk.Entry(self, width=10)
        self.ug5_male_students.grid(row=2, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Female:").grid(row=2, column=2, sticky="w", pady=5, padx=2)
        self.ug5_female_students = ttk.Entry(self, width=10)
        self.ug5_female_students.grid(row=2, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Total:").grid(row=2, column=4, sticky="w", pady=5, padx=2)
        self.ug5_total_students = ttk.Entry(self, width=10)
        self.ug5_total_students.grid(row=2, column=5, pady=5, sticky="ew", padx=2)
        
        # PG2 row - all three entries
        ttk.Label(self, text="PG2 Male:").grid(row=3, column=0, sticky="w", pady=5, padx=2)
        self.pg2_male_students = ttk.Entry(self, width=10)
        self.pg2_male_students.grid(row=3, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Female:").grid(row=3, column=2, sticky="w", pady=5, padx=2)
        self.pg2_female_students = ttk.Entry(self, width=10)
        self.pg2_female_students.grid(row=3, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Total:").grid(row=3, column=4, sticky="w", pady=5, padx=2)
        self.pg2_total_students = ttk.Entry(self, width=10)
        self.pg2_total_students.grid(row=3, column=5, pady=5, sticky="ew", padx=2)
        
        predict_btn = ttk.Button(self, text="Predict_WD", command=self.predict_score)
        clear_btn = ttk.Button(self, text="Clear", command=self.clear_fields)
        
        clear_btn.grid(row=4, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
        predict_btn.grid(row=4, column=3, columnspan=3, sticky="ew", padx=10, pady=5)
        
        self.output_entry = ttk.Entry(self, width=15, font=("Ariel", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=5, column=0, columnspan=3, sticky="ew", padx=2)
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "WD Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get WD Recommendation", command=self.get_recommendation)
        recommend_btn.grid(row=5, column=3, columnspan=3, sticky="ew", padx=2)
        
    def predict_score(self):
        try:
            ug4_male = float(self.ug4_male_students.get())
            ug4_female = float(self.ug4_female_students.get())
            ug4_total = float(self.ug4_total_students.get())
            
            ug5_male = float(self.ug5_male_students.get())
            ug5_female = float(self.ug4_female_students.get())
            ug5_total = float(self.ug5_total_students.get())
            
            pg2_male = float(self.pg2_male_students.get())
            pg2_female = float(self.pg2_female_students.get())
            pg2_total = float(self.pg2_total_students.get())
            
            wd_score = predict_wd(
                ug4_male, ug4_female, ug4_total,
                ug5_male, ug5_female, ug5_total,
                pg2_male, pg2_female, pg2_total,
            )
            
            self.output_entry.config(state="normal")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, f"{wd_score}")
            self.output_entry.config(state="readonly")
            
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    def get_recommendation(self):
        try:
            ug4_male = float(self.ug4_male_students.get())
            ug4_female = float(self.ug4_female_students.get())
            ug4_total = float(self.ug4_total_students.get())
            
            ug5_male = float(self.ug5_male_students.get())
            ug5_female = float(self.ug4_female_students.get())
            ug5_total = float(self.ug5_total_students.get())
            
            pg2_male = float(self.pg2_male_students.get())
            pg2_female = float(self.pg2_female_students.get())
            pg2_total = float(self.pg2_total_students.get())
        except ValueError:
            messagebox.showerror("Input Error", "Enter valid numbers")
            return
        
        if not self.gemini_frame:
            messagebox.showerror("Gemini Error", "Gemini frame not connected.")
            return
        
        wd_score_text = self.output_entry.get().strip()
        try:
            wd_score = float(wd_score_text)
        except ValueError:
            messagebox.showerror("Error", "Please predict WD Score first.")
            return
        
        values = {
            "ug4_male": ug4_male,
            "ug4_female": ug4_female,
            "ug4_total": ug4_total,
            "ug5_male": ug5_male,
            "ug5_female": ug5_female,
            "ug5_total": ug5_total,
            "pg2_male": pg2_male,
            "pg2_female": pg2_female,
            "pg2_total": pg2_total,
            "wd_score": wd_score,
        }
        
        prompt = build_prompt(values)
        self.gemini_frame.generate_recommendation(prompt)
    
    def clear_fields(self):
        self.ug4_male_students.delete(0, tk.END)
        self.ug4_female_students.delete(0, tk.END)
        self.ug4_total_students.delete(0, tk.END)
        self.ug5_male_students.delete(0, tk.END)
        self.ug5_female_students.delete(0, tk.END)
        self.ug5_total_students.delete(0, tk.END)
        self.pg2_male_students.delete(0, tk.END)
        self.pg2_female_students.delete(0, tk.END)
        self.pg2_total_students.delete(0, tk.END)
        self.output_entry.config(state="normal", foreground="gray")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, "WD Score will appear here")
        self.output_entry.config(state="readonly")