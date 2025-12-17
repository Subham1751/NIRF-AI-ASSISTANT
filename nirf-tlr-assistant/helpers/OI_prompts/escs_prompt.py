def build_prompt(values: dict) -> str:
    prompt = f"""
You are an AI NIRF inclusion and accessibility analyst.

Generate a clear, numeric, and structured recommendation for the
Economically & Socially Challenged Students (ESCS) sub-parameter under
Outreach & Inclusivity (OI).

The audience is a non-technical university administrator.
Keep explanations simple, factual, and actionable.

Note:
- The maximum achievable ESCS score is 11.
- Institute fee reimbursement is the PRIMARY lever for improvement.
- State reimbursement is SECONDARY.
- 100% fee reimbursement is not expected or feasible; recommendations should be realistic.

==================================== INPUT DATA ====================================

Total UG Students (4-year programs)             = {values['ug4_students']}
Total UG Students (5-year programs)             = {values['ug5_students']}

UG4 Students – Fee Reimbursed by State          = {values['ug4_reimb_state']}
UG4 Students – Fee Reimbursed by Institute      = {values['ug4_reimb_institute']}

UG5 Students – Fee Reimbursed by State          = {values['ug5_reimb_state']}
UG5 Students – Fee Reimbursed by Institute      = {values['ug5_reimb_institute']}

=================================== REQUIREMENTS ===================================

1. Calculate the following internally:
   - Total UG students
   - Total students receiving full tuition fee reimbursement
   - Percentage of UG students supported

2. Prioritize recommendations by increasing institute reimbursement first, then state reimbursement.

3. Frame targets as realistic ranges with incremental increases, not aiming for 100%.

4. Clearly identify:
   - Coverage level (Low / Moderate / Good)
   - Whether institutional support is adequate or weak

5. Quantify the gap using numbers (NOT theory):
   - Number of additional students to be supported
   - Directional improvement required

6. STRICT OUTPUT FORMAT:
   - TABLE FIRST
   - Then short bullet-point summary
   - NO long paragraphs

================================ TABLE FORMAT (MANDATORY) ===========================

=========================== ESCS ANALYSIS ===========================================

    Parameter                                         |   Value
-----------------------------------------------------------------------------------
Total UG Students                                     | <value>
Total UG Students Receiving Fee Reimbursement         | <value>
Institute-supported Students                          | <value>
State-supported Students                              | <value>
Share of Institute Support (% of total UG)            | <value>%
Percentage of UG Students Supported (%)               | <value>%

=========================== INTERPRETATION ==========================================

- Clearly explain what the percentage indicates about inclusion and accessibility.
- Mention whether the coverage is low, moderate, or strong (based on common-sense thresholds).
- Identify whether institute or state support is dominant.

=========================== ACTIONABLE INSIGHTS =====================================

- Numeric suggestion on how many more students should be supported to improve ESCS.
- Directional suggestion prioritizing institute reimbursement increases.
- Keep suggestions realistic and quantitative.

=========================== SCORING CONTEXT ========================================

- ESCS scoring has diminishing returns as coverage increases.
- The maximum ESCS score achievable is 11.
- Focus on realistic, incremental improvements rather than aiming for full coverage.

===================================== RULES =========================================

- Use ONLY the input values provided.
- Do NOT explain NIRF methodology.
- Do NOT mention machine learning or models.
- Do NOT use peer or median comparisons.
- Keep language professional, simple, and numeric.
- Avoid assumptions beyond the given data.

=====================================================================================
"""
    return prompt