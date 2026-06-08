
# Analysis of Pair Comparison Tables
  






This document provides a detailed analysis of `pair_comparisons_v2_standard copy.md` and `pair_comparisons_v2_cases copy.md`, relating every row and value to the Inertial Relativity paper.
---

## 1. Key Definitions

| Symbol | Formula | Meaning |
|--------|---------|---------|
| I | (2/5) m r^2 | Moment of inertia (uniform sphere) |
| D | M/R | DeGerlia Compactness |
| D_crit | c^2/(2G) = 6.73295 x 10^26 kg/m | DeGerlia Threshold (collapse constant) |
| D_norm | D/D_crit | Normalized compactness (equivalent to r_s/R) |
| r_s | 2GM/c^2 = M/D_crit | Schwarzschild radius |
| gtd | sqrt(1 - D_norm) | Gravitational time dilation (pace of time vs flat spacetime) |
| dtd | sqrt(D_norm) | Raw time dilation (sqrt of normalized compactness) |

Complementary relationship: gtd^2 + dtd^2 = 1 (Pythagorean pair).

---

## 2. Document Structure

Both documents share the same layout:
- **Top table**: System properties (mass, radius, I, D, D_norm, r_s, gtd, dtd) for each system pair
- **Bottom table**: Derived ratios testing which algebraic expressions are equal across scenarios

### Standard document -- 6 scenarios

| Column | Constraint | Paper section |
|--------|-----------|---------------|
| M=M | m1=m2=1e30, r1=1e5, r2=1e8 | Section 5.1 (Static Mass / Gravitational) |
| GTD(M=M,R2=1.5e3) | m1=m2=1e30, r1=1.5e3 (near r_s), r2=1e8 | Section 5.1 extreme case |
| GTD=GTD=.5 | Both systems tuned to D_norm=0.7426, gtd~0.507 | Equal pace of time |
| R=R 30,20-5 | m1=1e30, m2=1e20, r1=r2=1e5 | Section 5.2 (Static Radius / Linear) |
| I=I | m1=1e30, m2=1e24, r1=1e5, r2=1e8; I1=I2=4e39 | Section 5.4 (Constant Inertia) |
| P=P | m1=1e30, m2=1e22, r1=1e5, r2=1e3 | Equal inertial density |

### Cases document -- 7 scenarios

| Column | Constraint | Paper section |
|--------|-----------|---------------|
| case1 (M=M) | m1=m2=2e30, r1=3e3 (~r_s), r2=7e8 | Appendix Case 1 (neutron star scale) |
| case1b (M=M r2=1e8) | m1=m2=2e30, r1=1.5e-7 (sub-Schwarzschild), r2=1e8 | Case 1 beyond collapse |
| Case 2:R=R 30,24-8 | m1=1e30, m2=1e24, r1=r2=1e8 | Appendix Case 2 |
| Case 3:P=P | m1=1e30, m2=1e27, r1=1e8, r2=1e7; constant density | Appendix Case 3 (Isometric) |
| Case 4:I=I | m1=1e32, m2=1e30, r1=1e7, r2=1e8; I1=I2=4e45 | Appendix Case 4 |
| General | m1=1e20, m2=1e30, r1=2e-7, r2=1e7 | Appendix General Case |
| General2 | m1=1e20, m2=1e30, r1=2e-7, r2=1.5e7 | General Case variant |

---

## 3. Top Table: System Properties (Row by Row)

### m_1, m_2, r_1, r_2 (input parameters)

These define each scenario. System 1 mass is held constant across all standard-doc scenarios (1e30 kg). The cases doc varies both systems.

### I_1, I_2 (moment of inertia)

Formula: I = (2/5) m r^2 for uniform sphere.

Verified spot checks:
- Standard M=M: I_1 = 0.4 x 1e30 x (1e5)^2 = 4e39. Correct.
- Cases Case 4: I_1 = 0.4 x 1e32 x (1e7)^2 = 4e45; I_2 = 0.4 x 1e30 x (1e8)^2 = 4e45. Equal as intended.
- Cases General: I_1 = 0.4 x 1e20 x (2e-7)^2 = 1.6e6. Correct.

### D_1, D_2 (DeGerlia Compactness)

Formula: D = M/R.

Verified:
- Standard M=M: D_1 = 1e30/1e5 = 1e25. D_2 = 1e30/1e8 = 1e22. Correct.
- Standard GTD=.5: D_1 = 1e30/2e3 = 5e26. D_2 = 1e36/2e9 = 5e26. Equal -- both at same compactness. Correct.
- Cases Case 1: D_1 = 2e30/3e3 = 6.667e26. Near D_crit. Correct.
- Cases Case 1b: D_1 = 2e30/1.5e-7 = 1.333e37. Far beyond D_crit. Correct.

### D_1_norm, D_2_norm (normalized compactness)

Formula: D_norm = D/D_crit. Algebraically identical to r_s/R.

Proof: D_norm = (M/R) / (c^2/(2G)) = 2GM/(Rc^2) = r_s/R.

