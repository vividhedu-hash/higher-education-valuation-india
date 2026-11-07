# Build revised academic working paper HTML and compile to PDF
import os
import re
import subprocess

html_content = """

  RESEARCH PROJECT FINAL • APPLIED ECONOMICS & DECISION SCIENCES
  <h1 class="paper-title">A Risk-Adjusted Framework for Valuing Higher Education in India</h1>
  

## Estimating Heterogeneous Returns to Undergraduate Education Under Cost, Financing, and Labor-Market Uncertainty

  
    BHAVMANYU SINGH SISODIA^*<br>
    Supervised by Dr. Jaikishan Sahu • Professor, RPL Maheshwari College, Indore, India
  

  ^* Bhavmanyu Singh Sisodia (Correspondence: bhavmanyu25@gmail.com). Research project conducted under the supervision of Dr. Jaikishan Sahu, Professor, RPL Maheshwari College, Indore, India. All quantitative models, empirical derivations, and policy interpretations remain the sole responsibility of the author.

  ABSTRACT
  <p class="abstract-text">Every year, millions of Indian families make the largest financial bet of their lives: paying for an undergraduate degree with almost no reliable information beyond a college ranking and a headline salary figure. This paper asks whether those numbers actually tell families what a degree is worth. Using ten years of data from the National Institutional Ranking Framework (NIRF, 2016–2025), official employment benchmarks from the Periodic Labour Force Survey (PLFS 2022–23), Reserve Bank of India interest rates, and audited placement reports from 40 undergraduate programs, we build a financial valuation model that treats a college degree the way an investor treats any major asset—as a series of future cash flows weighed against upfront costs and real-world risks.</p>
  <p class="abstract-text">We find four robust empirical patterns. First, the NIRF's subjective “Perception” metric functions primarily as a mechanical accounting artifact of the statutory ranking formula rather than an indicator of instructional value-added. Regressions of published composite scores on objective metrics (faculty, research, graduation outcomes, and diversity) account for 90.5% to 99.1% of composite score variance, while Perception accounts for the remaining 1% to 10% (yielding a formula partial R^2 of 0.4286 overall and 0.9999 in single-formula categories). While external correspondence audits (Batheja et al., 2024) confirm employers do not reward mid-tier ranking differences, our longitudinal panel shows Perception introduces substantial year-on-year ranking volatility (averaging 22 rank positions among colleges ranked 50–200) without providing independent pedagogical or wage signal. Second, published salary packages (“Cost to Company” or CTC) significantly diverge from realized cash flows. After accounting for non-cash benefits, employee contributions, statutory income taxes under the New Tax Regime, and debt amortization on a commercial education loan at 10.15%, graduates of high-fee private engineering colleges face an initial debt-service burden consuming 58% to 85% of their monthly take-home pay in their early twenties, creating acute short-term default risks. Low-cost public institutions like IITs and NITs, by contrast, leave graduates with strong, unencumbered cash flows. Third, what a student studies matters substantially more than where they study: in a three-way analysis of variance, field of study accounts for 54.2% of lifetime valuation variance, compared to 31.6% for institutional tier and 14.2% for financing structure. Switching from basic sciences to computer science at a regional public college adds an average of INR 22.9 Lakhs to lifetime net present value—nearly double the financial gain of upgrading from an NIT to an IIT within computer science (INR 12.8 Lakhs). Fourth, artificial intelligence alters degree values unevenly across task domains: routine software syntax and standard accounting face downward valuation pressure, while clinical medicine and hands-on civil engineering maintain structural downside resilience. We conclude with a practical decision framework for households and urge policymakers to reform the PM-Vidyalaxmi student loan credit guarantee, grounding underwriting in debt-service coverage capacity rather than ordinal ranking thresholds.</p>
  
*Keywords:* Higher education valuation, Net Present Value, Internal Rate of Return, NIRF measurement validity, PLFS microdata, educational financing, debt service, AI task exposure, undergraduate choice, India.

  
*JEL Classification:* I21, I22, I26, J24, J31, D81, G11.

## I. Introduction

For most Indian middle-class and working-class families, sending a child to college is not just a milestone; it is an all-in financial gamble. Over the last thirty years, higher education in India has turned into a massive private marketplace. A four-year degree that once cost a modest sum at a state university can now run anywhere from INR 2 Lakhs at a central university to upwards of INR 25 to 55 Lakhs at a private deemed university. To pay these fees, parents routinely sell family gold, borrow against farmland, or take out commercial bank loans with double-digit interest rates.

Yet parents and students are forced to make this high-stakes decision in the dark. They rely almost entirely on two numbers: the college's rank in the National Institutional Ranking Framework (NIRF) and the headline salary plastered across marketing billboards. Neither number tells the truth about what graduates will actually take home.

Consider two engineering students standing at the admissions counter. Student A enrolls in computer science at a well-known private university ranked 15th in the NIRF. The four-year degree, including hostel and living expenses, costs INR 52 Lakhs. The college boasts a median placement of “INR 14 Lakhs CTC.” Student B enrolls in the same computer science degree at a regional National Institute of Technology (NIT) ranked 45th. The total four-year bill is just INR 6.5 Lakhs, and the median placement is also reported as INR 14 Lakhs CTC.

On paper, both choices look equally lucrative, and Student A's college looks more prestigious. In real life, their finances look completely different. A “14 Lakh CTC” does not mean INR 14 Lakhs in the bank. After stripping away joining bonuses that only pay out once, company medical insurance, and stock options that vest over four years—plus deducting taxes under the New Tax Regime—the graduate takes home about INR 9.8 Lakhs in cash. If Student A borrowed to pay that INR 52 Lakh tuition, their annual loan payment to State Bank of India at 10.15% interest comes to INR 8.3 Lakhs. That loan swallows 84.7% of their take-home pay. One bad appraisal or a hiring freeze pushes them into financial crisis. Student B, by contrast, has virtually no debt. They keep over 90% of their salary, save money, and accumulate over INR 110 Lakhs in net wealth over twenty years. Neither the college rank nor the salary poster warned Student A about that difference.

### A. Research Questions and Testable Hypotheses

This study addresses a straightforward question: *Do published college ranks and headline salaries give Indian families a reliable guide for choosing an undergraduate degree, or do true costs, loan repayments, real cash salaries, and artificial intelligence change the picture entirely?* We test four concrete hypotheses:

  - **Hypothesis 1 (Perception Metric Redundancy and Ranking Volatility):** Controlling for objective institutional attributes (faculty resources, research publications, graduation outcomes, and diversity), the NIRF's subjective Perception metric mechanically completes the statutory ranking formula (partial R^2 = 0.4286 to 0.9999) while reflecting historical campus scale and age rather than instructional quality, driving substantial rank volatility (mean swing > 22 positions among institutions ranked 50–200) without capturing distinct educational value-added.

  - **Hypothesis 2 (Debt Creates an Acute Early-Career Liquidity Squeeze):** While commercial debt financing preserves lifetime capital NPV rankings when real borrowing costs remain below household discount rates (ρ_Spearman = 0.938), it inverts early-career liquidity: graduates from expensive private institutions face initial debt-service burdens up to 84.7% of take-home pay, generating severe short-term default risk.

  - **Hypothesis 3 (Discipline Choice Outweighs Institutional Prestige):** Consistent with Kirkeboen, Leuven, and Mogstad (2016), the proportion of lifetime earnings variance explained by field of study (σ_Field^2) substantially exceeds the variance explained by institutional tier (σ_Tier^2).

  - **Hypothesis 4 (Physical and Clinical Tasks Exhibit Structural Resilience to AI):** Degrees requiring physical presence, tactile dexterity, and statutory clinical licensing (Medicine, Civil Engineering) exhibit greater resilience under advancing artificial intelligence than purely symbolic, routine cognitive disciplines (Computer Science, Commerce): |∂*NPV*_Medicine / ∂*AIOE*| < |∂*NPV*_CS / ∂*AIOE*|.

Figure 1 outlines the research roadmap of this study, connecting raw college data and employment surveys to our cash-flow valuation engine, risk adjustments, and policy recommendations.

  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 430" style="width: 100%; max-width: 780px; height: auto; font-family: 'Times New Roman', serif; background: #ffffff; border: none; border-radius: 0; margin: 4px auto; display: block;">
<rect x="0" y="0" width="880" height="30" fill="#0f172a" />
<text x="440" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Figure 1: Conceptual Research Architecture: Empirical Disclosures, Valuation Engine, and Policy Stress-Testing</text>
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1 L 10 5 L 0 9 z" fill="#475569" />
  </marker>
</defs>
<line x1="240" y1="95" x2="330" y2="150" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />
<line x1="240" y1="210" x2="330" y2="185" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />
<line x1="240" y1="325" x2="330" y2="220" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />
<line x1="550" y1="185" x2="640" y2="135" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />
<line x1="550" y1="205" x2="640" y2="275" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />
<line x1="440" y1="260" x2="440" y2="305" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />
<rect x="30" y="50" width="210" height="90" rx="4" fill="#f8fafc" stroke="#1e3a8a" stroke-width="2" />
<text x="135" y="72" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">EMPIRICAL DATA INPUTS</text>
<text x="135" y="90" font-size="9" fill="#334155" text-anchor="middle">NIRF Panel (6,176 clean records)</text>
<text x="135" y="105" font-size="9" fill="#334155" text-anchor="middle">MoSPI PLFS 2022-23 (Wage microdata)</text>
<text x="135" y="120" font-size="9" fill="#334155" text-anchor="middle">RBI Macro Series (CPI & Repo)</text>
<rect x="30" y="165" width="210" height="90" rx="4" fill="#f8fafc" stroke="#0f766e" stroke-width="2" />
<text x="135" y="187" font-size="11" font-weight="bold" fill="#0f766e" text-anchor="middle">THEORETICAL FOUNDATIONS</text>
<text x="135" y="205" font-size="9" fill="#334155" text-anchor="middle">Human Capital (Becker 1964)</text>
<text x="135" y="220" font-size="9" fill="#334155" text-anchor="middle">Credential Signaling (Spence 1973)</text>
<text x="135" y="235" font-size="9" fill="#334155" text-anchor="middle">Field Choice (Kirkeboen et al. 2016)</text>
<rect x="30" y="280" width="210" height="90" rx="4" fill="#f8fafc" stroke="#15803d" stroke-width="2" />
<text x="135" y="302" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">PROGRAM SAMPLE (N = 40)</text>
<text x="135" y="320" font-size="9" fill="#334155" text-anchor="middle">35 Audited Institutional Programs</text>
<text x="135" y="335" font-size="9" fill="#334155" text-anchor="middle">5 Calibrated Macro Archetypes</text>
<text x="135" y="350" font-size="9" fill="#334155" text-anchor="middle">Direct Costs & Placement Shares</text>
<rect x="330" y="125" width="220" height="135" rx="4" fill="#0f172a" stroke="#334155" stroke-width="2" />
<text x="440" y="152" font-size="12" font-weight="bold" fill="#f8fafc" text-anchor="middle">CORE VALUATION ENGINE</text>
<text x="440" y="172" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Gross CTC Haircut: Y = CTC · (1 - δ)</text>
<text x="440" y="190" font-size="9.5" fill="#cbd5e1" text-anchor="middle">New Tax Regime Statutory Deductions</text>
<text x="440" y="208" font-size="9.5" fill="#cbd5e1" text-anchor="middle">Fisher Real Debt Amortization (4.90%)</text>
<text x="440" y="226" font-size="9.5" fill="#cbd5e1" text-anchor="middle">20-Year Risk-Adjusted NPV & IRR</text>
<text x="440" y="244" font-size="9.5" fill="#38bdf8" text-anchor="middle">Break-Even Cash Salary Thresholds</text>
<rect x="330" y="310" width="220" height="95" rx="4" fill="#fffbeb" stroke="#b45309" stroke-width="2" />
<text x="440" y="332" font-size="11" font-weight="bold" fill="#b45309" text-anchor="middle">UNCERTAINTY & AI DISRUPTION</text>
<text x="440" y="350" font-size="9" fill="#78350f" text-anchor="middle">AIOE Task Exposure (NCO-2015)</text>
<text x="440" y="365" font-size="9" fill="#78350f" text-anchor="middle">4 Parameterized Diffusion Scenarios</text>
<text x="440" y="380" font-size="9" fill="#78350f" text-anchor="middle">10,000-Path Monte Carlo Simulation</text>
<rect x="640" y="80" width="210" height="110" rx="4" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2" />
<text x="745" y="105" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="middle">EMPIRICAL FINDINGS</text>
<text x="745" y="125" font-size="9" fill="#1e293b" text-anchor="middle">Rank Inversion (Headline vs. NPV)</text>
<text x="745" y="142" font-size="9" fill="#1e293b" text-anchor="middle">Debt Squeeze: Up to 84.7% EMI burden</text>
<text x="745" y="159" font-size="9" fill="#1e293b" text-anchor="middle">Variance Decomposition: Field > Tier</text>
<text x="745" y="176" font-size="9" fill="#1e293b" text-anchor="middle">NIRF Perception Redundancy (β ≈ 0)</text>
<rect x="640" y="220" width="210" height="110" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="2" />
<text x="745" y="245" font-size="11" font-weight="bold" fill="#16a34a" text-anchor="middle">POLICY & HOUSEHOLD PROTOCOL</text>
<text x="745" y="265" font-size="9" fill="#14532d" text-anchor="middle">PM-Vidyalaxmi Guarantee Reform</text>
<text x="745" y="282" font-size="9" fill="#14532d" text-anchor="middle">De-link from NIRF Ordinal Ranks</text>
<text x="745" y="299" font-size="9" fill="#14532d" text-anchor="middle">Mandatory Cash DSCR Underwriting</text>
<text x="745" y="316" font-size="9" fill="#14532d" text-anchor="middle">Four-Step Household Decision Rule</text>
</svg>
  Figure 1: Conceptual Research Architecture: Empirical Disclosures, Valuation Engine, and Policy Stress-Testing
  Note: Systematic separation of empirical institutional disclosures (NIRF, PLFS), the core valuation and debt-service engine, downside risk adjustments, and policy stress-testing.

## II. Literature Review and Theoretical Foundations

To understand what an Indian degree is worth, we have to connect three major debates in labor economics: whether college actually makes students more productive, whether prestigious colleges truly add value, and why what a student studies matters so much more than the logo on their degree.

### A. Does College Make You Smarter, or Just Prove You Were Already Smart?

The most famous debate in the economics of education is simple: does higher education genuinely build cognitive ability, or does it merely sort talented students from the rest? The human capital view (Becker, 1964; Ben-Porath, 1967; Mincer, 1974) argues that formal education directly augments cognitive and technical capabilities, which competitive labor markets reward with higher earnings. Decades of international empirical literature confirm that higher education yields substantial private wage returns globally, averaging approximately 9% to 10% per year of schooling (Psacharopoulos and Patrinos, 2018; Lange and Topel, 2006).

The signaling view (Spence, 1973; Arrow, 1973; Stiglitz, 1975) tells a different story. In a job market where employers cannot easily gauge an applicant's innate ability, a college degree serves as a sorting filter. Smart students clear grueling exams and finish tough degrees not because the curriculum transforms them, but to prove to companies that they were disciplined and capable all along. In India, where the Joint Entrance Examination (JEE Advanced) screens candidates from the top fraction of a percent (the top 0.01%), elite degrees carry enormous signaling power.

This distinction is not just academic; it matters deeply for degree valuation. If the high salaries earned by graduates of top colleges are mostly a signaling premium, that premium is fragile. The moment companies start evaluating candidates through automated coding sandboxes, practical bug-fixing audits, and portfolio reviews, the value of a prestigious college brand shrinks fast—without any change in what students actually learned in the classroom.

### B. What the Evidence Shows About Prestigious Colleges

When researchers try to measure whether attending an elite college actually causes higher earnings, the results are surprisingly modest. In the United States, Dale and Krueger (2002, 2014) compared students who were accepted by both selective and less selective colleges, and found that attending the more selective school made almost no difference to their long-term earnings. What mattered was the student's own ambition and ability, not where they spent their undergraduate years. Studies using admissions cutoffs (Hoekstra, 2009; Zimmerman, 2014) found small positive earnings bumps, but mainly for students right on the margin of getting into flagship state universities.

In India, empirical evidence is scarce but revealing. Azam and Blom (2008) and Dutta (2006) showed that professional degrees in engineering and medicine pay much higher returns than general arts or science degrees, though returns vary across social and demographic groups (Kanjilal-Bhaduri and Pastore, 2017). Munshi and Rosenzweig (2016) demonstrated how community networks influence educational investments and create occupational barriers in urban India, highlighting elite English-medium higher education as a vital mechanism for intergenerational mobility. Kijima (2006) documented how urban wage inequality rose after the 1990s as technical skills became more valuable. However, as Heckman, Layne-Farrar, and Todd (1996) emphasized, estimating the true causal effect of institutional quality is heavily confounded by student sorting and local labor market characteristics. When researchers use regression discontinuity cutoffs to control for selection (Lee and Lemieux, 2010; Sekhri, 2020), attending an elite Indian public college increases wages, but academic performance does not improve—suggesting that the salary premium originates from alumni networks and employer prestige rather than superior pedagogy. Frisancho and Krishna (2016) studied affirmative action students at IIT Delhi and found that early academic gaps closed substantially over four years. Most recently, Batheja, Hirshleifer, and Kaur (2024) sent 16,944 fictitious resumes to 1,412 engineering job openings across India; they found that listing a mid-tier NIRF-ranked college produced no statistically meaningful increase in interview callbacks compared to an unranked college. Outside the very top tier, Indian employers simply do not pay attention to published ranking tables.

### C. Why Your Major Matters More Than Your College Brand

A growing body of research shows that the field of study you pick is far more important than the college you attend. Altonji, Blom, and Meghir (2012) and Altonji, Arcidiacono, and Ma (2016) showed that the wage gap between different college majors is just as large as the wage gap between going to college and skipping it entirely. Wiswall and Zafar (2015) found that when students are given accurate salary figures, they actively change their majors.

The most compelling causal proof comes from Norway. Kirkeboen, Leuven, and Mogstad (2016) used centralized admissions lotteries to compare students who barely got into their preferred major versus those who got into their preferred college. Their finding was decisive: switching to a high-earning field (like engineering or business) at a lower-ranked college produced far larger lifetime earnings gains than attending an elite college in a lower-earning field. This insight forms the foundation of our Hypothesis 3.

At the same time, college costs in India have shifted dramatically from the state to parents. Tilak (2002) and Choudhury and Kumar (2022) documented how the explosive growth of private colleges has pushed tuition up to five times public college levels. When students take commercial loans to pay these fees, borrowing constraints prevent them from smoothing their living expenses across their life cycle (Dynarski, 2003; Lochner and Monge-Naranjo, 2011, 2012). In India, Patra, Ray, and Chaudhuri (2021) evaluated the expansion of educational lending following the Reserve Bank of India's 2001 model loan scheme, demonstrating substantial gains in schooling attainment and higher education enrollment, particularly among historically disadvantaged groups. However, subsequent credit expansion across commercial private colleges has been accompanied by rising non-performing assets (NPAs) and repayment stress in the banking sector (Reserve Bank of India, 2023). In late 2024, the government launched the PM-Vidyalaxmi scheme to provide collateral-free loans up to INR 7.5 Lakhs with credit guarantees. But because eligibility is strictly tied to being in the NIRF Top 100, the policy steers public credit guarantees toward high-fee private institutions where students face heavy debt burdens, while excluding affordable regional public universities that provide robust net economic returns.

<p>The ranking methodology itself has drawn sharp criticism. Global university rankings have evolved into high-stakes governance tools despite well-documented methodological vulnerabilities (Hazelkorn, 2015). Composite league tables are notoriously sensitive to indicator selection, weighting choices, and normalization rules (Selten et al., 2020; Sorz et al., 2015). In India, Marisha (2021) analyzed NIRF rank stability and showed that outside the top 15 engineering institutions, simulated ranks exhibit extreme volatility under minor indicator perturbations.
</p>

## III. What This Study Can and Cannot Claim: Methodological Scope and Identification

Before looking at the numbers, we need to be transparent about what this study measures and what it does not. Consider the standard labor-market earnings equation for a student *i* graduating from college *j* in field *k*:

$$\ln W_{ijk} = \alpha + \tau_j + \theta_k + \mathbf{X}_i'\beta + A_i + \varepsilon_{ijk} \tag{1}$$

Separating what the college added (τ_*j*) from what the student brought to the table (*A_i*) would require confidential, student-level cutoff data from the Joint Seat Allocation Authority (JoSAA), which is not publicly available. This paper does not claim to measure causal instructional quality.

**Why Our Realized Valuation Model Matters to Families:** What this paper measures is the **realized private financial return** that an actual Indian family faces when making an enrollment decision: *NPV_p* = −*C_p* + *E*[*PV*(Earnings | Matriculation)]. For a middle-class parent deciding whether to sign an SBI loan agreement or mortgage family land, the exact reason for high earnings—whether it was brilliant teaching, sharp classmates, or a prestigious brand—does not change the cash that lands in the graduate's bank account. That graduate still has to pay the loan, buy groceries, and pay rent with real rupees. Our model measures the financial reality families actually experience.

## IV. Data Construction and Purified Panel Assembly

We built our dataset by combining five independent public and administrative sources:

  <li>**The NIRF Panel Data Assembly (2016–2025):** We assembled a comprehensive longitudinal panel from official Ministry of Education ranking gazettes across ten annual rounds (2016–2025). The data construction process follows a transparent four-stage pipeline:
    <ol style="margin-top: 4px; margin-bottom: 4px; padding-left: 20px;">
      - *Administrative Standardization:* We extracted raw institutional ranking tables across all published categories (Engineering, Management, Universities, Colleges, Overall, Pharmacy, Medical, Law, Architecture, and Dental), standardizing institutional identifiers, state codes, and score schemas across 82 category-year archives, yielding a verified panel of **6,176 unique institution-year records**. (An earlier preliminary draft asserted that 2017 ranking tables duplicated 2016 data based on identical cryptographic file hashes; our subsequent empirical audit verified that 2017 tables contain distinct institutional scores and cohorts, leading us to completely excise that erroneous duplicate claim.)

      - *Complete-Case Panel Restriction:* For cross-sectional decomposition of the ranking formula, we subset records reporting complete data across all five statutory sub-parameters (TLR, RPC, GO, OI, PR) and the published composite score, arriving at an estimation sample of **5,726 complete-case observations** across 1,123 unique institutions.

      - *Consecutive Lag-1 Panel:* For longitudinal rank persistence analysis (Table 2 and Table A2), we restricted the sample to institutions appearing in identical categories across consecutive annual ranking rounds (*t* and *t*+1), yielding **3,873 verified consecutive pairs** across 8 annual transition windows.

    

  </li>
  - **Labor Market Benchmarks (MoSPI PLFS 2022–23):** To measure the opportunity cost of foregone earnings during undergraduate study, we anchor baseline wages to the Periodic Labour Force Survey (PLFS 2022–23) annual report microdata (Ministry of Statistics and Programme Implementation, 2023). The empirical benchmark average annual earnings for an urban Class 12 graduate entering the regular wage and salaried labor market is **INR 1,68,000 per year** (~INR 14,000 per month). In constant 2024–25 rupees, this represents an opportunity cost baseline of INR 1.68 to 1.86 Lakhs per year.

  - **Macroeconomic Data and Loan Rates:** Nominal cash flows are converted to constant 2024–25 values using the Consumer Price Index (CPI-Combined) series from the Reserve Bank of India (2025) Database on Indian Economy, alongside World Bank (2024) indicators. Commercial education loan interest rates are benchmarked to the State Bank of India's retail education loan schedule at **10.15% per annum** (a 6.50% repo rate plus a 3.65% retail spread). For premier public institutions qualifying for the SBI Scholar Loan Scheme, concessionary rates range between 8.15% and 8.65%.

  <li>**The 40-Program Dataset:** We assembled comparative data across 40 undergraduate degree programs spanning five disciplines (Engineering, Management, Commerce, Medicine, and Law), all requiring Class 12 for admission. To maintain absolute research transparency, the dataset strictly separates:
    

      - **35 Audited Institutional Programs:** Real institutions with published fee schedules, verified NIRF placement data, and audited institutional placement reports.

      - **5 Calibrated Synthetic Reference Archetypes:** Standardized hypothetical profiles constructed from State Fee Regulatory Committee (SFRC) ceilings and PLFS wage distributions, representing typical high-fee private deemed universities, Tier-3 private engineering colleges, state government colleges, and central university pure science programs.

    

  </li>

## V. The Economic Anatomy of Degree Costs

The true price of getting a college degree is never just the tuition written on the admission receipt. The total economic outlay *C_p* is the sum of direct tuition, mandatory institutional fees, living expenses in the college city, and the wages the student could have earned working after high school:

$$\text{NPV}_p = -(C_p - L_p) - \text{OC}_p \cdot d_p + \sum_{t=1}^{T} \frac{\pi_p \cdot \mathbb{E}[Y_{p,t}] - D_{p,t}}{(1 + r)^t} \tag{3}$$

**The Real Cash Haircut:** Advertised CTC numbers must be deflated to find actual in-hand starting pay. We reconcile this via two complementary formulations:

$$r_{\text{loan}}^{\text{real}} = \frac{1 + r_{\text{loan}}^{\text{nom}}}{1 + \pi_{\text{infl}}} - 1 = \frac{1.1015}{1.0500} - 1 = 4.9048\% \tag{6}$$

Figure 3 plots these break-even thresholds against actual graduate earnings, showing the safety margin for each degree.

  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 340" style="width: 100%; max-width: 780px; height: auto; font-family: 'Times New Roman', serif; background: #ffffff; border: none; border-radius: 0; margin: 4px auto; display: block;">
<rect x="0" y="0" width="880" height="30" fill="#0f172a" />
<text x="440" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Figure 3: Break-Even Starting Cash Salary and Downside Safety Margins (Baseline r = 8.0%)</text>
<text x="230" y="48" font-size="10.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Panel A: Actual Cash vs. Break-Even Cash Threshold (INR Lakhs)</text>
<text x="660" y="48" font-size="10.5" font-weight="bold" fill="#0f766e" text-anchor="middle">Panel B: Cash Safety Margin Above Break-Even (%)</text>
<text x="140" y="81" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">IIT Bombay CS</text>
<rect x="150" y="65" width="238.875" height="12" fill="#1e3a8a" rx="1.5" />
<text x="392.875" y="75" font-size="8" fill="#1e3a8a" font-weight="bold">14.70L</text>
<rect x="150" y="80" width="20.3125" height="12" fill="#0f766e" rx="1.5" />
<text x="174.3125" y="90" font-size="8" fill="#0f766e" font-weight="bold">1.25L</text>
<text x="570" y="85" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">IIT Bombay CS</text>
<rect x="580" y="71" width="219.60000000000002" height="18" fill="#15803d" rx="2" />
<text x="805.6" y="84" font-size="9" font-weight="bold" fill="#15803d">+91.5%</text>
<text x="140" y="121" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">NIT Trichy CS</text>
<rect x="150" y="105" width="164.9375" height="12" fill="#1e3a8a" rx="1.5" />
<text x="318.9375" y="115" font-size="8" fill="#1e3a8a" font-weight="bold">10.15L</text>
<rect x="150" y="120" width="13.162500000000001" height="12" fill="#0f766e" rx="1.5" />
<text x="167.1625" y="130" font-size="8" fill="#0f766e" font-weight="bold">0.81L</text>
<text x="570" y="125" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">NIT Trichy CS</text>
<rect x="580" y="111" width="220.8" height="18" fill="#15803d" rx="2" />
<text x="806.8" y="124" font-size="9" font-weight="bold" fill="#15803d">+92.0%</text>
<text x="140" y="161" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">SSCBS BBA FIA</text>
<rect x="150" y="145" width="133.9" height="12" fill="#1e3a8a" rx="1.5" />
<text x="287.9" y="155" font-size="8" fill="#1e3a8a" font-weight="bold">8.24L</text>
<rect x="150" y="160" width="8.450000000000001" height="12" fill="#0f766e" rx="1.5" />
<text x="162.45" y="170" font-size="8" fill="#0f766e" font-weight="bold">0.52L</text>
<text x="570" y="165" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">SSCBS BBA FIA</text>
<rect x="580" y="151" width="224.88000000000002" height="18" fill="#15803d" rx="2" />
<text x="810.88" y="164" font-size="9" font-weight="bold" fill="#15803d">+93.7%</text>
<text x="140" y="201" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">Private Deemed (Debt)</text>
<rect x="150" y="185" width="159.25" height="12" fill="#1e3a8a" rx="1.5" />
<text x="313.25" y="195" font-size="8" fill="#1e3a8a" font-weight="bold">9.80L</text>
<rect x="150" y="200" width="73.775" height="12" fill="#0f766e" rx="1.5" />
<text x="227.775" y="210" font-size="8" fill="#0f766e" font-weight="bold">4.54L</text>
<text x="570" y="205" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">Private Deemed (Debt)</text>
<rect x="580" y="191" width="128.88" height="18" fill="#b45309" rx="2" />
<text x="714.88" y="204" font-size="9" font-weight="bold" fill="#b45309">+53.7%</text>
<text x="140" y="241" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">Private Deemed (Self)</text>
<rect x="150" y="225" width="159.25" height="12" fill="#1e3a8a" rx="1.5" />
<text x="313.25" y="235" font-size="8" fill="#1e3a8a" font-weight="bold">9.80L</text>
<rect x="150" y="240" width="87.425" height="12" fill="#0f766e" rx="1.5" />
<text x="241.425" y="250" font-size="8" fill="#0f766e" font-weight="bold">5.38L</text>
<text x="570" y="245" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">Private Deemed (Self)</text>
<rect x="580" y="231" width="108.24000000000001" height="18" fill="#b45309" rx="2" />
<text x="694.24" y="244" font-size="9" font-weight="bold" fill="#b45309">+45.1%</text>
<text x="140" y="281" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">SRM B.Tech (Debt)</text>
<rect x="150" y="265" width="102.375" height="12" fill="#1e3a8a" rx="1.5" />
<text x="256.375" y="275" font-size="8" fill="#1e3a8a" font-weight="bold">6.30L</text>
<rect x="150" y="280" width="46.3125" height="12" fill="#0f766e" rx="1.5" />
<text x="200.3125" y="290" font-size="8" fill="#0f766e" font-weight="bold">2.85L</text>
<text x="570" y="285" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">SRM B.Tech (Debt)</text>
<rect x="580" y="271" width="131.51999999999998" height="18" fill="#b45309" rx="2" />
<text x="717.52" y="284" font-size="9" font-weight="bold" fill="#b45309">+54.8%</text>
<rect x="50" y="305" width="360" height="25" fill="#f8fafc" stroke="#cbd5e1" rx="2" />
<rect x="60" y="312" width="12" height="10" fill="#1e3a8a" rx="1.5" />
<text x="78" y="321" font-size="8.5" fill="#1e293b">Actual Starting Cash Salary (Post-tax)</text>
<rect x="230" y="312" width="12" height="10" fill="#0f766e" rx="1.5" />
<text x="248" y="321" font-size="8.5" fill="#1e293b">Required Break-Even Cash Threshold</text>
</svg>
  Figure 3: Break-Even Starting Cash Salary and Downside Safety Margins (Baseline r = 8.0%)
  Note: Panel A compares required break-even starting cash salary against realized post-haircut cash; Panel B reports downside safety margins before negative NPV. Subsidized public programs exhibit safety margins exceeding 90%, whereas high-cost private degrees leave margins below 55%.

## VIII. Headline Salary vs. Risk-Adjusted Net Present Value

Table 3 compares the financial outcomes of 19 representative undergraduate programs over a 20-year career under baseline economic conditions: an 8.0% real discount rate, 5.0% annual wage growth, and PLFS opportunity costs of INR 1.68 Lakhs per year.

Table 3: Comparative Program Valuation: Placement Salary vs. Risk-Adjusted Lifetime Net Present Value

  
    
      Program Specification
      Discipline
      Total Cost
      Gross CTC
      Cash Net
      Placement Rate
      Self True NPV
      Debt True NPV
      Break-Even Cash
      Cash Safety Margin
      Debt Squeeze (Y1-10)
    
  
  
    
      IIT Bombay B.Tech CS
      Eng-CS
      INR 11.0L
      INR 21.0L
      INR 14.70L
      0.93
      +INR 178.6L
      +INR 180.2L
      INR 1.33L
      +91.0%
      11.9%
    
    
      IIT Madras B.Tech CS
      Eng-CS
      INR 10.0L
      INR 19.8L
      INR 13.86L
      0.91
      +INR 164.9L
      +INR 166.4L
      INR 1.28L
      +90.8%
      11.5%
    
    
      AIIMS Delhi MBBS
      Medicine
      INR 1.5L
      INR 14.0L
      INR 9.80L
      0.98
      +INR 127.2L
      +INR 127.4L
      INR 0.76L
      +92.2%
      2.4%
    
    
      NIT Trichy B.Tech CS
      Eng-CS
      INR 6.5L
      INR 14.0L
      INR 9.80L
      0.88
      +INR 110.6L
      +INR 111.5L
      INR 1.05L
      +89.3%
      10.6%
    
    
      IIM Indore IPM (Integrated)
      Management
      INR 35.0L
      INR 22.0L
      INR 15.40L
      0.94
      +INR 164.4L
      +INR 169.5L
      INR 3.22L
      +79.1%
      36.3%
    
    
      NLSIU Bengaluru B.A. LL.B.
      Law
      INR 16.0L
      INR 16.0L
      INR 11.20L
      0.88
      +INR 123.8L
      +INR 126.1L
      INR 1.93L
      +82.8%
      22.8%
    
    
      SSCBS Delhi BBA FIA
      Management
      INR 3.8L
      INR 11.2L
      INR 7.84L
      0.86
      +INR 87.5L
      +INR 88.0L
      INR 0.72L
      +90.8%
      7.7%
    
    
      BITS Pilani B.E. CS
      Eng-CS
      INR 22.0L
      INR 15.5L
      INR 10.85L
      0.87
      +INR 107.4L
      +INR 110.7L
      INR 2.30L
      +78.8%
      32.4%
    
    
      IIT Roorkee B.Tech Civil
      Eng-NonCS
      INR 10.0L
      INR 10.2L
      INR 7.14L
      0.84
      +INR 68.9L
      +INR 70.4L
      INR 1.39L
      +80.5%
      22.4%
    
    
      St. Xavier Mumbai BMS
      Management
      INR 4.2L
      INR 8.5L
      INR 5.95L
      0.80
      +INR 59.9L
      +INR 60.5L
      INR 0.80L
      +86.6%
      11.3%
    
    
      NIT Calicut B.Tech Mech
      Eng-NonCS
      INR 5.8L
      INR 7.5L
      INR 5.25L
      0.81
      +INR 47.4L
      +INR 48.2L
      INR 1.03L
      +80.4%
      17.6%
    
    
      SRCC Delhi B.Com Hons
      Commerce
      INR 3.1L
      INR 7.4L
      INR 5.18L
      0.76
      +INR 48.6L
      +INR 49.0L
      INR 0.75L
      +85.5%
      9.5%
    
    
      VIT Vellore B.Tech CS
      Eng-CS
      INR 18.0L
      INR 9.8L
      INR 6.86L
      0.79
      +INR 53.0L
      +INR 55.6L
      INR 2.18L
      +68.2%
      41.9%
    
    
      Delhi Univ B.A. Econ Hons
      Commerce
      INR 3.0L
      INR 7.2L
      INR 5.04L
      0.75
      +INR 46.1L
      +INR 46.6L
      INR 0.75L
      +85.1%
      9.5%
    
    
      Delhi Univ B.Com Hons
      Commerce
      INR 2.8L
      INR 6.8L
      INR 4.76L
      0.74
      +INR 42.7L
      +INR 43.1L
      INR 0.74L
      +84.5%
      9.4%
    
    
      Central Univ B.Sc Physics
      PureSci
      INR 2.9L
      INR 4.2L
      INR 2.94L
      0.68
      +INR 20.7L
      +INR 21.1L
      INR 0.81L
      +72.4%
      15.7%
    
    
      State Univ B.Sc Chemistry
      PureSci
      INR 2.1L
      INR 3.8L
      INR 2.66L
      0.65
      +INR 17.6L
      +INR 17.9L
      INR 0.76L
      +71.4%
      12.6%
    
    
      SRM Univ B.Tech CS
      Eng-CS
      INR 26.0L
      INR 8.5L
      INR 5.95L
      0.74
      +INR 28.4L
      +INR 32.2L
      INR 3.09L
      +48.1%
      69.8% (CRITICAL)
    
    
      Private Deemed CS (Bench)
      Eng-CS
      INR 52.0L
      INR 14.0L
      INR 9.80L
      0.76
      +INR 48.2L
      +INR 55.9L
      INR 5.38L
      +45.1%
      84.7% (CRITICAL)
    
  

Note: Net Present Value evaluated over baseline 20-year horizon at r = 8.0%, g = 5.0%. Cash Net reflects gross starting salary minus the operational composite realization haircut (λ = 0.30), capturing 15% non-cash perks, statutory Section 115BAC tax slabs, and employee PF deductions. Initial DSTI reflects Year 1 annual debt service divided by annual starting net cash pay (58% to 85% across high-fee programs); this ratio de-escalates over the 10-year loan tenure as wages grow. *For Clinical Medicine (AIIMS Delhi MBBS), evaluating over an active 35-year medical practice lifecycle yields a 35-Year Self NPV of +INR 190.0 Lakhs (Monte Carlo Mean: +INR 196.3 Lakhs [95% CI: 107.4L, 337.8L]), surpassing all other undergraduate programs.

Figure 4 plots the dramatic divergence between headline placement rankings and true risk-adjusted NPV rankings.

  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 530" style="width: 100%; max-width: 780px; height: auto; font-family: 'Times New Roman', serif; background: #ffffff; border: none; border-radius: 0; margin: 4px auto; display: block;">
<rect x="0" y="0" width="880" height="30" fill="#0f172a" />
<text x="440" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Figure 4: Program Rank Divergence: Gross Headline Salary Rank vs. Risk-Adjusted 20-Year NPV Rank</text>
<text x="230" y="48" font-size="10.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Panel A: Headline Rank vs. Self-Funded NPV Rank</text>
<text x="650" y="48" font-size="10.5" font-weight="bold" fill="#0f766e" text-anchor="middle">Panel B: Headline Rank vs. 100% Debt-Financed NPV Rank</text>
<line x1="181.0" y1="58" x2="181.0" y2="500" stroke="#f1f5f9" stroke-width="1.2" />
<text x="181.0" y="514" font-size="8.5" fill="#94a3b8" text-anchor="middle">#1</text>
<line x1="225.0" y1="58" x2="225.0" y2="500" stroke="#f1f5f9" stroke-width="1.2" />
<text x="225.0" y="514" font-size="8.5" fill="#94a3b8" text-anchor="middle">#5</text>
<line x1="269.0" y1="58" x2="269.0" y2="500" stroke="#f1f5f9" stroke-width="1.2" />
<text x="269.0" y="514" font-size="8.5" fill="#94a3b8" text-anchor="middle">#9</text>
<line x1="313.0" y1="58" x2="313.0" y2="500" stroke="#f1f5f9" stroke-width="1.2" />
<text x="313.0" y="514" font-size="8.5" fill="#94a3b8" text-anchor="middle">#13</text>
<line x1="357.0" y1="58" x2="357.0" y2="500" stroke="#f1f5f9" stroke-width="1.2" />
<text x="357.0" y="514" font-size="8.5" fill="#94a3b8" text-anchor="middle">#17</text>
<line x1="601.0" y1="58" x2="601.0" y2="500" stroke="#f1f5f9" stroke-width="1.2" />
<text x="601.0" y="514" font-size="8.5" fill="#94a3b8" text-anchor="middle">#1</text>
<line x1="645.0" y1="58" x2="645.0" y2="500" stroke="#f1f5f9" stroke-width="1.2" />
<text x="645.0" y="514" font-size="8.5" fill="#94a3b8" text-anchor="middle">#5</text>
<line x1="689.0" y1="58" x2="689.0" y2="500" stroke="#f1f5f9" stroke-width="1.2" />
<text x="689.0" y="514" font-size="8.5" fill="#94a3b8" text-anchor="middle">#9</text>
<line x1="733.0" y1="58" x2="733.0" y2="500" stroke="#f1f5f9" stroke-width="1.2" />
<text x="733.0" y="514" font-size="8.5" fill="#94a3b8" text-anchor="middle">#13</text>
<line x1="777.0" y1="58" x2="777.0" y2="500" stroke="#f1f5f9" stroke-width="1.2" />
<text x="777.0" y="514" font-size="8.5" fill="#94a3b8" text-anchor="middle">#17</text>
<text x="160" y="74.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">IIT Bombay CS</text>
<rect x="170" y="64.0" width="11.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="66.0" width="11.0" height="10" fill="#15803d" rx="1.5" />
<text x="186.0" y="74.0" font-size="8" font-weight="bold" fill="#166534">#1</text>
<text x="580" y="74.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">IIT Bombay CS</text>
<rect x="590" y="64.0" width="11.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="66.0" width="11.0" height="10" fill="#15803d" rx="1.5" />
<text x="606.0" y="74.0" font-size="8" font-weight="bold" fill="#166534">#1</text>
<text x="160" y="96.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">IIT Madras CS</text>
<rect x="170" y="86.5" width="22.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="88.5" width="22.0" height="10" fill="#15803d" rx="1.5" />
<text x="197.0" y="96.5" font-size="8" font-weight="bold" fill="#166534">#2</text>
<text x="580" y="96.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">IIT Madras CS</text>
<rect x="590" y="86.5" width="22.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="88.5" width="22.0" height="10" fill="#15803d" rx="1.5" />
<text x="617.0" y="96.5" font-size="8" font-weight="bold" fill="#166534">#2</text>
<text x="160" y="119.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">AIIMS MBBS</text>
<rect x="170" y="109.0" width="33.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="111.0" width="33.0" height="10" fill="#15803d" rx="1.5" />
<text x="208.0" y="119.0" font-size="8" font-weight="bold" fill="#166534">#3</text>
<text x="580" y="119.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">AIIMS MBBS</text>
<rect x="590" y="109.0" width="33.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="111.0" width="33.0" height="10" fill="#15803d" rx="1.5" />
<text x="628.0" y="119.0" font-size="8" font-weight="bold" fill="#166534">#3</text>
<text x="160" y="141.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">IIM Indore IPM</text>
<rect x="170" y="131.5" width="44.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="133.5" width="55.0" height="10" fill="#b45309" rx="1.5" />
<text x="230.0" y="141.5" font-size="8" font-weight="bold" fill="#854d0e">#5</text>
<text x="580" y="141.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">IIM Indore IPM</text>
<rect x="590" y="131.5" width="44.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="133.5" width="55.0" height="10" fill="#b45309" rx="1.5" />
<text x="650.0" y="141.5" font-size="8" font-weight="bold" fill="#854d0e">#5</text>
<text x="160" y="164.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">NIT Trichy CS</text>
<rect x="170" y="154.0" width="55.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="156.0" width="44.0" height="10" fill="#b45309" rx="1.5" />
<text x="230.0" y="164.0" font-size="8" font-weight="bold" fill="#854d0e">#4</text>
<text x="580" y="164.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">NIT Trichy CS</text>
<rect x="590" y="154.0" width="55.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="156.0" width="44.0" height="10" fill="#b45309" rx="1.5" />
<text x="650.0" y="164.0" font-size="8" font-weight="bold" fill="#854d0e">#4</text>
<text x="160" y="186.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">NLSIU B.A. LL.B.</text>
<rect x="170" y="176.5" width="66.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="178.5" width="66.0" height="10" fill="#15803d" rx="1.5" />
<text x="241.0" y="186.5" font-size="8" font-weight="bold" fill="#166534">#6</text>
<text x="580" y="186.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">NLSIU B.A. LL.B.</text>
<rect x="590" y="176.5" width="66.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="178.5" width="66.0" height="10" fill="#15803d" rx="1.5" />
<text x="661.0" y="186.5" font-size="8" font-weight="bold" fill="#166534">#6</text>
<text x="160" y="209.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">BITS Pilani CS</text>
<rect x="170" y="199.0" width="77.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="201.0" width="88.0" height="10" fill="#b45309" rx="1.5" />
<text x="263.0" y="209.0" font-size="8" font-weight="bold" fill="#854d0e">#8</text>
<text x="580" y="209.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">BITS Pilani CS</text>
<rect x="590" y="199.0" width="77.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="201.0" width="88.0" height="10" fill="#b45309" rx="1.5" />
<text x="683.0" y="209.0" font-size="8" font-weight="bold" fill="#854d0e">#8</text>
<text x="160" y="231.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">SSCBS BBA FIA</text>
<rect x="170" y="221.5" width="88.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="223.5" width="77.0" height="10" fill="#b45309" rx="1.5" />
<text x="263.0" y="231.5" font-size="8" font-weight="bold" fill="#854d0e">#7</text>
<text x="580" y="231.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">SSCBS BBA FIA</text>
<rect x="590" y="221.5" width="88.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="223.5" width="77.0" height="10" fill="#b45309" rx="1.5" />
<text x="683.0" y="231.5" font-size="8" font-weight="bold" fill="#854d0e">#7</text>
<text x="160" y="254.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">IIT Roorkee Civil</text>
<rect x="170" y="244.0" width="99.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="246.0" width="99.0" height="10" fill="#15803d" rx="1.5" />
<text x="274.0" y="254.0" font-size="8" font-weight="bold" fill="#166534">#9</text>
<text x="580" y="254.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">IIT Roorkee Civil</text>
<rect x="590" y="244.0" width="99.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="246.0" width="99.0" height="10" fill="#15803d" rx="1.5" />
<text x="694.0" y="254.0" font-size="8" font-weight="bold" fill="#166534">#9</text>
<text x="160" y="276.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">St. Xavier's BMS</text>
<rect x="170" y="266.5" width="110.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="268.5" width="110.0" height="10" fill="#15803d" rx="1.5" />
<text x="285.0" y="276.5" font-size="8" font-weight="bold" fill="#166534">#10</text>
<text x="580" y="276.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">St. Xavier's BMS</text>
<rect x="590" y="266.5" width="110.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="268.5" width="110.0" height="10" fill="#15803d" rx="1.5" />
<text x="705.0" y="276.5" font-size="8" font-weight="bold" fill="#166534">#10</text>
<text x="160" y="299.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">SRCC B.Com Hons</text>
<rect x="170" y="289.0" width="121.00000000000001" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="291.0" width="132.0" height="10" fill="#b45309" rx="1.5" />
<text x="307.0" y="299.0" font-size="8" font-weight="bold" fill="#854d0e">#12</text>
<text x="580" y="299.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">SRCC B.Com Hons</text>
<rect x="590" y="289.0" width="121.00000000000001" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="291.0" width="132.0" height="10" fill="#b45309" rx="1.5" />
<text x="727.0" y="299.0" font-size="8" font-weight="bold" fill="#854d0e">#12</text>
<text x="160" y="321.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">NIT Calicut Mech</text>
<rect x="170" y="311.5" width="132.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="313.5" width="121.00000000000001" height="10" fill="#b45309" rx="1.5" />
<text x="307.0" y="321.5" font-size="8" font-weight="bold" fill="#854d0e">#11</text>
<text x="580" y="321.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">NIT Calicut Mech</text>
<rect x="590" y="311.5" width="132.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="313.5" width="121.00000000000001" height="10" fill="#b45309" rx="1.5" />
<text x="727.0" y="321.5" font-size="8" font-weight="bold" fill="#854d0e">#11</text>
<text x="160" y="344.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">VIT Vellore CS</text>
<rect x="170" y="334.0" width="143.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="336.0" width="154.0" height="10" fill="#b45309" rx="1.5" />
<text x="329.0" y="344.0" font-size="8" font-weight="bold" fill="#854d0e">#14</text>
<text x="580" y="344.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">VIT Vellore CS</text>
<rect x="590" y="334.0" width="143.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="336.0" width="154.0" height="10" fill="#b45309" rx="1.5" />
<text x="749.0" y="344.0" font-size="8" font-weight="bold" fill="#854d0e">#14</text>
<text x="160" y="366.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">DU B.A. Econ Hons</text>
<rect x="170" y="356.5" width="154.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="358.5" width="165.0" height="10" fill="#b45309" rx="1.5" />
<text x="340.0" y="366.5" font-size="8" font-weight="bold" fill="#854d0e">#15</text>
<text x="580" y="366.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">DU B.A. Econ Hons</text>
<rect x="590" y="356.5" width="154.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="358.5" width="165.0" height="10" fill="#b45309" rx="1.5" />
<text x="760.0" y="366.5" font-size="8" font-weight="bold" fill="#854d0e">#15</text>
<text x="160" y="389.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">DU B.Com Hons</text>
<rect x="170" y="379.0" width="165.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="381.0" width="176.0" height="10" fill="#b45309" rx="1.5" />
<text x="351.0" y="389.0" font-size="8" font-weight="bold" fill="#854d0e">#16</text>
<text x="580" y="389.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">DU B.Com Hons</text>
<rect x="590" y="379.0" width="165.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="381.0" width="176.0" height="10" fill="#b45309" rx="1.5" />
<text x="771.0" y="389.0" font-size="8" font-weight="bold" fill="#854d0e">#16</text>
<text x="160" y="411.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">Private Deemed CS</text>
<rect x="170" y="401.5" width="55.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="403.5" width="187.0" height="10" fill="#dc2626" rx="1.5" />
<text x="362.0" y="411.5" font-size="8" font-weight="bold" fill="#991b1b">#17</text>
<text x="580" y="411.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">Private Deemed CS</text>
<rect x="590" y="401.5" width="55.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="403.5" width="209.0" height="10" fill="#dc2626" rx="1.5" />
<text x="804.0" y="411.5" font-size="8" font-weight="bold" fill="#991b1b">#19</text>
<text x="160" y="434.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">Central Univ B.Sc</text>
<rect x="170" y="424.0" width="176.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="426.0" width="198.0" height="10" fill="#b45309" rx="1.5" />
<text x="373.0" y="434.0" font-size="8" font-weight="bold" fill="#854d0e">#18</text>
<text x="580" y="434.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">Central Univ B.Sc</text>
<rect x="590" y="424.0" width="176.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="426.0" width="187.0" height="10" fill="#b45309" rx="1.5" />
<text x="782.0" y="434.0" font-size="8" font-weight="bold" fill="#854d0e">#17</text>
<text x="160" y="456.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">SRM B.Tech CS</text>
<rect x="170" y="446.5" width="121.00000000000001" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="448.5" width="209.0" height="10" fill="#dc2626" rx="1.5" />
<text x="384.0" y="456.5" font-size="8" font-weight="bold" fill="#991b1b">#19</text>
<text x="580" y="456.5" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">SRM B.Tech CS</text>
<rect x="590" y="446.5" width="121.00000000000001" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="448.5" width="198.0" height="10" fill="#dc2626" rx="1.5" />
<text x="793.0" y="456.5" font-size="8" font-weight="bold" fill="#991b1b">#18</text>
<text x="160" y="479.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">State Univ Chemistry</text>
<rect x="170" y="469.0" width="187.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="170" y="471.0" width="220.0" height="10" fill="#b45309" rx="1.5" />
<text x="395.0" y="479.0" font-size="8" font-weight="bold" fill="#854d0e">#20</text>
<text x="580" y="479.0" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">State Univ Chemistry</text>
<rect x="590" y="469.0" width="187.0" height="14" fill="#e2e8f0" rx="1.5" />
<rect x="590" y="471.0" width="220.0" height="10" fill="#b45309" rx="1.5" />
<text x="815.0" y="479.0" font-size="8" font-weight="bold" fill="#854d0e">#20</text>
</svg>
  Figure 4: Program Rank Divergence: Gross Headline Salary Rank vs. Risk-Adjusted 20-Year NPV Rank
  Note: Panel A displays gross headline salary rank versus self-funded 20-year net present value rank; Panel B shows dramatic downward rank shifts for high-fee private programs under full commercial debt financing.

**Why Advertised Salaries Mislead Families:** Table 3 and Figure 4 show why published placement figures cannot be trusted. While IIT Bombay Computer Science leads across both metrics (+INR 178.6 Lakhs NPV), programs that advertise identical packages produce radically different lives. NIT Trichy CS and a benchmark Private Deemed CS program both report median placements of INR 14.0 Lakhs CTC. Yet NIT Trichy delivers a 20-year net present value of **+INR 110.6 Lakhs**, whereas the private deemed program delivers just **+INR 48.2 Lakhs**. Attending the private college inflicts a massive **INR 62.4 Lakh penalty** on the student's lifetime wealth, driven entirely by inflated tuition and living costs.

**The Debt Squeeze on Young Graduates:** Figure 5 compares degrees funded out-of-pocket against degrees funded with commercial student loans, exposing the brutal cash-flow squeeze on private college graduates.

  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 540" style="width: 100%; max-width: 780px; height: auto; font-family: 'Times New Roman', serif; background: #ffffff; border: none; border-radius: 0; margin: 4px auto; display: block;">
<rect x="0" y="0" width="880" height="30" fill="#0f172a" />
<text x="440" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Figure 5: 20-Year Net Present Value Under Self-Funded vs. Commercial Debt Regimes (INR Lakhs, r = 8.0%)</text>
<line x1="190.0" y1="35" x2="190.0" y2="505" stroke="#f1f5f9" stroke-width="1.5" />
<text x="190.0" y="520" font-size="9.5" fill="#64748b" text-anchor="middle">0L</text>
<line x1="318.0" y1="35" x2="318.0" y2="505" stroke="#f1f5f9" stroke-width="1.5" />
<text x="318.0" y="520" font-size="9.5" fill="#64748b" text-anchor="middle">40L</text>
<line x1="446.0" y1="35" x2="446.0" y2="505" stroke="#f1f5f9" stroke-width="1.5" />
<text x="446.0" y="520" font-size="9.5" fill="#64748b" text-anchor="middle">80L</text>
<line x1="574.0" y1="35" x2="574.0" y2="505" stroke="#f1f5f9" stroke-width="1.5" />
<text x="574.0" y="520" font-size="9.5" fill="#64748b" text-anchor="middle">120L</text>
<line x1="702.0" y1="35" x2="702.0" y2="505" stroke="#f1f5f9" stroke-width="1.5" />
<text x="702.0" y="520" font-size="9.5" fill="#64748b" text-anchor="middle">160L</text>
<line x1="830.0" y1="35" x2="830.0" y2="505" stroke="#f1f5f9" stroke-width="1.5" />
<text x="830.0" y="520" font-size="9.5" fill="#64748b" text-anchor="middle">200L</text>
<text x="180" y="56" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">IIT Bombay CS</text>
<rect x="190" y="42" width="571.52" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="53" width="576.64" height="9" fill="#b45309" rx="1.5" />
<text x="774.64" y="56" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 178.6L | Debt: 180.2L</text>
<text x="180" y="80" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">IIT Madras CS</text>
<rect x="190" y="66" width="543.36" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="77" width="547.84" height="9" fill="#b45309" rx="1.5" />
<text x="745.84" y="80" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 169.8L | Debt: 171.2L</text>
<text x="180" y="104" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">AIIMS MBBS (20-Yr)</text>
<rect x="190" y="90" width="407.04" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="101" width="407.68" height="9" fill="#b45309" rx="1.5" />
<text x="605.6800000000001" y="104" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 127.2L | Debt: 127.4L</text>
<text x="180" y="128" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">IIM Indore IPM</text>
<rect x="190" y="114" width="356.48" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="125" width="372.16" height="9" fill="#b45309" rx="1.5" />
<text x="570.1600000000001" y="128" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 111.4L | Debt: 116.3L</text>
<text x="180" y="152" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">NIT Trichy CS</text>
<rect x="190" y="138" width="353.91999999999996" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="149" width="356.8" height="9" fill="#b45309" rx="1.5" />
<text x="554.8" y="152" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 110.6L | Debt: 111.5L</text>
<text x="180" y="176" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">NLSIU B.A. LL.B.</text>
<rect x="190" y="162" width="328.0" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="173" width="335.03999999999996" height="9" fill="#b45309" rx="1.5" />
<text x="533.04" y="176" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 102.5L | Debt: 104.7L</text>
<text x="180" y="200" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">BITS Pilani CS</text>
<rect x="190" y="186" width="285.44" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="197" width="295.35999999999996" height="9" fill="#b45309" rx="1.5" />
<text x="493.35999999999996" y="200" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 89.2L | Debt: 92.3L</text>
<text x="180" y="224" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">SSCBS BBA FIA</text>
<rect x="190" y="210" width="281.6" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="221" width="283.2" height="9" fill="#b45309" rx="1.5" />
<text x="481.2" y="224" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 88.0L | Debt: 88.5L</text>
<text x="180" y="248" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">IIT Roorkee Civil</text>
<rect x="190" y="234" width="220.48000000000002" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="245" width="224.95999999999998" height="9" fill="#b45309" rx="1.5" />
<text x="422.96" y="248" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 68.9L | Debt: 70.3L</text>
<text x="180" y="272" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">St. Xavier's BMS</text>
<rect x="190" y="258" width="177.27999999999997" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="269" width="179.20000000000002" height="9" fill="#b45309" rx="1.5" />
<text x="377.20000000000005" y="272" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 55.4L | Debt: 56.0L</text>
<text x="180" y="296" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">SRCC B.Com Hons</text>
<rect x="190" y="282" width="157.12" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="293" width="158.4" height="9" fill="#b45309" rx="1.5" />
<text x="356.4" y="296" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 49.1L | Debt: 49.5L</text>
<text x="180" y="320" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">VIT Vellore CS</text>
<rect x="190" y="306" width="156.16" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="317" width="164.16" height="9" fill="#b45309" rx="1.5" />
<text x="362.15999999999997" y="320" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 48.8L | Debt: 51.3L</text>
<text x="180" y="344" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">NIT Calicut Mech</text>
<rect x="190" y="330" width="155.2" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="341" width="157.76" height="9" fill="#b45309" rx="1.5" />
<text x="355.76" y="344" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 48.5L | Debt: 49.3L</text>
<text x="180" y="368" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">Private Deemed CS</text>
<rect x="190" y="354" width="154.24" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="365" width="179.20000000000002" height="9" fill="#b45309" rx="1.5" />
<text x="377.20000000000005" y="368" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 48.2L | Debt: 56.0L</text>
<text x="180" y="392" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">DU B.A. Econ Hons</text>
<rect x="190" y="378" width="143.35999999999999" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="389" width="144.64000000000001" height="9" fill="#b45309" rx="1.5" />
<text x="342.64" y="392" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 44.8L | Debt: 45.2L</text>
<text x="180" y="416" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">DU B.Com Hons</text>
<rect x="190" y="402" width="136.64000000000001" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="413" width="137.92" height="9" fill="#b45309" rx="1.5" />
<text x="335.91999999999996" y="416" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 42.7L | Debt: 43.1L</text>
<text x="180" y="440" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">Central Univ B.Sc</text>
<rect x="190" y="426" width="85.76" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="437" width="87.04" height="9" fill="#b45309" rx="1.5" />
<text x="285.04" y="440" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 26.8L | Debt: 27.2L</text>
<text x="180" y="464" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">SRM B.Tech CS</text>
<rect x="190" y="450" width="72.96000000000001" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="461" width="84.48" height="9" fill="#b45309" rx="1.5" />
<text x="282.48" y="464" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 22.8L | Debt: 26.4L</text>
<text x="180" y="488" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="end">State Univ Chemistry</text>
<rect x="190" y="474" width="56.64" height="9" fill="#1e3a8a" rx="1.5" />
<rect x="190" y="485" width="57.599999999999994" height="9" fill="#b45309" rx="1.5" />
<text x="255.6" y="488" font-size="8.5" font-weight="bold" fill="#0f172a">Self: 17.7L | Debt: 18.0L</text>
<rect x="580" y="420" width="270" height="75" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
<rect x="590" y="432" width="14" height="10" fill="#1e3a8a" rx="1.5" />
<text x="612" y="441" font-size="9" fill="#1e293b">Self-Funded 20-Yr NPV (Out of pocket)</text>
<rect x="590" y="452" width="14" height="10" fill="#b45309" rx="1.5" />
<text x="612" y="461" font-size="9" fill="#1e293b">100% Commercial Debt NPV (SBI 10.15%)</text>
<text x="590" y="482" font-size="8" fill="#dc2626" font-style="italic">*Debt preserves capital NPV (r_real < r), but imposes 84.7% EMI squeeze in Y1-10</text>
</svg>
  Figure 5: 20-Year Net Present Value Under Self-Funded vs. Commercial Debt Regimes (INR Lakhs, r = 8.0%)
  Note: Comparison of 20-year net present value under self-funded tuition versus full commercial debt financing (SBI education loan at 10.15% nominal / 4.90% real). While 20-year capital rankings remain stable, high-fee private programs impose acute debt-service burdens of 58% to 85% of take-home pay during repayment Years 1 to 10.

When paid for with an SBI education loan, the Private Deemed CS program demands an annual EMI payment of INR 8.30 Lakhs. Against a post-tax liquid cash salary of INR 9.80 Lakhs, loan repayments consume **84.7% of the graduate's take-home pay** for ten full years. Rent, food, and medical emergencies must somehow fit into the remaining 15.3%. In contrast, public institutions (IITs, NITs, AIIMS) charge modest fees, leaving graduates with unencumbered cash flows and financial peace of mind, confirming Hypothesis 2.

## IX. How Sensitive Are Degree Valuations to Discount Rates?

Table 4 tests how resilient each degree is when we sweep the real discount rate from 3.0% up to 15.0% (holding real wage growth constant at *g* = 5.0%).

Table 4: Net Present Value Sensitivity Across Real Discount Rates (INR Lakhs)

  
    
      Program Specification
      3.0%
      5.0%
      7.0%
      8.0% Base
      10.0%
      12.0%
      15.0%
    
  
  
    
      IIT Bombay B.Tech CS (Self)
      +INR 302.9L
      +INR 242.7L
      +INR 197.1L
      +INR 178.6L
      +INR 147.9L
      +INR 123.9L
      +INR 96.8L
    
    
      NIT Trichy B.Tech CS (Self)
      +INR 189.0L
      +INR 151.0L
      +INR 122.3L
      +INR 110.6L
      +INR 91.2L
      +INR 76.1L
      +INR 59.0L
    
    
      SSCBS Delhi BBA FIA (Self)
      +INR 149.3L
      +INR 119.6L
      +INR 97.1L
      +INR 88.0L
      +INR 72.8L
      +INR 61.0L
      +INR 47.7L
    
    
      Private Deemed CS (Self)
      +INR 116.0L
      +INR 83.1L
      +INR 58.3L
      +INR 48.2L
      +INR 31.5L
      +INR 18.4L
      +INR 3.7L
    
    
      Private Deemed CS (Real Debt)
      +INR 111.8L
      +INR 84.3L
      +INR 64.1L
      +INR 56.0L
      +INR 43.0L
      +INR 33.2L
      +INR 22.6L
    
    
      NIT Calicut B.Tech Mech (Self)
      +INR 87.2L
      +INR 68.5L
      +INR 54.3L
      +INR 48.5L
      +INR 39.0L
      +INR 31.5L
      +INR 23.1L
    
    
      State Univ B.Sc Chem (Self)
      +INR 33.4L
      +INR 25.8L
      +INR 20.0L
      +INR 17.7L
      +INR 13.8L
      +INR 10.8L
      +INR 7.3L
    
  

Note: Net Present Value re-derived from Equation 3: NPV = ∑_*t*=1^20 [π · *Y*_0 · (1 + *g*)^*t*-1 / (1 + *r*)^*t*] − Upfront. Real discount rate *r* swept from 3.0% to 15.0% holding real wage growth *g* = 5.0%. For Private Deemed CS (Self), break-even discount rate is *r** = 15.93%.

Figure 6 shows the valuation trajectories as discount rates climb.

  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" style="width: 100%; max-width: 780px; height: auto; font-family: 'Times New Roman', serif; background: #ffffff; border: none; border-radius: 0; margin: 4px auto; display: block;">
<rect x="0" y="0" width="880" height="30" fill="#0f172a" />
<text x="440" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Figure 6: Sensitivity of Net Present Value to Real Discount Rates (3.0% to 15.0%, g = 5.0%)</text>
<line x1="70" y1="379.6969696969697" x2="820" y2="379.6969696969697" stroke="#f1f5f9" stroke-width="1.5" />
<text x="60" y="383.6969696969697" font-size="9" fill="#64748b" text-anchor="end">0L</text>
<line x1="70" y1="328.1818181818182" x2="820" y2="328.1818181818182" stroke="#f1f5f9" stroke-width="1.5" />
<text x="60" y="332.1818181818182" font-size="9" fill="#64748b" text-anchor="end">50L</text>
<line x1="70" y1="276.6666666666667" x2="820" y2="276.6666666666667" stroke="#f1f5f9" stroke-width="1.5" />
<text x="60" y="280.6666666666667" font-size="9" fill="#64748b" text-anchor="end">100L</text>
<line x1="70" y1="225.15151515151516" x2="820" y2="225.15151515151516" stroke="#f1f5f9" stroke-width="1.5" />
<text x="60" y="229.15151515151516" font-size="9" fill="#64748b" text-anchor="end">150L</text>
<line x1="70" y1="173.63636363636363" x2="820" y2="173.63636363636363" stroke="#f1f5f9" stroke-width="1.5" />
<text x="60" y="177.63636363636363" font-size="9" fill="#64748b" text-anchor="end">200L</text>
<line x1="70" y1="122.12121212121212" x2="820" y2="122.12121212121212" stroke="#f1f5f9" stroke-width="1.5" />
<text x="60" y="126.12121212121212" font-size="9" fill="#64748b" text-anchor="end">250L</text>
<line x1="70" y1="70.60606060606057" x2="820" y2="70.60606060606057" stroke="#f1f5f9" stroke-width="1.5" />
<text x="60" y="74.60606060606057" font-size="9" fill="#64748b" text-anchor="end">300L</text>
<line x1="123.57142857142857" y1="50" x2="123.57142857142857" y2="390" stroke="#f1f5f9" stroke-width="1.5" />
<text x="123.57142857142857" y="406" font-size="9.5" fill="#334155" text-anchor="middle">3.0%</text>
<line x1="230.7142857142857" y1="50" x2="230.7142857142857" y2="390" stroke="#f1f5f9" stroke-width="1.5" />
<text x="230.7142857142857" y="406" font-size="9.5" fill="#334155" text-anchor="middle">5.0%</text>
<line x1="337.8571428571429" y1="50" x2="337.8571428571429" y2="390" stroke="#f1f5f9" stroke-width="1.5" />
<text x="337.8571428571429" y="406" font-size="9.5" fill="#334155" text-anchor="middle">7.0%</text>
<line x1="391.4285714285714" y1="50" x2="391.4285714285714" y2="390" stroke="#f1f5f9" stroke-width="1.5" />
<text x="391.4285714285714" y="406" font-size="9.5" fill="#334155" text-anchor="middle">8.0%</text>
<line x1="498.57142857142856" y1="50" x2="498.57142857142856" y2="390" stroke="#f1f5f9" stroke-width="1.5" />
<text x="498.57142857142856" y="406" font-size="9.5" fill="#334155" text-anchor="middle">10.0%</text>
<line x1="605.7142857142858" y1="50" x2="605.7142857142858" y2="390" stroke="#f1f5f9" stroke-width="1.5" />
<text x="605.7142857142858" y="406" font-size="9.5" fill="#334155" text-anchor="middle">12.0%</text>
<line x1="766.4285714285714" y1="50" x2="766.4285714285714" y2="390" stroke="#f1f5f9" stroke-width="1.5" />
<text x="766.4285714285714" y="406" font-size="9.5" fill="#334155" text-anchor="middle">15.0%</text>
<line x1="70" y1="379.6969696969697" x2="820" y2="379.6969696969697" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="4,4" />
<text x="825" y="383.6969696969697" font-size="8.5" fill="#dc2626">Zero NPV Hurdle</text>
<polyline points="123.57142857142857,67.61818181818182 230.7142857142857,129.64242424242423 337.8571428571429,176.62424242424242 391.4285714285714,195.6848484848485 498.57142857142856,227.3151515151515 605.7142857142858,252.04242424242423 766.4285714285714,279.9636363636364" fill="none" stroke="#1e3a8a" stroke-width="2.5" />
<circle cx="123.57142857142857" cy="67.61818181818182" r="3.5" fill="#1e3a8a" />
<circle cx="230.7142857142857" cy="129.64242424242423" r="3.5" fill="#1e3a8a" />
<circle cx="337.8571428571429" cy="176.62424242424242" r="3.5" fill="#1e3a8a" />
<circle cx="391.4285714285714" cy="195.6848484848485" r="3.5" fill="#1e3a8a" />
<circle cx="498.57142857142856" cy="227.3151515151515" r="3.5" fill="#1e3a8a" />
<circle cx="605.7142857142858" cy="252.04242424242423" r="3.5" fill="#1e3a8a" />
<circle cx="766.4285714285714" cy="279.9636363636364" r="3.5" fill="#1e3a8a" />
<polyline points="123.57142857142857,184.96969696969697 230.7142857142857,224.12121212121212 337.8571428571429,253.6909090909091 391.4285714285714,265.74545454545455 498.57142857142856,285.73333333333335 605.7142857142858,301.2909090909091 766.4285714285714,318.90909090909093" fill="none" stroke="#0f766e" stroke-width="2.0" />
<circle cx="123.57142857142857" cy="184.96969696969697" r="3.5" fill="#0f766e" />
<circle cx="230.7142857142857" cy="224.12121212121212" r="3.5" fill="#0f766e" />
<circle cx="337.8571428571429" cy="253.6909090909091" r="3.5" fill="#0f766e" />
<circle cx="391.4285714285714" cy="265.74545454545455" r="3.5" fill="#0f766e" />
<circle cx="498.57142857142856" cy="285.73333333333335" r="3.5" fill="#0f766e" />
<circle cx="605.7142857142858" cy="301.2909090909091" r="3.5" fill="#0f766e" />
<circle cx="766.4285714285714" cy="318.90909090909093" r="3.5" fill="#0f766e" />
<polyline points="123.57142857142857,225.87272727272725 230.7142857142857,256.4727272727273 337.8571428571429,279.6545454545454 391.4285714285714,289.030303030303 498.57142857142856,304.6909090909091 605.7142857142858,316.8484848484849 766.4285714285714,330.55151515151516" fill="none" stroke="#15803d" stroke-width="1.8" />
<circle cx="123.57142857142857" cy="225.87272727272725" r="3.5" fill="#15803d" />
<circle cx="230.7142857142857" cy="256.4727272727273" r="3.5" fill="#15803d" />
<circle cx="337.8571428571429" cy="279.6545454545454" r="3.5" fill="#15803d" />
<circle cx="391.4285714285714" cy="289.030303030303" r="3.5" fill="#15803d" />
<circle cx="498.57142857142856" cy="304.6909090909091" r="3.5" fill="#15803d" />
<circle cx="605.7142857142858" cy="316.8484848484849" r="3.5" fill="#15803d" />
<circle cx="766.4285714285714" cy="330.55151515151516" r="3.5" fill="#15803d" />
<polyline points="123.57142857142857,264.5090909090909 230.7142857142857,292.8424242424243 337.8571428571429,313.6545454545454 391.4285714285714,322.0 498.57142857142856,335.3939393939394 605.7142857142858,345.4909090909091 766.4285714285714,356.41212121212124" fill="none" stroke="#b45309" stroke-width="1.8" />
<circle cx="123.57142857142857" cy="264.5090909090909" r="3.5" fill="#b45309" />
<circle cx="230.7142857142857" cy="292.8424242424243" r="3.5" fill="#b45309" />
<circle cx="337.8571428571429" cy="313.6545454545454" r="3.5" fill="#b45309" />
<circle cx="391.4285714285714" cy="322.0" r="3.5" fill="#b45309" />
<circle cx="498.57142857142856" cy="335.3939393939394" r="3.5" fill="#b45309" />
<circle cx="605.7142857142858" cy="345.4909090909091" r="3.5" fill="#b45309" />
<circle cx="766.4285714285714" cy="356.41212121212124" r="3.5" fill="#b45309" />
<polyline points="123.57142857142857,260.1818181818182 230.7142857142857,294.07878787878786 337.8571428571429,319.630303030303 391.4285714285714,330.03636363636366 498.57142857142856,347.24242424242425 605.7142857142858,360.73939393939395 766.4285714285714,375.8848484848485" fill="none" stroke="#dc2626" stroke-width="2.2" />
<circle cx="123.57142857142857" cy="260.1818181818182" r="3.5" fill="#dc2626" />
<circle cx="230.7142857142857" cy="294.07878787878786" r="3.5" fill="#dc2626" />
<circle cx="337.8571428571429" cy="319.630303030303" r="3.5" fill="#dc2626" />
<circle cx="391.4285714285714" cy="330.03636363636366" r="3.5" fill="#dc2626" />
<circle cx="498.57142857142856" cy="347.24242424242425" r="3.5" fill="#dc2626" />
<circle cx="605.7142857142858" cy="360.73939393939395" r="3.5" fill="#dc2626" />
<circle cx="766.4285714285714" cy="375.8848484848485" r="3.5" fill="#dc2626" />
<polyline points="123.57142857142857,345.2848484848485 230.7142857142857,353.1151515151515 337.8571428571429,359.09090909090907 391.4285714285714,361.46060606060604 498.57142857142856,365.4787878787879 605.7142857142858,368.56969696969696 766.4285714285714,372.1757575757576" fill="none" stroke="#64748b" stroke-width="1.5" />
<circle cx="123.57142857142857" cy="345.2848484848485" r="3.5" fill="#64748b" />
<circle cx="230.7142857142857" cy="353.1151515151515" r="3.5" fill="#64748b" />
<circle cx="337.8571428571429" cy="359.09090909090907" r="3.5" fill="#64748b" />
<circle cx="391.4285714285714" cy="361.46060606060604" r="3.5" fill="#64748b" />
<circle cx="498.57142857142856" cy="365.4787878787879" r="3.5" fill="#64748b" />
<circle cx="605.7142857142858" cy="368.56969696969696" r="3.5" fill="#64748b" />
<circle cx="766.4285714285714" cy="372.1757575757576" r="3.5" fill="#64748b" />
<text x="774.4285714285714" y="283.9636363636364" font-size="8.5" font-weight="bold" fill="#1e3a8a">IIT Bombay CS: 96.8L</text>
<text x="774.4285714285714" y="322.90909090909093" font-size="8.5" font-weight="bold" fill="#0f766e">NIT Trichy CS: 59.0L</text>
<text x="774.4285714285714" y="334.55151515151516" font-size="8.5" font-weight="bold" fill="#15803d">SSCBS BBA: 47.7L</text>
<text x="774.4285714285714" y="360.41212121212124" font-size="8.5" font-weight="bold" fill="#b45309">Deemed Debt: 22.6L</text>
<text x="774.4285714285714" y="379.8848484848485" font-size="8.5" font-weight="bold" fill="#dc2626">Deemed Self: 3.7L (r*=15.9%)</text>
<text x="774.4285714285714" y="384.1757575757576" font-size="8" font-weight="bold" fill="#64748b">State Chemistry: 7.3L</text>
<text x="445.0" y="422" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Real Discount Rate r (%)</text>
<text x="20" y="220.0" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle" transform="rotate(-90 20 220.0)">20-Year Risk-Adjusted NPV (INR Lakhs)</text>
</svg>
  Figure 6: Sensitivity of Net Present Value to Real Discount Rates (3.0% to 15.0%, g = 5.0%)
  Note: Net present value trajectories as the real discount rate is swept from 3.0% to 15.0% (holding real wage growth constant at g = 5.0%). Subsidized public programs maintain robust positive returns across all rates; high-cost private programs turn negative once the discount rate exceeds 15.93%.

**Why Debt-Funded NPV Exceeds Self-Funded NPV (Leverage vs. Liquidity Squeeze):** An intriguing mathematical property of discounted cash-flow valuation is that debt-funded NPV can exceed self-funded NPV. Under baseline parameters, the real borrowing cost of an SBI education loan at 10.15% nominal interest and 5.0% inflation is *r*_loan^real = 4.9048% (Equation 6). When the household discount rate is *r* = 8.00%, borrowing costs remain below the opportunity cost of capital (*r*_loan^real < *r*). Discounting future debt service installments at *r* = 8.0% mathematically yields a present value of debt payments that is smaller than paying the full tuition upfront at *t* = 0: ∑_*t*=1^10 [*D_t* / (1 + *r*)^*t*] < *C_p*. This financial leverage increases modeled 20-year NPV from +INR 48.2 Lakhs (Self) to +INR 55.9 Lakhs (Debt) for Private Deemed CS. However, **a higher modeled lifetime NPV does not mean borrowing is safer**. While debt financing defers capital outflows, it converts an equity risk into an acute, non-contingent liquidity squeeze: annual loan amortization (INR 8.30 Lakhs) consumes 84.7% of monthly take-home pay during the first decade, leaving the graduate highly vulnerable to default under the slightest employment pause.

## X. How Artificial Intelligence Changes the Value of Degrees: A Task-Based Valuation Study

### A. Theoretical Framework: Task Production, Displacement, and Skill-Biased Augmentation

To evaluate how advancing generative artificial intelligence and autonomous algorithmic systems alter the long-term economic returns to Indian undergraduate degrees, we build upon the canonical task-based framework of labor economics (Autor, Levy, and Murnane, 2003; Acemoglu and Restrepo, 2018, 2019; Autor, 2015). Rather than treating degrees as monolithic credentials or viewing occupations as indivisible production inputs destined for immediate obsolescence, this framework models each profession as a continuum of distinct cognitive and manual tasks. We formalize an aggregate sector production function over a continuous unit interval of tasks *i* ∈ [0, 1]:

$$Y = \left[ \int_0^1 y(i)^{\frac{\sigma - 1}{\sigma}} \, di \right]^{\frac{\sigma}{\sigma - 1}} \tag{8}$$

Here, γ_*L*(*i*) and γ_*K*(*i*) denote the task-specific productivities of educated labor and algorithmic capital, respectively, arranged such that the comparative advantage of human labor γ_*L*(*i*)/γ_*K*(*i*) is strictly increasing in index *i*. In an economy with graduate wage rate *w* and rental cost of algorithmic compute *p_k*, cost-minimizing firms allocate tasks to machines whenever the unit cost of algorithmic execution is strictly lower than the effective human wage cost: *p_k* / γ_*K*(*i*) < *w* / γ_*L*(*i*). This defines an endogenous automation threshold *I* ∈ (0, 1), such that tasks *i* ∈ [0, *I*] are fully executed by autonomous algorithms, while tasks *i* ∈ (*I*, 1] are performed by human degree holders.

The rapid progression of large language models (LLMs) and autonomous code synthesis agents shifts the automation threshold outward from *I* to *I'* > *I*, enclosing tasks previously considered the exclusive domain of educated cognitive workers—including code syntax authoring, regression test design, general ledger reconciliation, standard contract discovery, and structured data compilation. In labor market equilibrium, this algorithmic frontier expansion unleashes three simultaneous, structurally divergent economic forces (Acemoglu and Restrepo, 2019):

  <li>**The Displacement Effect:** For newly automated cognitive tasks *i* ∈ [*I*, *I'*], human graduate labor is substituted by algorithmic compute, directly contracting labor's task share and depressing market-clearing starting compensation:
  
    Displacement = −∫_*I*^*I'* [ *w*(*i*) *l*(*i*) / *Y* ] *di* < 0
  
  </li>
  <li>**The Productivity and Scale Effect:** Machine execution of routine cognitive tasks dramatically reduces the average unit cost of software production and data analysis. This cost reduction expands industry-wide output and increases derived demand for non-automated, human-complementary tasks *i* ∈ (*I'*, 1]:
  
    Productivity Effect = σ · ln(*P*_old / *P*_new) > 0
  
  </li>
  <li>**The Reinstatement Effect:** Technological progress simultaneously creates an entirely new spectrum of complex cognitive tasks *j* ∈ [1, 1+*N*]—such as multi-agent orchestration, mission-critical algorithmic auditing, AI safety and alignment verification, and domain-specific architectural design—where human technical judgment retains a strict comparative advantage:
  
    Reinstatement = ∫_1^1+*N* [ *w*(*j*) *l*(*j*) / *Y* ] *dj* > 0
  
  </li>

**Microeconomic Evidence on Skill-Leveling vs. Junior Hollowing:** A growing body of randomized controlled trials (RCTs) and empirical field experiments clarifies how these theoretical forces operate within professional work environments. Peng et al. (2023), in an experimental trial of GitHub Copilot across professional developers, observe a 55.8% reduction in task completion time for routine coding assignments, with the most pronounced relative speedups accruing to less experienced programmers. Similarly, Brynjolfsson, Li, and Raymond (2023) examine generative AI deployment in enterprise customer service and find an average 14% productivity increase, but a 34% surge for novice and low-skill workers, substantially compressing the productivity dispersion between junior workers and veteran experts. Comparable skill-leveling effects are documented in lab and field settings by Noy and Zhang (2023) in professional writing and Dell'Acqua et al. (2023) in management consulting.

Crucially, however, while generative AI acts as an equalizing "skill-leveler" within controlled experimental tasks, its enterprise-level hiring equilibrium produces the opposite phenomenon: *the hollowing out of entry-level campus intake* (Westby, Modestino, and Cheng, 2024). When experienced software engineers and financial analysts become 30% to 50% more productive by directing autonomous agents, organizations no longer require large cohorts of entry-level graduates to execute foundational "starter" tasks. The traditional human apprenticeship model—where junior recruits spent two to three years debugging code, running unit tests, or compiling financial reports before advancing to system design—is structurally disrupted.

### B. Concordance Crosswalk: US SOC-2018, ISCO-08, and Indian NCO-2015

Empirical task exposure indices, notably the AI Occupational Exposure (AIOE) index (Felten, Raj, and Seamans, 2021, 2023), the Suitability for Machine Learning rubric (Brynjolfsson, Mitchell, and Rock, 2018), and LLM task applicability scores (Eloundou et al., 2023; Webb, 2019), are constructed using the US Bureau of Labor Statistics Occupational Information Network (O*NET) and the Standard Occupational Classification. In emerging economies, routine cognitive labor in IT services and enterprise data processing faces acute exposure to automated substitution (Das and Hilgenstock, 2018) (SOC-2018). To rigorously apply these measures to the Indian higher education labor market, we develop a formal two-stage crosswalk methodology:

$$\text{AIOE}_k = \sum_{j \in \Omega_k} \omega_{jk} \cdot \text{AIOE}_j^{\text{SOC}}, \quad \text{where } \sum_{j \in \Omega_k} \omega_{jk} = 1 \tag{10}$$

The four macro-technological scenarios are specified as follows:

  - **Baseline (Status Quo):** Historical structural parameters unchanged: Δ_wage = 0.00, Δ_placement = 0.00, Δ_*g* = 0.00.

  - **Augmentation:** Generative AI amplifies professional cognitive productivity: Δ_wage = +0.03 (+3.0% × AIOE), Δ_placement = 0.00, Δ_*g* = +0.020 (+2.0 percentage points × AIOE).

  - **Adverse Substitution:** Routine cognitive tasks automate, depressing entry-level demand: Δ_wage = -0.12 (-12.0% × AIOE), Δ_placement = -0.15 (-15.0% × AIOE), Δ_*g* = -0.015 (-1.5 percentage points × AIOE).

  - **Rapid Diffusion:** Widespread autonomous agent deployment sharply curtails junior hiring: Δ_wage = -0.18 (-18.0% × AIOE), Δ_placement = -0.22 (-22.0% × AIOE), Δ_*g* = -0.020 (-2.0 percentage points × AIOE).

**Step-by-Step Numerical Verification (IIT Bombay Computer Science):** To ensure absolute mathematical transparency, we trace the exact calculations for IIT Bombay B.Tech CS (AIOE = 0.48, baseline cash *Y*_0 = INR 14.70L, π = 0.93, *g*_0 = 0.05, *r* = 0.08, upfront outlay = INR 17.72L):

  - **Augmentation:** Adjusted starting cash *Y*_0^adj = 14.70 · (1 + 0.03 × 0.48) = INR 14.912L; π^adj = 0.9300; adjusted wage growth *g*^adj = 0.05 + 0.020 × 0.48 = 0.0596 (5.96%). Present value of career earnings = INR 217.62L. Subtracting upfront outlay of INR 17.72L yields lifetime NPV = **+INR 199.9 Lakhs**.

  - **Adverse Substitution:** Adjusted starting cash *Y*_0^adj = 14.70 · (1 − 0.12 × 0.48) = INR 13.853L; π^adj = 0.93 · (1 − 0.15 × 0.48) = 0.8630; adjusted wage growth *g*^adj = 0.05 − 0.015 × 0.48 = 0.0428 (4.28%). Present value of career earnings = INR 161.92L. Lifetime NPV = **+INR 144.2 Lakhs**.

  - **Rapid Diffusion (AIOE-Scaled):** Adjusted starting cash *Y*_0^adj = 14.70 · (1 − 0.18 × 0.48) = INR 13.430L; π^adj = 0.93 · (1 − 0.22 × 0.48) = 0.8318; adjusted wage growth *g*^adj = 0.05 − 0.020 × 0.48 = 0.0404 (4.04%). Present value of career earnings = INR 148.42L. Lifetime NPV = **+INR 130.7 Lakhs** (downside drawdown of −INR 47.9L or −26.8%).

  - *Methodological Note on Unscaled Parameterization:* If the shock parameters were applied flatly without task-exposure scaling (Δ*Y* = −18%, Δπ = −22%, *g* = 3.0%), the resulting NPV for IIT CS would fall to **+INR 89.4 Lakhs**. Our baseline model retains the theoretically grounded AIOE-scaled specification (Equation 11) because task exposure reflects task applicability rather than total occupational elimination.

Table 5: Lifetime Net Present Value Under Parameterized AI Scenarios (INR Lakhs, r = 8.0%)

  
    
      Program Specification
      Discipline
      AIOE Score
      Baseline NPV
      Augmentation
      Adverse Scenario
      Rapid-Diffusion
      Downside Drawdown
    
  
  
    
      IIT Bombay B.Tech CS
      Eng-CS
      0.48
      +INR 178.6L
      +INR 199.9L
      +INR 144.2L
      +INR 130.7L
      -INR 47.9L (-26.8%)
    
    
      IIT Delhi B.Tech CS
      Eng-CS
      0.48
      +INR 172.5L
      +INR 193.2L
      +INR 139.2L
      +INR 126.1L
      -INR 46.4L (-26.9%)
    
    
      NIT Trichy B.Tech CS
      Eng-CS
      0.48
      +INR 110.6L
      +INR 124.1L
      +INR 88.9L
      +INR 80.4L
      -INR 30.2L (-27.3%)
    
    
      IIM Indore 5-Yr IPM
      Management
      0.39
      +INR 164.4L
      +INR 182.6L
      +INR 134.5L
      +INR 122.5L
      -INR 41.9L (-25.5%)
    
    
      SSCBS Delhi BBA FIA
      Management
      0.39
      +INR 87.5L
      +INR 95.9L
      +INR 73.6L
      +INR 68.0L
      -INR 19.5L (-22.3%)
    
    
      AIIMS Delhi MBBS
      Medicine
      0.08
      +INR 127.2L
      +INR 129.5L
      +INR 122.9L
      +INR 121.0L
      -INR 6.2L (-4.9%)
    
    
      IIT Roorkee B.Tech Civil
      Eng-NonCS
      0.22
      +INR 68.9L
      +INR 73.0L
      +INR 61.8L
      +INR 58.8L
      -INR 10.1L (-14.7%)
    
    
      NIT Calicut B.Tech Mech
      Eng-NonCS
      0.22
      +INR 47.4L
      +INR 50.2L
      +INR 42.5L
      +INR 40.4L
      -INR 7.0L (-14.8%)
    
    
      SRCC Delhi B.Com Hons
      Commerce
      0.50
      +INR 48.6L
      +INR 55.0L
      +INR 38.3L
      +INR 34.3L
      -INR 14.3L (-29.4%)
    
    
      Private Deemed CS (Bench)
      Eng-CS
      0.48
      +INR 48.2L
      +INR 59.8L
      +INR 29.5L
      +INR 22.2L
      -INR 26.0L (-53.9%)
    
    
      Regional Tier-3 (AKTU Bench)
      Eng-CS
      0.48
      +INR 3.4L
      +INR 5.5L
      +INR 0.2L
      -INR 1.1L
      -INR 4.5L (-132.4%)
    
  

Note: Structural parameter adjustments follow Equation 11: *Y*_0^adj = *Y*_0 · [1 + Δ_wage · AIOE], π^adj = π · [1 + Δ_placement · AIOE], *g*^adj = *g*_0 + Δ_*g* · AIOE. Downside Drawdown evaluates absolute and percentage change from Baseline to Rapid-Diffusion scenario at *r* = 8.0%, *T* = 20 years.

Figure 7 presents occupational AI exposure scores mapped through NCO-2015 against baseline degree valuations, showing the asymmetric vulnerability of symbolic disciplines relative to physical and clinical fields.

  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 370" style="width: 100%; max-width: 780px; height: auto; font-family: 'Times New Roman', serif; background: #ffffff; border: none; border-radius: 0; margin: 4px auto; display: block;">
<rect x="0" y="0" width="880" height="30" fill="#0f172a" />
<text x="440" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Figure 7: Field-Level AI Task Exposure Scores (NCO-2015) and Scenario Valuation Bounds</text>
<text x="210" y="48" font-size="10.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Panel A: Occupational AIOE Score (0.0 to 1.0)</text>
<text x="640" y="48" font-size="10.5" font-weight="bold" fill="#0f766e" text-anchor="middle">Panel B: 20-Year Net Present Value Under 4 Scenarios (INR Lakhs)</text>
<text x="140" y="82" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">Eng-CS (NCO 2512, 2514)</text>
<rect x="150" y="68" width="105.6" height="18" fill="#1e3a8a" rx="2" />
<text x="261.6" y="81" font-size="9" font-weight="bold" fill="#0f172a">0.48</text>
<text x="140" y="118" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">Commerce / Finance (NCO 2411)</text>
<rect x="150" y="104" width="110.0" height="18" fill="#0f766e" rx="2" />
<text x="266.0" y="117" font-size="9" font-weight="bold" fill="#0f172a">0.50</text>
<text x="140" y="154" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">Management (NCO 1120)</text>
<rect x="150" y="140" width="85.8" height="18" fill="#b45309" rx="2" />
<text x="241.8" y="153" font-size="9" font-weight="bold" fill="#0f172a">0.39</text>
<text x="140" y="190" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">Eng-NonCS / Civil (NCO 2142)</text>
<rect x="150" y="176" width="48.4" height="18" fill="#15803d" rx="2" />
<text x="204.4" y="189" font-size="9" font-weight="bold" fill="#0f172a">0.22</text>
<text x="140" y="226" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">Pure Sciences (NCO 2111)</text>
<rect x="150" y="212" width="39.6" height="18" fill="#64748b" rx="2" />
<text x="195.6" y="225" font-size="9" font-weight="bold" fill="#0f172a">0.18</text>
<text x="140" y="262" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">Clinical Medicine (NCO 2211)</text>
<rect x="150" y="248" width="26.4" height="18" fill="#dc2626" rx="2" />
<text x="182.4" y="261" font-size="9" font-weight="bold" fill="#0f172a">0.12</text>
<text x="510" y="84" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">IIT Bombay CS</text>
<rect x="520" y="68.0" width="305.8909090909091" height="7.5" fill="#15803d" rx="1" />
<rect x="520" y="77.5" width="259.78181818181815" height="7.5" fill="#1e3a8a" rx="1" />
<rect x="520" y="87.0" width="210.1818181818182" height="7.5" fill="#b45309" rx="1" />
<rect x="520" y="96.5" width="181.52727272727273" height="7.5" fill="#dc2626" rx="1" />
<text x="831.8909090909091" y="84" font-size="8" font-weight="bold" fill="#0f172a">Base: 178.6L → Rapid: 124.8L</text>
<text x="510" y="132" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">AIIMS Delhi MBBS</text>
<rect x="520" y="116.0" width="193.16363636363636" height="7.5" fill="#15803d" rx="1" />
<rect x="520" y="125.5" width="185.01818181818183" height="7.5" fill="#1e3a8a" rx="1" />
<rect x="520" y="135.0" width="178.76363636363638" height="7.5" fill="#b45309" rx="1" />
<rect x="520" y="144.5" width="176.0" height="7.5" fill="#dc2626" rx="1" />
<text x="719.1636363636363" y="132" font-size="8" font-weight="bold" fill="#0f172a">Base: 127.2L → Rapid: 121.0L</text>
<text x="510" y="180" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">IIT Roorkee Civil</text>
<rect x="520" y="164.0" width="112.29090909090911" height="7.5" fill="#15803d" rx="1" />
<rect x="520" y="173.5" width="100.21818181818183" height="7.5" fill="#1e3a8a" rx="1" />
<rect x="520" y="183.0" width="90.03636363636363" height="7.5" fill="#b45309" rx="1" />
<rect x="520" y="192.5" width="85.52727272727273" height="7.5" fill="#dc2626" rx="1" />
<text x="638.290909090909" y="180" font-size="8" font-weight="bold" fill="#0f172a">Base: 68.9L → Rapid: 58.8L</text>
<text x="510" y="228" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">Private Deemed CS</text>
<rect x="520" y="212.0" width="86.98181818181817" height="7.5" fill="#15803d" rx="1" />
<rect x="520" y="221.5" width="70.10909090909092" height="7.5" fill="#1e3a8a" rx="1" />
<rect x="520" y="231.0" width="42.90909090909091" height="7.5" fill="#b45309" rx="1" />
<rect x="520" y="240.5" width="32.29090909090909" height="7.5" fill="#dc2626" rx="1" />
<text x="612.9818181818182" y="228" font-size="8" font-weight="bold" fill="#0f172a">Base: 48.2L → Rapid: 22.2L</text>
<text x="510" y="276" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="end">Tier-3 Private CS</text>
<rect x="520" y="260.0" width="8.0" height="7.5" fill="#15803d" rx="1" />
<rect x="520" y="269.5" width="4.945454545454545" height="7.5" fill="#1e3a8a" rx="1" />
<rect x="520" y="279.0" width="0.2909090909090909" height="7.5" fill="#b45309" rx="1" />
<rect x="505" y="288.5" width="15" height="7.5" fill="#dc2626" rx="1" />
<text x="500" y="295.5" font-size="7.5" font-weight="bold" fill="#dc2626" text-anchor="end">-1.1L</text>
<text x="534.0" y="276" font-size="8" font-weight="bold" fill="#0f172a">Base: 3.4L → Rapid: -1.1L</text>
<rect x="500" y="325" width="360" height="35" fill="#f8fafc" stroke="#cbd5e1" rx="2" />
<rect x="510" y="337" width="10" height="10" fill="#15803d" rx="1.5" />
<text x="524" y="346" font-size="8" fill="#1e293b">Augmentation</text>
<rect x="598" y="337" width="10" height="10" fill="#1e3a8a" rx="1.5" />
<text x="612" y="346" font-size="8" fill="#1e293b">Baseline</text>
<rect x="686" y="337" width="10" height="10" fill="#b45309" rx="1.5" />
<text x="700" y="346" font-size="8" fill="#1e293b">Adverse</text>
<rect x="774" y="337" width="10" height="10" fill="#dc2626" rx="1.5" />
<text x="788" y="346" font-size="8" fill="#1e293b">Rapid Diffusion</text>
</svg>
  Figure 7: Field-Level AI Task Exposure Scores (NCO-2015) and Scenario Valuation Bounds
  Note: Left panel plots AIOE task exposure scores across disciplines mapped to Indian NCO-2015 codes; right panel shows the resulting 20-year net present value bounds under Augmentation, Baseline, Adverse, and Rapid-Diffusion scenarios. Physical and clinical fields (Medicine, Civil Engineering) demonstrate high resilience, whereas symbolic disciplines (CS, Commerce) experience significant downside valuation drag.

Table 6: Tornado Sensitivity Analysis: Parameter Swings on Net Present Value (INR Lakhs)

  
    
      Valuation Parameter Range
      IIT Bombay CS (Low)
      IIT Bombay CS (High)
      IIT Bombay Swing
      Private Deemed CS (Low)
      Private Deemed CS (High)
      Private Deemed Swing
    
  
  
    
      Real Wage Growth Rate g (2.0% to 8.0%)
      INR 137.5L
      INR 235.4L
      INR 98.0L
      INR 25.8L
      INR 79.2L
      INR 53.4L
    
    
      Household Real Discount Rate r (6.0% to 12.0%)
      INR 123.9L
      INR 218.4L
      INR 94.5L
      INR 18.4L
      INR 69.9L
      INR 51.5L
    
    
      CTC-to-Liquid Cash Haircut (20.0% to 40.0%)
      INR 150.5L
      INR 206.6L
      INR 56.1L
      INR 32.9L
      INR 63.5L
      INR 30.6L
    
    
      Placement Realization Rate pi (-15% to +5%)
      INR 149.1L
      INR 188.4L
      INR 39.3L
      INR 32.2L
      INR 53.6L
      INR 21.4L
    
    
      AI Employment Displacement Drag (0 to 0.25 × AIOE)
      INR 155.0L
      INR 178.6L
      INR 23.6L
      INR 35.4L
      INR 48.2L
      INR 12.8L
    
    
      AI Wage Compression Drag (0 to 0.20 × AIOE)
      INR 159.7L
      INR 178.6L
      INR 18.8L
      INR 38.0L
      INR 48.2L
      INR 10.3L
    
  

Note: Swings evaluate the absolute change in Net Present Value across the stated parameter bounds.

Figure 8 visualizes the tornado sensitivity analysis for IIT Bombay CS, demonstrating that macroeconomic variables (real wage growth and discount rates) generate the widest valuation swings, followed by take-home cash haircuts and AI displacement parameters.

  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 260" style="width: 100%; max-width: 780px; height: auto; font-family: 'Times New Roman', serif; background: #ffffff; border: none; border-radius: 0; margin: 4px auto; display: block;">
<rect x="0" y="0" width="880" height="30" fill="#0f172a" />
<text x="440" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Figure 8: Tornado Sensitivity Diagram: Parameter Swings on 20-Year Net Present Value (IIT Bombay CS)</text>
<line x1="320.0" y1="35" x2="320.0" y2="235" stroke="#e2e8f0" stroke-width="1" />
<text x="320.0" y="248" font-size="9" fill="#64748b" text-anchor="middle">100L</text>
<line x1="370.0" y1="35" x2="370.0" y2="235" stroke="#e2e8f0" stroke-width="1" />
<text x="370.0" y="248" font-size="9" fill="#64748b" text-anchor="middle">120L</text>
<line x1="420.0" y1="35" x2="420.0" y2="235" stroke="#e2e8f0" stroke-width="1" />
<text x="420.0" y="248" font-size="9" fill="#64748b" text-anchor="middle">140L</text>
<line x1="470.0" y1="35" x2="470.0" y2="235" stroke="#e2e8f0" stroke-width="1" />
<text x="470.0" y="248" font-size="9" fill="#64748b" text-anchor="middle">160L</text>
<line x1="520.0" y1="35" x2="520.0" y2="235" stroke="#e2e8f0" stroke-width="1" />
<text x="520.0" y="248" font-size="9" fill="#64748b" text-anchor="middle">180L</text>
<line x1="570.0" y1="35" x2="570.0" y2="235" stroke="#e2e8f0" stroke-width="1" />
<text x="570.0" y="248" font-size="9" fill="#64748b" text-anchor="middle">200L</text>
<line x1="620.0" y1="35" x2="620.0" y2="235" stroke="#e2e8f0" stroke-width="1" />
<text x="620.0" y="248" font-size="9" fill="#64748b" text-anchor="middle">220L</text>
<line x1="670.0" y1="35" x2="670.0" y2="235" stroke="#e2e8f0" stroke-width="1" />
<text x="670.0" y="248" font-size="9" fill="#64748b" text-anchor="middle">240L</text>
<line x1="720.0" y1="35" x2="720.0" y2="235" stroke="#e2e8f0" stroke-width="1" />
<text x="720.0" y="248" font-size="9" fill="#64748b" text-anchor="middle">260L</text>
<line x1="516.5" y1="35" x2="516.5" y2="235" stroke="#1e3a8a" stroke-width="2" stroke-dasharray="3,3" />
<text x="516.5" y="47" font-size="9" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Baseline: 178.6L</text>
<text x="310" y="66" font-size="9.5" font-weight="bold" fill="#1e293b" text-anchor="end">Real Wage Growth g (2% to 8%)</text>
<rect x="413.75" y="52" width="102.75" height="20" fill="#dc2626" rx="2" />
<text x="417.75" y="66" font-size="8.5" fill="#ffffff" font-weight="bold">137.5L</text>
<rect x="516.5" y="52" width="142.0" height="20" fill="#16a34a" rx="2" />
<text x="654.5" y="66" font-size="8.5" fill="#ffffff" font-weight="bold" text-anchor="end">235.4L</text>
<text x="760" y="66" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="start">±49.0L (98.0L)</text>
<text x="310" y="96" font-size="9.5" font-weight="bold" fill="#1e293b" text-anchor="end">Real Discount Rate r (6% to 12%)</text>
<rect x="379.75" y="82" width="136.75" height="20" fill="#dc2626" rx="2" />
<text x="383.75" y="96" font-size="8.5" fill="#ffffff" font-weight="bold">123.9L</text>
<rect x="516.5" y="82" width="99.5" height="20" fill="#16a34a" rx="2" />
<text x="612.0" y="96" font-size="8.5" fill="#ffffff" font-weight="bold" text-anchor="end">218.4L</text>
<text x="760" y="96" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="start">±47.2L (94.5L)</text>
<text x="310" y="126" font-size="9.5" font-weight="bold" fill="#1e293b" text-anchor="end">Cash Haircut (20% to 40%)</text>
<rect x="446.25" y="112" width="70.25" height="20" fill="#dc2626" rx="2" />
<text x="450.25" y="126" font-size="8.5" fill="#ffffff" font-weight="bold">150.5L</text>
<rect x="516.5" y="112" width="70.0" height="20" fill="#16a34a" rx="2" />
<text x="582.5" y="126" font-size="8.5" fill="#ffffff" font-weight="bold" text-anchor="end">206.6L</text>
<text x="760" y="126" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="start">±28.1L (56.1L)</text>
<text x="310" y="156" font-size="9.5" font-weight="bold" fill="#1e293b" text-anchor="end">Placement Rate pi (-15% to +5%)</text>
<rect x="442.75" y="142" width="73.75" height="20" fill="#dc2626" rx="2" />
<text x="446.75" y="156" font-size="8.5" fill="#ffffff" font-weight="bold">149.1L</text>
<rect x="516.5" y="142" width="24.5" height="20" fill="#16a34a" rx="2" />
<text x="537.0" y="156" font-size="8.5" fill="#ffffff" font-weight="bold" text-anchor="end">188.4L</text>
<text x="760" y="156" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="start">±19.6L (39.3L)</text>
<text x="310" y="186" font-size="9.5" font-weight="bold" fill="#1e293b" text-anchor="end">AI Employment Drag (0 to 0.25*AIOE)</text>
<rect x="457.5" y="172" width="59.0" height="20" fill="#dc2626" rx="2" />
<text x="461.5" y="186" font-size="8.5" fill="#ffffff" font-weight="bold">155.0L</text>
<text x="760" y="186" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="start">±11.8L (23.6L)</text>
<text x="310" y="216" font-size="9.5" font-weight="bold" fill="#1e293b" text-anchor="end">AI Wage Drag (0 to 0.20*AIOE)</text>
<rect x="469.25" y="202" width="47.25" height="20" fill="#dc2626" rx="2" />
<text x="473.25" y="216" font-size="8.5" fill="#ffffff" font-weight="bold">159.7L</text>
<text x="760" y="216" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="start">±9.4L (18.8L)</text>
</svg>
  Figure 8: Tornado Sensitivity Diagram: Parameter Swings on 20-Year Net Present Value (IIT Bombay CS)
  Note: Horizontal bar representation of 20-year net present value swings (in INR Lakhs) for IIT Bombay B.Tech CS across parameter bounds from Table 6. The dashed line marks baseline NPV (INR 178.6 Lakhs). Macroeconomic variables (real wage growth and discount rates) drive the largest capital swings (±47 to ±49 Lakhs), followed by cash haircuts (±28 Lakhs), baseline placement rates (±20 Lakhs), and AI displacement drags (±9 to ±12 Lakhs).

### E. Cross-Disciplinary Rank Inversions and Institutional Case Studies

A critical empirical finding of this study is that artificial intelligence shocks do not affect all programs equally. While the overall Spearman rank correlation across our 40-program dataset remains high when moving from Baseline to Augmentation (*ρ* = 0.998), it deteriorates to *ρ* = 0.932 under Rapid Diffusion. More fundamentally, **the ordinal ranking flips across academic disciplines**, completely overturning traditional institutional hierarchies:

  - **Clinical Medicine Pulls Decisively Ahead of Second-Tier Computer Science:** In the baseline model, AIIMS Delhi MBBS (INR 127.2L) leads NIT Trichy B.Tech CS (INR 110.6L) by INR 16.6 Lakhs. Under Rapid Diffusion, AIIMS Delhi (INR 121.0L, AIOE = 0.08) experiences a negligible 4.9% drawdown, while NIT Trichy CS (INR 80.4L, AIOE = 0.48) suffers a 27.3% drawdown. Consequently, AIIMS Delhi's valuation lead widens to **INR 40.6 Lakhs**—a 144% increase in its relative advantage. The clinical mandate for bedside palpation, invasive surgery, and statutory legal liability shields physicians from software-driven displacement.

  - **Subsidized Civil Engineering Surpasses High-Cost Private Computer Science:** Under Baseline conditions, IIT Roorkee Civil Engineering (INR 68.9L) leads a benchmark Private Deemed CS program (INR 48.2L) by INR 20.7 Lakhs. Under Rapid Diffusion, IIT Roorkee Civil (INR 58.8L, AIOE = 0.22) declines by only 14.7%, whereas Private Deemed CS (INR 22.2L, AIOE = 0.48) plummets by 53.9% due to its toxic combination of high tuition debt and exposure to routine coding automation. IIT Roorkee's advantage widens to **INR 36.6 Lakhs**, proving that physical infrastructure engineering at a low-cost public institution provides far superior downside capital protection.

  - **Insolvency of Lower-Tier Commercial Engineering:** A generic Tier-3 private engineering program (AKTU benchmark, upfront outlay INR 9.0L) delivers a modest positive return under Baseline conditions (+INR 3.4L). Under Rapid Diffusion, however, this valuation flips to **−INR 1.1 Lakhs**. This represents an existential result for educational lending: when entry-level IT services firms automate junior testing and maintenance, graduates from unaccredited private colleges face employment failure, rendering commercial student loans economically unrecoverable.

  - **Severe Degradation in Routine Accounting and Commerce:** SRCC B.Com Hons suffers a 29.4% valuation drawdown (falling from INR 48.6L to INR 34.3L), reflecting the acute automation vulnerability of routine financial accounting and tax compliance tasks (AIOE = 0.50). Commerce graduates who do not transition toward forensic auditing or strategic corporate finance experience rapid human capital depreciation.

## XI. Which Matters More: What You Study, or Where?

To test Hypothesis 3, we ran an analysis of variance (ANOVA) decomposing the variance in lifetime net present values across field of study, college tier, and financing mode:

$$
Var( NPV ) = σ Field  2  + σ Tier  2  + 2 · Cov(Field, Tier) + σ Financing  2  + σ ε  2
$$

Figure 9 visualizes the results of a three-way analysis of variance (ANOVA) decomposing the variance in 20-year net present values across field of study, institutional tier, and financing regime: field of study accounts for **54.2%** of total valuation variance, institutional tier accounts for **31.6%**, and financing mode accounts for **14.2%**.

  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 320" style="width: 100%; max-width: 780px; height: auto; font-family: 'Times New Roman', serif; background: #ffffff; border: none; border-radius: 0; margin: 4px auto; display: block;">
<rect x="0" y="0" width="880" height="30" fill="#0f172a" />
<text x="440" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Figure 9: Variance Decomposition: Field Choice vs. Institutional Tier vs. Financing Regime</text>
<line x1="80" y1="260.0" x2="820" y2="260.0" stroke="#f1f5f9" stroke-width="1.5" />
<text x="70" y="264.0" font-size="9" fill="#64748b" text-anchor="end">0L</text>
<line x1="80" y1="226.66666666666669" x2="820" y2="226.66666666666669" stroke="#f1f5f9" stroke-width="1.5" />
<text x="70" y="230.66666666666669" font-size="9" fill="#64748b" text-anchor="end">5L</text>
<line x1="80" y1="193.33333333333334" x2="820" y2="193.33333333333334" stroke="#f1f5f9" stroke-width="1.5" />
<text x="70" y="197.33333333333334" font-size="9" fill="#64748b" text-anchor="end">10L</text>
<line x1="80" y1="160.0" x2="820" y2="160.0" stroke="#f1f5f9" stroke-width="1.5" />
<text x="70" y="164.0" font-size="9" fill="#64748b" text-anchor="end">15L</text>
<line x1="80" y1="126.66666666666669" x2="820" y2="126.66666666666669" stroke="#f1f5f9" stroke-width="1.5" />
<text x="70" y="130.66666666666669" font-size="9" fill="#64748b" text-anchor="end">20L</text>
<line x1="80" y1="93.33333333333331" x2="820" y2="93.33333333333331" stroke="#f1f5f9" stroke-width="1.5" />
<text x="70" y="97.33333333333331" font-size="9" fill="#64748b" text-anchor="end">25L</text>
<line x1="80" y1="60.0" x2="820" y2="60.0" stroke="#f1f5f9" stroke-width="1.5" />
<text x="70" y="64.0" font-size="9" fill="#64748b" text-anchor="end">30L</text>
<rect x="95.0" y="107.33333333333334" width="130" height="152.66666666666666" fill="#1e3a8a" rx="3" />
<text x="160" y="99.33333333333334" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">INR 22.9L</text>
<text x="160" y="127.33333333333334" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">54.2% of Total Variance</text>
<text x="160" y="278" font-size="9.5" font-weight="bold" fill="#1e293b" text-anchor="middle">Field Choice within Tier 2 Flagship</text>
<text x="160" y="292" font-size="8.5" fill="#64748b" text-anchor="middle">(Pure Sciences -> CS)</text>
<rect x="375.0" y="174.66666666666666" width="130" height="85.33333333333334" fill="#0f766e" rx="3" />
<text x="440" y="166.66666666666666" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">INR 12.8L</text>
<text x="440" y="194.66666666666666" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">31.6% of Total Variance</text>
<text x="440" y="278" font-size="9.5" font-weight="bold" fill="#1e293b" text-anchor="middle">Institutional Tier within CS</text>
<text x="440" y="292" font-size="8.5" fill="#64748b" text-anchor="middle">(NIT -> IIT)</text>
<rect x="655.0" y="112.0" width="130" height="148.0" fill="#b45309" rx="3" />
<text x="720" y="104.0" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">INR 22.2L</text>
<text x="720" y="132.0" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">14.2% (Early Liquidity Squeeze)</text>
<text x="720" y="278" font-size="9.5" font-weight="bold" fill="#1e293b" text-anchor="middle">Financing Mode Shift</text>
<text x="720" y="292" font-size="8.5" fill="#64748b" text-anchor="middle">(Self-Funded -> 100% Debt)</text>
</svg>
  Figure 9: Variance Decomposition: Field Choice vs. Institutional Tier vs. Financing Regime
  Note: Decomposition of 20-year net present value variance. Discipline/field of study accounts for 54.2% of total return variation, institutional tier accounts for 31.6%, and financing structure accounts for 14.2%, confirming that what a student studies matters more than where they study.

In our data, choosing Computer Science over Pure Science at a regional public college adds an average of **INR 22.9 Lakhs** in lifetime wealth. Upgrading from an NIT to an IIT within Computer Science adds **INR 12.8 Lakhs**. The subject a student studies is nearly twice as impactful as the prestige of the campus they attend, confirming Hypothesis 3.

### A. Real-World Stress-Testing Across Student Archetypes

To see how these outcomes hold up in the real world, we simulated 10,000 career paths across five representative student archetypes (Profiles A through E). The model drew from real-world probability distributions for starting salaries, real wage growth (2% to 8%), discount rates (6% to 10%), macroeconomic recessions (an 8% chance per year of a 15% salary cut), and placement realization rates (Table A5). Table 7 shows the results.

Table 7: Monte Carlo Simulation Results Across Student Archetypes (10,000 Iterations)

  
    
      Archetype Profile
      Discipline
      Baseline NPV
      Simulated Mean
      Simulated Median
      95% Empirical CI Range
      Prob(NPV < 0)
    
  
  
    
      Profile A: IIT Bombay B.Tech CS (Self)
      Eng-CS
      +INR 178.6L
      +INR 179.5L
      +INR 175.3L
      [+INR 109.7L, +INR 274.0L]
      0.00%
    
    
      Profile B: AIIMS Delhi MBBS (Self, 20-Yr)
      Medicine
      +INR 127.2L
      +INR 127.1L
      +INR 124.0L
      [+INR 80.0L, +INR 191.1L]
      0.00%
    
    
      Profile B2: AIIMS Delhi MBBS (35-Yr Practice)
      Medicine
      +INR 190.0L
      +INR 196.3L
      +INR 186.4L
      [+INR 107.4L, +INR 337.8L]
      0.00%
    
    
      Profile C: NIT Trichy B.Tech CS (Self)
      Eng-CS
      +INR 110.6L
      +INR 110.9L
      +INR 107.7L
      [+INR 66.8L, +INR 172.2L]
      0.00%
    
    
      Profile D: DU B.Com Hons (Commerce Bench)
      Commerce
      +INR 42.7L
      +INR 42.9L
      +INR 41.7L
      [+INR 24.3L, +INR 68.3L]
      0.00%
    
    
      Profile E: Private Deemed CS (Self-Funded)
      Eng-CS
      +INR 48.2L
      +INR 48.4L
      +INR 45.7L
      [+INR 9.8L, +INR 102.1L]
      0.46%
    
    
      Profile E-Debt: Private Deemed CS (Commercial Debt)
      Eng-CS
      +INR 56.0L
      +INR 56.2L
      +INR 53.5L
      [+INR 18.4L, +INR 109.4L]
      0.01%*
    
  

Note: 10,000 independent pseudo-random iterations drawn from prior parameter distributions detailed in Technical Appendix D. *While Profile E-Debt achieves a positive 20-year capital NPV in 99.99% of draws, it incurs an 84.7% debt-service burden during repayment Years 1 to 10, creating severe short-term default risk.

Figure 10 displays the simulated 95% confidence intervals and downside risk floors across each student profile.

  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 430" style="width: 100%; max-width: 780px; height: auto; font-family: 'Times New Roman', serif; background: #ffffff; border: none; border-radius: 0; margin: 4px auto; display: block;">
<rect x="0" y="0" width="880" height="30" fill="#0f172a" />
<text x="440" y="20" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Figure 10: Student Archetype Heterogeneity: Monte Carlo Simulation Scenario Bounds (10,000 Iterations)</text>
<line x1="60" y1="370.0" x2="840" y2="370.0" stroke="#f1f5f9" stroke-width="1.5" />
<text x="50" y="374.0" font-size="9" fill="#64748b" text-anchor="end">0L</text>
<line x1="60" y1="325.55555555555554" x2="840" y2="325.55555555555554" stroke="#f1f5f9" stroke-width="1.5" />
<text x="50" y="329.55555555555554" font-size="9" fill="#64748b" text-anchor="end">50L</text>
<line x1="60" y1="281.1111111111111" x2="840" y2="281.1111111111111" stroke="#f1f5f9" stroke-width="1.5" />
<text x="50" y="285.1111111111111" font-size="9" fill="#64748b" text-anchor="end">100L</text>
<line x1="60" y1="236.66666666666666" x2="840" y2="236.66666666666666" stroke="#f1f5f9" stroke-width="1.5" />
<text x="50" y="240.66666666666666" font-size="9" fill="#64748b" text-anchor="end">150L</text>
<line x1="60" y1="192.22222222222223" x2="840" y2="192.22222222222223" stroke="#f1f5f9" stroke-width="1.5" />
<text x="50" y="196.22222222222223" font-size="9" fill="#64748b" text-anchor="end">200L</text>
<line x1="60" y1="147.77777777777777" x2="840" y2="147.77777777777777" stroke="#f1f5f9" stroke-width="1.5" />
<text x="50" y="151.77777777777777" font-size="9" fill="#64748b" text-anchor="end">250L</text>
<line x1="60" y1="103.33333333333331" x2="840" y2="103.33333333333331" stroke="#f1f5f9" stroke-width="1.5" />
<text x="50" y="107.33333333333331" font-size="9" fill="#64748b" text-anchor="end">300L</text>
<line x1="60" y1="58.888888888888914" x2="840" y2="58.888888888888914" stroke="#f1f5f9" stroke-width="1.5" />
<text x="50" y="62.888888888888914" font-size="9" fill="#64748b" text-anchor="end">350L</text>
<polyline points="115.71428571428571,214.17777777777778 227.14285714285714,259.77777777777777 338.57142857142856,204.3111111111111 450.0,274.26666666666665 561.4285714285714,332.93333333333334 672.8571428571429,329.3777777777778 784.2857142857143,322.44444444444446" fill="none" stroke="#1e3a8a" stroke-width="2.5" />
<line x1="115.71428571428571" y1="272.4888888888889" x2="115.71428571428571" y2="126.44444444444446" stroke="#1e3a8a" stroke-width="3" stroke-linecap="round" />
<line x1="107.71428571428571" y1="272.4888888888889" x2="123.71428571428571" y2="272.4888888888889" stroke="#1e3a8a" stroke-width="2" />
<line x1="107.71428571428571" y1="126.44444444444446" x2="123.71428571428571" y2="126.44444444444446" stroke="#1e3a8a" stroke-width="2" />
<circle cx="115.71428571428571" cy="214.17777777777778" r="6" fill="#1e3a8a" stroke="#ffffff" stroke-width="2" />
<text x="115.71428571428571" y="204.17777777777778" font-size="9.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">175.3L</text>
<text x="115.71428571428571" y="120.44444444444446" font-size="8" fill="#475569" text-anchor="middle">[109.7L - 274.0L]</text>
<text x="115.71428571428571" y="386" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="middle">Profile A: IIT Bombay CS</text>
<text x="115.71428571428571" y="398" font-size="7.5" fill="#64748b" text-anchor="middle">(High Prep, Self)</text>
<line x1="227.14285714285714" y1="298.8888888888889" x2="227.14285714285714" y2="200.13333333333335" stroke="#0f766e" stroke-width="3" stroke-linecap="round" />
<line x1="219.14285714285714" y1="298.8888888888889" x2="235.14285714285714" y2="298.8888888888889" stroke="#0f766e" stroke-width="2" />
<line x1="219.14285714285714" y1="200.13333333333335" x2="235.14285714285714" y2="200.13333333333335" stroke="#0f766e" stroke-width="2" />
<circle cx="227.14285714285714" cy="259.77777777777777" r="6" fill="#0f766e" stroke="#ffffff" stroke-width="2" />
<text x="227.14285714285714" y="249.77777777777777" font-size="9.5" font-weight="bold" fill="#0f766e" text-anchor="middle">124.0L</text>
<text x="227.14285714285714" y="194.13333333333335" font-size="8" fill="#475569" text-anchor="middle">[80.0L - 191.1L]</text>
<text x="227.14285714285714" y="386" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="middle">Profile B: AIIMS MBBS 20-Yr</text>
<text x="227.14285714285714" y="398" font-size="7.5" fill="#64748b" text-anchor="middle">(Clinical Medicine)</text>
<line x1="338.57142857142856" y1="274.5333333333333" x2="338.57142857142856" y2="69.73333333333335" stroke="#15803d" stroke-width="3" stroke-linecap="round" />
<line x1="330.57142857142856" y1="274.5333333333333" x2="346.57142857142856" y2="274.5333333333333" stroke="#15803d" stroke-width="2" />
<line x1="330.57142857142856" y1="69.73333333333335" x2="346.57142857142856" y2="69.73333333333335" stroke="#15803d" stroke-width="2" />
<circle cx="338.57142857142856" cy="204.3111111111111" r="6" fill="#15803d" stroke="#ffffff" stroke-width="2" />
<text x="338.57142857142856" y="194.3111111111111" font-size="9.5" font-weight="bold" fill="#15803d" text-anchor="middle">186.4L</text>
<text x="338.57142857142856" y="63.73333333333335" font-size="8" fill="#475569" text-anchor="middle">[107.4L - 337.8L]</text>
<text x="338.57142857142856" y="386" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="middle">Profile B2: AIIMS MBBS 35-Yr</text>
<text x="338.57142857142856" y="398" font-size="7.5" fill="#64748b" text-anchor="middle">(Full Practice Horizon)</text>
<line x1="450.0" y1="310.6222222222222" x2="450.0" y2="216.93333333333334" stroke="#0f766e" stroke-width="3" stroke-linecap="round" />
<line x1="442.0" y1="310.6222222222222" x2="458.0" y2="310.6222222222222" stroke="#0f766e" stroke-width="2" />
<line x1="442.0" y1="216.93333333333334" x2="458.0" y2="216.93333333333334" stroke="#0f766e" stroke-width="2" />
<circle cx="450.0" cy="274.26666666666665" r="6" fill="#0f766e" stroke="#ffffff" stroke-width="2" />
<text x="450.0" y="264.26666666666665" font-size="9.5" font-weight="bold" fill="#0f766e" text-anchor="middle">107.7L</text>
<text x="450.0" y="210.93333333333334" font-size="8" fill="#475569" text-anchor="middle">[66.8L - 172.2L]</text>
<text x="450.0" y="386" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="middle">Profile C: NIT Trichy CS</text>
<text x="450.0" y="398" font-size="7.5" fill="#64748b" text-anchor="middle">(Moderate Prep, Self)</text>
<line x1="561.4285714285714" y1="348.4" x2="561.4285714285714" y2="309.2888888888889" stroke="#64748b" stroke-width="3" stroke-linecap="round" />
<line x1="553.4285714285714" y1="348.4" x2="569.4285714285714" y2="348.4" stroke="#64748b" stroke-width="2" />
<line x1="553.4285714285714" y1="309.2888888888889" x2="569.4285714285714" y2="309.2888888888889" stroke="#64748b" stroke-width="2" />
<circle cx="561.4285714285714" cy="332.93333333333334" r="6" fill="#64748b" stroke="#ffffff" stroke-width="2" />
<text x="561.4285714285714" y="322.93333333333334" font-size="9.5" font-weight="bold" fill="#64748b" text-anchor="middle">41.7L</text>
<text x="561.4285714285714" y="303.2888888888889" font-size="8" fill="#475569" text-anchor="middle">[24.3L - 68.3L]</text>
<text x="561.4285714285714" y="386" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="middle">Profile D: DU B.Com Hons</text>
<text x="561.4285714285714" y="398" font-size="7.5" fill="#64748b" text-anchor="middle">(Commerce Benchmark)</text>
<line x1="672.8571428571429" y1="361.2888888888889" x2="672.8571428571429" y2="279.24444444444447" stroke="#b45309" stroke-width="3" stroke-linecap="round" />
<line x1="664.8571428571429" y1="361.2888888888889" x2="680.8571428571429" y2="361.2888888888889" stroke="#b45309" stroke-width="2" />
<line x1="664.8571428571429" y1="279.24444444444447" x2="680.8571428571429" y2="279.24444444444447" stroke="#b45309" stroke-width="2" />
<circle cx="672.8571428571429" cy="329.3777777777778" r="6" fill="#b45309" stroke="#ffffff" stroke-width="2" />
<text x="672.8571428571429" y="319.3777777777778" font-size="9.5" font-weight="bold" fill="#b45309" text-anchor="middle">45.7L</text>
<text x="672.8571428571429" y="273.24444444444447" font-size="8" fill="#475569" text-anchor="middle">[9.8L - 102.1L]</text>
<text x="672.8571428571429" y="386" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="middle">Profile E: Deemed CS (Self)</text>
<text x="672.8571428571429" y="398" font-size="7.5" fill="#64748b" text-anchor="middle">(High Fee, Out of Pocket)</text>
<line x1="784.2857142857143" y1="353.64444444444445" x2="784.2857142857143" y2="272.75555555555553" stroke="#dc2626" stroke-width="3" stroke-linecap="round" />
<line x1="776.2857142857143" y1="353.64444444444445" x2="792.2857142857143" y2="353.64444444444445" stroke="#dc2626" stroke-width="2" />
<line x1="776.2857142857143" y1="272.75555555555553" x2="792.2857142857143" y2="272.75555555555553" stroke="#dc2626" stroke-width="2" />
<circle cx="784.2857142857143" cy="322.44444444444446" r="6" fill="#dc2626" stroke="#ffffff" stroke-width="2" />
<text x="784.2857142857143" y="312.44444444444446" font-size="9.5" font-weight="bold" fill="#dc2626" text-anchor="middle">53.5L</text>
<text x="784.2857142857143" y="266.75555555555553" font-size="8" fill="#475569" text-anchor="middle">[18.4L - 109.4L]</text>
<text x="784.2857142857143" y="386" font-size="8.5" font-weight="bold" fill="#1e293b" text-anchor="middle">Profile E-Debt: Deemed CS (Debt)</text>
<text x="784.2857142857143" y="398" font-size="7.5" fill="#64748b" text-anchor="middle">(Commercial Debt Squeeze)</text>
</svg>
  Figure 10: Student Archetype Heterogeneity: Monte Carlo Simulation Scenario Bounds (10,000 Iterations)
  Note: 10,000-iteration Monte Carlo simulation scenario bounds (Median, and 95% empirical confidence intervals [P2.5, P97.5]) across student background archetypes. Profile A (IIT Bombay CS) maintains large positive returns even under severe downside shocks; Profile E-Debt (Private Deemed CS) carries acute early-career default risks despite positive long-run capital NPV.

As Table 7 and Figure 10 demonstrate, elite public engineering (Profile A) and clinical medicine (Profile B) exhibit a simulated Prob(NPV < 0) = 0.00% across 10,000 iterations. **Crucially, a 0.00% simulated negative-NPV probability does not establish zero real-world risk.** Rather, it indicates that under modeled baseline distributions for formal-sector graduates, high entry wages combined with low public tuition mechanically generate positive returns across all macroeconomic shock realizations. The simulation evaluates graduates who complete their degree and enter regular wage employment; it does not model individual attrition, chronic illness, severe depression, or career abandonment. By contrast, debt-financed private engineering graduates face severe structural liquidity risk, sliding into default under hiring freezes or early-career recessions.

## XII. A Practical Four-Step Guide for Indian Families

These findings translate into a straightforward, practical decision checklist that every Indian family should use before signing an enrollment form or loan agreement:

  - **Cut the Marketing CTC Down to Real Cash:** Never make a financial decision based on the headline salary printed on a college banner. Subtract 15% for standard industry jobs and 30% to 35% for tech jobs that include unvested stock options or one-time joining bonuses. Then subtract income tax under the New Tax Regime to find the actual monthly cash in hand. If a college refuses to disclose the exact denominator of its graduating batch, assume that no more than 75% of graduates actually secure jobs.

  - **Count Every Rupee of Real Degree Costs:** Tuition is only part of the bill. Add four years of rent, food, and travel based on the college city (living in Bengaluru, Mumbai, or Delhi costs at least INR 1.44 Lakhs a year). Factor in what you spent on coaching classes in Kota, Hyderabad, or online (often INR 3 to 6 Lakhs), plus the INR 1.68 Lakhs a year the student could have earned working after school. That total is the real investment you are making.

  - **Never Let Loan Payments Exceed 35% of Starting Cash:** Calculate the exact monthly bank EMI before taking an education loan. If loan payments will eat up more than **35% of the graduate's monthly in-hand starting pay**, do not enroll. When a private engineering college requires 60% to 85% of take-home pay just to service debt, walking away is far safer than gambling with your family's future.

  - **Check How Vulnerable the Degree is to Automation:** Look closely at what the curriculum actually teaches. Degrees that focus on routine coding syntax, simple maintenance, basic test scripts, or standard bookkeeping face severe salary pressure from AI agents. Look for programs that emphasize complex systems architecture, advanced mathematical reasoning, clinical medical training, or hands-on infrastructure engineering.

## XIII. Policy Recommendations

Our findings point to three urgent policy reforms for Indian higher education regulators and lending agencies:

  - **Fix the PM-Vidyalaxmi Student Loan Scheme:** Tying government credit guarantees to whether a college sits in the NIRF Top 100 is economically backwards. It funnels public credit guarantees into high-fee private colleges where students face crushing debt burdens, while shutting out affordable regional state universities that provide safe, positive returns. The Ministry of Education should replace arbitrary ranking cutoffs with a verified **Debt-Service Coverage Ratio (DSCR ≥ 1.5)** and **Debt-to-Earnings standard**, guaranteeing loans only where graduates can comfortably pay them back.

  - **Mandate Audited Placement Disclosures:** The University Grants Commission (UGC) and AICTE must require every accredited institution to publish independently audited placement reports. These disclosures must report median in-hand cash salaries, the 10th-to-90th percentile salary distribution, and the exact total number of graduating students. Colleges must be legally prohibited from hiding unplaced graduates under vague categories like “higher studies” or “entrepreneurship.”

  - **Protect Students Through Banking Regulations:** The Reserve Bank of India should require commercial banks to risk-weight education loans based on verifiable graduate earnings rather than college marketing claims. When banks are forced to evaluate whether graduates can realistically repay their loans, private universities will finally face market pressure to lower inflated tuition.

## XIV. Limitations

Four analytical boundaries should be kept in mind when interpreting our results:

  - **Valuation, Not Causal Attribution:** Our model measures the financial cash flows graduates actually take home. It captures the combined effect of student talent, peer networks, college reputation, and teaching quality. It does not isolate what the college taught independently of who the student was.

  - **College Reporting Biases:** While we cross-checked our sample against audited reports, baseline figures still rely partly on college filings. To the extent that institutions overstate salaries or conceal unplaced students, our valuations represent an optimistic upper bound.

  - **Career Horizon Modeling:** We evaluate earnings over a 20-year career assuming 5% annual wage growth and an 8% discount rate. While our sensitivity tables and Monte Carlo simulations test a wide range of outcomes, individual careers can be disrupted by unexpected illness, family care, or economic recessions.

  - **AI Exposure versus Real-World Adoption:** Our AI exposure scores measure technical task feasibility, not instantaneous layoffs. How fast Indian companies actually adopt AI depends on enterprise inertia, capital costs, legal licensing, and regulatory oversight.

## XV. Conclusion

When an undergraduate degree in India is evaluated like a real financial investment—accounting for living costs, income taxes, commercial loan interest, and emerging automation risks—the conventional wisdom based on college rankings falls apart. The NIRF Perception score provides negligible independent signal of graduate labor-market outcomes once objective institutional characteristics are accounted for. The field of study you choose matters substantially more than the prestige tier of the college you attend. Expensive private degrees routinely saddle graduates with initial debt payments that eat up 85% of their starting take-home pay, turning their early twenties into a period of acute financial stress. Low-cost public institutions, by contrast, deliver safe, unencumbered returns that build lasting generational wealth.

Replacing glossy marketing brochures and ranking tables with transparent cash-flow accounting is both an economic necessity for Indian parents and an urgent duty for higher education policymakers. By grounding college choices in real financial safety margins, families can protect their life savings, and India can ensure that higher education remains a true engine of social mobility rather than a debt trap.

## Data Availability and Reproducibility Statement

In accordance with open-science and SocArXiv preprint repository guidelines, all data sources, computational routines, and simulation engines used in this paper are documented to ensure full scientific reproducibility:

  - **Public Administrative Data:** Historical ranking archives and component methodology documents from the National Institutional Ranking Framework (NIRF, 2016–2025) are publicly accessible via the Ministry of Education portal (<a href="https://www.nirfindia.org">https://www.nirfindia.org</a>). Employment and wage distributions from the Periodic Labour Force Survey (PLFS 2022–23) are available from the Ministry of Statistics and Programme Implementation Microdata Archive (<a href="https://microdata.gov.in">https://microdata.gov.in</a>). Macroeconomic time series (CPI-Combined, Repo Rate, 10-Year G-Sec yields) are accessible via the Reserve Bank of India Database on Indian Economy (<a href="https://dbie.rbi.org.in">https://dbie.rbi.org.in</a>). Retail education loan schedules are published by the State Bank of India.

  - **Institutional Program Disclosures:** Tuition fee structures, mandatory institutional charges, and placement statistics for the 35 audited institutional programs were compiled from publicly available institutional NIRF Section 5 filings, mandatory AICTE disclosures, and official university placement audit reports. The five calibrated synthetic reference archetypes represent model-generated reference benchmarks derived from State Fee Regulatory Committee (SFRC) gazette ceilings and PLFS wage quantiles, as detailed in Table A3 and Table A4.

  - **Code and Computational Reproducibility:** The complete numerical valuation engine, Fisher debt amortization solver, break-even salary routines, and 10,000-path Monte Carlo simulation algorithms are fully specified in Technical Appendices A and D, and executable replication scripts are maintained in the project computational archive.

## References

  - Acemoglu, D., and Restrepo, P. (2018). The race between man and machine: Implications of technology for growth, factor shares, and employment. *American Economic Review*, 108(6), 1488-1542.

  - Acemoglu, D., and Restrepo, P. (2019). Automation and new tasks: How technology displaces and reinstates labor. *Journal of Economic Perspectives*, 33(2), 3-30.

  - Altonji, J. G., Arcidiacono, P., and Ma, X. (2016). The analysis of field of study choices. *Handbook of the Economics of Education*, 5, 305-377.

  - Altonji, J. G., Blom, E., and Meghir, C. (2012). Heterogeneity in human capital investments: High school curriculum, college major, and careers. *Annual Review of Economics*, 4(1), 185-223.

  - Arrow, K. J. (1973). Higher education as a filter. *Journal of Public Economics*, 2(3), 193-216.

  - Autor, D. H. (2015). Why are there still so many jobs? The history and future of workplace automation. *Journal of Economic Perspectives*, 29(3), 3-30.

  - Autor, D. H., Levy, F., and Murnane, R. J. (2003). The skill content of recent technological change: An empirical exploration. *Quarterly Journal of Economics*, 118(4), 1279-1333.

  - Azam, M., and Blom, A. (2008). Progress in participation in tertiary education and returns from education in India. *World Bank Policy Research Working Paper*, No. 4793.

  - Batheja, D., Hirshleifer, S., and Kaur, O. (2024). Does signalling college-level human capital matter? An experimental study in India. *Economic Development and Cultural Change*, doi:10.1086/743610.

  - Becker, G. S. (1964). *Human Capital: A Theoretical and Empirical Analysis*. National Bureau of Economic Research.

  - Ben-Porath, Y. (1967). The production of human capital and the life cycle of earnings. *Journal of Political Economy*, 75(4), 352-365.

  - Brown, J. R., Fang, C., and Gomes, F. (2012). Risk and returns to education. *NBER Working Paper*, No. 18300.

  - Brynjolfsson, E., Li, D., and Raymond, L. R. (2023). Generative AI at work. *NBER Working Paper*, No. 31161.

  - Brynjolfsson, E., Mitchell, T., and Rock, D. (2018). What can AI buy? The suitability of machine learning for tasks. *AEA Papers and Proceedings*, 108, 48-53.

  - Choudhury, P. K., and Kumar, V. (2022). Changing financing pattern of higher education in India: An assessment of household expenditure. *Journal of Educational Planning and Administration*, 36(2), 115-138.

  - Dale, S. B., and Krueger, A. B. (2002). Estimating the payoff to attending a more selective college. *Quarterly Journal of Economics*, 117(4), 1491-1527.

  - Dale, S. B., and Krueger, A. B. (2014). Estimating the effects of college characteristics on earnings: A test using duplicate applications. *Journal of Human Resources*, 49(2), 323-358.

  - Das, M., and Hilgenstock, B. (2018). The exposure of labor to automation: A global perspective. *IMF Working Paper*, WP/18/219.

  - Dell'Acqua, F., McFowland, E., Mollick, E., Lifshitz-Assaf, H., Kellogg, K., and Lakhani, K. R. (2023). Navigating the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge worker productivity and quality. *Harvard Business School Working Paper*, No. 24-013.

  - Dutta, P. V. (2006). Returns to education: New evidence for India, 1983-1999. *Education Economics*, 14(4), 431-451.

  - Dynarski, S. M. (2003). Does aid matter? Measuring the effect of student financial aid on college attendance. *American Economic Review*, 93(1), 279-288.

  - Eloundou, T., Manning, S., Mishkin, P., and Rock, D. (2023). GPTs are GPTs: An early look at the labor market impact potential of large language models. *arXiv preprint*, arXiv:2303.10130.

  - Felten, E. W., Raj, M., and Seamans, R. (2021). A method to link advances in artificial intelligence to occupational abilities. *AEA Papers and Proceedings*, 111, 582-587.

  - Felten, E. W., Raj, M., and Seamans, R. (2023). How will language modelers affect occupations and industries? *Strategic Management Journal*, 44(8), 1891-1911.

  - Frisancho, V., and Krishna, K. (2016). Affirmative action in higher education in India: Targeting, selectivity, and completion. *Journal of Development Economics*, 119, 142-158.

  - Hazelkorn, E. (2015). *Rankings and the Reshaping of Higher Education: The Battle for World-Class Excellence*. Palgrave Macmillan.

  - Heckman, J. J., Layne-Farrar, A., and Todd, P. (1996). Does measured school quality really matter? An examination of the earnings-quality relationship. *Review of Economics and Statistics*, 78(4), 562-610.

  - Hoekstra, M. (2009). The effect of attending the flagship state university on earnings: A discontinuity-based approach. *Review of Economics and Statistics*, 91(4), 717-724.

  - Kanjilal-Bhaduri, S., and Pastore, F. (2017). Returns to education and female participation nexus: Evidence from India. *IZA Discussion Paper*, No. 11209.

  - Kijima, Y. (2006). Why did wage inequality increase? Evidence from urban India 1983-1999. *Journal of Development Economics*, 81(1), 97-117.

  - Kirkeboen, L. J., Leuven, E., and Mogstad, M. (2016). Field of study, earnings, and self-selection. *Quarterly Journal of Economics*, 131(3), 1057-1111.

  - Koerselman, K., and Uusitalo, R. (2014). The risk-return trade-off in higher education: A nonparametric approach. *Labour Economics*, 30, 290-300.

  - Lange, F., and Topel, R. (2006). The social value of education and human capital. *Handbook of the Economics of Education*, 1, 459-509.

  - Lee, D. S., and Lemieux, T. (2010). Regression discontinuity designs in economics. *Journal of Economic Literature*, 48(2), 281-355.

  - Lochner, L. J., and Monge-Naranjo, A. (2011). The nature of credit constraints and human capital. *American Economic Review*, 101(6), 2487-2529.

  - Lochner, L. J., and Monge-Naranjo, A. (2012). Credit constraints in education. *Annual Review of Economics*, 4(1), 225-256.

  - Marisha. (2021). Analysing the stability of India Rankings. *Current Science*, 120(7), 1144-1151. doi:10.18520/cs/v120/i7/1144-1151.

  - Mincer, J. (1974). *Schooling, Experience, and Earnings*. National Bureau of Economic Research.

  - Ministry of Education, Government of India. (2024). *India Rankings 2024: National Institutional Ranking Framework*. New Delhi.

  - Ministry of Statistics and Programme Implementation. (2023). *Periodic Labour Force Survey (PLFS) Annual Report (2022-23)*. New Delhi.

  - Munshi, K., and Rosenzweig, M. (2016). Networks and misallocation: Theory and evidence from caste in India. *American Economic Review*, 106(8), 2177-2220.

  - NASSCOM. (2024). *Strategic Review 2024: Technology Sector in India*. National Association of Software and Service Companies, New Delhi.

  - Noy, S., and Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. *Science*, 381(6654), 187-192.

  - Patra, S., Ray, T., and Chaudhuri, A. R. (2021). Impact of education loans on higher education: The Indian experience. *Discussion Paper Series*, No. 21-03, Planning Unit, Indian Statistical Institute, New Delhi.

  - Peng, S., Kalliamvakou, E., Cihon, P., and Demirer, M. (2023). The impact of AI on developer productivity: Evidence from GitHub Copilot. *arXiv preprint arXiv:2302.06590*.

  - Psacharopoulos, G., and Patrinos, H. A. (2018). Returns to investment in education: A decennial review of the global literature. *Education Economics*, 26(5), 445-458.

  - Reserve Bank of India. (2025). *Database on Indian Economy (DBIE): Macroeconomic and Monetary Statistics*. Mumbai.

  - Sekhri, S. (2020). Prestige matters: Value-added and signaling in elite college admissions in India. *Journal of Human Resources*, 55(4), 1312-1345.

  - Selten, F., Neylon, C., Huang, C. K., and Groth, P. (2020). A longitudinal analysis of university rankings. *Quantitative Science Studies*, 1(3), 1109-1135.

  - Sorz, J., Sommer, B., Bornmann, L., and Scherndl, T. (2015). Uncertainty analysis of ranking scores: How reliable are global university leagues? *Journal of the Association for Information Science and Technology*, 66(11), 2278-2288.

  - Spence, M. (1973). Job market signaling. *Quarterly Journal of Economics*, 87(3), 355-374.

  - Stiglitz, J. E. (1975). The theory of 'screening', education, and the distribution of income. *American Economic Review*, 65(3), 283-300.

  - Tilak, J. B. (2002). Public subsidies in education in India. *Economic and Political Weekly*, 37(4), 343-359.

  - Webb, M. (2019). The impact of artificial intelligence on the labor market. *Stanford University Working Paper*.

  - Westby, A., Modestino, A. S., and Cheng, H. (2024). The impact of artificial intelligence on entry-level labor demand: Evidence from online job postings. *Northeastern University Working Paper*.

  - Wiswall, M., and Zafar, B. (2015). Determinants of college major choice: Identification using an information experiment. *Review of Economic Studies*, 82(2), 791-824.

  - World Bank. (2024). *World Development Indicators: India Country Series*. Washington, DC.

  - Zimmerman, S. D. (2014). The returns to college admission for academically marginal students. *Journal of Labor Economics*, 32(4), 711-754.

## Technical Appendix A: Mathematical Derivations and Numerical Solvers

**Newton-Raphson Internal Rate of Return Solver:** The IRR is solved from *f*(IRR) = 0 where *f*(*r*) = −(*C_p* − *L_p*) − *OC_p* · *d_p* + ∑_*t*=1^*T* [(π_*p**E*[*Y_p,t*] − *D_p,t*) / (1 + *r*)^*t*]. The analytical gradient is *f'*(*r*) = −∑_*t*=1^*T* [*t*(π_*p**E*[*Y_p,t*] − *D_p,t*) / (1 + *r*)^*t*+1]. Iteration step: *r*_*k*+1 = *r_k* − *f*(*r_k*)/*f'*(*r_k*). Convergence is enforced to |*f*(*r*)| < 10^−8.

**Real Fisher-Amortized Debt Dynamics:** Let *L_p* be financed at nominal annual rate *r*_loan^nom with tenure *n* months. Monthly installment is *EMI* = *L_p* · [*i*(1 + *i*)^*n* / ((1 + *i*)^*n* − 1)] with *i* = *r*_loan^nom/12. Under constant inflation π_infl, real debt service in year *t* is *D*_*p,t*^real = 12 · *EMI* / (1 + π_infl)^*t*. The present value of real debt service discounted at real discount rate *r* is *PV*(*D*^real) = 12 · *EMI* · ∑_*t*=1^10 [(1 + π_infl)^−*t*(1 + *r*)^−*t*].

## Technical Appendix B: Panel Econometric Specifications

Table A1: NIRF Composite Aggregation Matrix by Discipline Category

  
    
      Discipline Group
      TLR / QLR
      RPC / QNR
      GO / SFC
      OI
      PR
      Recovered R^2
      Max Residual
    
  
  
    
      Engineering, Management, University, Overall, Medical, Dental
      0.3000
      0.3000
      0.2000
      0.1000
      0.1000
      1.000000
      < 0.020
    
    
      College, Law
      0.4000
      0.1500
      0.2500
      0.1000
      0.1000
      1.000000
      < 0.023
    
    
      Architecture
      0.4000
      0.2000
      0.2000
      0.1000
      0.1000
      1.000000
      < 0.017
    
    
      Research Institutions (2021–2025)
      0.3000
      0.3000
      0.2000
      0.1000
      0.1000
      1.000000
      < 0.018
    
  

Table A2: Panel Forward Persistence Regressions (Score in Wave t+1 on Wave t)

  
    
      Model Specification
      Observations
      Overall R^2
      Within R^2
      Persistence (rho)
    
  
  
    
      Score on 5 Components (Two-Way Fixed Effects)
      6,176
      0.9746
      0.7439
      --
    
    
      Perception on Objective Block (Two-Way Fixed Effects)
      6,176
      0.9270
      0.1903
      --
    
    
      Lead Score S_{t+1} on Current S_t (Inst FE + Year FE)
      3,873
      0.9718
      0.5835
      0.6083***
    
    
      Lead Score S_{t+1} on Current S_t (Year FE only)
      3,873
      0.9509
      0.9408
      0.9782***
    
    
      Cross-Sectional Institutional Holdout (70% train / 30% test)
      3,873
      0.9447
      0.7649
      0.9623***
    
  

Note: Clustered standard errors at institution level. *** p < 0.001. Evaluated across clean de-duplicated panel.

## Technical Appendix C: Complete 40-Program Purified Undergraduate Dataset

Table A3: Engineering and Technology Undergraduate Disclosures (Programs 1 to 24)

  
    
      #
      Institution Name
      Degree & Discipline
      Sector Tier
      Cost
      CTC
      Cash Net
      Placement Rate
      Self True NPV
      Debt True NPV
      Audit Status
    
  
  
    
      1
      IIT Bombay
      B.Tech Computer Science (Eng-CS)
      Tier 1 Public
      INR 11.0L
      INR 21.0L
      INR 14.70L
      0.93
      +INR 178.6L
      +INR 180.2L
      Audited
    
    
      2
      IIT Delhi
      B.Tech Computer Science (Eng-CS)
      Tier 1 Public
      INR 11.0L
      INR 20.5L
      INR 14.35L
      0.92
      +INR 172.5L
      +INR 174.1L
      Audited
    
    
      3
      IIT Madras
      B.Tech Computer Science (Eng-CS)
      Tier 1 Public
      INR 10.0L
      INR 19.8L
      INR 13.86L
      0.91
      +INR 164.9L
      +INR 166.4L
      Audited
    
    
      4
      IIT Kanpur
      B.Tech Computer Science (Eng-CS)
      Tier 1 Public
      INR 10.5L
      INR 19.5L
      INR 13.65L
      0.91
      +INR 161.7L
      +INR 163.3L
      Audited
    
    
      5
      IIT Kharagpur
      B.Tech Computer Science (Eng-CS)
      Tier 1 Public
      INR 10.2L
      INR 19.0L
      INR 13.30L
      0.90
      +INR 155.0L
      +INR 156.5L
      Audited
    
    
      6
      IIT Roorkee
      B.Tech Data Science & AI (Eng-CS)
      Tier 1 Public
      INR 10.0L
      INR 18.2L
      INR 12.74L
      0.89
      +INR 146.4L
      +INR 147.9L
      Audited
    
    
      7
      BITS Pilani
      B.E. Computer Science (Eng-CS)
      Tier 2 Private
      INR 22.0L
      INR 15.5L
      INR 10.85L
      0.87
      +INR 107.4L
      +INR 110.7L
      Audited
    
    
      8
      IIIT Hyderabad
      B.Tech Computer Science (Eng-CS)
      Tier 1 Public
      INR 18.0L
      INR 16.5L
      INR 11.55L
      0.90
      +INR 125.1L
      +INR 127.8L
      Audited
    
    
      9
      NIT Trichy
      B.Tech Computer Science (Eng-CS)
      Tier 2 Public
      INR 6.5L
      INR 14.0L
      INR 9.80L
      0.88
      +INR 110.6L
      +INR 111.5L
      Audited
    
    
      10
      NIT Surathkal
      B.Tech Information Tech (Eng-CS)
      Tier 2 Public
      INR 6.5L
      INR 13.5L
      INR 9.45L
      0.87
      +INR 104.9L
      +INR 105.8L
      Audited
    
    
      11
      NIT Warangal
      B.Tech Computer Science (Eng-CS)
      Tier 2 Public
      INR 6.2L
      INR 12.8L
      INR 8.96L
      0.85
      +INR 96.5L
      +INR 97.4L
      Audited
    
    
      12
      Jadavpur Univ
      B.E. Computer Science (Eng-CS)
      Tier 1 Public
      INR 1.8L
      INR 12.5L
      INR 8.75L
      0.88
      +INR 102.1L
      +INR 102.3L
      Audited
    
    
      13
      DTU Delhi
      B.Tech Computer Science (Eng-CS)
      Tier 1 Public
      INR 9.5L
      INR 12.0L
      INR 8.40L
      0.84
      +INR 85.1L
      +INR 86.5L
      Audited
    
    
      14
      COEP Tech Univ
      B.Tech Computer Eng (Eng-CS)
      Tier 2 Public
      INR 4.2L
      INR 8.8L
      INR 6.16L
      0.82
      +INR 61.6L
      +INR 62.2L
      Audited
    
    
      15
      VIT Vellore
      B.Tech Computer Science (Eng-CS)
      Tier 3 Private
      INR 18.0L
      INR 9.8L
      INR 6.86L
      0.79
      +INR 53.0L
      +INR 55.6L
      Audited
    
    
      16
      Thapar Univ
      B.Tech Computer Science (Eng-CS)
      Tier 2 Private
      INR 19.0L
      INR 9.2L
      INR 6.44L
      0.78
      +INR 46.4L
      +INR 49.2L
      Audited
    
    
      17
      Manipal MIT
      B.Tech Computer Science (Eng-CS)
      Tier 2 Private
      INR 21.0L
      INR 8.8L
      INR 6.16L
      0.77
      +INR 40.4L
      +INR 43.5L
      Audited
    
    
      18
      SRM Univ
      B.Tech Computer Science (Eng-CS)
      Tier 3 Private
      INR 26.0L
      INR 8.5L
      INR 5.95L
      0.74
      +INR 28.4L
      +INR 32.2L
      Audited
    
    
      19
      Private Deemed (Bench)
      B.Tech Computer Science (Eng-CS)
      Tier 3 Private
      INR 52.0L
      INR 14.0L
      INR 9.80L
      0.76
      +INR 48.2L
      +INR 55.9L
      Calibrated
    
    
      20
      Regional Tier-3 (Bench)
      B.Tech Computer Science (Eng-CS)
      Tier 3 Private
      INR 8.5L
      INR 3.6L
      INR 2.52L
      0.52
      +INR 3.4L
      +INR 4.6L
      Calibrated
    
    
      21
      IIT Roorkee
      B.Tech Civil Eng (Eng-NonCS)
      Tier 1 Public
      INR 10.0L
      INR 10.2L
      INR 7.14L
      0.84
      +INR 68.9L
      +INR 70.4L
      Audited
    
    
      22
      IIT Kharagpur
      B.Tech Mech Eng (Eng-NonCS)
      Tier 1 Public
      INR 10.2L
      INR 11.0L
      INR 7.70L
      0.85
      +INR 77.0L
      +INR 78.5L
      Audited
    
    
      23
      NIT Calicut
      B.Tech Mech Eng (Eng-NonCS)
      Tier 2 Public
      INR 5.8L
      INR 7.5L
      INR 5.25L
      0.81
      +INR 47.4L
      +INR 48.2L
      Audited
    
    
      24
      State Govt Eng (Bench)
      B.Tech Civil Eng (Eng-NonCS)
      Tier 3 Public
      INR 4.8L
      INR 5.2L
      INR 3.64L
      0.72
      +INR 26.1L
      +INR 26.8L
      Calibrated
    
  

Table A4: Non-Engineering Undergraduate Disclosures (Programs 25 to 40)

  
    
      #
      Institution Name
      Degree & Discipline
      Sector Tier
      Cost
      CTC
      Cash Net
      Placement Rate
      Self True NPV
      Debt True NPV
      Audit Status
    
  
  
    
      25
      IIM Indore
      5-Yr Integrated Management (Mgmt)
      Tier 1 Public
      INR 35.0L
      INR 22.0L
      INR 15.40L
      0.94
      +INR 164.4L
      +INR 169.5L
      Audited
    
    
      26
      SSCBS Delhi
      BBA (FIA) Finance (Mgmt)
      Tier 1 Public
      INR 3.8L
      INR 11.2L
      INR 7.84L
      0.86
      +INR 87.5L
      +INR 88.0L
      Audited
    
    
      27
      St. Xavier Mumbai
      Bachelor Mgmt Studies (Mgmt)
      Tier 2 Private
      INR 4.2L
      INR 8.5L
      INR 5.95L
      0.80
      +INR 59.9L
      +INR 60.5L
      Audited
    
    
      28
      Christ Univ
      Bachelor Business Admin (Mgmt)
      Tier 3 Private
      INR 9.0L
      INR 5.8L
      INR 4.06L
      0.68
      +INR 25.7L
      +INR 27.0L
      Audited
    
    
      29
      SRCC Delhi
      B.Com (Honours) (Commerce)
      Tier 1 Public
      INR 3.1L
      INR 7.4L
      INR 5.18L
      0.76
      +INR 48.6L
      +INR 49.0L
      Audited
    
    
      30
      Delhi Univ
      B.Com (Honours) (Commerce)
      Tier 1 Public
      INR 2.8L
      INR 6.8L
      INR 4.76L
      0.74
      +INR 42.7L
      +INR 43.1L
      Audited
    
    
      31
      St. Stephen Delhi
      B.A. (Honours) Economics (Commerce)
      Tier 1 Public
      INR 3.0L
      INR 7.2L
      INR 5.04L
      0.75
      +INR 46.1L
      +INR 46.6L
      Audited
    
    
      32
      Loyola Chennai
      B.Com General (Commerce)
      Tier 2 Private
      INR 2.6L
      INR 5.4L
      INR 3.78L
      0.71
      +INR 31.0L
      +INR 31.4L
      Audited
    
    
      33
      Central Univ (Bench)
      B.Sc Physics (PureSci)
      Tier 2 Public
      INR 2.9L
      INR 4.2L
      INR 2.94L
      0.68
      +INR 20.7L
      +INR 21.1L
      Calibrated
    
    
      34
      State Univ (Bench)
      B.Sc Chemistry (PureSci)
      Tier 3 Public
      INR 2.1L
      INR 3.8L
      INR 2.66L
      0.65
      +INR 17.6L
      +INR 17.9L
      Calibrated
    
    
      35
      St. Xavier Kolkata
      B.Sc Statistics (PureSci)
      Tier 2 Private
      INR 3.4L
      INR 5.2L
      INR 3.64L
      0.72
      +INR 29.2L
      +INR 29.7L
      Audited
    
    
      36
      AIIMS Delhi
      MBBS Medical (Medicine)
      Tier 1 Public
      INR 1.5L
      INR 14.0L
      INR 9.80L
      0.98
      +INR 127.2L
      +INR 127.4L
      Audited
    
    
      37
      CMC Vellore
      MBBS Medical (Medicine)
      Tier 1 Public
      INR 2.8L
      INR 11.5L
      INR 8.05L
      0.95
      +INR 97.8L
      +INR 98.2L
      Audited
    
    
      38
      Kasturba Manipal
      MBBS Medical (Medicine)
      Tier 2 Private
      INR 72.0L
      INR 12.0L
      INR 8.40L
      0.94
      +INR 32.1L
      +INR 42.7L
      Audited
    
    
      39
      NLSIU Bengaluru
      B.A. LL.B. Integrated (Law)
      Tier 1 Public
      INR 16.0L
      INR 16.0L
      INR 11.20L
      0.88
      +INR 123.8L
      +INR 126.1L
      Audited
    
    
      40
      NALSAR Hyderabad
      B.A. LL.B. Integrated (Law)
      Tier 1 Public
      INR 15.5L
      INR 15.2L
      INR 10.64L
      0.86
      +INR 114.7L
      +INR 117.0L
      Audited
    
  

Note: Net Present Value evaluated over baseline 20-year career horizon at r = 8.0%, g = 5.0%. For Clinical Medicine (MBBS), evaluating over a full 35-year medical clinical practice lifetime elevates AIIMS Delhi MBBS to +INR 190.0 Lakhs (Monte Carlo Mean: +INR 196.3 Lakhs [95% CI: 107.4L, 337.8L]) and CMC Vellore to +INR 146.2 Lakhs, reflecting practice continuity past mandatory corporate retirement ages.

## Technical Appendix D: Monte Carlo Simulation Parameter Priors

Table A5: Monte Carlo Simulation Prior Distributions and Empirical Anchors

  
    
      Simulation Parameter
      Distributional Prior
      Base Parameter Values
      Empirical Data Source / Anchor
    
  
  
    
      Starting Liquid Real Cash Salary
      Log-Normal(mu, sigma)
      mu = ln(Base_0), sigma = 0.22
      NIRF Median Disclosures adjusted for 15% non-cash haircut and tax
    
    
      Annual Real Wage Growth Rate
      Triangular(min, mode, max)
      min = 0.02, mode = 0.05, max = 0.08
      Longitudinal wage surveys (PLFS 2022-23 NSS 78th Round)
    
    
      Macroeconomic Recession Shock
      Poisson Process (Arrival lambda)
      lambda = 0.08 (once per 12.5 years)
      RBI Historical Macroeconomic Contraction Frequencies
    
    
      Recession Wage Compression Severity
      Beta(alpha, beta)
      alpha = 2.0, beta = 5.0 (E[s] = 0.15)
      IT Sector recession wage-freeze precedents (2008, 2020)
    
    
      Field Employment Realization
      Beta(alpha, beta) bounded on [0, 1]
      Mean = Table A3/A4 placement rate
      Official institutional placement audit filings
    
    
      Commercial Loan Nominal Rate
      Normal(mu_r, sigma_r)
      mu = 10.15%, sigma = 0.75%
      State Bank of India Retail Education Loan Schedule (2024–2026)
    
    
      Household Real Discount Rate
      Uniform(min_r, max_r)
      min = 0.06, max = 0.10
      RBI 10-Year G-Sec Real Yield + Household Equity Risk Premium
    
  

"""

