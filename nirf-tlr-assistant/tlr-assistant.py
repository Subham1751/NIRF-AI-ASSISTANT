import os
import threading
import tkinter as tk
from tkinter import ttk
import google.generativeai as genai
from ui.ss_calculator import SSCalculatorFrame
from ui.fsr_calculator import FSRCalculatorFrame
from ui.fqe_calculator import FQECalculatorFrame
from ui.fru_calculator import FRUCalculatorFrame
from helpers.spinner import (start_spinner, stop_spinner)
from ui.gemini_recommendation import GeminiRecommendationFrame
from helpers.ansi_color_codes import (COLOR_ERROR, COLOR_HEADER, COLOR_INFO,
    COLOR_OK, COLOR_RESET, COLOR_WARNING)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel("gemini-2.5-flash")
else:
    gemini_model = None

def call_gemini(prompt: str) -> str:
    if not gemini_model:
        raise RuntimeError("GEMINI_API_KEY env variable not set.")
    
    response = gemini_model.generate_content(prompt)
    return response.text

    def worker():
        try:
            answer = call_gemini(prompt)
            result_text = f"✅ Gemini Response:\n\n{answer}"
            print(f"{COLOR_OK}[Gemini] Response received successfully.{COLOR_RESET}")
        except Exception as e:
            result_text = f"❌ Error calling Gemini API:\n{e}"
            print(f"{COLOR_ERROR}[Gemini] Error: {e}{COLOR_RESET}")

        def update_ui():
            stop_spinner()
            output_text.delete("1.0", "end")
            output_text.insert("1.0", result_text)

        root.after(0, update_ui)

    threading.Thread(target=worker, daemon=True).start()

def create_submit_button(root, entries, output_text):
    button = ttk.Button(
        root,
        text="Get TLR Recommendation",
    )
    button.pack(pady=15)

def main():
    root = tk.Tk()
    root.title("NIRF TLR Assistant")
    root.geometry("1200x900")
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=2)
    
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    
    ss_frame = SSCalculatorFrame(root)
    ss_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    fsr_frame = FSRCalculatorFrame(root)
    fsr_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    
    fqe_frame = FQECalculatorFrame(root)
    fqe_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    
    fru_frame = FRUCalculatorFrame(root)
    fru_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
    
    gemini_frame = GeminiRecommendationFrame(root)
    gemini_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    
    print("UI Loaded Successfully")
    root.mainloop()

if __name__ == "__main__":
    main()