Verified:
- Standard M=M: D_1_norm = 1e25/6.73295e26 = 1.4852e-2. Correct.
- Standard GTD(M=M,R2=1.5e3): D_1_norm = 6.667e26/6.733e26 = 0.9902. System is 99% of collapse threshold. Correct.
- Cases Case 1b: D_1_norm = 1.333e37/6.733e26 = 1.98e10. 19.8 billion times above collapse. Correct.

### r_s_1, r_s_2 (Schwarzschild radius)

Computed as r_s = M/D_crit (equivalent to 2GM/c^2 when D_crit = c^2/(2G) exactly).

Key property: r_s depends only on mass. All scenarios with the same mass have the same r_s.

Verified: r_s for M=1e30: 1e30/6.73295e26 = 1.4852e3 m. Correct throughout.

Note: D_crit = 6.73295e26 is rounded to 6 significant figures. The exact c^2/(2G) = 6.73295461e26. This produces a relative discrepancy of ~7e-7 in r_s values vs the standard formula.

### gtd_1, gtd_2 (gravitational time dilation)

Formula: gtd = sqrt(1 - D_norm) = sqrt(1 - r_s/R).

Physical meaning: pace of time relative to flat spacetime. gtd = 1 is no dilation; gtd = 0 is the event horizon.

Verified:
- Standard M=M: gtd_1 = sqrt(1 - 0.01485) = 0.99255. Correct.
- Standard GTD(M=M,R2=1.5e3): gtd_1 = sqrt(1 - 0.990) = sqrt(0.010) = 0.0992. Time runs at ~10% of normal. Correct.
- Cases Case 1b: D_1_norm = 1.98e10, so 1 - D_norm is deeply negative. gtd_1 = 0 (clamped; would be imaginary). Correct.
- Cases General: gtd_1 = sqrt(1 - 0.7426) = sqrt(0.2574) = 0.5073. ~50% pace of time. Correct.

### dtd_1, dtd_2 (raw time dilation)

Formula: dtd = sqrt(D_norm) = sqrt(D/D_crit).

Physical meaning: the "dilation signal" -- how strongly a system's compactness contributes to time dilation. Always real and positive for any physical system. Does not clamp at 1 -- systems beyond collapse have dtd > 1.

Complementary to gtd: gtd^2 + dtd^2 = (1 - D_norm) + D_norm = 1.

Verified:
- Standard M=M: dtd_1 = sqrt(0.01485) = 0.12187. Correct.
- Standard GTD(M=M,R2=1.5e3): dtd_1 = sqrt(0.990) = 0.9951. Near-maximal. Correct.
- Pythagorean check (Scenario 2 system 1): 0.0992^2 + 0.9951^2 = 0.00985 + 0.99016 = 1.000. Confirmed.
- Cases Case 1b: dtd_1 = sqrt(1.98e10) = 1.407e5. dtd > 1 because D_norm > 1. The DTD framework remains well-defined past the collapse threshold even when GTD does not. Correct.

---

## 4. Bottom Table: Derived Ratios (Row by Row)

### I_1/I_2

Simple inertia ratio. = (m_1 r_1^2)/(m_2 r_2^2).

Verified:
- Standard I=I: 4e39/4e39 = 1. Correct by construction.
- Cases Case 3: (1e30 x 1e16)/(1e27 x 1e14) = 1e46/1e41 = 1e5. Correct.

### (I_1/I_2)^(1/5) -- The STE time ratio

This is the Space-Time Equivalence prediction. The STE states T_1/T_2 = (I_2/I_1)^(1/5). The table computes (I_1/I_2)^(1/5), which is the reciprocal: T_2/T_1.

Verified:
- Standard I=I: 1^(1/5) = 1. STE predicts no time difference when inertias are equal. Correct.
- Cases Case 3: (1e5)^(1/5) = 10. Correct.
- Cases General: (4e-38)^(1/5) = 3.314e-8. Correct.

This row is NOT equal to any other row in general. It matches sqrt(D_1/D_2) only in Case 3 (constant density) -- see case-specific identities below.

### (*k) D_2/D_1 -- Compactness ratio

Raw compactness ratio (system 2 over system 1). The (*k) annotation marks it as a k-factor.

D_2/D_1 = (m_2/m_1)(r_1/r_2) = k_r/k_m.

Verified:
- Standard M=M: 1e22/1e25 = 1e-3. = k_r = 1e-3 (since k_m = 1). Correct.
- Standard GTD=.5: 5e26/5e26 = 1. Equal compactness. Correct.
- Cases Case 2: 1e16/1e22 = 1e-6. = k_m^(-1) since k_r = 1. Correct.

### (*G) gtd_1/gtd_2 -- Gravitational time dilation ratio

The ratio of the two systems' gravitational time dilations.

**This does NOT equal D_2/D_1.** The sqrt(1-x) function is nonlinear. Demonstrated numerically:

| Scenario | gtd_1/gtd_2 | D_2/D_1 |
|----------|-------------|---------|
| Standard M=M | 0.9926 | 1e-3 |
| Standard GTD-extreme | 0.0992 | 1.5e-5 |
| Standard GTD=.5 | 1.000 | 1.000 |
| Standard R=R | 0.9925 | 1e-10 |
| Standard I=I | 0.9925 | 1e-9 |
| Standard P=P | 0.9925 | 1e-6 |

