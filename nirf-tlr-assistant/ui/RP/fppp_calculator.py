import tkinter as tk
from tkinter import ttk, messagebox
from input_scripts.RP.predict_fppp import predict_fppp
from helpers.RP_prompts.FPPP_prompt import build_prompt

class FPPPCalculatorFrame(ttk.LabelFrame):
    def set_gemini_frame(self, gemini_frame):
        self.gemini_frame = gemini_frame
    
    def __init__(self, parent):
        super().__init__(parent, text="FPPP Calculator", padding=10)
        self.gemini_frame = None
        
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
        predict_btn = ttk.Button(self, text="Predict FPPP", command=self.predict_score)
        clear_btn = ttk.Button(self, text="Clear")
        
        clear_btn.grid(row=4, column=0, columnspan=3, sticky="ew", padx=2, pady=5)
        predict_btn.grid(row=4, column=3, columnspan=3, sticky="ew", padx=2, pady=5)
        
        # Row 5: Output and recommendation
        self.output_entry = ttk.Entry(self, width=15, font=("Arial", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=5, column=0, columnspan=3, sticky="ew", padx=2, pady=(0, 15))
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "FPPP Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get FPPP Recommendation", command=self.get_recommendation)
        recommend_btn.grid(row=5, column=3, columnspan=3, sticky="ew", padx=2, pady=(0, 15))
    
    def predict_score(self):
        try:
            spon_amt_24 = float(self.spon_amt_24_23.get())
            spon_amt_23 = float(self.spon_amt_23_22.get())
            spon_amt_22 = float(self.spon_amt_22_21.get())
            
            consul_amt_24 = float(self.consul_amt_24_23.get())
            consul_amt_23 = float(self.consul_amt_23_22.get())
            consul_amt_22 = float(self.consul_amt_22_21.get())
            
            total_fac = int(self.tot_fac.get())
            
            fppp_score = predict_fppp(
                spon_amt_24, spon_amt_23, spon_amt_22, consul_amt_24,
                consul_amt_23, consul_amt_22, total_fac
            )
            
            self.output_entry.config(state="normal")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, f"{fppp_score}")
            self.output_entry.config(state="readonly")
        
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    def get_recommendation(self):
        try:
            spon_amt_24 = float(self.spon_amt_24_23.get())
            spon_amt_23 = float(self.spon_amt_23_22.get())
            spon_amt_22 = float(self.spon_amt_22_21.get())
            
            consul_amt_24 = float(self.consul_amt_24_23.get())
            consul_amt_23 = float(self.consul_amt_23_22.get())
            consul_amt_22 = float(self.consul_amt_22_21.get())
            
            total_fac = int(self.tot_fac.get())
        
        except ValueError:
            messagebox.showerror("Input Error", "Enter valid numbers.")
            return
        
        if not self.gemini_frame:
            messagebox.showerror("Gemini Error", "Gemini frame not connected.")
            return
        
        fppp_score_text = self.output_entry.get().strip()
        try:
            fppp_score = float(fppp_score_text)
        except ValueError:
            messagebox.showerror("Error", "Please predict FPPP Score first.")
            return
        
        values = {
            "spon_amt_24": spon_amt_24,
            "spon_amt_23": spon_amt_23,
            "spon_amt_22": spon_amt_22,
            "consul_amt_24": consul_amt_24,
            "consul_amt_23": consul_amt_23,
            "consul_amt_22": consul_amt_22,
            "total_faculty": total_fac,
            "fppp_score": fppp_score
        }
        
        prompt = build_prompt(values)
        self.gemini_frame.generate_recommendation(prompt)
            
    
    def clear_fields(self):
        self.spon_amt_24_23.delete(0, tk.END)
        self.spon_amt_23_22.delete(0, tk.END)
        self.spon_amt_22_21.delete(0, tk.END)
        self.consul_amt_24_23.delete(0, tk.END)
        self.consul_amt_23_22.delete(0, tk.END)
        self.consul_amt_22_21.delete(0, tk.END)
        self.tot_fac.delete(0, tk.END)
        self.output_entry.delete(0, tk.END)
            