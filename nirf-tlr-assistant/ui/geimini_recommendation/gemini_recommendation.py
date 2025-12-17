import os
import threading
import tkinter as tk
from tkinter import ttk, messagebox
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel("gemini-2.5-flash")
else:
    gemini_model = None

class GeminiRecommendationFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.model = gemini_model
        if self.model is None:
            print("Warning: Gemini API key not found.")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Add scrollbar for output text
        output_frame = ttk.Frame(self)
        output_frame.grid(row=0, column=0, pady=10, sticky="nsew")
        output_frame.grid_columnconfigure(0, weight=1)
        output_frame.grid_rowconfigure(0, weight=1)
        
        # Vertical scrollbar
        scrollbar = ttk.Scrollbar(output_frame, orient="vertical")
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Text widget with scrollbar
        self.output = tk.Text(output_frame, wrap="word", height=16, yscrollcommand=scrollbar.set)
        self.output.grid(row=0, column=0, sticky="nsew")
        
        scrollbar.config(command=self.output.yview)
    
    def generate_recommendation(self, prompt):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "Generating recommendation...\n")
        
        def run():
            try:
                response = self.model.generate_content(prompt)
                text = response.text
            except Exception as e:
                text = f"Error: {e}"
            
            self.output.after(0, lambda: self._update_output(text))
        
        t = threading.Thread(target=run, daemon=True)
        t.start()
    
    def _update_output(self, text):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, text)
        
    def run_recommendation(self):
        self.generate_recommendation("Give general NIRF improvement suggestions.")