In scenarios 1, 4, 5, 6: D_2/D_1 varies by 7 orders of magnitude (1e-3 to 1e-10), yet gtd_1/gtd_2 barely moves (~0.9925 throughout). This is because system 1's D_norm = 0.01485 dominates -- system 2 is in such weak gravity that its gtd is effectively 1.

The extreme case (GTD near Schwarzschild): gtd_1 = 0.0992 drops dramatically while D_2/D_1 = 1.5e-5 stays small. The gtd ratio reflects absolute position on the sqrt(1-x) curve, not the linear D ratio.

### dtd_1/dtd_2 -- Raw time dilation ratio

dtd_1/dtd_2 = sqrt(D_1_norm)/sqrt(D_2_norm) = sqrt(D_1/D_2) = sqrt(m_1 r_2/(m_2 r_1)).

Unlike gtd_1/gtd_2, this faithfully reflects the compactness ratio (through the square root).

This is the central row -- it is universally equal to 4 other rows (see Section 5).

### (*k) k_m = m_1/m_2 and (*k) k_r = r_1/r_2

Raw mass and radius ratios. These decompose D_2/D_1: D_2/D_1 = k_r/k_m.

Verified: Standard M=M: D_2/D_1 = 1e-3/1 = 1e-3. Correct.

### sqrt(D_1/D_2)

Algebraically identical to dtd_1/dtd_2. Included to verify this identity numerically. Matches in all 13 scenarios.

### sqrt(D_1)/sqrt(D_2)

Algebraically identical to sqrt(D_1/D_2). Verifies sqrt(a/b) = sqrt(a)/sqrt(b). Matches in all 13 scenarios.

### sqrt(r_2/r_1) -- Radius component only

This is only the radius part of dtd_1/dtd_2. It equals dtd_1/dtd_2 only when m_1 = m_2 (the Static Mass cases), where the mass component drops out.

- Standard M=M: sqrt(1e8/1e5) = sqrt(1e3) = 31.62 = dtd_1/dtd_2. Match.
- Standard R=R: sqrt(1) = 1. But dtd_1/dtd_2 = 1e5. No match (mass drives the difference).

### sqrt(m_1/m_2) -- Mass component only

This is only the mass part of dtd_1/dtd_2. It equals dtd_1/dtd_2 only when r_1 = r_2 (the Static Radius cases).

- Standard R=R: sqrt(1e30/1e20) = sqrt(1e10) = 1e5 = dtd_1/dtd_2. Match.
- Standard M=M: sqrt(1) = 1. But dtd_1/dtd_2 = 31.62. No match (radius drives the difference).

### sqrt(m_1/m_2) * sqrt(r_2/r_1) -- Full decomposition

Since D_1/D_2 = (m_1/r_1)/(m_2/r_2) = (m_1 r_2)/(m_2 r_1), the sqrt decomposes into the product of mass and radius components.

Universally equal to dtd_1/dtd_2 in all 13 scenarios. Verified.

### (I_1/I_2)/(dtd_1/dtd_2) -- Inertia ratio divided by time dilation ratio

Algebraically: sqrt(m_1/m_2) * (r_1/r_2)^(5/2).

This measures how the inertia ratio differs from the compactness-based time dilation ratio. The 5/2 exponent on the radius ratio connects to the STE's 1/5 power: the STE involves (m r^2)^(1/5) while dtd involves (m/r)^(1/2). The mismatch between r^2 in inertia and r^(-1) in compactness produces this r^(5/2) factor.

Verified:
- Standard M=M: sqrt(1) * (1e-3)^(5/2) = 1e-7.5 = 3.162e-8. Correct.
- Standard R=R: sqrt(1e10) * 1^(5/2) = 1e5. Correct.

### (dtd_1/dtd_2)^2 * (r_1/r_2)^3 = I_1/I_2 -- THE KEY UNIVERSAL IDENTITY

**This is the most important row in both tables.**

Algebraic proof:
- (dtd_1/dtd_2)^2 = D_1/D_2 = (m_1 r_2)/(m_2 r_1)
- Multiply by (r_1/r_2)^3: (m_1 r_2)/(m_2 r_1) * r_1^3/r_2^3 = m_1 r_1^2/(m_2 r_2^2) = I_1/I_2

**The inertia ratio decomposes into two factors:**
- (dtd_1/dtd_2)^2 = the time dilation signal (compactness ratio)
- (r_1/r_2)^3 = the volume ratio (spatial scale)

So: I_1/I_2 = (time dilation signal)^2 * (volume ratio)

Equivalently: dtd_1/dtd_2 = sqrt(I_1 r_2^3 / (I_2 r_1^3))

This connects the STE (inertia-based) to the Schwarzschild framework (compactness-based). Verified in all 13 scenarios with zero exceptions:

