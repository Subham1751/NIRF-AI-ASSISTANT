import tkinter as tk
from tkinter import ttk, messagebox
from helpers.GO_prompts.GMS_prompt import build_prompt
from input_scripts.GO.predict_gms import predict_gms

class GMSCalculatorFrame(ttk.LabelFrame):
    def set_gemini_frame(self, gemini_frame):
        self.gemini_frame = gemini_frame
        
    def __init__(self, parent):
        super().__init__(parent, text="GMS Calculator", padding=10)
        self.gemini_frame = None
        
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
        
        btn_docs = ttk.Button(self, text="📘 GMS Docs", style="Docs.TButton")
        btn_docs.grid(row=0, column=0, columnspan=6, sticky="ew")
    
        ttk.Label(self, text="UG4-MS(21-22): ").grid(row=1, column=0, sticky="w", pady=5, padx=2)
        self.ug4_ms_21_total_entry = ttk.Entry(self, width=10)
        self.ug4_ms_21_total_entry.grid(row=1, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="UG4-MS(22-23): ").grid(row=1, column=2, sticky="w", pady=5, padx=2)
        self.ug4_ms_22_total_entry = ttk.Entry(self, width=10)
        self.ug4_ms_22_total_entry.grid(row=1, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="UG4-MS(23-24): ").grid(row=1, column=4, sticky="w", pady=5, padx=2)
        self.ug4_ms_23_total_entry = ttk.Entry(self, width=10)
        self.ug4_ms_23_total_entry.grid(row=1, column=5, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="UG5-MS(21-22): ").grid(row=2, column=0, sticky="w", pady=5, padx=2)
        self.ug5_ms_21_total_entry = ttk.Entry(self, width=10)
        self.ug5_ms_21_total_entry.grid(row=2, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="UG5-MS(22-23): ").grid(row=2, column=2, sticky="w", pady=5, padx=2)
        self.ug5_ms_22_total_entry = ttk.Entry(self, width=10)
        self.ug5_ms_22_total_entry.grid(row=2, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="UG5-MS(23-24): ").grid(row=2, column=4, sticky="w", pady=5, padx=2)
        self.ug5_ms_23_total_entry = ttk.Entry(self, width=10)
        self.ug5_ms_23_total_entry.grid(row=2, column=5, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="PG2-MS(21-22): ").grid(row=3, column=0, sticky="w", pady=5, padx=2)
        self.pg2_ms_21_total_entry = ttk.Entry(self, width=10)
        self.pg2_ms_21_total_entry.grid(row=3, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="PG2-MS(22-23): ").grid(row=3, column=2, sticky="w", pady=5, padx=2)
        self.pg2_ms_22_total_entry = ttk.Entry(self, width=10)
        self.pg2_ms_22_total_entry.grid(row=3, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="PG2-MS(23-24): ").grid(row=3, column=4, sticky="w", pady=5, padx=2)
        self.pg2_ms_23_total_entry = ttk.Entry(self, width=10)
        self.pg2_ms_23_total_entry.grid(row=3, column=5, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="PG3-MS(21-22): ").grid(row=4, column=0, sticky="w", pady=5, padx=2)
        self.pg3_ms_21_total_entry = ttk.Entry(self, width=10)
        self.pg3_ms_21_total_entry.grid(row=4, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="PG3-MS(22-23): ").grid(row=4, column=2, sticky="w", pady=5, padx=2)
        self.pg3_ms_22_total_entry = ttk.Entry(self, width=10)
        self.pg3_ms_22_total_entry.grid(row=4, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="PG3-MS(23-24): ").grid(row=4, column=4, sticky="w", pady=5, padx=2)
        self.pg3_ms_23_total_entry = ttk.Entry(self, width=10)
        self.pg3_ms_23_total_entry.grid(row=4, column=5, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="PG5-MS(21-22): ").grid(row=5, column=0, sticky="w", pady=5, padx=2)
        self.pg5_ms_21_total_entry = ttk.Entry(self, width=10)
        self.pg5_ms_21_total_entry.grid(row=5, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="PG5-MS(22-23): ").grid(row=5, column=2, sticky="w", pady=5, padx=2)
        self.pg5_ms_22_total_entry = ttk.Entry(self, width=10)
        self.pg5_ms_22_total_entry.grid(row=5, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="PG5-MS(23-24): ").grid(row=5, column=4, sticky="w", pady=5, padx=2)
        self.pg5_ms_23_total_entry = ttk.Entry(self, width=10)
        self.pg5_ms_23_total_entry.grid(row=5, column=5, pady=5, sticky="ew", padx=2)
        
        predict_btn = ttk.Button(self, text="Predict_GMS", command=self.predict_score)
        clear_btn = ttk.Button(self, text="Clear", command=self.clear_fields)
        
        clear_btn.grid(row=6, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
        predict_btn.grid(row=6, column=3, columnspan=3, sticky="ew", padx=10, pady=5)
        
        self.output_entry = ttk.Entry(self, width=15, font=("Arial", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=7, column=0, columnspan=3, sticky="ew", padx=2)
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "GMS Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get GMS Recommendation", command=self.get_recommendation)
        recommend_btn.grid(row=7, column=3, columnspan=3, sticky="ew", padx=2)
    
    def predict_score(self):
        try:
            ug4_ms_21 = float(self.ug4_ms_21_total_entry.get())
            ug4_ms_22 = float(self.ug4_ms_22_total_entry.get())
            ug4_ms_23 = float(self.ug4_ms_23_total_entry.get())
            
            ug5_ms_21 = float(self.ug5_ms_21_total_entry.get())
            ug5_ms_22 = float(self.ug5_ms_22_total_entry.get())
            ug5_ms_23 = float(self.ug5_ms_23_total_entry.get())
            
            pg2_ms_21 = float(self.pg2_ms_21_total_entry.get())
            pg2_ms_22 = float(self.pg2_ms_22_total_entry.get())
            pg2_ms_23 = float(self.pg2_ms_23_total_entry.get())
            
            pg3_ms_21 = float(self.pg3_ms_21_total_entry.get())
            pg3_ms_22 = float(self.pg3_ms_22_total_entry.get())
            pg3_ms_23 = float(self.pg3_ms_23_total_entry.get())
            
            pg5_ms_21 = float(self.pg5_ms_21_total_entry.get())
            pg5_ms_22 = float(self.pg5_ms_22_total_entry.get())
            pg5_ms_23 = float(self.pg5_ms_23_total_entry.get())
            
            gms_score = predict_gms(
                ug4_ms_21, ug4_ms_22, ug4_ms_23,
                ug5_ms_21, ug5_ms_22, ug5_ms_23,
                pg2_ms_21, pg2_ms_22, pg2_ms_23,
                pg3_ms_21, pg3_ms_22, pg3_ms_23,
                pg5_ms_21, pg5_ms_22, pg5_ms_23
            )
            
            self.output_entry.config(state="normal")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, f"{gms_score}")
            self.output_entry.config(state="readonly")
        
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    def get_recommendation(self):
        try:
            ug4_ms_21 = float(self.ug4_ms_21_total_entry.get())
            ug4_ms_22 = float(self.ug4_ms_22_total_entry.get())
            ug4_ms_23 = float(self.ug4_ms_23_total_entry.get())
            
            ug5_ms_21 = float(self.ug5_ms_21_total_entry.get())
            ug5_ms_22 = float(self.ug5_ms_22_total_entry.get())
            ug5_ms_23 = float(self.ug5_ms_23_total_entry.get())
            
            pg2_ms_21 = float(self.pg2_ms_21_total_entry.get())
            pg2_ms_22 = float(self.pg2_ms_22_total_entry.get())
            pg2_ms_23 = float(self.pg2_ms_23_total_entry.get())
            
            pg3_ms_21 = float(self.pg3_ms_21_total_entry.get())
            pg3_ms_22 = float(self.pg3_ms_22_total_entry.get())
            pg3_ms_23 = float(self.pg3_ms_23_total_entry.get())
            
            pg5_ms_21 = float(self.pg5_ms_21_total_entry.get())
            pg5_ms_22 = float(self.pg5_ms_22_total_entry.get())
            pg5_ms_23 = float(self.pg5_ms_23_total_entry.get())
            
        except ValueError:
            messagebox.showerror("Input Error", "Enter valid numbers.")
            return
        
        if not self.gemini_frame:
            messagebox.showerror("Gemini Error", "Gemini frame not connected.")
            return
        
        gms_score_text = self.output_entry.get().strip()
        try:
            gms_score = float(gms_score_text)
        except ValueError:
            messagebox.showerror("Error", "Please predict GMS Score first.")
            return
        
        values = {
            "ug4_ms_21": ug4_ms_21,
            "ug4_ms_22": ug4_ms_22,
            "ug4_ms_23": ug4_ms_23,
            "ug5_ms_21": ug5_ms_21,
            "ug5_ms_22": ug5_ms_22,
            "ug5_ms_23": ug5_ms_23,
            "pg2_ms_21": pg2_ms_21,
            "pg2_ms_22": pg2_ms_22,
            "pg2_ms_23": pg2_ms_23,
            "pg3_ms_21": pg3_ms_21,
            "pg3_ms_22": pg3_ms_22,
            "pg3_ms_23": pg3_ms_23,
            "pg5_ms_21": pg5_ms_21,
            "pg5_ms_22": pg5_ms_22,
            "pg5_ms_23": pg5_ms_23,
            "gms_score": gms_score
        }
        
        prompt = build_prompt(values)
        self.gemini_frame.generate_recommendation(prompt)
    
    def clear_fields(self):
        self.ug4_ms_21_total_entry.delete(0, tk.END)
        self.ug4_ms_22_total_entry.delete(0, tk.END)
        self.ug4_ms_23_total_entry.delete(0, tk.END)
        self.ug5_ms_21_total_entry.delete(0, tk.END)
        self.ug5_ms_22_total_entry.delete(0, tk.END)
        self.ug5_ms_23_total_entry.delete(0, tk.END)
        self.pg2_ms_21_total_entry.delete(0, tk.END)
        self.pg2_ms_22_total_entry.delete(0, tk.END)
        self.pg2_ms_23_total_entry.delete(0, tk.END)
        self.pg3_ms_21_total_entry.delete(0, tk.END)
        self.pg3_ms_22_total_entry.delete(0, tk.END)
        self.pg3_ms_23_total_entry.delete(0, tk.END)
        self.pg5_ms_21_total_entry.delete(0, tk.END)
        self.pg5_ms_22_total_entry.delete(0, tk.END)
        self.pg5_ms_23_total_entry.delete(0, tk.END)
        self.output_entry.delete(0, tk.END)