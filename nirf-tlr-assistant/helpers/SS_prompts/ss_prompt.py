def build_prompt(values: dict) -> str:
    prompt = f"""
        You are an AI NIRF analyst.
        Generate a strictly numeric, benchmark-based recommendation using the
        training dataset medians provided below.
        
        ### INPUT DATA
        NT_total = {values['nt']}
        NE_total = {values['ne']}
        NP_total = {values['np']}
        SS_predicted = {values['ss_score']}
        
        ### TRAINING DATA MEDIANS (BENCHMARKS)
        median_NT = {values['median_NT']}
        median_NE = {values['median_NE']}
        median_NP = {values['median_NP']}
        median_SS = {values['median_SS']}
        
        ### REQUIREMENTS
        1. Compare each input value (NT, NE, NP, SS) with the training dataset median.
        2. Calculate:
            - gap = input_value - median_value
            - percent_difference = (gap / median_value) * 100
        3. Identify which parameters are below median.
        4. Provide numeric targets such as:
            - "Increase NE_total by +480"
            - "Increase NP_total by +200"
        5. STRICT OUTPUT FORMAT: TABLE ONLY (NOT JSON)
        
        ### TABLE FORMAT (MANDATORY)
        Return the output in the following table format exactly:
        ============================== SS ANALYSIS ======================================================================

            Parameter                |  Input  | Median  |  Gap    | % Diff   |      Status          |  Target Value
        -----------------------------------------------------------------------------------------------------------------
        SANCTIONED_STUDENTS (NT)     | <value> | <value> | <value> | <value>% | <Above/Below Median> | <numeric target>
        ENROLLED STUDENTS (NE)       | <value> | <value> | <value> | <value>% | <Above/Below Median> | <numeric target>
        ENROLLED PHD STUDENTS (NP)   | <value> | <value> | <value> | <value>% | <Above/Below Median> | <numeric target>
        EXISTING SS Score            | <value> | <value> | <value> | <value>% | <interpretation>     | <numeric target>

        ============================== SUMMARY ==========================================================================

        - Bullet 1 (numeric)
        - Bullet 2 (numeric)
        - Bullet 3 (numeric)

        =========================== INTERPRETATION ======================================================================

        Provide short, professional, data-driven explanations for each parameter (NT, NE, NP, SS_score)
        based strictly on the numeric values in the table above.

        ### INTERPRETATION FORMAT (MANDATORY)
        - NT: <1–2 sentence numeric interpretation>
        - NE: <1–2 sentence numeric interpretation>
        - NP: <1–2 sentence numeric interpretation>
        - SS Score: <1–2 sentence numeric interpretation>

        ### RULES
        - Only interpret what the numbers show (gap, percentage difference, above/below median).
        - Do NOT write theory or long paragraphs.
        - Do NOT explain NIRF methodology.
        - Do NOT repeat information unnecessarily.
        - Keep the tone professional, concise, and analytical.
        """
    return prompt