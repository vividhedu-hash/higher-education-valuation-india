# Full Monte Carlo simulation script to generate exact, reproducible 95% CIs
import random
import math

random.seed(42)

def run_monte_carlo(n_iter=10000):
    # Parameter distributions per archetype:
    # 1. IIT Bombay CS: Base cash = 14.70, Cost = 11.0, dur = 4, Base plc = 0.93
    # 2. AIIMS Delhi MBBS: Base cash = 9.80, Cost = 1.5, dur = 5.5, Base plc = 0.98
    # 3. NIT Trichy CS: Base cash = 9.80, Cost = 6.5, dur = 4, Base plc = 0.88
    # 4. DU B.Com Hons: Base cash = 4.76, Cost = 2.8, dur = 3, Base plc = 0.74
    # 5. Private Deemed CS: Base cash = 9.80, Cost = 52.0, dur = 4, Base plc = 0.76

    archetypes = [
        ("Profile A: IIT Bombay CS (Self)", 14.70, 0.93, 11.0, 4, False),
        ("Profile B: AIIMS Delhi MBBS (Self, 20-Yr)", 9.80, 0.98, 1.5, 5.5, False),
        ("Profile B2: AIIMS Delhi MBBS (35-Yr Horizon)", 9.80, 0.98, 1.5, 5.5, True),
        ("Profile C: NIT Trichy CS (Self)", 9.80, 0.88, 6.5, 4, False),
        ("Profile D: DU B.Com Hons (Self)", 4.76, 0.74, 2.8, 3, False),
        ("Profile E: Private Deemed CS (Self)", 9.80, 0.76, 52.0, 4, False),
        ("Profile E-Debt: Private Deemed CS (Debt)", 9.80, 0.76, 52.0, 4, False),
    ]

    results = {}
    
    for name, base_cash, base_plc, cost, dur, is_35yr in archetypes:
        T = 35 if is_35yr else 20
        oc = 1.68
        upfront = cost + oc * dur
        npvs = []
        
        for _ in range(n_iter):
            # Draw r ~ Uniform(0.06, 0.10)
            r = random.uniform(0.06, 0.10)
            # Draw g ~ Triangular(0.02, 0.05, 0.08)
            g = random.triangular(0.02, 0.08, 0.05)
            # Draw cash ~ LogNormal with mean = base_cash, sigma = 0.15
            # mu = ln(base_cash) - 0.5 * sigma^2
            sigma = 0.15
            mu = math.log(base_cash) - 0.5 * (sigma**2)
            cash_draw = random.lognormvariate(mu, sigma)
            # Draw placement ~ Beta centered at base_plc, std ~ 0.04
            # Mean = a/(a+b) = base_plc => a = base_plc * kappa
            kappa = 50.0
            a = base_plc * kappa
            b = (1.0 - base_plc) * kappa
            plc_draw = random.betavariate(a, b)
            
            # Macro shock: Poisson arrival with prob = 0.08 per year
            # If shock occurs, 15% salary haircut in that year
            pv = 0.0
            for t in range(1, T + 1):
                shock = 0.85 if random.random() < 0.08 else 1.0
                wage_t = plc_draw * cash_draw * ((1.0 + g)**(t - 1)) * shock
                
                if "Debt" in name:
                    # Amortized real debt payment years 1 to 10
                    # Nominal rate ~ Normal(0.1015, 0.0075)
                    r_loan_nom = random.gauss(0.1015, 0.0075)
                    r_loan_real = (1.0 + r_loan_nom) / 1.05 - 1.0
                    i_real = r_loan_real / 12.0
                    emi = cost * (i_real * (1.0 + i_real)**120) / ((1.0 + i_real)**120 - 1.0)
                    debt_t = (12.0 * emi) if t <= 10 else 0.0
                    net_cf = wage_t - debt_t
                else:
                    net_cf = wage_t
                    
                pv += net_cf / ((1.0 + r)**t)
                
            if "Debt" in name:
                # Upfront is only foregone earnings
                npv_val = pv - oc * dur
            else:
                npv_val = pv - upfront
                
            npvs.append(npv_val)
            
        npvs.sort()
        mean_val = sum(npvs) / n_iter
        median_val = npvs[n_iter // 2]
        ci_lower = npvs[int(n_iter * 0.025)]
        ci_upper = npvs[int(n_iter * 0.975)]
        prob_neg = sum(1 for x in npvs if x < 0) / n_iter
        
        results[name] = {
            "mean": mean_val,
            "median": median_val,
            "ci_lower": ci_lower,
            "ci_upper": ci_upper,
            "prob_neg": prob_neg,
        }
        
    print("=== MONTE CARLO SIMULATION RESULTS (10,000 ITERATIONS) ===")
    print(f"{'Archetype Profile':40s} | {'Mean NPV':10s} | {'Median':10s} | {'95% CI Range':20s} | {'Prob(NPV<0)':12s}")
    print("-" * 100)
    for name, m in results.items():
        ci_str = f"[{m['ci_lower']:6.1f}L, {m['ci_upper']:6.1f}L]"
        print(f"{name:40s} | {m['mean']:8.1f}L | {m['median']:8.1f}L | {ci_str:20s} | {m['prob_neg']*100:6.2f}%")

if __name__ == "__main__":
    run_monte_carlo()
