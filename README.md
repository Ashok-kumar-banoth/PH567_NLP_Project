# Nonlinear Dynamics: Logistic-Map Simulations and an Educational Cipher Demonstration

This repository records a numerical study of the logistic map and a small
interval-mapping text-cipher demonstration.  It is a course-project archive,
not a cryptographic software package.

## Contents

| Path | Purpose |
| --- | --- |
| `baptista_chaos_encryption.py` | Original repository script, preserved unchanged. |
| `code/baptista_chaos_encryption.py` | A copy of the original script, retained alongside the submitted materials. |
| `code/nonlinear_dynamics_chaos_encryption.py` | Supplied Google Colab export used to generate the simulations and figures. |
| `results/` | Seven supplied, generated PNG figures. |
| `report/` | LaTeX report source and bibliography. |

## Setup and execution

The submitted script was exported from Google Colab and uses Python, NumPy,
and Matplotlib.  It was run in Colab to produce the included figures.

```bash
python -m venv .venv
# Windows PowerShell
.venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
python code/nonlinear_dynamics_chaos_encryption.py
```

For a local run, remove or comment out the final two lines beginning
`from google.colab import files` and `files.download(...)`; those lines are
only for downloading a ZIP from Colab.  The calculations and PNG generation
occur before them.  In Colab, the script may be run as exported.

## Model and numerical settings

The simulation uses the logistic map

```text
x_(n+1) = r x_n (1 - x_n)
```

unless a parameter sweep is stated otherwise.  The main orbit uses `r = 4.0`
and `x0 = 0.213`.

| Calculation | Settings in the submitted script |
| --- | --- |
| Time series | 300 iterations, `r = 4.0`, `x0 = 0.213` |
| Bifurcation diagram | 3,000 values in `[2.8, 4.0]`; 1,000 transient and 200 stored iterates per value |
| Lyapunov sweep | 3,000 values in `[2.5, 4.0]`; 1,000 transient and 3,000 accumulation iterates per value |
| Sensitivity | `r = 4.0`; initial values `0.213` and `0.213 + 1e-10`; 70 iterates |
| Invariant density | `r = 4.0`; 1,000 transient and 500,000 retained samples |
| Text demonstration | 26 equal-width intervals over `[0,1]`, `r = 4.0`, initial state `0.213` |

## Results

The supplied run reports a Lyapunov exponent at `r = 4` of `0.693020`,
compared with the analytical value `ln(2) = 0.693147`.  The 500,000-sample
invariant-density calculation has mean `0.4992599`, close to the theoretical
mean `0.5`.  Four test messages - `CHAOS`, `LOGISTICMAP`,
`NONLINEARDYNAMICS`, and `ENCRYPTION` - were recovered exactly.  These are
correctness checks for the demonstration only; they are not a security
evaluation.

### Figure guide

| Figure | What it shows |
| --- | --- |
| `logistic_map_timeseries.png` | Chaotic-looking orbit for the selected initial state at `r = 4`. |
| `bifurcation_diagram.png` | Long-term states as the control parameter varies. |
| `lyapunov_exponent.png` | Numerically estimated largest Lyapunov exponent across the parameter sweep. |
| `sensitivity.png` | Nearby initial conditions separating under iteration. |
| `trajectory_separation.png` | Same separation displayed on a logarithmic vertical scale. |
| `invariant_density.png` | Empirical histogram against the `r = 4` invariant density. |
| `ciphertext_distribution.png` | Iteration-count distribution for the four small text tests. |

## Scope and security disclosure

The text cipher is a **simplified educational interval-mapping demonstration**.
It is not a faithful reproduction of Baptista's 1998 algorithm and is not
secure for real-world use.  In particular, it uses a fixed `r = 4.0`, a fixed
initial state for each test, 26 equal-width letter intervals, ordinary
floating-point iteration, and no modern key management, authentication, or
cryptographic security analysis.  It also skips characters outside `A`--`Z`.

The accompanying report distinguishes the simulations performed here from the
literature review.  It does not claim to reproduce the original protocol,
published attacks, countermeasures, finite-precision analysis, or a security
evaluation.  For background, see Baptista (1998), Alvarez et al. (2003), and
Li et al. (2004) in `report/references.bib`.
