def build_prompt(values: dict) -> str:
    prompt = f"""
You are an expert advisor on **NIRF Graduation Outcomes (GO)** parameter.

Your task is to generate a **clear, numeric, and practically achievable recommendation**
to improve the **GPHD (Ph.D. Graduation Output)** score of an institution.

The audience is **university leadership** (Vice Chancellor, Registrar, Deans).
Use **simple language**, avoid theory, and focus on **actionable improvements**.

================================================================================
CONTEXT
================================================================================
• GPHD measures the **average number of Ph.D. students graduating** over the last 3 years.
• It reflects the **strength, stability, and effectiveness** of the institution’s research ecosystem.
• GPHD score is derived using a **relative model**, not a fixed formula.

================================================================================
INSTITUTION INPUTS (Ph.D. Graduations)
================================================================================

2021–22
- Full-Time Ph.D. Graduates: {values['tot_fphd_21']}
- Part-Time Ph.D. Graduates: {values['tot_pphd_21']}
- Total Ph.D. Graduates: {values['tot_fphd_21'] + values['tot_pphd_21']}

2022–23
- Full-Time Ph.D. Graduates: {values['tot_fphd_22']}
- Part-Time Ph.D. Graduates: {values['tot_pphd_22']}
- Total Ph.D. Graduates: {values['tot_fphd_22'] + values['tot_pphd_22']}

2023–24
- Full-Time Ph.D. Graduates: {values['tot_fphd_23']}
- Part-Time Ph.D. Graduates: {values['tot_pphd_23']}
- Total Ph.D. Graduates: {values['tot_fphd_23'] + values['tot_pphd_23']}

Average Ph.D. Graduates (3 Years):
- {(values['tot_fphd_21'] + values['tot_pphd_21'] +
    values['tot_fphd_22'] + values['tot_pphd_22'] + 
    values['tot_fphd_23'] + values['tot_pphd_23']) / 3:.2f}

================================================================================
CURRENT RESULT
================================================================================
Predicted GPHD Score: **{values['gphd_score']}**

================================================================================
WHAT YOU MUST ANALYZE
================================================================================
1. Year-wise consistency of Ph.D. graduations
2. Balance between Full-Time and Part-Time Ph.D. output
3. Whether the research output is:
   - Stable
   - Increasing
   - Or stagnant across years

================================================================================
OUTPUT FORMAT (STRICT – FOLLOW EXACTLY)
================================================================================

=========================== GPHD PERFORMANCE SUMMARY =============================

- Predicted GPHD Score: <value>
- Average Ph.D. Graduates per year: <value>
- Nature of output: Stable / Improving / Stagnant

============================= KEY OBSERVATIONS ==================================

- Explain the trend using **only the numbers given**
- Identify years with low graduation output
- Comment on dependency on part-time vs full-time Ph.D. scholars

========================== ACTIONABLE RECOMMENDATIONS =============================

Provide **3–5 practical and achievable actions**, such as:
- Improving Ph.D. completion timelines
- Strengthening supervisor-to-scholar planning
- Increasing full-time Ph.D. intake in targeted departments
- Providing structured milestone tracking for Ph.D. scholars
- Department-level research completion monitoring

Avoid generic statements like “increase research quality”.

=========================== EXPECTED PRACTICAL IMPACT =============================

- Explain how **incremental increases** in Ph.D. graduations
  (e.g., +5 to +10 scholars per year) can:
  - Improve research stability
  - Improve GPHD score gradually
- Do NOT promise unrealistic jumps or full marks.

================================================================================
IMPORTANT RULES
================================================================================
- Do NOT explain NIRF methodology
- Do NOT mention benchmarks or other universities
- Do NOT mention machine learning or models
- Use numbers, not vague terms
- Keep recommendations realistic and institution-friendly

================================================================================
Now generate the recommendation.
"""
    return prompt