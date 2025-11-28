import os
import tkinter as tk
from tkinter import ttk, messagebox
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel("gemini-2.5-flash")
else:
    gemini_model = None

def create_input_frame(root):
    frame = ttk.Frame(root, padding=10)
    frame.pack(fill="x")
    
    labels = [
        "Total Students",
        "Total Faculty",
        "PhD Faculty",
        "PhD Students",
        "Annual Expenditure(in crore)",
        "Seat Occupancy (%)",
    ]
    
    entries = {}

    institute_header = ttk.Label(frame, text="Institute Data", font=("Arial", 12, "bold"))
    institute_header.grid(row=0, column=0, sticky="w", pady=(0,5))
    
    for i, label_text in enumerate(labels):
        label = ttk.Label(frame, text=label_text)
        label.grid(row=i+1, column=0, sticky="w", pady=5)
        
        entry = ttk.Entry(frame, width=30)
        entry.grid(row=i+1, column=1, sticky="w", pady=5, padx=10)
        
        entries[label_text] = entry

    separator = ttk.Separator(frame, orient="horizontal")
    separator.grid(row=7, column=0, columnspan=2, sticky="we", pady=10)

    goal_header = ttk.Label(frame, text="Goal Settings", font=("Arial", 12, "bold"))
    goal_header.grid(row=8, column=0, sticky="w", pady=(0,5))

    target_label = ttk.Label(frame, text="Target TLR Score")
    target_label.grid(row=9, column=0, sticky="w", pady=5)
    target_entry = ttk.Entry(frame, width=30)
    target_entry.grid(row=9, column=1, sticky="w", pady=5, padx=10)
    entries["Target TLR Score"] = target_entry
    
    return frame, entries

def create_output_box(root):
    output_label = ttk.Label(root, text="Output:")
    output_label.pack(anchor="w", padx=10)
    
    output_text = tk.Text(root, wrap="word", height=20)
    output_text.pack(fill="both", expand=True, padx=10, pady=10)
    
    return output_text

def collect_input_values(entries):
    total_students = int(entries["Total Students"].get())
    total_faculty = int(entries["Total Faculty"].get())
    phd_faculty = int(entries["PhD Faculty"].get())
    phd_students = int(entries["PhD Students"].get())
    annual_expenditure = float(entries["Annual Expenditure(in crore)"].get())
    occupancy = int(entries["Seat Occupancy (%)"].get())
    target_tlr_score = int(entries["Target TLR Score"].get())
    
    return {
        "total_students": total_students,
        "total_faculty": total_faculty,
        "phd_faculty": phd_faculty,
        "phd_students": phd_students,
        "annual_expenditure": annual_expenditure,
        "occupancy": occupancy,
        "target_score": target_tlr_score,
    }

def build_prompt(values: dict) -> str:
    """
    Build a natural language prompt for Perplexity
    using the cleaned numeric values.
    """
    total_students = values["total_students"]
    total_faculty = values["total_faculty"]
    phd_faculty = values["phd_faculty"]
    phd_students = values["phd_students"]
    annual_expenditure = values["annual_expenditure"]
    occupancy = values["occupancy"]
    target_score = values["target_score"]

    prompt = f"""
You are an expert in NIRF ranking (India). 
Analyze the institute data and provide the TLR breakdown in a strictly structured, easy-to-read format.

Institute Data:
- Total students: {total_students}
- Total faculty: {total_faculty}
- PhD faculty: {phd_faculty}
- PhD students: {phd_students}
- Annual expenditure: ₹{annual_expenditure} crore
- Seat occupancy: {occupancy}%
- Target TLR Score: {target_score}

Return your answer ONLY in the following format:

==============================
📌 TLR COMPONENT SCORES (Indexed)
==============================
1. SS (Student Strength): <score>/20  
2. FSR (Faculty-Student Ratio): <score>/30  
3. FQE (Faculty Qualifications & Experience): <score>/20  
4. FRU (Financial Resources & Utilization): <score>/30  

==============================
📌 TOTAL TLR SCORE
==============================
<total_score>/100

==============================
📌 COMPONENT-WISE ANALYSIS
==============================
Explain the meaning of each component in simple, short bullet points.
Use:
- Current status
- Weakness
- Strengths
- Gap to target score

==============================
📌 REQUIRED IMPROVEMENTS (NUMBERED)
==============================
Provide **numbered** improvement actions like this:
1. Increase faculty count from X → Y  
2. Increase PhD faculty percentage from X% → Y%  
3. Improve financial expenditure per student from X → Y  
4. Improve seat occupancy to 95%+

Keep them sharp, numeric, and practical.

==============================
📌 TARGET VALUES TABLE
==============================
Return a table like this (text-based):

| Component | Current | Required | Gap |
|----------|---------|----------|------|
| Faculty Count | X | Y | +Z |
| PhD Faculty % | X% | Y% | +Z% |
| Expenditure per student | ₹X | ₹Y | ₹Z |
| PhD Students | X | Y | +Z |

==============================
📌 FINAL SUMMARY (SHORT)
==============================
Give a very short 3–4 line actionable summary in simple language.

Make the output visually clean and easy to read in a Tkinter Text widget.
"""
    return prompt

def call_gemini(prompt: str) -> str:
    if not gemini_model:
        raise RuntimeError("GEMINI_API_KEY env variable not set.")
    
    response = gemini_model.generate_content(prompt)
    return response.text

def handle_submit(entries, output_text):
    try:
        values = collect_input_values(entries)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
        return
    
    prompt = build_prompt(values)
    
    output_text.delete("1.0", "end")
    output_text.insert("1.0", "Contacting Gemini...\nPlease wait...")
    
    try:
        answer = call_gemini(prompt)
    except Exception as e:
        output_text.delete("1.0", "end")
        output_text.insert("1.0", f"Error calling Gemini API: \n{e}")
        return
    
    output_text.delete("1.0", "end")
    output_text.insert("1.0", answer)

def create_submit_button(root, entries, output_text):
    button = ttk.Button(
        root,
        text="Get TLR Recommendation",
        command=lambda: handle_submit(entries, output_text)
    )
    button.pack(pady=15)

def main():
    root = tk.Tk()
    root.title("NIRF TLR Assistant")
    root.geometry("900x900")
    
    input_frame, entries = create_input_frame(root)
    output_text = create_output_box(root)
    create_submit_button(root, entries, output_text)
    
    print(input_frame)
    print(output_text)

    root.mainloop()

if __name__ == "__main__":
    main()