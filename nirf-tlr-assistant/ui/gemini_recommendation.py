import os
import threading
import tkinter as tk
from tkinter import ttk, messagebox
import google.generativeai as genai

from helpers.build_prompt import build_prompt
from helpers.spinner import start_spinner, stop_spinner

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel("gemini-2.5-flash")
else:
    gemini_model = None

class GeminiRecommendationFrame(ttk.LabelFrame):

    def __init__(self, parent):
        super().__init__(parent)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        submit_btn = ttk.Button(
            self, 
            text="Get Gemini Recommendation"
        )
        submit_btn.grid(row=0, column=0, pady=12)

        # Add scrollbar for output text
        output_frame = ttk.Frame(self)
        output_frame.grid(row=1, column=0, pady=10, sticky="nsew")
        output_frame.grid_columnconfigure(0, weight=1)
        output_frame.grid_rowconfigure(0, weight=1)
        
        # Vertical scrollbar
        scrollbar = ttk.Scrollbar(output_frame, orient="vertical")
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Text widget with scrollbar
        self.output = tk.Text(output_frame, wrap="word", height=16, yscrollcommand=scrollbar.set)
        self.output.grid(row=0, column=0, sticky="nsew")
        
        scrollbar.config(command=self.output.yview)