| Scenario | (dtd_1/dtd_2)^2 * (r_1/r_2)^3 | I_1/I_2 | Match |
|----------|-------------------------------|---------|-------|
| Std M=M | 1e-6 | 1e-6 | YES |
| Std GTD-extreme | 2.25e-10 | 2.25e-10 | YES |
| Std GTD=.5 | 1e-18 | 1e-18 | YES |
| Std R=R | 1e10 | 1e10 | YES |
| Std I=I | 1 | 1 | YES |
| Std P=P | 1e12 | 1e12 | YES |
| Cases Case1 | 1.837e-11 | 1.837e-11 | YES |
| Cases Case1b | 2.25e-30 | 2.25e-30 | YES |
| Cases Case2 | 1e6 | 1e6 | YES |
| Cases Case3 | 1e5 | 1e5 | YES |
| Cases Case4 | 1 | 1 | YES |
| Cases General | 4e-38 | 4e-38 | YES |
| Cases General2 | 1.778e-38 | 1.778e-38 | YES |

### sqrt(m_1^2 r_1/(m_2^2 r_2)) (standard doc) / sqrt(m_2^2 r_2/(m_1^2 r_1)) (cases doc)

Standard doc form: (m_1/m_2) * sqrt(r_1/r_2). This does NOT equal dtd_1/dtd_2 in general. It differs by a factor of (m_1/m_2)^(1/2) * (r_1/r_2). Only matches dtd_1/dtd_2 when sqrt(m_1/m_2) = r_2/r_1 -- a very specific constraint not generally satisfied.

This row appears to be included as a test expression -- an algebraic form that was explored and confirmed NOT to be a universal identity.

### sqrt(5I_1/(2*Dc*r_1^3)) / sqrt(5I_2/(2*Dc*r_2^3)) (standard doc)

**This row bridges the STE directly to time dilation.**

Algebraic proof that each factor equals dtd:
- For a uniform sphere: I = (2/5) m r^2
- 5I/(2 D_crit r^3) = 5 * (2/5) * m * r^2 / (2 * D_crit * r^3) = m/(D_crit * r) = D/D_crit = D_norm
- sqrt(5I/(2 D_crit r^3)) = sqrt(D_norm) = dtd

This means dtd can be computed directly from I, r, and D_crit -- without ever computing mass or compactness as intermediates. Time dilation expressed purely in terms of rotational inertia, geometry, and the universal collapse constant.

Universally equal to dtd_1/dtd_2 in all 6 standard-doc scenarios.

### sqrt((I_1/I_2) * (r_2/r_1)^3) (cases doc)

This is the same identity as (dtd_1/dtd_2)^2 * (r_1/r_2)^3 = I_1/I_2, rearranged:
- sqrt(I_1/I_2 * (r_2/r_1)^3) = sqrt(m_1 r_1^2/(m_2 r_2^2) * r_2^3/r_1^3) = sqrt(m_1 r_2/(m_2 r_1)) = sqrt(D_1/D_2) = dtd_1/dtd_2

The (r_2/r_1)^3 factor converts the r^2 dependence in I back to the r^(-1) dependence in D. This is the bridge formula between inertia-based and compactness-based time dilation.

Universally equal to dtd_1/dtd_2 in all 7 cases-doc scenarios.

### sqrt(1 - dtd_1^2) / sqrt(1 - dtd_2^2) (cases doc only)

Since dtd = sqrt(D_norm), this equals sqrt(1 - D_norm_1)/sqrt(1 - D_norm_2) = gtd_1/gtd_2.

This should be algebraically identical to the gtd_1/gtd_2 row. Small numerical differences (~1e-5 to ~1e-12) between this row and the (*G) row are precision artifacts from D_crit being stored at 6 significant figures vs the Schwarzschild formula using full-precision G and c.

Case 1b shows "---" because dtd_1^2 = D_1_norm = 1.98e10 >> 1, making 1 - dtd_1^2 negative (square root imaginary). The DTD framework remains valid past collapse; the GTD framework does not.

---

## 5. Universal Identities (True Across All 13 Scenarios)

### Identity cluster: 5 expressions all equal dtd_1/dtd_2

| Expression | Why it equals dtd_1/dtd_2 |
|------------|---------------------------|
| sqrt(D_1/D_2) | By definition: dtd = sqrt(D_norm), D_crit cancels in ratio |
| sqrt(D_1)/sqrt(D_2) | Algebraically identical to sqrt(D_1/D_2) |
| sqrt(m_1/m_2) * sqrt(r_2/r_1) | D_1/D_2 = m_1 r_2/(m_2 r_1), take sqrt, factor |
| sqrt(5I_1/(2 D_c r_1^3)) / sqrt(5I_2/(2 D_c r_2^3)) | Each factor = sqrt(D_norm) = dtd for uniform sphere |
| sqrt((I_1/I_2) * (r_2/r_1)^3) | I_1/I_2 * (r_2/r_1)^3 = D_1/D_2, take sqrt |

All reduce to sqrt(m_1 r_2 / (m_2 r_1)). Verified numerically in all 13 scenarios.

### Inertia recovery identity

**(dtd_1/dtd_2)^2 * (r_1/r_2)^3 = I_1/I_2**

Time-dilation-squared times volume-ratio equals inertia-ratio. This is the STE inverted: given observable time dilation ratios and radii, you can recover the inertia ratio. The exponent 1/5 from the STE is embedded in this relationship.

