# FULL CROSS-CHECK REPORT
# Run: py full_report.py

import re

with open('build_paper_html.py', 'r', encoding='utf-8') as f:
    text = f.read()

css_end = text.find('</style>')
css_part = text[:css_end]
body_part = text[css_end:]

PASS = "[PASS]"
FAIL = "[FAIL]"

checks = {}

# --- CSS Checks ---
checks["No abstract-box CSS"] = ('.abstract-box {' not in css_part)
checks["No meta-grid CSS"] = ('.meta-grid {' not in css_part)
checks["formula-box transparent"] = ('background: transparent !important' in css_part)
checks["formula-box no border"] = ('border: none !important' in css_part)
checks["h2 no border-bottom"] = ('border-bottom: none' in css_part)
checks["Table th transparent bg"] = ('background-color: transparent !important' in css_part)
checks["SVG no border (CSS)"] = ('figure-container svg' in css_part and 'border: none' in css_part)
checks["p margin-bottom:0"] = ('margin-bottom: 0;' in css_part)
checks["p text-indent: 1.5em"] = ('text-indent: 1.5em' in css_part)
checks["h2+p no-indent rule"] = ('h2 + p' in css_part)
checks["h3+p no-indent rule"] = ('h3 + p' in css_part)
checks["ref-entry CSS exists"] = ('.ref-entry {' in css_part)
checks["references-block CSS"] = ('.references-block {' in css_part)
checks["@page :first exists"] = ('@page :first' in css_part)
checks["Running headers defined"] = ('@top-right' in css_part and '@top-left' in css_part)
checks["Page number footer"] = ('@bottom-center' in css_part)

# --- HTML Structure Checks ---
checks["No abstract-box HTML"] = ('class="abstract-box"' not in body_part)
checks["Has abstract-container"] = ('class="abstract-container"' in body_part)
checks["No meta-grid HTML"] = ('<table class="meta-grid">' not in body_part)
checks["Has author-footnote"] = ('class="author-footnote"' in body_part)
checks["Has abstract title"] = ('<div class="abstract-title">ABSTRACT</div>' in body_part)
checks["2 abstract-meta paras"] = (body_part.count('<p class="abstract-meta">') == 2)
checks["Abstract has no <br>"] = ('<br>' not in body_part[body_part.find('abstract-container'):body_part.find('</div>\n\n<h2', body_part.find('abstract-container'))])
checks["58 ref-entries"] = (body_part.count('class="ref-entry"') == 58)
checks["references-block div"] = ('<div class="references-block">' in body_part)

# --- Section Headings ---
h2s = re.findall(r'<h2 class="sec-title"[^>]*>([^<]+)', body_part)
roman_sections = [h for h in h2s if re.match(r'^[IVX]+\.', h)]
checks["All 15 Roman numeral sections"] = (len(roman_sections) == 15)
checks["Appendices retain A/B/C/D"] = ('Technical Appendix A' in body_part)
checks["Section II reference in text"] = ('Section II' in body_part and 'Section 2' not in body_part)

# --- JEL / Keywords ---
checks["JEL appears exactly once"] = (body_part.count('JEL Classification') == 1)
checks["Keywords appears once"] = (body_part.count('<em>Keywords:</em>') == 1)

# --- Figures ---
fig_caps = re.findall(r'<div class="figure-caption">([^<]+)</div>', body_part)
checks["Exactly 10 figures"] = (len(fig_caps) == 10)
svg_old_border = 'border: 1px solid #cbd5e1' in body_part
checks["No old SVG borders in HTML"] = (not svg_old_border)

# --- Tables ---
tab_titles = re.findall(r'<div class="table-title">([^<]+)</div>', body_part)
checks["Exactly 13 tables"] = (len(tab_titles) == 13)

# --- Equations ---
eq_ids = re.findall(r'<div class="formula-id">\(([^)]+)\)</div>', text)
expected_eqs = ["1", "2", "3", "4", "5a", "5b", "6", "7", "8", "9", "10", "11"]
checks["Equations 1-11 sequential"] = (eq_ids == expected_eqs or eq_ids == [str(i) for i in range(1,12)])

# --- Key Numerical Data ---
key_values = [
    "+INR 199.9 Lakhs", "+INR 144.2 Lakhs", "+INR 130.7 Lakhs", "+INR 89.4 Lakhs",
    "+INR 178.6 Lakhs", "+INR 110.6 Lakhs", "84.7%", "10.15%", "22.9 Lakhs", "12.8 Lakhs",
    "6,176", "Westby, Modestino, and Cheng (2024)", "Peng et al. (2023)",
    "Brynjolfsson, Li, and Raymond (2023)", "NASSCOM (2024)",
]
for val in key_values:
    checks[f"Data: {val[:30]}"] = (val in text)

# --- Print Report ---
print("=" * 65)
print("CROSS-CHECK VALIDATION REPORT")
print("=" * 65)
pass_count = sum(1 for v in checks.values() if v)
fail_count = sum(1 for v in checks.values() if not v)
for label, result in checks.items():
    icon = PASS if result else FAIL
    print(f"  {icon}  {label}")

print("=" * 65)
print(f"  TOTAL: {pass_count} PASSED, {fail_count} FAILED")
print("=" * 65)
