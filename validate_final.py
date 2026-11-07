import re

with open('build_paper_html.py', 'r', encoding='utf-8') as f:
    text = f.read()

css_end = text.find('</style>')
body_part = text[css_end:]
css_part = text[:css_end]

print("=== FINAL VALIDATION ===")

# 1. Verify JEL count
jel_count = body_part.count('JEL Classification')
print(f"JEL Classification mentions: {jel_count} (expected 1)")

# 2. Verify Figure 2 caption consistency
fig2_svgtext = re.findall(r'Figure 2:[^\n<"]+', body_part)
print(f"\nFigure 2 mentions: {set(fig2_svgtext)}")

# 3. Verify abstract-meta paragraphs
abs_m = re.findall(r'<p class="abstract-meta">', body_part)
print(f"\nAbstract meta paras: {len(abs_m)} (expected 2: Keywords + JEL)")

# 4. Verify references-block div and ref-entry
ref_block_count = body_part.count('<div class="references-block">')
ref_entry_count = body_part.count('class="ref-entry"')
print(f"\nReferences block divs: {ref_block_count}")
print(f"ref-entry elements: {ref_entry_count} (expected 58)")

# 5. Verify references-block CSS is present
has_refblock_css = '.references-block' in css_part
print(f"Has .references-block CSS: {has_refblock_css}")

# 6. Verify no orphaned abstract-box
has_abs_box_html = 'class="abstract-box"' in body_part
has_abs_box_css = '.abstract-box {' in css_part
print(f"\nHas abstract-box HTML: {has_abs_box_html}")
print(f"Has abstract-box CSS definition: {has_abs_box_css}")

# 7. Verify heading counts
h2s = re.findall(r'<h2 class="sec-title"[^>]*>([^<]+)', body_part)
h3s = re.findall(r'<h3 class="subsec-title"[^>]*>([^<]+)', body_part)
print(f"\nH2 sections: {len(h2s)}")
for h in h2s:
    print(f"  {h}")
print(f"\nH3 subsections: {len(h3s)}")
for h in h3s:
    print(f"  {h}")

# 8. Verify all equations sequential
eq_ids = re.findall(r'<div class="formula-id">\(([^)]+)\)</div>', text)
print(f"\nEquation IDs: {eq_ids}")
expected_eqs = ["1", "2", "3", "4", "5a", "5b", "6", "7", "8", "9", "10", "11"]
missing = [e for e in expected_eqs if e not in eq_ids]
extra = [e for e in eq_ids if e not in expected_eqs]
print(f"Missing equations: {missing}")
print(f"Extra equations: {extra}")

# 9. Verify all 10 figures
fig_caps = re.findall(r'<div class="figure-caption">([^<]+)</div>', body_part)
print(f"\nFigure captions ({len(fig_caps)}):")
for fc in fig_caps:
    print(f"  {fc}")

# 10. Verify all 13 tables
tab_titles = re.findall(r'<div class="table-title">([^<]+)</div>', body_part)
print(f"\nTable titles ({len(tab_titles)}):")
for t in tab_titles:
    print(f"  {t}")

# 11. Key numerical values
print("\n=== KEY DATA VALUES ===")
checks = [
    ("+INR 199.9 Lakhs", "IIT Bombay NPV Baseline"),
    ("+INR 144.2 Lakhs", "IIT Bombay NPV Gradual AI"),
    ("+INR 130.7 Lakhs", "IIT Bombay NPV Rapid AI"),
    ("+INR 89.4 Lakhs", "IIT Bombay NPV Unscaled"),
    ("+INR 178.6 Lakhs", "NPV 178.6L"),
    ("+INR 110.6 Lakhs", "NPV 110.6L"),
    ("84.7%", "EMI burden 84.7%"),
    ("10.15%", "SBI loan 10.15%"),
    ("22.9 Lakhs", "Field premium 22.9L"),
    ("12.8 Lakhs", "Tier premium 12.8L"),
    ("6,176", "NIRF panel size"),
    ("Westby, Modestino, and Cheng (2024)", "Westby cite"),
    ("Peng et al. (2023)", "Peng cite"),
    ("Brynjolfsson, Li, and Raymond (2023)", "Brynjolfsson cite"),
    ("NASSCOM (2024)", "NASSCOM cite"),
]
all_pass = True
for needle, label in checks:
    present = needle in text
    status = "PASS" if present else "FAIL"
    if not present:
        all_pass = False
    print(f"  [{status}] {label}: '{needle}'")

print(f"\nAll key data checks PASSED: {all_pass}")
