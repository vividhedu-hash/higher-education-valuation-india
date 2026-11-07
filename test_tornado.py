
def calc_npv(ctc, cost, dur, emp, r=0.08, g=0.05, haircut_total=0.30, aioe=0.48, aioe_wage_drag=0.0, aioe_emp_drag=0.0):
    cash = ctc * (1 - haircut_total) * (1 - aioe_wage_drag * aioe)
    effective_emp = emp * (1 - aioe_emp_drag * aioe)
    pv = sum(effective_emp * cash * ((1 + g)**(t - 1)) / ((1 + r)**t) for t in range(1, 21))
    return pv - cost - 1.68 * dur

base_npv = calc_npv(21.0, 11.0, 4, 0.93)
print('Baseline IIT Bombay CS NPV: %.1f L' % base_npv)

params = [
    ('Real Discount Rate r (6% to 12%)',
     calc_npv(21.0, 11.0, 4, 0.93, r=0.12), calc_npv(21.0, 11.0, 4, 0.93, r=0.06)),
    ('Real Wage Growth g (2% to 8%)',
     calc_npv(21.0, 11.0, 4, 0.93, g=0.02), calc_npv(21.0, 11.0, 4, 0.93, g=0.08)),
    ('Employment Rate pi (-15% to +5%)',
     calc_npv(21.0, 11.0, 4, 0.93 * 0.85), calc_npv(21.0, 11.0, 4, min(1.0, 0.93 * 1.05))),
    ('Cash/CTC Haircut (20% to 40%)',
     calc_npv(21.0, 11.0, 4, 0.93, haircut_total=0.40), calc_npv(21.0, 11.0, 4, 0.93, haircut_total=0.20)),
    ('AI Wage Drag (0% to 20% * AIOE)',
     calc_npv(21.0, 11.0, 4, 0.93, aioe_wage_drag=0.20), calc_npv(21.0, 11.0, 4, 0.93, aioe_wage_drag=0.0)),
    ('AI Emp Drag (0% to 25% * AIOE)',
     calc_npv(21.0, 11.0, 4, 0.93, aioe_emp_drag=0.25), calc_npv(21.0, 11.0, 4, 0.93, aioe_emp_drag=0.0)),
]

for name, low, high in params:
    swing = abs(high - low)
    print('%-35s | Low: %6.1f L | High: %6.1f L | Swing: %6.1f L' % (name, low, high, swing))
