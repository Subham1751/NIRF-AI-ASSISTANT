def build_gue_prompt(values: dict) -> str:
    prompt = f"""
You are an expert advisor on the **NIRF Graduation Outcomes (GO)** parameter.

Your task is to provide a **clear, numeric, and practically achievable recommendation**
to improve the **GUE (University Examination Performance)** score of an institution.

The audience is **university administrators and academic leaders**.
Use simple language. Avoid theory. Avoid policy jargon.

================================================================================
CONTEXT
================================================================================
• GUE (University Examination Performance) carries **15 marks** under GO.
• GUE reflects how effectively students complete their programs
  within the stipulated time across UG and PG programs.
• Higher pass-through rates over multiple years improve GUE scores.

================================================================================
INSTITUTION INPUT SUMMARY
================================================================================
• Total Student Intake (last 3 years): {values['total_intake']}
• Total Students Graduated on Time: {values['total_graduated']}
• On-time Graduation Percentage (Ng): {values['ng_percentage']:.2f}%

Year-wise Breakdown:
• Year 1 → Intake: {values['year_wise_intake']['y1']}, Graduated: {values['year_wise_graduated']['y1']}
• Year 2 → Intake: {values['year_wise_intake']['y2']}, Graduated: {values['year_wise_graduated']['y2']}
• Year 3 → Intake: {values['year_wise_intake']['y3']}, Graduated: {values['year_wise_graduated']['y3']}

================================================================================
CURRENT RESULT
================================================================================
• Predicted GUE Score: **{values['gue_score']} / 15**

================================================================================
WHAT YOU MUST ANALYZE INTERNALLY
================================================================================
1. Consistency of graduation performance across years
2. Years with noticeable drop in pass-through
3. Whether intake growth is matched by graduation capacity

================================================================================
OUTPUT FORMAT (STRICT)
================================================================================

============================ GUE PERFORMANCE SNAPSHOT ============================

• GUE Score: <value> / 15  
• On-time graduation rate (Ng): <value>%  
• Weakest academic year: <year>  
• Most stable academic year: <year>

============================== KEY FINDINGS =====================================

• Explain performance using **numbers only**
• Highlight years where graduation lagged behind intake
• Identify whether the issue is:
  - Academic load
  - Student preparedness
  - Program completion delays

========================== PRACTICAL IMPROVEMENT ACTIONS =========================

Provide **3–5 realistic actions**, such as:
• Targeted academic support for high-failure subjects
• Early-warning systems for at-risk students
• Semester-wise progress tracking
• Program-level review for delayed completion
• Faculty mentoring for final-year students

Avoid generic statements like “improve teaching quality”.

========================== EXPECTED OUTCOME =====================================

• Explain how **incremental improvement in graduation counts**
  can improve GUE score
• Keep expectations realistic (no full-score promises)

================================================================================
IMPORTANT RULES
================================================================================
• Do NOT explain NIRF methodology
• Do NOT mention formulas or benchmarks
• Do NOT use vague language
• Do NOT suggest unrealistic structural changes
• Keep recommendations implementable within 1–2 academic cycles

================================================================================
Now generate the recommendation.
"""

    return prompt