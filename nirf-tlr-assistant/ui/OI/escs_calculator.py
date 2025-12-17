import tkinter as tk
from tkinter import ttk, messagebox
from train_escs_model import predict_escc
from helpers.OI_prompts.escs_prompt import build_prompt

class ESCSCalculatorFrame(ttk.LabelFrame):
    def set_gemini_frame(self, gemini_frame):
        self.gemini_frame = gemini_frame
        
    def __init__(self, parent):
        super().__init__(parent, text="ESCS Calculator", padding=10)
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
        
        btn_docs = ttk.Button(self, text="📘 ESCS Docs", style="Docs.TButton")
        btn_docs.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        # Row 1: UG4 Reimb State, UG4 Reimb Institute, Total UG4 Students
        ttk.Label(self, text="UG4 Reimb State: ").grid(row=1, column=0, sticky="w", pady=5, padx=2)
        self.ug4_reimb_state_entry = ttk.Entry(self, width=10)
        self.ug4_reimb_state_entry.grid(row=1, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="UG4 Reimb Institute: ").grid(row=1, column=2, sticky="w", pady=5, padx=2)
        self.ug4_reimb_institute_entry = ttk.Entry(self, width=10)
        self.ug4_reimb_institute_entry.grid(row=1, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Total UG4 Students: ").grid(row=1, column=4, sticky="w", pady=5, padx=2)
        self.total_ug4students_entry = ttk.Entry(self, width=10)
        self.total_ug4students_entry.grid(row=1, column=5, pady=5, sticky="ew", padx=2)
        
        # Row 2: UG5 Reimb State, UG5 Reimb Institute, Total UG5 Students
        ttk.Label(self, text="UG5 Reimb State: ").grid(row=2, column=0, sticky="w", pady=5, padx=2)
        self.ug5_reimb_state_entry = ttk.Entry(self, width=10)
        self.ug5_reimb_state_entry.grid(row=2, column=1, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="UG5 Reimb Institute: ").grid(row=2, column=2, sticky="w", pady=5, padx=2)
        self.ug5_reimb_institute_entry = ttk.Entry(self, width=10)
        self.ug5_reimb_institute_entry.grid(row=2, column=3, pady=5, sticky="ew", padx=2)
        
        ttk.Label(self, text="Total UG5 Students: ").grid(row=2, column=4, sticky="w", pady=5, padx=2)
        self.total_ug5students_entry= ttk.Entry(self, width=10)
        self.total_ug5students_entry.grid(row=2, column=5, pady=5, sticky="ew", padx=2)
        
        predict_btn = ttk.Button(self, text="Predict_ESCS", command=self.predict_score)
        clear_btn = ttk.Button(self, text="Clear", command=self.clear_fields)
        
        clear_btn.grid(row=3, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
        predict_btn.grid(row=3, column=3, columnspan=3, sticky="ew", padx=10, pady=5)
        
        self.output_entry = ttk.Entry(self, width=15, font=("Arial", 12, "bold"), state="readonly", foreground="gray")
        self.output_entry.grid(row=4, column=0, columnspan=3, sticky="ew", padx=2)
        
        self.output_entry.config(state="normal")
        self.output_entry.insert(0, "ESCS Score will appear here")
        self.output_entry.config(state="readonly")
        
        recommend_btn = ttk.Button(self, text="Get ESCS Recommendation", command=self.get_recommendation)
        recommend_btn.grid(row=4, column=3, columnspan=3, sticky="ew", padx=2)
    
    def predict_score(self):
        try:
            ug4_reimb_state = float(self.ug4_reimb_state_entry.get())
            ug4_reimb_institute = float(self.ug4_reimb_institute_entry.get())
            ug4_students = float(self.total_ug4students_entry.get())
            ug5_reimb_state = float(self.ug5_reimb_state_entry.get())
            ug5_reimb_institute = float(self.ug5_reimb_institute_entry.get())
            ug5_students = float(self.total_ug5students_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return
        
        try:
            escs_score = predict_escc(
                ug4_reimb_state, ug4_reimb_institute, ug4_students,
                ug5_reimb_state, ug5_reimb_institute, ug5_students,
            )
            self.output_entry.config(state="normal", foreground="white")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, str(escs_score))
            self.output_entry.config(state="readonly")
        except Exception as e:
            messagebox.showerror("Prediction Error", str(e))
    
    def get_recommendation(self):
        try:
            ug4_reimb_state = float(self.ug4_reimb_state_entry.get())
            ug4_reimb_institute = float(self.ug4_reimb_institute_entry.get())
            ug4_students = float(self.total_ug4students_entry.get())
            ug5_reimb_state = float(self.ug5_reimb_state_entry.get())
            ug5_reimb_institute = float(self.ug5_reimb_institute_entry.get())
            ug5_students = float(self.total_ug5students_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return
        
        if not self.gemini_frame:
            messagebox.showerror("Gemini Error", "Gemini frame not connected.")
            return
        
        escs_score_text = self.output_entry.get().strip()
        try:
            escs_score = float(escs_score_text)
        except ValueError:
            messagebox.showerror("Error", "Please predict ESCS Score first.")
            return
        
        values = {
            "ug4_students": ug4_students,
            "ug5_students": ug5_students,
            "ug4_reimb_state": ug4_reimb_state,
            "ug4_reimb_institute": ug4_reimb_institute,
            "ug5_reimb_state": ug5_reimb_state,
            "ug5_reimb_institute": ug5_reimb_institute,
            "escs_score": escs_score,
        }
        
        prompt = build_prompt(values)
        self.gemini_frame.generate_recommendation(prompt)
    
    def clear_fields(self):
        self.total_ug4students_entry.delete(0, tk.END)
        self.total_ug5students_entry.delete(0, tk.END)
        self.ug4_reimb_state_entry.delete(0, tk.END)
        self.ug4_reimb_institute_entry.delete(0, tk.END)
        self.ug5_reimb_state_entry.delete(0, tk.END)
        self.ug5_reimb_institute_entry.delete(0, tk.END)
        self.output_entry.delete(0, tk.END)