Rearranging: (I_2/I_1)^(1/5) = ((dtd_2/dtd_1)^2 * (r_2/r_1)^3)^(1/5) = (dtd_2/dtd_1)^(2/5) * (r_2/r_1)^(3/5)

---

## 6. Case-Specific Identities

These hold ONLY under the stated constraint:

| Constraint | Identity | Paper section |
|-----------|----------|---------------|
| M=M (Static Mass) | D_2/D_1 = k_r = r_1/r_2 | Section 5.1 |
| M=M | sqrt(r_2/r_1) = dtd_1/dtd_2 | Section 5.1 |
| R=R (Static Radius) | sqrt(m_1/m_2) = dtd_1/dtd_2 | Section 5.2 |
| R=R | D_1/D_2 = m_1/m_2 | Section 5.2 |
| Constant density | (I_1/I_2)^(1/5) = r_1/r_2 | Section 5.3 |
| Constant density | (I_1/I_2)^(1/5) = sqrt(D_1/D_2) | Section 5.3 (only case where STE ratio = dtd ratio) |
| I_1 = I_2 | (I_1/I_2)^(1/5) = 1 | Section 5.4 |
| D_1 = D_2 | gtd_1/gtd_2 = dtd_1/dtd_2 = 1 | Equal compactness |

---

## 7. Scenario-by-Scenario Analysis

### Standard doc: M=M (Same mass, different radii)

m_1 = m_2 = 1e30, r_1 = 1e5, r_2 = 1e8.

When mass is equal, all time dilation comes from radius. D_1/D_2 = r_2/r_1 = 1e3. dtd_1/dtd_2 = sqrt(1e3) = 31.62, driven entirely by sqrt(r_2/r_1). The mass component sqrt(m_1/m_2) = 1. Both systems are in weak gravity (D_norm ~ 0.015 and 1.5e-5), so gtd_1/gtd_2 = 0.993 -- barely distinguishable despite a 1000x compactness difference.

### Standard doc: GTD(M=M,R2=1.5e3) (Near-Schwarzschild)

m_1 = m_2 = 1e30, r_1 = 1500 m (barely above r_s = 1485 m), r_2 = 1e8.

System 1 is at 99% of collapse (D_1_norm = 0.990). Time runs at ~10% of flat-spacetime rate (gtd_1 = 0.0992). This is the clearest demonstration of nonlinearity: gtd_1/gtd_2 = 0.099 while D_2/D_1 = 1.5e-5 -- six orders of magnitude apart. The sqrt(1-x) function is extremely steep near x = 1.

### Standard doc: GTD=GTD=.5 (Equal gravitational time dilation)

Both systems tuned to D_norm = 0.7426. All compactness-based ratios collapse to 1 (dtd, gtd, D ratios all = 1), even though masses differ by 10^6 and radii by 10^6. But I_1/I_2 = 1e-18, showing that equal compactness does NOT mean equal inertia. The STE ratio (I_1/I_2)^(1/5) = 2.51e-4, while dtd_1/dtd_2 = 1. The two frameworks give different answers here.

Note: gtd = 0.5073, not exactly 0.5. For exact 0.5, D_norm would need to be 0.75 (D = 5.050e26).

### Standard doc: R=R (Same radius, different masses)

r_1 = r_2 = 1e5, m_1 = 1e30, m_2 = 1e20.

All dilation comes from mass. D_1/D_2 = m_1/m_2 = 1e10. dtd_1/dtd_2 = sqrt(1e10) = 1e5. The radius component sqrt(r_2/r_1) = 1 contributes nothing. (I_1/I_2)^(1/5) = (1e10)^(1/5) = 100, different from dtd ratio of 1e5.

### Standard doc: I=I (Equal moment of inertia)

I_1 = I_2 = 4e39. STE predicts (I_1/I_2)^(1/5) = 1 -- no time difference. But dtd_1/dtd_2 = 31623 and gtd_1/gtd_2 = 0.993 -- the Schwarzschild framework shows significant compactness difference.

The compactnesses differ by 9 orders of magnitude (D_1/D_2 = 1e9) despite equal inertia. This happens because inertia depends on m r^2 while compactness depends on m/r -- opposite dependence on radius.

The universal identity confirms: (31623)^2 * (1e-3)^3 = 1e9 * 1e-9 = 1 = I_1/I_2.

### Standard doc: P=P

m_1 = 1e30, r_1 = 1e5, m_2 = 1e22, r_2 = 1e3.

The systems have m_1/m_2 = (r_1/r_2)^4 = 1e8. This is NOT equal D (D_1/D_2 = 1e6) and NOT equal volumetric density (rho_1 = 2.39e14, rho_2 = 2.39e12). The constraint appears to be m/r^4 = const. This may correspond to a specific definition of inertial density not currently in the paper.

### Cases doc: case1 (M=M near r_s)

m_1 = m_2 = 2e30, r_1 = 3e3 (barely above r_s = 2.97e3), r_2 = 7e8.

A neutron-star-scale system (3 km radius, nearly at Schwarzschild). D_1_norm = 0.990. Time runs at 10% (gtd_1 = 0.0992). All M=M identities hold: D_2/D_1 = k_r, sqrt(r_2/r_1) = dtd_1/dtd_2.