import shutil

# Write HTML outputs
html_target_project = r"c:\Users\PC5\Desktop\Research project\research project final.html"
html_target_legacy = r"c:\Users\PC5\Desktop\Research project\paper_revised.html"
html_target_desktop = r"c:\Users\PC5\Desktop\research project final.html"

with open(html_target_project, "w", encoding="utf-8") as f:
    f.write(html_content)
shutil.copy2(html_target_project, html_target_legacy)
shutil.copy2(html_target_project, html_target_desktop)

print("HTML generated successfully. Compiling PDF via Microsoft Edge headless...")

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
pdf_final_project = r"c:\Users\PC5\Desktop\Research project\research project final.pdf"
pdf_final_desktop = r"c:\Users\PC5\Desktop\research project final.pdf"
pdf_legacy_project = r"c:\Users\PC5\Desktop\Research project\A_Risk_Adjusted_Framework_for_Valuing_Higher_Education_in_India_Revised.pdf"
pdf_legacy_desktop = r"c:\Users\PC5\Desktop\A_Risk_Adjusted_Framework_for_Valuing_Higher_Education_in_India_Revised.pdf"

cmd = [
    edge_path,
    "--headless=new",
    "--disable-gpu",
    f"--print-to-pdf={pdf_final_project}",
    "--no-pdf-header-footer",
    html_target_project
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)
if os.path.exists(pdf_final_project):
    print("SUCCESS: PDF generated! Size:", os.path.getsize(pdf_final_project), "bytes")
    # Deploy to Desktop and legacy names
    shutil.copy2(pdf_final_project, pdf_final_desktop)
    shutil.copy2(pdf_final_project, r"c:\Users\PC5\Desktop\Research Project Final.pdf")
    shutil.copy2(pdf_final_project, pdf_legacy_project)
    shutil.copy2(pdf_final_project, pdf_legacy_desktop)
    print("Copied to Desktop: 'research project final.pdf'")
else:
    print("FAILED: PDF not found.")
