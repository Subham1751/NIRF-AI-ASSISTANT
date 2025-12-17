def build_prompt(values: dict) -> str:

    prompt = f"""
You are an AI assistant evaluating the **Regional Diversity (RD)** sub-parameter
under **Outreach & Inclusivity (OI)** for NIRF ranking.

Your task is to generate a **numeric, structured, and actionable recommendation**
based ONLY on the provided input data.

The audience is **non-technical university leadership**.
Use simple language. Avoid theory. Avoid policy explanations.

================================================================================
INPUT DATA
================================================================================

UG (4-Year Programs)
- Outside State Students     : {values['ug4_out_state']}
- Outside Country Students   : {values['ug4_out_country']}
- Total Students             : {values['ug4_tot_students']}

UG (5-Year Programs)
- Outside State Students     : {values['ug5_out_state']}
- Outside Country Students   : {values['ug5_out_country']}
- Total Students             : {values['ug5_tot_students']}

PG (2-Year Programs)
- Outside State Students     : {values['pg2_out_state']}
- Outside Country Students   : {values['pg2_out_country']}
- Total Students             : {values['pg2_tot_students']}

Predicted RD Score            : {values['rd_score']}

================================================================================
WHAT YOU MUST CALCULATE INTERNALLY
================================================================================

1. Total students across UG + PG
2. Total students from outside the state
3. Total international students
4. Percentage of:
   - Outside state students
   - International students

================================================================================
OUTPUT FORMAT (STRICT – DO NOT CHANGE)
================================================================================

============================ RD SUMMARY ==========================================

    Metric                                      | Value
----------------------------------------------------------------------------------
Total Students                                  | <number>
Outside State Students                          | <number>
International Students                          | <number>
Outside State Percentage                        | <percentage> %
International Students Percentage               | <percentage> %
Predicted RD Score                              | <score>

========================= PROGRAM-WISE DISTRIBUTION ===============================

    Program Level           | Outside State     | International     | Total Students
----------------------------------------------------------------------------------
UG (4-Year)                 | <value>           | <value>           | <value>
UG (5-Year)                 | <value>           | <value>           | <value>
PG (2-Year)                 | <value>           | <value>           | <value>

============================== INTERPRETATION =====================================

- Briefly explain the institution’s regional diversity using the calculated percentages.
- Identify whether national or international diversity is weaker.
- Explain how this distribution affects the RD score.

=========================== ACTIONABLE RECOMMENDATIONS =============================

- Provide **numeric and realistic suggestions** to improve RD.
- Focus on **incremental increases**, not ideal targets.
- Mention whether **national outreach** or **international outreach** should be prioritized.
- Keep recommendations practical (admissions outreach, partnerships, visibility).

================================================================================
IMPORTANT RULES
================================================================================

- Use ONLY the numbers provided above.
- Do NOT explain NIRF policy or scoring philosophy.
- Do NOT mention machine learning or model training.
- Do NOT use long paragraphs.
- Keep tone professional, neutral, and data-driven.

================================================================================
"""
    return prompt