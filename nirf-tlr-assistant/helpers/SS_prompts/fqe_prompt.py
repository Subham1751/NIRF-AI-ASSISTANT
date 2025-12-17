def build_prompt(values: dict) -> str:
    prompt = f"""
        You are an AI NIRF analyst. Generate a strictly numeric, benchmark-driven recommendation for the
        FQE (Faculty Quality & Experience) parameter.

        =========================== INPUT DATA ===========================
        Total Faculty (TF)                     = {values['tf']}
        Faculty With PhD (FP)                  = {values['pf']}
        Total Students (TS)                    = {values['ts']}
        Faculty Exp ≤ 8 yrs (F1)               = {values['fe1']}
        Faculty Exp 8–15 yrs (F2)              = {values['fe2']}
        Faculty Exp > 15 yrs (F3)              = {values['fe3']}
        Required Faculty (derived TS/15)       = {values['req_fac']}

        FRA (%)                                = {values['fra']}
        FQ Score                               = {values['fq']}
        FE Score                               = {values['fe']}
        Final FQE Score                        = {values['fqe_score']}

        ============================ BENCHMARKS ============================
        Ideal FRA                               = 95%
        Ideal Faculty Mix (F1:F2:F3)            = 33% : 33% : 33%
        Ideal FQ Score                          = 10
        Ideal FE Score                          = 10
        Ideal FQE                               = 20

        ============================== REQUIREMENTS ==============================
        1. Compute the gap between each input value and its ideal benchmark.
           (Gemini must determine the formula itself. Do NOT assume any formula.)
        2. Compute % difference.
        3. Identify overshoot/undershoot.
        4. Recommend exact numeric corrections, such as:
            - "Increase PhD faculty by +18 to reach 95% FRA"
            - "Shift 12 faculty into 8–15 yrs category"
            - "Recruit 7 senior faculty (>15 yrs) to balance F3"
        5. STRICT OUTPUT FORMAT. NO THEORY. NO PARAGRAPHS.

        =========================== FQE NUMERIC ANALYSIS ==========================

        Metric                 | Input      | Ideal Value | Gap   | % Difference | Status        | Target
        -----------------------------------------------------------------------------------------------------
        FRA (%)                | <val>      | 95%         | <val> | <val>%       | <Above/Below> | <target>
        Faculty exp <= 8       | <val>      | 33%         | <val> | <val>%       | <Above/Below> | <target>
        Faculty exp            | <val>      | 33%         | <val> | <val>%       | <Above/Below> | <target>
        Faculty Mix F3 (%)     | <val>      | 33%         | <val> | <val>%       | <Above/Below> | <target>
        FQ Score               | <val>      | 10          | <val> | <val>%       | <Above/Below> | <target>
        FE Score               | <val>      | 10          | <val> | <val>%       | <Above/Below> | <target>
        FQE Score              | <val>      | 20          | <val> | <val>%       | <Above/Below> | <target>

        =============================== SUMMARY ===============================
        - Bullet 1: numeric, actionable
        - Bullet 2: numeric, actionable
        - Bullet 3: numeric, actionable

        =========================== INTERPRETATION ============================
        Provide professional, crisp, 1–2 line numeric insights for:
        - FRA
        - Faculty Experience Mix
        - FQE Score

        ### RULES:
        - Only interpret numbers.
        - No descriptive theories.
        - No long paragraphs.
        - Strictly numeric and professional.
        """
    return prompt
