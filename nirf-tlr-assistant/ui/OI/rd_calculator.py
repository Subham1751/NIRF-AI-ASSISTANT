import tkinter as tk
from tkinter import ttk, messagebox
from input_scripts.OI.predict_rd import predict_rd
from helpers.OI_prompts.rd_prompt import build_prompt

class RDCalculatorFrame(ttk.LabelFrame):
    def set_gemini_frame(self, gemini_frame):
        self.gemini_frame = gemini_frame
    
    def __init__(self, parent):
        super().__init__(parent, text="RD Calculator", padding=10)
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
        
        btn_docs = ttk.Button(self, text="📘 RD Docs", style="Docs.TButton")
        btn_docs.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        # Row 1: UG4 OutState, UG5 OutState, PG2 OutState
        ttk.Label(self, text="UG4 OutS:").grid(row=1, column=0, sticky="w", pady=5, padx=2)
        self.ug4_out_state = ttk.Entry(self, width=10)
        self.ug4_out_state.grid(row=1, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="UG5 OutS:").grid(row=1, column=2, sticky="w", pady=5, padx=2)
        self.ug5_out_state = ttk.Entry(self, width=10)
        self.ug5_out_state.grid(row=1, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="PG2 OutS:").grid(row=1, column=4, sticky="w", pady=5, padx=2)
        self.pg2_out_state = ttk.Entry(self, width=10)
        self.pg2_out_state.grid(row=1, column=5, pady=5, sticky="ew", padx=2)
        
        # Row 2: UG4 OutCountry, UG5 OutCountry, PG2 OutCountry
        ttk.Label(self, text="UG4 OutC:").grid(row=2, column=0, sticky="w", pady=5, padx=2)
        self.ug4_out_country = ttk.Entry(self, width=10)
        self.ug4_out_country.grid(row=2, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="UG5 OutC:").grid(row=2, column=2, sticky="w", pady=5, padx=2)
        self.ug5_out_country = ttk.Entry(self, width=10)
        self.ug5_out_country.grid(row=2, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="PG2 OutC:").grid(row=2, column=4, sticky="w", pady=5, padx=2)
        self.pg2_out_country = ttk.Entry(self, width=10)
        self.pg2_out_country.grid(row=2, column=5, pady=5, sticky="ew", padx=2)
        
        # Row 3: UG4 Total, UG5 Total, PG2 Total
        ttk.Label(self, text="UG4 Tot:").grid(row=3, column=0, sticky="w", pady=5, padx=2)
        self.ug4_total_students = ttk.Entry(self, width=10)
        self.ug4_total_students.grid(row=3, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="UG5 Tot:").grid(row=3, column=2, sticky="w", pady=5, padx=2)
        self.ug5_total_students = ttk.Entry(self, width=10)
        self.ug5_total_students.grid(row=3, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="PG2 Tot:").grid(row=3, column=4, sticky="w", pady=5, padx=2)
        self.pg2_total_students = ttk.Entry(self, width=10)
        self.pg2_total_students.grid(row=3, column=5, pady=5, sticky="ew", padx=2)
        
        # Row 4: Buttons
        predict_btn = ttk.Button(self, text="Predict RD", command=self.predict_score)
        clear_btn = ttk.Button(self, text="Clear", command=self.clear_fields)
        
        clear_btn.grid(row=4, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
        predict_btn.grid(row=4, column=3, columnspan=3, sticky="ew", padx=10, pady=5)
        
        # Row 5: Output and Recommendation
        self.output_entry = ttk.Entry(self, width=15, font=("Arial", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=5, column=0, columnspan=3, sticky="ew", padx=2)
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "RD Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get RD Recommendation", command=self.get_recommendation)
        recommend_btn.grid(row=5, column=3, columnspan=3, sticky="ew", padx=2)
    
    def predict_score(self):
        try:
            ug4_out_state = float(self.ug4_out_state.get())
            ug5_out_state = float(self.ug5_out_state.get())
            pg2_out_state = float(self.pg2_out_state.get())
            
            ug4_out_country = float(self.ug4_out_country.get())
            ug5_out_country = float(self.ug5_out_country.get())
            pg2_out_country = float(self.pg2_out_country.get())
            
            ug4_tot_students = float(self.ug4_total_students.get())
            ug5_tot_students = float(self.ug5_total_students.get())
            pg2_tot_studnts = float(self.pg2_total_students.get())
            
            rd_score = predict_rd(
                ug4_out_state, ug5_out_state, pg2_out_state,
                ug4_out_country, ug5_out_country, pg2_out_country,
                ug4_tot_students, ug5_tot_students, pg2_tot_studnts
            )
            
            self.output_entry.config(state="normal")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, f"{rd_score}")
            self.output_entry.config(state="readonly")
            
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    def get_recommendation(self):
        try:
            ug4_out_state = float(self.ug4_out_state.get())
            ug5_out_state = float(self.ug5_out_state.get())
            pg2_out_state = float(self.pg2_out_state.get())
            
            ug4_out_country = float(self.ug4_out_country.get())
            ug5_out_country = float(self.ug5_out_country.get())
            pg2_out_country = float(self.pg2_out_country.get())
            
            ug4_tot_students = float(self.ug4_total_students.get())
            ug5_tot_students = float(self.ug5_total_students.get())
            pg2_tot_studnts = float(self.pg2_total_students.get())
        except ValueError:
            messagebox.showerror("Input Error", "Enter valid numbers")
            return
        
        if not self.gemini_frame:
            messagebox.showerror("Gemini Error", "Gemini frame not connected")
            return
        
        rd_score_text = self.output_entry.get().strip()
        try:
            rd_score = float(rd_score_text)
        except ValueError:
            messagebox.showerror("Error", "Please predict RD Score first.")
            return
        
        values = {
            "ug4_out_state": ug4_out_state,
            "ug5_out_state": ug5_out_state,
            "pg2_out_state": pg2_out_state,
            "ug4_out_country": ug4_out_country,
            "ug5_out_country": ug5_out_country,
            "pg2_out_country": pg2_out_country,
            "ug4_tot_students": ug4_tot_students,
            "ug5_tot_students": ug5_tot_students,
            "pg2_tot_students": pg2_tot_studnts,
            "rd_score": rd_score
        }
        
        prompt = build_prompt(values)
        self.gemini_frame.generate_recommendation(prompt)
            
    def clear_fields(self):
        self.ug4_out_state.delete(0, tk.END)
        self.ug5_out_state.delete(0, tk.END)
        self.pg2_out_state.delete(0, tk.END)
        self.ug4_out_country.delete(0, tk.END)
        self.ug5_out_country.delete(0, tk.END)
        self.pg2_out_country.delete(0, tk.END)
        self.ug4_total_students.delete(0, tk.END)
        self.ug5_total_students.delete(0, tk.END)
        self.pg2_total_students.delete(0, tk.END)
        self.output_entry.config(state="normal", foreground="gray")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, "RD Score will appear here")
        self.output_entry.config(state="readonly")