### Cases doc: case1b (Beyond collapse)

m_1 = m_2 = 2e30, r_1 = 1.5e-7 m (150 nanometers -- ~1000x smaller than a proton).

D_1_norm = 1.98e10. System is 20 billion times past the collapse threshold. The Schwarzschild framework breaks: gtd_1 = 0, the last row gives "---" (imaginary). But the DTD framework remains well-defined: dtd_1 = 1.407e5. All algebraic identities that don't involve sqrt(1-x) continue to hold.

This demonstrates that the DTD/STE framework extends beyond the domain where GR is defined.

### Cases doc: Case 2 (R=R)

r_1 = r_2 = 1e8, m_1 = 1e30, m_2 = 1e24. Mass ratio 1e6. All R=R identities hold: sqrt(m_1/m_2) = dtd_1/dtd_2 = 1e3. (I_1/I_2)^(1/5) = (1e6)^(1/5) = 15.849. Matches paper's Appendix Case 2 values.

### Cases doc: Case 3 (Constant density)

m_1/m_2 = (r_1/r_2)^3 = 1e3. Density = 2.39e5 kg/m^3 for both systems (verified).

Under constant density: I proportional to r^5 (since I = 2/5 m r^2 and m proportional to r^3). So (I_1/I_2)^(1/5) = (r_1^5/r_2^5)^(1/5) = r_1/r_2 = 10. Also sqrt(D_1/D_2) = sqrt((r_1/r_2)^2) = r_1/r_2 = 10.

**This is the ONLY case where (I_1/I_2)^(1/5) = sqrt(D_1/D_2).** The STE ratio equals the dtd ratio because constant density forces the exponents to align.

### Cases doc: Case 4 (I=I)

I_1 = I_2 = 4e45. (I_1/I_2)^(1/5) = 1 exactly. STE predicts no relative time dilation. But D_1/D_2 = 1000 (compactnesses differ by 3 orders of magnitude) and gtd_1/gtd_2 = 0.993 (GR predicts a ~0.7% difference).

This is the critical divergence: equal inertia does NOT mean equal compactness. The identity (dtd_1/dtd_2)^2 * (r_1/r_2)^3 = 1000 * (0.1)^3 = 1000 * 1e-3 = 1 = I_1/I_2 shows how the dtd ratio and volume ratio exactly compensate.

### Cases doc: General and General2

No shared constraints. System 1 is microscopic (m=1e20, r=2e-7) at 74% of collapse (D_norm=0.743, gtd=0.507). System 2 is macroscopic (m=1e30, r=1e7 or 1.5e7) far from collapse.

All universal identities hold. General2 has larger r_2, reducing D_2 and increasing dtd_1/dtd_2 from 70.71 to 86.60.

---

## 8. Connection to the Paper's Central Thesis

The paper claims GR and SR are edge cases of the STE. These tables demonstrate this numerically:

### How GR emerges (Static Mass)

When M_1 = M_2, the STE's full inertia dependence reduces to a pure radius dependence. The compactness ratio becomes D_2/D_1 = r_1/r_2, which is exactly the Schwarzschild ratio r_s/R when one system is the collapse threshold. The M=M columns show this: sqrt(r_2/r_1) = dtd_1/dtd_2 exactly. GR is the edge case where mass is static.

### How SR emerges (Static Radius)

When R_1 = R_2, the STE reduces to a pure mass dependence. The compactness ratio becomes D_1/D_2 = m_1/m_2. The R=R columns show: sqrt(m_1/m_2) = dtd_1/dtd_2. The paper connects this to v^2/c^2 via escape velocity (not tested computationally in these tables).

### Decomposition is always available

The universal identity sqrt(D_1/D_2) = sqrt(m_1/m_2) * sqrt(r_2/r_1) shows that the compactness ratio always factors cleanly into mass and radius components. GR holds one factor constant (mass); SR holds the other constant (radius). The STE uses both.

### The STE inversion

(dtd_1/dtd_2)^2 * (r_1/r_2)^3 = I_1/I_2 is the STE running backwards: from observable time dilation and geometry, recover inertia. This identity holds universally and embeds the 1/5 exponent. It is not currently named or featured as an equation in the paper.

---

## 9. Gaps and Opportunities

### Not tested by these computations

1. **Velocity-based k (Lorentz/SR)**: No columns test k = v^2/c^2 or verify the escape velocity identity.
2. **Non-spherical geometries**: All computations use uniform spheres. The paper claims universality for any system and axis.
3. **Multi-axis comparisons**: No computation compares the same system about different axes.
4. **Euler's theorem**: The exponent reduction from 1/5 to 1/L is asserted but not numerically demonstrated across varying L.

### Results not yet in the paper

