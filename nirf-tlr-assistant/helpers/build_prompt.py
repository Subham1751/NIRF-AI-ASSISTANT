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

==============================
🏫 INSTITUTE DATA
==============================
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