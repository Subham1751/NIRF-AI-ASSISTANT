import tkinter as tk
from tkinter import ttk, messagebox
from input_scripts.GO.predict_gphd import predict_gphd
from helpers.GO_prompts.GPHD_prompt import build_prompt

class GPHDCalculatorFrame(ttk.LabelFrame):
    def set_gemini_frame(self, gemini_frame):
        self.gemini_frame = gemini_frame
        
    def __init__(self, parent):
        super().__init__(parent, text="GPHD Calculator", padding=10)
        
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
        
        btn_docs = ttk.Button(self, text="📘 GPHD Docs", style="Docs.TButton")
        btn_docs.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        # Row-1: All three Intake fields
        ttk.Label(self, text="Tot_FullPhD_23: ").grid(row=1, column=0, sticky="w", pady=5, padx=2)
        self.total_fphd_23 = ttk.Entry(self, width=10)
        self.total_fphd_23.grid(row=1, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Tot_FullPHD_22: ").grid(row=1, column=2, sticky="w", pady=5, padx=2)
        self.total_fphd_22 = ttk.Entry(self, width=10)
        self.total_fphd_22.grid(row=1, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Tot_FullPHD_21: ").grid(row=1, column=4, sticky="w", pady=5, padx=2)
        self.total_fphd_21 = ttk.Entry(self, width=10)
        self.total_fphd_21.grid(row=1, column=5, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Tot_PartPhD_23: ").grid(row=2, column=0, sticky="w", pady=5, padx=2)
        self.total_pphd_23 = ttk.Entry(self, width=10)
        self.total_pphd_23.grid(row=2, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Tot_PartPHD_22: ").grid(row=2, column=2, sticky="w", pady=5, padx=2)
        self.total_pphd_22 = ttk.Entry(self, width=10)
        self.total_pphd_22.grid(row=2, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Tot_PartPHD_21: ").grid(row=2, column=4, sticky="w", pady=5, padx=2)
        self.total_pphd_21 = ttk.Entry(self, width=10)
        self.total_pphd_21.grid(row=2, column=5, pady=5, sticky="ew", padx=2)
        
        predict_btn = ttk.Button(self, text="Predict_GPHD", command=self.predict_score)
        clear_btn = ttk.Button(self, text="Clear", command=self.clear_fields)
        
        clear_btn.grid(row=3, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
        predict_btn.grid(row=3, column=3, columnspan=3, sticky="ew", padx=10, pady=5)
        
        self.output_entry = ttk.Entry(self, width=15, font=("Arial", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=4, column=0, columnspan=3, sticky="ew", padx=2)
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "GPHD Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get GPHD Recommendation", command=self.get_recommendation)
        recommend_btn.grid(row=4, column=3, columnspan=3, sticky="ew", padx=2)
        
    def predict_score(self):
        try:
            tot_fphd_23 = float(self.total_fphd_23.get())
            tot_fphd_22 = float(self.total_fphd_22.get())
            tot_fphd_21 = float(self.total_fphd_21.get())
            tot_pphd_23 = float(self.total_pphd_23.get())
            tot_pphd_22 = float(self.total_pphd_22.get())
            tot_pphd_21 = float(self.total_pphd_21.get())
            
            gphd_score = predict_gphd(
                tot_fphd_23, tot_fphd_22, tot_fphd_21,
                tot_pphd_23, tot_pphd_22, tot_pphd_21
            )
            
            self.output_entry.config(state="normal")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, f"{gphd_score}")
            self.output_entry.config(state="readonly")
        
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    def get_recommendation(self):
        try:
            tot_fphd_23 = float(self.total_fphd_23.get())
            tot_fphd_22 = float(self.total_fphd_22.get())
            tot_fphd_21 = float(self.total_fphd_21.get())
            tot_pphd_23 = float(self.total_pphd_23.get())
            tot_pphd_22 = float(self.total_pphd_22.get())
            tot_pphd_21 = float(self.total_pphd_21.get())
            
        except ValueError:
            messagebox.showerror("Input Error", "Enter valid numbers")
            return
        
        if not self.gemini_frame:
            messagebox.showerror("Gemini Error", "Gemini frame not connected")
            return
        
        gphd_score_text = self.output_entry.get().strip()
        try:
            gphd_score = float(gphd_score_text)
        except ValueError:
            messagebox.showerror("Error", "Please predict GPHD Score first")
            return
        
        values = {
            'tot_fphd_23': tot_fphd_23,
            'tot_fphd_22': tot_fphd_22,
            'tot_fphd_21': tot_fphd_21,
            'tot_pphd_23': tot_pphd_23,
            'tot_pphd_22': tot_pphd_22,
            'tot_pphd_21': tot_pphd_21,
            'gphd_score': gphd_score
        }
        
        prompt = build_prompt(values)
        self.gemini_frame.generate_recommendation(prompt)
    
    def clear_fields(self):
        self.total_fphd_23.delete(0, tk.END)
        self.total_fphd_22.delete(0, tk.END)
        self.total_fphd_21.delete(0, tk.END)
        self.total_pphd_23.delete(0, tk.END)
        self.total_pphd_22.delete(0, tk.END)
        self.total_pphd_21.delete(0, tk.END)
        self.output_entry.delete(0, tk.END)
        