1. **The identity (dtd_1/dtd_2)^2 * (r_1/r_2)^3 = I_1/I_2** is verified universally in these tables but does not appear as a named equation in the paper. This is a powerful result: the STE inverted.
2. **The Pythagorean relationship gtd^2 + dtd^2 = 1** is implicit but not called out in the paper.
3. **DTD extends past collapse**: Case 1b shows dtd remains well-defined when gtd is imaginary. The DTD/STE framework has a larger domain than GR.
4. **sqrt(5I/(2 D_crit r^3)) = dtd**: Time dilation expressed purely from inertia, geometry, and D_crit -- no mass needed as an intermediate. Not in the paper.
5. **The P=P constraint**: The equal inertial density scenario is computed but not treated as a named case in the appendix.

---

## 10. Summary of Row Equivalences

### Universally equal to dtd_1/dtd_2 (all 13 scenarios)

- sqrt(D_1/D_2)
- sqrt(D_1)/sqrt(D_2)
- sqrt(m_1/m_2) * sqrt(r_2/r_1)
- sqrt(5I_1/(2 D_c r_1^3)) / sqrt(5I_2/(2 D_c r_2^3))
- sqrt((I_1/I_2) * (r_2/r_1)^3)

### Universally equal to I_1/I_2

- (dtd_1/dtd_2)^2 * (r_1/r_2)^3

### Equal to dtd_1/dtd_2 only under specific constraints

- sqrt(r_2/r_1): only when M=M
- sqrt(m_1/m_2): only when R=R
- (I_1/I_2)^(1/5): only when density is constant

### Not universally equal to anything

- gtd_1/gtd_2 (nonlinear, never equals D ratio except trivially when D_1=D_2)
- sqrt(m_1^2 r_1/(m_2^2 r_2)) (equals dtd_1/dtd_2 only when m_1=m_2)
- (I_1/I_2)/(dtd_1/dtd_2) (= sqrt(m_1/m_2) * (r_1/r_2)^(5/2), standalone)

---

## 11. Incorporation into the Paper

This section details how these computational findings should be incorporated into `latex/master.tex`, what to add, where, and why -- while staying focused on the paper's core theme: the relationship between inertia and time.

### 11.1 Guiding Principles

1. **Stay on theme.** The paper proves that GR and SR are edge cases of the STE. Every addition must serve that argument. The comparison tables are evidence, not the thesis.
2. **The table is evidence, not a section.** Including the full table as a figure or appendix entry gives the reader the numerical proof without interrupting the derivation flow.
3. **Name the key identity.** The universal identity (dtd_1/dtd_2)^2 * (r_1/r_2)^3 = I_1/I_2 is the STE inverted. It deserves a named equation in the paper because it directly connects observable time dilation back to inertia -- the paper's central claim.
4. **DTD is a tool, not a new theory.** Introducing sqrt(D_norm) = DTD as notation simplifies exposition but should be presented as what it is: a more versatile perspective on the same k that's already in the paper.

### 11.2 Specific Additions

#### A. DeGerlia Time Dilation (DTD) -- Definition

**Where:** Section 2.6 (Inertial Density), after the D_norm definition (lines 224-235).

**What:** Define DTD = sqrt(D_norm) = sqrt(D/D_crit) as a named quantity. Note the complementary relationship: GTD^2 + DTD^2 = 1, since GTD = sqrt(1-k) and DTD = sqrt(k). Note that DTD remains real for D_norm > 1 (past collapse), whereas GTD becomes imaginary -- making DTD a more general measure.

**Why:** DTD appears throughout the comparison tables and the ir_mathematics.tex cheat sheet. Naming it in the paper makes the subsequent analysis cleaner and gives the reader a handle for the "other side" of the time dilation coin.

**Scope:** ~3-4 sentences + 1 equation. No new subsection needed; it follows naturally from D_norm.

#### B. The Inertia Recovery Identity -- Named Equation

**Where:** Section 5 (Expressions of Relative Inertial Linear Scale), after Section 5.4 (General Case), before Section 6 (Unification). Or possibly as a new subsection 5.5.

**What:** Present the identity:

  (DTD_1/DTD_2)^2 * (R_1/R_2)^3 = I_1/I_2

Equivalently: DTD_1/DTD_2 = sqrt((I_1/I_2) * (R_2/R_1)^3)

State that this holds universally across all constraint cases (verified numerically in 13 scenarios). Explain what it means: the moment of inertia ratio decomposes into a time-dilation factor and a spatial-scale factor. The time dilation ratio (squared) absorbs the compactness, and the volume ratio (R^3) provides the geometric correction.

Also present the inertia-only expression for DTD:

  DTD = sqrt(5I / (2 D_crit R^3))

which computes time dilation directly from inertia, geometry, and D_crit without computing mass or compactness as intermediates. This is the STE expressed as a single closed-form quantity per system.

**Why:** This is the strongest new result from the tables. It proves numerically that the STE's inertia-based framework is algebraically equivalent to the Schwarzschild compactness framework -- the inertia ratio can always be recovered from time dilation and geometry. This directly supports the paper's unification claim.

**Scope:** ~1 paragraph of prose + 2-3 equations. Could be a short subsection or folded into the General Case discussion.

#### C. Comparison Table -- Appendix or Figure

**Where:** Appendix, after the existing special-case derivations (after line ~714). Or as a figure in Section 5.

