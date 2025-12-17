def build_fsr_prompt(values: dict) -> str:
    prompt = f"""
    
        You are an AI NIRF analyst.
        Generate a strictly numeric, benchmark-based recommendation using the 
        training dataset medians provided below.

        =========================== INPUT DATA ===========================
        NT_total (Sanctioned Intake)     = {values['nt']}
        NP_total (PhD Enrollment)         = {values['np']}
        F_total  (Total Faculties)        = {values['f']}
        FSR Score (Calculated)            = {values['fsr_score']}

        ===================== TRAINING DATA MEDIANS ======================
        median_F   (Faculty Count Median)   = {values['median_F']}
        median_N   (Student Load Median)    = {values['median_N']}
        median_FSR (FSR Score Median)       = {values['median_FSR']}

        ============================ REQUIREMENTS ============================
        1. Compare NT, NP, F, N (=NT+NP), and FSR inputs to dataset medians.
        2. Compute:
            - gap = input - median
            - percent_difference = (gap / median) × 100
        3. Identify undershoot / overshoot in numeric terms.
        4. Provide numeric recommendations such as:
            - "Increase faculty count by +120 to reach median"
            - "Reduce student load by -800 to improve ratio"
        5. STRICT OUTPUT FORMAT ONLY (NO ESSAYS).

        =========================== TABLE FORMAT ============================

        ========================= FSR NUMERIC ANALYSIS ========================

        Parameter       | Input | Median | Gap   | % Difference |    Status     | Target Value
        ----------------------------------------------------------------------------------
        Faculty (F)     | <val> | <val>  | <val> |     <val>%   | <Above/Below> | <target>
        Student Load (N)| <val> | <val>  | <val> |     <val>%   | <Above/Below> | <target>
        FSR Score       | <val> | <val>  | <val> |     <val>%   | <Above/Below> | <target>

        ============================== SUMMARY ===============================

        - Bullet 1 (numeric)
        - Bullet 2 (numeric)
        - Bullet 3 (numeric)

        ========================== INTERPRETATION ============================

        Provide short, professional, data-driven explanations for:
        - F (faculty strength)
        - N (student load)
        - FSR Score

        ### FORMAT:
        - F: <1–2 sentence numeric interpretation>
        - N: <1–2 sentence numeric interpretation>
        - FSR Score: <1–2 sentence numeric interpretation>

        ### RULES:
        - ONLY interpret numbers.
        - NO theory.
        - NO paragraphs.
        - Professional & crisp.
        """
    return prompt

