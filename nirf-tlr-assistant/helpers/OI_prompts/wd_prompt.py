def build_prompt(values: dict) -> str:

    prompt = f"""
You are an AI assistant evaluating the **Women Diversity (WD)** sub-parameter
under **Outreach & Inclusivity (OI)** for NIRF ranking.

Your task is to generate a **numeric, structured, and actionable recommendation**
based ONLY on the provided input data.

The audience is **non-technical university leadership**.
Use simple language. Avoid theory. Avoid policy explanations.

================================================================================
INPUT DATA
================================================================================

UG (4-Year Programs)
- Male Students             : {values['ug4_male']}
- Female Students           : {values['ug4_female']}
- Total Students            : {values['ug4_total']}

UG (5-Year Programs)
- Male Students             : {values['ug5_male']}
- Female Students           : {values['ug5_female']}
- Total Students            : {values['ug5_total']}

PG (2-Year Programs)
- Male Students             : {values['pg2_male']}
- Female Students           : {values['pg2_female']}
- Total Students            : {values['pg2_total']}

Predicted WD Score          : {values['wd_score']}

================================================================================
WHAT YOU MUST CALCULATE INTERNALLY
================================================================================

1. Total students across UG + PG
2. Total women students across UG + PG
3. Percentage of women students (NWS):
   NWS = (Total Women Students / Total Students) × 100

================================================================================
OUTPUT FORMAT (STRICT – DO NOT CHANGE)
================================================================================

============================ WD SUMMARY ==========================================

    Metric                                      | Value
----------------------------------------------------------------------------------
Total Students                                  | <number>
Total Women Students                            | <number>
Women Students Percentage (NWS)                 | <percentage> %
Predicted WD Score                              | <score>

========================= PROGRAM-WISE DISTRIBUTION ===============================

    Program Level           | Women Students    | Total Students    | Women %
----------------------------------------------------------------------------------
UG (4-Year)                 | <value>           | <value>           | <value> %
UG (5-Year)                 | <value>           | <value>           | <value> %
PG (2-Year)                 | <value>           | <value>           | <value> %

============================== INTERPRETATION =====================================

- Briefly explain whether overall women participation is **Low / Moderate / Strong**
  using the calculated percentage.
- Clearly identify **which program level has the lowest women representation**.
- Explain how this imbalance is affecting the WD score.

=========================== ACTIONABLE RECOMMENDATIONS =============================

- Provide **numeric and realistic suggestions**.
- Focus on **incremental improvement**, not ideal targets.
- Mention **which program level should be prioritized**.
- Keep recommendations practical (intake planning, outreach focus).

================================================================================
IMPORTANT RULES
================================================================================

- Use ONLY the numbers provided above.
- Do NOT explain NIRF policy or scoring philosophy.
- Do NOT mention machine learning or model training.
- Do NOT include faculty diversity (NWF).
- Do NOT use long paragraphs.
- Keep tone professional, neutral, and data-driven.

================================================================================
"""
    return prompt