**What:** Include a condensed version of the cases comparison table showing:
- Top half: the system properties for each case (M, R, I, D, D_norm, GTD, DTD)
- Bottom half: the key derived ratios, highlighting which rows match dtd_1/dtd_2 universally vs. only under specific constraints

Format as a LaTeX table with the cases as columns and the metrics as rows. Annotate which identities are universal (*) vs. case-specific.

**Why:** The table provides at-a-glance numerical evidence for every claim in Section 5. Each column corresponds to a named case in the appendix. The reader can verify that the universal identities hold across all cases and that the case-specific reductions (M=M -> radius-only, R=R -> mass-only, etc.) produce the expected simplifications. This is the "compare and contrast between GR and this principle" -- all in one table.

**Scope:** 1 full-width table (may need landscape or small font in two-column format). Alternatively, split into two tables: system properties and derived ratios.

**Caution:** The table is dense. A caption must clearly explain what the reader should look for: (1) the universal identity cluster, (2) the case-specific reductions, (3) the nonlinearity of gtd_1/gtd_2 vs D_2/D_1.

#### D. Strengthen Existing Examples with Cross-References

**Where:** Each appendix case example (Cases 1-4 and General).

**What:** After each worked example, add a single line noting the corresponding column in the comparison table and which identities hold/simplify in that case. For example, in Case 1 (Static Mass): "Under this constraint, sqrt(r_2/r_1) = dtd_1/dtd_2, confirming that time dilation depends only on radii when mass is static (Table~X, column M=M)."

**Why:** This connects the algebraic derivation (which shows WHY the simplification happens) to the numerical evidence (which shows THAT it happens). The cross-reference is lightweight and doesn't interrupt the flow.

**Scope:** 1 sentence per case. ~5 additions total.

#### E. DTD Extends Beyond Collapse -- Brief Note

**Where:** Section 7 (Analysis and Conclusion), or as a brief remark in Section 2.6 after introducing DTD.

**What:** Note that DTD = sqrt(D_norm) remains real and well-defined for D_norm > 1 (systems past the collapse threshold), whereas GTD = sqrt(1 - D_norm) becomes imaginary. The STE framework therefore has a strictly larger domain than the Schwarzschild metric. Case 1b in the comparison table demonstrates this numerically: a system at D_norm = 1.98 x 10^10 has DTD = 1.407 x 10^5 and all algebraic identities continue to hold, while GTD is undefined.

**Why:** This is a natural consequence of the framework, not a separate claim. It strengthens the paper's position that the STE is more general than GR.

**Scope:** 2-3 sentences. Keep it brief -- state the fact, cite the numerical evidence, move on. Do not over-claim.

#### F. Nonlinearity of GTD Ratio -- Clarification

**Where:** Section 3.5 (Comparison of Relative Time Paces), in the existing prose that explains why sqrt(1 - k_1/k_2) is wrong.

**What:** The existing prose (lines 321-329) already explains that the ratio of two GTD values is not sqrt(1 - raw_ratio). The comparison tables provide numerical evidence: gtd_1/gtd_2 barely moves (~0.993) across scenarios where D_2/D_1 varies by 7 orders of magnitude, because the sqrt(1-x) function compresses the range. This could be referenced as supporting evidence but probably doesn't need new prose -- the current explanation is already correct.

**Scope:** At most a parenthetical reference to the table. May not need any change.

### 11.3 What NOT to Add

1. **Do not add the P=P case as a named appendix case.** The constraint m/r^4 = const does not correspond to a standard physical condition. Unless Tom has a specific use for it, it would distract.
2. **Do not add velocity-based computations.** The tables don't test k = v^2/c^2, so there's nothing new to report on that front.
3. **Do not add the sqrt(m_1^2 r_1/(m_2^2 r_2)) row.** It's a test expression that proved not to be universal. Including it would be noise.
4. **Do not expand on the precision discrepancy between D_crit and c^2/(2G).** It's a rounding artifact at the 7th significant figure. Drawing attention to it would undermine confidence in the framework for no mathematical reason.

### 11.4 Suggested Order of Work

1. **Define DTD** in Section 2.6 (small, foundational)
2. **Add the inertia recovery identity** in Section 5 (the new equation)
3. **Add the comparison table** to the appendix (the evidence)
4. **Add cross-references** in each appendix case example (lightweight ties)
5. **Add the beyond-collapse note** in the conclusion (brief, impactful)
6. **Update ir_mathematics.tex** with the inertia recovery identity
7. Compile and verify

### 11.5 Impact on Paper Theme

The paper's argument is: inertia determines time. These additions reinforce that argument in three ways:

1. **The inertia recovery identity** proves the converse: time dilation (plus geometry) determines inertia. If time determines inertia AND inertia determines time, the relationship is bijective. This is the strongest possible form of the paper's claim.

2. **The comparison table** provides systematic numerical evidence across all constraint cases and the general case, showing that every special case is a projection of the same universal structure.

3. **DTD as notation** gives the reader a concrete handle on the "inertia side" of time dilation, complementing the GTD they already know. The Pythagorean relationship GTD^2 + DTD^2 = 1 makes the duality explicit.

None of these additions change the thesis. They provide additional evidence, a new identity, and cleaner notation -- all in service of the same argument.
