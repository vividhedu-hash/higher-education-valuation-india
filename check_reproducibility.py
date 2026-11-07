# Exact reproduction check for all tables and scenarios
import math

def npv(cash, placement, upfront, r, g=0.05, T=20):
    pv = sum(placement * cash * ((1.0 + g) ** (t - 1)) / ((1.0 + r) ** t)
             for t in range(1, T + 1))
    return pv - upfront

def real_debt_pv(principal, r, infl=0.05, r_loan_nom=0.1015, tenure=120):
    r_real = (1.0 + r_loan_nom) / (1.0 + infl) - 1.0
    i_real = r_real / 12.0
    emi_real = principal * (i_real * (1.0 + i_real)**tenure) / ((1.0 + i_real)**tenure - 1.0)
    annual_ds_real = 12.0 * emi_real
    return sum(annual_ds_real / ((1.0 + r)**t) for t in range(1, 11))

rates = [0.03, 0.05, 0.07, 0.08, 0.10, 0.12, 0.15]

progs = [
    ("IIT Bombay B.Tech CS (Self)", 14.70, 0.93, 11.0 + 1.68*4),
    ("NIT Trichy B.Tech CS (Self)", 9.80, 0.88, 6.5 + 1.68*4),
    ("SSCBS Delhi BBA FIA (Self)", 7.84, 0.86, 3.8 + 1.68*3),
    ("Private Deemed CS (Self)", 9.80, 0.76, 52.0 + 1.68*4),
    ("NIT Calicut Mech (Self)", 5.25, 0.81, 5.8 + 1.68*4),
    ("State Univ Chem (Self)", 2.66, 0.65, 2.1 + 1.68*3),
]

print("=== EXACT TABLE 4 (Discount-Rate Sensitivity) ===")
header = f"{'Program Specification':32s} | " + " | ".join(f"{r*100:4.1f}% " for r in rates)
print(header)
print("-" * len(header))
for name, cash, plc, upfront in progs:
    vals = [f"{npv(cash, plc, upfront, r):6.1f}L" for r in rates]
    print(f"{name:32s} | " + " | ".join(vals))

# Private Deemed CS (Real Debt)
debt_vals = []
for r in rates:
    pv_earn = sum(0.76 * 9.80 * (1.05**(t-1)) / ((1.0+r)**t) for t in range(1, 21))
    pv_debt = real_debt_pv(52.0, r)
    npv_d = pv_earn - 1.68*4 - pv_debt
    debt_vals.append(f"{npv_d:6.1f}L")
print(f"{'Private Deemed CS (Real Debt)':32s} | " + " | ".join(debt_vals))
