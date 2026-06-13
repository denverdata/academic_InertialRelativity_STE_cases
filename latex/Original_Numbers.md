\begin{mdframed}
\textbf{Example (Static Mass, Table Case 1):} System 1 is the system being measured; System 2 is a same-mass reference system at a different radius.

System properties:

$S_1$: $M_1 = 2.00000 \times 10^{30}$\,kg, $R_1 = 3.00000 \times 10^{3}$\,m, $\rho_1 = 1.76839 \times 10^{19}$\,kg/m$^3$, $I_1 = 7.20000 \times 10^{36}$\,kg$\cdot$m$^2$.

$S_2$: $M_2 = 2.00000 \times 10^{30}$\,kg, $R_2 = 7.00000 \times 10^{8}$\,m, $\rho_2 = 1.39203 \times 10^{3}$\,kg/m$^3$, $I_2 = 3.92000 \times 10^{47}$\,kg$\cdot$m$^2$.

Calculate GTD ratio via DTD:
dtd1=sqrt(k1_d) 
where k1_D=(m1/r1)/D_crit = 2.00000e30/3000 / 6.73295e26 = 9.90155e-1
dtd1=sqrt(9.90155e-1) = 9.95065e-1

dtd2=sqrt(k) 
where k2_D=(m2/r2)/D_crit = sqrt(2.00000e30kg/7e8m / 6.73295e26kg/m) = 4.24352e-6
dtd2=sqrt(4.24352e-6) = 2.05998e-3

dtd1/dtd2 = 9.95065e-1 / 2.05998e-3 = 4.82981e2

gtg1/gtg2=sqrt(1-dtd1^2)/sqrt(1-dtd2^2) = sqrt(1-(9.95065e-1)^2)/sqrt(1-(2.05998e-3)^2) = =sqrt(9.84500e-3)/sqrt(1-4.24352e-6) = 9.92220e-2/(1-2.12176e-6) = 9.92222e-2

Verify by calculataing Gtd directly via the Schwarzschild radius ratio:

Schwarzschild radii:
\[
r_{s,1} = 2GM_1/c^2 = 2.97046 \times 10^{3} \text{ m}
\]
\[
r_{s,2} = 2GM_2/c^2 = 2.97046 \times 10^{3} \text{ m}
\]

Calculaete k_r values from the R_s/r ratio:
k1_r_r=R1_s/r1 = 2.97046e3/3e3 = 9.90155e-1
k2_r_r=R2_s/r2 = 2.97046e3/7e8 = 4.24352e-6

Calculate GTD via Schwarzschild radius ratio:
gtd1=sqrt(1-k1_r) = sqrt(9.84500e-3) = 9.92220e-2
gtd2=sqrt(1-k2_r) = sqrt(1-4.24352e-6) = 1-2.12176e-6

Time-dilation ratio between System 1 and System 2, computed two ways:
gtd1_r/gtd2_r = 9.92222e-2
how does gtd1_r/gtd2_r compare to gtd1_d/gtd2_d? They are the same, confirming that the same compactness ratio $k$ is returned by both the Schwarzschild radius and the DeGerlia compactness ratio, and that both yield the same GTD result.

All values above appear in column $M\!=\!M$ of Table~\ref{tab:pair_properties} in \ref{app:pair_table}.
\end{mdframed}


---



\begin{mdframed}
\textbf{Example (Static Mass, Table Case 1):} System 1 is the system being measured; System 2 is a same-mass reference system at a different radius.

System properties:

$S_1$: $M_1 = 2.00000 \times 10^{30}$\,kg, $R_1 = 3.00000 \times 10^{3}$\,m, $\rho_1 = 1.76839 \times 10^{19}$\,kg/m$^3$, $I_1 = 7.20000 \times 10^{36}$\,kg$\cdot$m$^2$.

$S_2$: $M_2 = 2.00000 \times 10^{30}$\,kg, $R_2 = 7.00000 \times 10^{8}$\,m, $\rho_2 = 1.39203 \times 10^{3}$\,kg/m$^3$, $I_2 = 3.92000 \times 10^{47}$\,kg$\cdot$m$^2$.

Calculate GTD ratio via DTD:
\begin{align*}
\mathrm{DTD}_1 &= \sqrt{k_{D,1}} \\
\text{where } k_{D,1} &= \frac{M_1/R_1}{D_{crit}} = \frac{2.00000 \times 10^{30}/3.00000 \times 10^{3}}{6.73295 \times 10^{26}} = 9.9015538 \times 10^{-1} \\
\mathrm{DTD}_1 &= \sqrt{9.9015538 \times 10^{-1}} = 9.9506552 \times 10^{-1}
\end{align*}
\begin{align*}
\mathrm{DTD}_2 &= \sqrt{k_{D,2}} \\
\text{where } k_{D,2} &= \frac{M_2/R_2}{D_{crit}} = \frac{2.00000 \times 10^{30}/7.00000 \times 10^{8}}{6.73295 \times 10^{26}} = 4.24352 \times 10^{-6} \\
\mathrm{DTD}_2 &= \sqrt{4.24352 \times 10^{-6}} = 2.05998 \times 10^{-3}
\end{align*}
\[
\mathrm{DTD}_1/\mathrm{DTD}_2 = \frac{9.9506552 \times 10^{-1}}{2.05998 \times 10^{-3}} = 4.83046 \times 10^{2}
\]
\begin{align*}
\mathrm{GTD}_1/\mathrm{GTD}_2 &= \frac{\sqrt{1 - \mathrm{DTD}_1^2}}{\sqrt{1 - \mathrm{DTD}_2^2}} \\
  &= \frac{\sqrt{1 - (9.9506552 \times 10^{-1})^2}}{\sqrt{1 - (2.05998 \times 10^{-3})^2}} \\
  &= \frac{\sqrt{9.84462 \times 10^{-3}}}{\sqrt{1 - 4.24352 \times 10^{-6}}} \\
  &= \frac{9.9220058 \times 10^{-2}}{1 - 2.12176 \times 10^{-6}} \\
  &= 1 - 9.00780 \times 10^{-1}
\end{align*}

Verify by calculating GTD directly via the Schwarzschild radius ratio:

Schwarzschild radii:
\[
r_{s,1} = 2GM_1/c^2 = 2.97046 \times 10^{3} \text{ m}
\]
\[
r_{s,2} = 2GM_2/c^2 = 2.97046 \times 10^{3} \text{ m}
\]

Calculate $k_R$ values from the $r_s/R$ ratio:
\begin{align*}
k_{R,1} &= \frac{r_{s,1}}{R_1} = \frac{2.97046 \times 10^{3}}{3.00000 \times 10^{3}} = 9.9015333 \times 10^{-1} \\
k_{R,2} &= \frac{r_{s,2}}{R_2} = \frac{2.97046 \times 10^{3}}{7.00000 \times 10^{8}} = 4.24351 \times 10^{-6}
\end{align*}

Calculate GTD via Schwarzschild radius ratio:
\begin{align*}
\mathrm{GTD}_1 &= \sqrt{1 - k_{R,1}} = \sqrt{9.84667 \times 10^{-3}} = 1 - 9.00770 \times 10^{-1} \\
\mathrm{GTD}_2 &= \sqrt{1 - k_{R,2}} = \sqrt{1 - 4.24351 \times 10^{-6}} = 1 - 2.12176 \times 10^{-6}
\end{align*}

Time-dilation ratio between System 1 and System 2, computed two ways:
\[
\mathrm{GTD}_{R,1}/\mathrm{GTD}_{R,2} = 1 - 9.00770 \times 10^{-1}
\]
how does $\mathrm{GTD}_{R,1}/\mathrm{GTD}_{R,2}$ compare to $\mathrm{GTD}_{D,1}/\mathrm{GTD}_{D,2}$? They are the same, confirming that the same compactness ratio $k$ is returned by both the Schwarzschild radius and the DeGerlia compactness ratio, and that both yield the same GTD result.

All values above appear in column $M\!=\!M$ of Table~\ref{tab:pair_properties} in \ref{app:pair_table}.
\end{mdframed}


---
---V***




\begin{mdframed}[
linewidth=0.8pt,
roundcorner=4pt,
innerleftmargin=10pt,
innerrightmargin=10pt,
innertopmargin=10pt,
innerbottommargin=10pt
]

\noindent\textbf{Example (Static Mass, Table Case 1):}
System 1 is the system being measured; System 2 is a same-mass reference system at a different radius.

\medskip

\noindent\textbf{System properties:}

\begin{align*}
S_1:\quad
&M_1 = 2.00000 \times 10^{30},\mathrm{kg},
&&R_1 = 3.00000 \times 10^{3},\mathrm{m},\
&\rho_1 = 1.76839 \times 10^{19},\mathrm{kg/m^3},
&&I_1 = 7.20000 \times 10^{36},\mathrm{kg\cdot m^2}.
\end{align*}

\begin{align*}
S_2:\quad
&M_2 = 2.00000 \times 10^{30},\mathrm{kg},
&&R_2 = 7.00000 \times 10^{8},\mathrm{m},\
&\rho_2 = 1.39203 \times 10^{3},\mathrm{kg/m^3},
&&I_2 = 3.92000 \times 10^{47},\mathrm{kg\cdot m^2}.
\end{align*}

\medskip

\noindent\textbf{Calculate GTD ratio via DTD:}

\begin{align*}
\mathrm{dtd1} &= \sqrt{k1_d}
\end{align*}

\noindent where
\begin{align*}
k1_D
&= \frac{(m1/r1)}{D_\mathrm{crit}}\
&= \frac{2.00000e30/3000}{6.73295e26}\
&= 9.90155e-1.
\end{align*}

\begin{align*}
\mathrm{dtd1}
&= \sqrt{9.90155e-1}\
&= 9.95065e-1.
\end{align*}

\begin{align*}
\mathrm{dtd2} &= \sqrt{k}
\end{align*}

\noindent where
\begin{align*}
k2_D
&= \frac{(m2/r2)}{D_\mathrm{crit}}\
&= \sqrt{\frac{2.00000e30,\mathrm{kg}/7e8,\mathrm{m}}
{6.73295e26,\mathrm{kg/m}}}\
&= 4.24352e-6.
\end{align*}

\begin{align*}
\mathrm{dtd2}
&= \sqrt{4.24352e-6}\
&= 2.05998e-3.
\end{align*}

\begin{align*}
\frac{\mathrm{dtd1}}{\mathrm{dtd2}}
&= \frac{9.95065e-1}{2.05998e-3}\
&= 4.82981e2.
\end{align*}

\medskip

\noindent\textbf{GTD ratio from DTD:}

\begin{align*}
\frac{\mathrm{gtg1}}{\mathrm{gtg2}}
&= \frac{\sqrt{1-\mathrm{dtd1}^2}}{\sqrt{1-\mathrm{dtd2}^2}}\
&= \frac{\sqrt{1-(9.95065e-1)^2}}
{\sqrt{1-(2.05998e-3)^2}}\
&= \frac{\sqrt{9.84500e-3}}
{\sqrt{1-4.24352e-6}}\
&= \frac{9.92220e-2}{1-2.12176e-6}\
&= 9.92222e-2.
\end{align*}

\medskip

\noindent\textbf{Verify by calculataing Gtd directly via the Schwarzschild radius ratio:}

\noindent\textbf{Schwarzschild radii:}
\begin{align*}
r_{s,1}
&= 2GM_1/c^2\
&= 2.97046 \times 10^{3},\mathrm{m},
\end{align*}

\begin{align*}
r_{s,2}
&= 2GM_2/c^2\
&= 2.97046 \times 10^{3},\mathrm{m}.
\end{align*}

\medskip

\noindent\textbf{Calculaete k\_r values from the R\_s/r ratio:}

\begin{align*}
k_{1,r,r}
&= R_{1,s}/r_1\\
&= 2.97046e3/3e3\\
&= 9.9015333e-1.
\end{align*}

\begin{align*}
k_{2,r,r}
&= R_{2,s}/r_2\\
&= 2.97046e3/7e8\\
&= 4.24352e-6.
\end{align*}

\medskip

\noindent\textbf{Calculate GTD via Schwarzschild radius ratio:}

\begin{align*}
\mathrm{gtd1}
&= \sqrt{1-k1_r}\
&= \sqrt{1-9.9015333e-1}\
&= \sqrt{9.84667e-3}\
&= 9.92303e-2\
&= 1-9.007697e-1.
\end{align*}

\begin{align*}
\mathrm{gtd2}
&= \sqrt{1-k2_r}\
&= \sqrt{1-4.24352e-6}\
&= \sqrt{9.999957565e-1}\
&= 9.999978782e-1\
&= 1 - 2.12180e-6.
\end{align*}

\medskip

\noindent\textbf{Time-dilation ratio between System 1 and System 2, computed two ways:}

\begin{align*}
\mathrm{gtd1_r}/\mathrm{gtd2_r}
&= 9.92222e-2.
\end{align*}

\noindent how does gtd1\_r/gtd2\_r compare to gtd1\_d/gtd2\_d? They are the same, confirming that the same compactness ratio k is returned by both the Schwarzschild radius and the DeGerlia compactness ratio, and that both yield the same GTD result.

\medskip

\noindent
All values above appear in column M\!=\!M of Table~\ref{tab:pair_properties} in \ref{app:pair_table}.

\end{mdframed}


---
last good one:


\subsection{Example (Static Mass, Table Case 1)}
\label{subsec:example_static_mass_table_case_1}

\begin{mdframed}[
linewidth=0.8pt,
roundcorner=4pt,
innerleftmargin=10pt,
innerrightmargin=10pt,
innertopmargin=10pt,
innerbottommargin=10pt
]

\noindent\textbf{Example (Static Mass, Table Case 1):} System 1 is the system being measured; System 2 is a same-mass reference system at a different radius.

\medskip

\noindent\textbf{System properties:}

\begin{align*}
S_1:\quad
&M_1 = 2.00000 \times 10^{30},\text{kg},&
&R_1 = 3.00000 \times 10^{3},\text{m},\
&\rho_1 = 1.76839 \times 10^{19},\text{kg/m}^3,&
&I_1 = 7.20000 \times 10^{36},\text{kg}\cdot\text{m}^2.
\end{align*}

\begin{align*}
S_2:\quad
&M_2 = 2.00000 \times 10^{30},\text{kg},&
&R_2 = 7.00000 \times 10^{8},\text{m},\
&\rho_2 = 1.39203 \times 10^{3},\text{kg/m}^3,&
&I_2 = 3.92000 \times 10^{47},\text{kg}\cdot\text{m}^2.
\end{align*}

\medskip

\noindent\textbf{Calculate GTD ratio via DTD:}

\begin{align*}
dtd1 &= \sqrt{k1_d}
\end{align*}

\noindent where
\begin{align*}
k1_D
&= (m1/r1)/D_{\text{crit}}\
&= 2.00000e30/3.00000e3 ,/, 6.73295e26\
&= 9.9015538e-1
\end{align*}

\begin{align*}
dtd1
&= \sqrt{9.9015538e-1}\
&= 9.9506551e-1
\end{align*}

\medskip

\begin{align*}
dtd2 &= \sqrt{k}
\end{align*}

\noindent where
\begin{align*}
k2_D
&= (m2/r2)/D_{\text{crit}}\
&= \sqrt{2.00000e30kg/7.00000e8m ,/, 6.73295e26kg/m}\
&= 4.24352e-6
\end{align*}

\begin{align*}
dtd2
&= \sqrt{4.24352e-6}\
&= 2.05998e-3
\end{align*}

\begin{align*}
dtd1/dtd2
&= 9.9506551e-1 ,/, 2.05998e-3\
&= 4.82981e2
\end{align*}

\medskip

\noindent\textbf{GTD ratio from DTD:}

\begin{align*}
gtg1/gtg2
&= \sqrt{1-dtd1^2}/\sqrt{1-dtd2^2}\
&= \sqrt{1-(9.9506551e-1)^2}/\sqrt{1-(2.05998e-3)^2}\
&= \sqrt{1-9.9015536e-1}/\sqrt{1-4.24352e-6}\
&= \sqrt{9.84464e-3}/\sqrt{9.999957565e-1}\
&= 9.92220e-2/(9.999978782)\
&= 9.9220369e-2
\end{align*}

\medskip

\noindent\textbf{Verify by calculataing Gtd directly via the Schwarzschild radius ratio:}

\medskip

\noindent\textbf{Schwarzschild radii:}

r_{s,1} = 2GM_1/c^2 = 2.97046 \times 10^{3} \text{ m}

r_{s,2} = 2GM_2/c^2 = 2.97046 \times 10^{3} \text{ m}

\medskip

\noindent\textbf{Calculaete k_r values from the R_s/r ratio:}

\begin{align*}
k1_r_r
&= R1_s/r1\
&= 2.97046e3/3.00000e3\
&= 9.9015333e-1
\end{align*}

\begin{align*}
k2_r_r
&= R2_s/r2\
&= 2.97046e3/7.00000e8\
&= 4.24352e-6
\end{align*}

\medskip

\noindent\textbf{Calculate GTD via Schwarzschild radius ratio:}

\begin{align*}
gtd1
&= \sqrt{1-k1_r}\
&= \sqrt{1-9.9015333e-1}\
&= \sqrt{9.84667e-3}\
&= 9.92303e-2\
&= 1-9.007697e-1
\end{align*}

\begin{align*}
gtd2
&= \sqrt{1-k2_r}\
&= \sqrt{1-4.24352e-6}\
&= \sqrt{9.999957565e-1}\
&= 9.999978782e-1\
&= 1 - 2.12180e-6
\end{align*}

gtd1_r/gtd2_r = 9.92303e-2\ /\ 9.999978782e-1 = 9.92305e-2

\medskip

\noindent\textbf{Time-dilation ratio between System 1 and System 2, computed two ways:}

\begin{align*}
gtd1_d/gtd2_d &= 9.92203e-2
gtd1_r/gtd2_r &= 9.92305e-2
difference=0.000002 (below the margin of error imparted by G)

\end{align*}

\noindent how does gtd1_r/gtd2_r compare to gtd1_d/gtd2_d? They are the same, confirming that the same compactness ratio $k$ is returned by both the Schwarzschild radius and the DeGerlia compactness ratio, and that both yield the same GTD result.

\medskip

\noindent All values above appear in column $M!=!M$ of Table~\ref{tab:pair_properties} in \ref{app:pair_table}.

\end{mdframed}


---



\begin{mdframed}
\textbf{Example (Static Mass, Table Case 1):} System 1 is the system being measured; System 2 is a same-mass reference system at a different radius.

System properties:

$S_1$: $M_1 = 2.00000 \times 10^{30}$\,kg, $R_1 = 3.00000 \times 10^{3}$\,m, $\rho_1 = 1.76839 \times 10^{19}$\,kg/m$^3$, $I_1 = 7.20000 \times 10^{36}$\,kg$\cdot$m$^2$.

$S_2$: $M_2 = 2.00000 \times 10^{30}$\,kg, $R_2 = 7.00000 \times 10^{8}$\,m, $\rho_2 = 1.39203 \times 10^{3}$\,kg/m$^3$, $I_2 = 3.92000 \times 10^{47}$\,kg$\cdot$m$^2$.

Calculate GTD ratio via DTD:
\[
dtd1 = \sqrt{k1_d}
\]
where
\begin{align*}
k &= (M_1/R_1)/D_{\mathrm{crit}} = (2.00000e30/3.00000e3) / 6.73295e26\\
  &= 9.9015538e-1
\end{align*}
\[
dtd1 = \sqrt{9.9015538e-1} = 9.9506551e-1
\]
\[
dtd2 = \sqrt{k}
\]
where
\begin{align*}
k &= (M_2/R_2)/D_{\mathrm{crit}} = (2.00000e30/7.00000e8) / 6.73295e26\\
  &= 4.24352e-6
\end{align*}
\[
dtd2 = \sqrt{4.24352e-6} = 2.05998e-3
\]
\[
dtd1/dtd2 = 9.9506551e-1 / 2.05998e-3 = 4.82981e2
\]

GTD ratio from DTD:
\begin{align*}
gtg1/gtg2
&= \sqrt{1-dtd1^2}/\sqrt{1-dtd2^2}\\
&= \sqrt{1-(9.9506551e-1)^2}/\sqrt{1-(2.05998e-3)^2}\\
&= \sqrt{1-9.9015536e-1}/\sqrt{1-4.24352e-6}\\
&= \sqrt{9.84464e-3}/\sqrt{9.999957565e-1}\\
&= 9.92220e-2/(9.999978782)\\
&= 9.9220369e-2
\end{align*}

Verify by calculataing Gtd directly via the Schwarzschild radius ratio:

Schwarzschild radii:
\[
r_{s1} = 2GM_1/c^2 = 2.97046 \times 10^{3} \text{ m}
\]
\[
r_{s2} = 2GM_2/c^2 = 2.97046 \times 10^{3} \text{ m}
\]

Calculaete k\_r values from the R\_s/r ratio:
\[
k_{r1} = r_{s1}/R_1 = 2.97046e3/3.00000e3 = 9.9015333e-1
\]
\[
k2_r = r2_s/R2 = 2.97046e3/7.00000e8 = 4.24352e-6
\]

Calculate GTD via Schwarzschild radius ratio:
\begin{align*}
gtd1 &= \sqrt{1-k1_r} = \sqrt{1-9.9015333e-1} = \sqrt{9.84667e-3}\\
  &= 9.92303e-2 = 1-9.007697e-1\\
gtd2 &= \sqrt{1-k2_r} = \sqrt{1-4.24352e-6} = \sqrt{9.999957565e-1}\\
  &= 9.999978782e-1 = 1 - 2.12180e-6
\end{align*}
\begin{align*}
gtd1_r/gtd2_r &= 9.92303e-2\ /\ 9.999978782e-1\\
  &= 9.92305e-2
\end{align*}

Time-dilation ratio between System 1 and System 2, computed two ways:
\[
gtd1_d/gtd2_d = 9.92203e-2
\]
\[
gtd1_r/gtd2_r = 9.92305e-2
\]
\begin{align*}
\text{difference} &= 0.000002\\
&\quad \text{(below the margin of error imparted by G)}
\end{align*}

how does gtd1\_r/gtd2\_r compare to gtd1\_d/gtd2\_d? They are the same, confirming that the same compactness ratio $k$ is returned by both the Schwarzschild radius and the DeGerlia compactness ratio, and that both yield the same GTD result.

All values above appear in column $M!=!M$ of Table~\ref{tab:pair_properties} in \ref{app:pair_table}.

\end{mdframed}


---
Good one!!


\begin{mdframed}
\textbf{Example (Static Mass, Table Case 1):} System 1 is the system being measured; System 2 is a same-mass reference system at a different radius.

System properties:

$S_1$: $M_1 = 2.00000 \times 10^{30}$\,kg, $R_1 = 3.00000 \times 10^{3}$\,m, $\rho_1 = 1.76839 \times 10^{19}$\,kg/m$^3$, $I_1 = 7.20000 \times 10^{36}$\,kg$\cdot$m$^2$.

$S_2$: $M_2 = 2.00000 \times 10^{30}$\,kg, $R_2 = 7.00000 \times 10^{8}$\,m, $\rho_2 = 1.39203 \times 10^{3}$\,kg/m$^3$, $I_2 = 3.92000 \times 10^{47}$\,kg$\cdot$m$^2$.

Calculate GTD ratio via DTD:
\[
dtd1 = \sqrt{k1_d}
\]
where
\begin{align*}
k &= (M_1/R_1)/D_{\mathrm{crit}} = (2.00000e30/3.00000e3) / 6.73295e26\\
  &= 9.9015538e-1
\end{align*}
\[
dtd1 = \sqrt{9.9015538e-1} = 9.9506551e-1
\]
\[
dtd2 = \sqrt{k}
\]
where
\begin{align*}
k &= (M_2/R_2)/D_{\mathrm{crit}} = (2.00000e30/7.00000e8) / 6.73295e26\\
  &= 4.24352e-6
\end{align*}
\[
dtd2 = \sqrt{4.24352e-6} = 2.05998e-3
\]
\[
dtd1/dtd2 = 9.9506551e-1 / 2.05998e-3 = 4.82981e2
\]

GTD ratio from DTD:
\begin{align*}
gtg1/gtg2
&= \sqrt{1-dtd1^2}/\sqrt{1-dtd2^2}\\
&= \sqrt{1-(9.9506551e-1)^2}/\sqrt{1-(2.05998e-3)^2}\\
&= \sqrt{1-9.9015536e-1}/\sqrt{1-4.24352e-6}\\
&= \sqrt{9.84464e-3}/\sqrt{9.999957565e-1}\\
&= 9.92220e-2/(9.999978782)\\
&= 9.9220369e-2
\end{align*}

Verify by calculataing Gtd directly via the Schwarzschild radius ratio:

Schwarzschild radii:
\[
r_{s1} = 2GM_1/c^2 = 2.97046 \times 10^{3} \text{ m}
\]
\[
r_{s2} = 2GM_2/c^2 = 2.97046 \times 10^{3} \text{ m}
\]

Calculaete k\_r values from the R\_s/r ratio:
\[
k_{r1} = r_{s1}/R_1 = 2.97046e3/3.00000e3 = 9.9015333e-1
\]
\[
k2_r = r2_s/R2 = 2.97046e3/7.00000e8 = 4.24352e-6
\]

Calculate GTD via Schwarzschild radius ratio:
\begin{align*}
gtd1 &= \sqrt{1-k1_r} = \sqrt{1-9.9015333e-1} = \sqrt{9.84667e-3}\\
  &= 9.92303e-2 = 1-9.007697e-1\\
gtd2 &= \sqrt{1-k2_r} = \sqrt{1-4.24352e-6} = \sqrt{9.999957565e-1}\\
  &= 9.999978782e-1 = 1 - 2.12180e-6
\end{align*}
\begin{align*}
gtd1_r/gtd2_r &= 9.92303e-2\ /\ 9.999978782e-1\\
  &= 9.92305e-2
\end{align*}

Time-dilation ratio between System 1 and System 2, computed two ways:
\[
gtd1_d/gtd2_d = 9.92203e-2
\]
\[
gtd1_r/gtd2_r = 9.92305e-2
\]
\begin{align*}
\text{difference} &= 0.000002\\
&\quad \text{(below the margin of error imparted by G)}
\end{align*}

how does gtd1\_r/gtd2\_r compare to gtd1\_d/gtd2\_d? They are the same, confirming that the same compactness ratio $k$ is returned by both the Schwarzschild radius and the DeGerlia compactness ratio, and that both yield the same GTD result.

All values above appear in column $M!=!M$ of Table~\ref{tab:pair_properties} in \ref{app:pair_table}.

\end{mdframed}


---

good also??
\begin{mdframed}
\textbf{Example (Static Mass, Table Case 1):} System 1 is the system being measured; System 2 is a same-mass reference system at a different radius.

\medskip\noindent\textbf{System properties:}

$S_1$: $M_1 = 2.00000 \times 10^{30}$\,kg, $R_1 = 3.00000 \times 10^{3}$\,m, $\rho_1 = 1.76839 \times 10^{19}$\,kg/m$^3$, $I_1 = 7.20000 \times 10^{36}$\,kg$\cdot$m$^2$.

$S_2$: $M_2 = 2.00000 \times 10^{30}$\,kg, $R_2 = 7.00000 \times 10^{8}$\,m, $\rho_2 = 1.39203 \times 10^{3}$\,kg/m$^3$, $I_2 = 3.92000 \times 10^{47}$\,kg$\cdot$m$^2$.

\medskip\noindent\textbf{Calculate GTD ratio via DTD:}
\[
dtd1 = \sqrt{k1_d}
\]

where
\[
\begin{aligned}
k &= (M_1/R_1)/D_{\mathrm{crit}} = (2.00000e30/3.00000e3) / 6.73295e26\\
  &= 9.9015538e-1
\end{aligned}
\]
\[
dtd1 = \sqrt{9.9015538e-1} = 9.9506551e-1
\]
\[
dtd2 = \sqrt{k}
\]

where
\[
\begin{aligned}
k &= (M_2/R_2)/D_{\mathrm{crit}} = (2.00000e30/7.00000e8) / 6.73295e26\\
  &= 4.24352e-6
\end{aligned}
\]
\[
dtd2 = \sqrt{4.24352e-6} = 2.05998e-3
\]
\[
dtd1/dtd2 = 9.9506551e-1 / 2.05998e-3 = 4.82981e2
\]

\medskip\noindent\textbf{GTD ratio from DTD:}
\[
\begin{aligned}
gtg1/gtg2
&= \sqrt{1-dtd1^2}/\sqrt{1-dtd2^2}\\
&= \sqrt{1-(9.9506551e-1)^2}/\sqrt{1-(2.05998e-3)^2}\\
&= \sqrt{1-9.9015536e-1}/\sqrt{1-4.24352e-6}\\
&= \sqrt{9.84464e-3}/\sqrt{9.999957565e-1}\\
&= 9.92220e-2/(9.999978782)\\
&= 9.9220369e-2
\end{aligned}
\]

\medskip\noindent\textbf{Verify by calculataing Gtd directly via the Schwarzschild radius ratio:}

Schwarzschild radii:
\[
r_{s1} = 2GM_1/c^2 = 2.97046 \times 10^{3} \text{ m}
\]
\[
r_{s2} = 2GM_2/c^2 = 2.97046 \times 10^{3} \text{ m}
\]

Calculaete k\_r values from the R\_s/r ratio:
\[
k_{r1} = r_{s1}/R_1 = 2.97046e3/3.00000e3 = 9.9015333e-1
\]
\[
k2_r = r2_s/R2 = 2.97046e3/7.00000e8 = 4.24352e-6
\]

Calculate GTD via Schwarzschild radius ratio:
\[
\begin{aligned}
gtd1 &= \sqrt{1-k1_r} = \sqrt{1-9.9015333e-1} = \sqrt{9.84667e-3}\\
  &= 9.92303e-2 = 1-9.007697e-1\\
gtd2 &= \sqrt{1-k2_r} = \sqrt{1-4.24352e-6} = \sqrt{9.999957565e-1}\\
  &= 9.999978782e-1 = 1 - 2.12180e-6
\end{aligned}
\]
\[
\begin{aligned}
gtd1_r/gtd2_r &= 9.92303e-2\ /\ 9.999978782e-1\\
  &= 9.92305e-2
\end{aligned}
\]

\medskip\noindent\textbf{Time-dilation ratio between System 1 and System 2, computed two ways:}
\[
gtd1_d/gtd2_d = 9.92203e-2
\]
\[
gtd1_r/gtd2_r = 9.92305e-2
\]
\[
\begin{aligned}
\text{difference} &= 0.000002\\
&\quad \text{(below the margin of error imparted by G)}
\end{aligned}
\]

how does gtd1\_r/gtd2\_r compare to gtd1\_d/gtd2\_d? They are the same, confirming that the same compactness ratio $k$ is returned by both the Schwarzschild radius and the DeGerlia compactness ratio, and that both yield the same GTD result.

All values above appear in column $M!=!M$ of Table~\ref{tab:pair_properties} in \ref{app:pair_table}.

\end{mdframed}


---


new example added


%.  [[static mass example - this example reflects two systems that is very near the Schwarzschild radius]]
%---

\begin{mdframed}
\textbf{Example (Static Mass):} System 1 is the system being measured; System 2 is a same-mass reference at its Schwarzschild radius. The benchmark configuration sets $D_{norm2} = 1$, the condition under which the two-system compactness ratio reduces to the standard one-system Schwarzschild GTD expression.

\medskip\noindent\textbf{System properties:}

\begin{center}
\small
\begin{tabular}{@{}lrr@{}}
\toprule
 & System 1 ($S_1$) & System 2 ($S_2$) \\
\midrule
$M$ (\unit{\kilogram}) & \num{2.00000e30} & \num{2.00000e30} \\
$R$ (\unit{\meter}) & \num{3.00000e3} & \num{2.97046e3} \\
\bottomrule
\end{tabular}
\end{center}

\noindent $R_2 = r_s = 2GM_2/c^2$: System 2 sits at its Schwarzschild radius.

\medskip\noindent\textbf{Calculate GTD ratio via DTD:}
\[
\mathrm{DTD}_1 = \sqrt{k_{d1}}
\]

where
\[
\begin{aligned}
k_{d1} &= (M_1/R_1)/D_{\mathrm{crit}}\\
  &= (2.00000 \times 10^{30}\,\text{kg}/3.00000 \times 10^{3}\,\text{m}) / 6.73295 \times 10^{26}\,\text{kg/m}\\
  &= 9.9015538 \times 10^{-1}
\end{aligned}
\]
\[
\mathrm{DTD}_1 = \sqrt{9.9015538 \times 10^{-1}} = 9.9506551 \times 10^{-1}
\]
\[
\mathrm{DTD}_2 = \sqrt{k_{d2}}
\]

where
\[
\begin{aligned}
k_{d2} &= (M_2/R_2)/D_{\mathrm{crit}}\\
  &= (2.00000 \times 10^{30}\,\text{kg}/2.97046 \times 10^{3}\,\text{m}) / 6.73295 \times 10^{26}\,\text{kg/m}\\
  &= 1.00000
\end{aligned}
\]
\[
\mathrm{DTD}_2 = \sqrt{1.00000} = 1.00000
\]
\[
\mathrm{DTD}_1/\mathrm{DTD}_2 = 9.9506551 \times 10^{-1} / 1.00000 = 9.9506551 \times 10^{-1}
\]

With $k_{d2} = 1$, the two-system compactness ratio reduces to System 1's individual compactness.

\medskip\noindent\textbf{GTD ratio from DTD:}
\[
\begin{aligned}
\mathrm{GTD}_{d1} &= \sqrt{1-\mathrm{DTD}_1^2} = \sqrt{9.84462 \times 10^{-3}}\\
  &= 9.92207 \times 10^{-2} = 1-9.00780 \times 10^{-1}
\end{aligned}
\]

\medskip\noindent\textbf{Verify by calculating GTD directly via the Schwarzschild radius ratio:}

Schwarzschild radii:
\[
r_{s1} = 2GM_1/c^2 = 2.97046 \times 10^{3} \text{ m}
\]
\[
r_{s2} = 2GM_2/c^2 = 2.97046 \times 10^{3} \text{ m}
\]

Calculate $k_r$ values from the $r_s/R$ ratio:
\[
\begin{aligned}
k_{r1} &= r_{s1}/R_1 = 2.97046 \times 10^{3}\,\text{m}/3.00000 \times 10^{3}\,\text{m}\\
  &= 9.9015333 \times 10^{-1}
\end{aligned}
\]
\[
k_{r2} = r_{s2}/R_2 = 2.97046 \times 10^{3}\,\text{m}/2.97046 \times 10^{3}\,\text{m} = 1.00000
\]

Calculate GTD via Schwarzschild radius ratio:
\[
\begin{aligned}
\mathrm{GTD}_{r1} &= \sqrt{1-k_{r1}} = \sqrt{9.84530 \times 10^{-3}}\\
  &= 9.92235 \times 10^{-2} = 1-9.00777 \times 10^{-1}\\
\mathrm{GTD}_{r2} &= \sqrt{1-k_{r2}} = \sqrt{1-1.00000} = 0
\end{aligned}
\]

\medskip\noindent\textbf{Time-dilation ratio between System 1 and System 2, computed two ways:} with $\mathrm{GTD}_2 = 0$, the ratio reduces to System 1's individual GTD:
\[
\mathrm{GTD}_{d1} = 9.92207 \times 10^{-2}
\]
\[
\mathrm{GTD}_{r1} = 9.92235 \times 10^{-2}
\]
\[
\begin{aligned}
\text{difference} &= 3.41449 \times 10^{-6}\\
&\quad \text{(below the margin of error imparted by G)}
\end{aligned}
\]

How does $\mathrm{GTD}_{r1}$ compare to $\mathrm{GTD}_{d1}$? They are the same, confirming that the same compactness ratio $k$ is returned by both the Schwarzschild radius and the DeGerlia compactness ratio, and that both yield the same GTD result.
\end{mdframed}

---


\subsection{Example (Static Mass, Table Case 1)}
\label{subsec:example_static_mass_table_case_1}

\begin{mdframed}
\textbf{Example (Static Mass, Table Case 1):} System 1 is the system being measured; System 2 is a same-mass reference system at a different radius.

\medskip\noindent\textbf{System properties:}

$S_1$: $M_1 = 2.00000 \times 10^{30}$\,kg, $R_1 = 3.00000 \times 10^{3}$\,m, $\rho_1 = 1.76839 \times 10^{19}$\,kg/m$^3$, $I_1 = 7.20000 \times 10^{36}$\,kg$\cdot$m$^2$.

$S_2$: $M_2 = 2.00000 \times 10^{30}$\,kg, $R_2 = 7.00000 \times 10^{8}$\,m, $\rho_2 = 1.39203 \times 10^{3}$\,kg/m$^3$, $I_2 = 3.92000 \times 10^{47}$\,kg$\cdot$m$^2$.

\medskip\noindent\textbf{Calculate GTD ratio via DTD:}
\[
dtd1 = \sqrt{k1_d}
\]

where
\[
\begin{aligned}
k &= (M_1/R_1)/D_{\mathrm{crit}} = (2.00000e30/3.00000e3) / 6.73295e26\\
  &= 9.9015538e-1
\end{aligned}
\]
\[
dtd1 = \sqrt{9.9015538e-1} = 9.9506551e-1
\]
\[
dtd2 = \sqrt{k}
\]

where
\[
\begin{aligned}
k &= (M_2/R_2)/D_{\mathrm{crit}} = (2.00000e30/7.00000e8) / 6.73295e26\\
  &= 4.24352e-6
\end{aligned}
\]
\[
dtd2 = \sqrt{4.24352e-6} = 2.05998e-3
\]
\[
dtd1/dtd2 = 9.9506551e-1 / 2.05998e-3 = 4.82981e2
\]

\medskip\noindent\textbf{GTD ratio from DTD:}
\[
\begin{aligned}
gtg1/gtg2
&= \sqrt{1-dtd1^2}/\sqrt{1-dtd2^2}\\
&= \sqrt{1-(9.9506551e-1)^2}/\sqrt{1-(2.05998e-3)^2}\\
&= \sqrt{1-9.9015536e-1}/\sqrt{1-4.24352e-6}\\
&= \sqrt{9.84464e-3}/\sqrt{9.999957565e-1}\\
&= 9.92220e-2/(9.999978782)\\
&= 9.9220369e-2
\end{aligned}
\]

\medskip\noindent\textbf{Verify by calculataing Gtd directly via the Schwarzschild radius ratio:}

Schwarzschild radii:
\[
r_{s1} = 2GM_1/c^2 = 2.97046 \times 10^{3} \text{ m}
\]
\[
r_{s2} = 2GM_2/c^2 = 2.97046 \times 10^{3} \text{ m}
\]

Calculaete k\_r values from the R\_s/r ratio:
\[
k_{r1} = r_{s1}/R_1 = 2.97046e3/3.00000e3 = 9.9015333e-1
\]
\[
k2_r = r2_s/R2 = 2.97046e3/7.00000e8 = 4.24352e-6
\]

Calculate GTD via Schwarzschild radius ratio:
\[
\begin{aligned}
gtd1 &= \sqrt{1-k1_r} = \sqrt{1-9.9015333e-1} = \sqrt{9.84667e-3}\\
  &= 9.92303e-2 = 1-9.007697e-1\\
gtd2 &= \sqrt{1-k2_r} = \sqrt{1-4.24352e-6} = \sqrt{9.999957565e-1}\\
  &= 9.999978782e-1 = 1 - 2.12180e-6
\end{aligned}
\]
\[
\begin{aligned}
gtd1_r/gtd2_r &= 9.92303e-2\ /\ 9.999978782e-1\\
  &= 9.92305e-2
\end{aligned}
\]

\medskip\noindent\textbf{Time-dilation ratio between System 1 and System 2, computed two ways:}
\[
gtd1_d/gtd2_d = 9.92203e-2
\]
\[
gtd1_r/gtd2_r = 9.92305e-2
\]
\[
\begin{aligned}
\text{difference} &= 0.000002\\
&\quad \text{(below the margin of error imparted by G)}
\end{aligned}
\]

how does gtd1\_r/gtd2\_r compare to gtd1\_d/gtd2\_d? They are the same, confirming that the same compactness ratio $k$ is returned by both the Schwarzschild radius and the DeGerlia compactness ratio, and that both yield the same GTD result.

All values above appear in column $M!=!M$ of Table~\ref{tab:pair_properties} in \ref{app:pair_table}.

\end{mdframed}


---

Final version - seems okay, has some unique


When the two systems share the same mass, the mass terms cancel in $k$:
\[
k = \frac{M_1 R_2}{M_2 R_1} = \frac{R_2}{R_1}
\]
The compactness ratio reduces to a ratio of radii. Equivalently in terms of DeGerlia compactness $D = M/R$, this is $D_1/D_2 = R_2/R_1$; each system's normalized DeGerlia compactness against the DeGerlia Threshold yields $D/D_{crit} = r_s/R$, recovering the Schwarzschild gravitational time dilation parameter.

%---
%.  [[static mass example - this example reflects two systems that is very near the Schwarzschild radius]]
%---

\begin{mdframed}
\textbf{Example (Static Mass):} System 1 is the system being measured; System 2 is a same-mass reference at its Schwarzschild radius. The benchmark configuration sets $D_{norm2} = 1$, the condition under which the two-system compactness ratio reduces to the standard one-system Schwarzschild GTD expression.

\medskip\noindent\textbf{System properties:}

\begin{center}
\small
\begin{tabular}{@{}lrr@{}}
\toprule
 & System 1 ($S_1$) & System 2 ($S_2$) \\
\midrule
$M$ (\unit{\kilogram}) & \num{2.00000e30} & \num{2.00000e30} \\
$R$ (\unit{\meter}) & \num{3.00000e3} & \num{2.97046e3} \\
\bottomrule
\end{tabular}
\end{center}

\noindent $R_2 = r_s = 2GM_2/c^2$.

\medskip\noindent\textbf{Calculate GTD ratio via DTD:}
\[
\mathrm{DTD}_1 = \sqrt{k_{d1}}
\]

where
\[
\begin{aligned}
k_{d1} &= (M_1/R_1)/D_{\mathrm{crit}}\\
  &= (2.00000 \times 10^{30}\,\text{kg}/3.00000 \times 10^{3}\,\text{m}) / 6.73295 \times 10^{26}\,\text{kg/m}\\
  &= 9.9015538 \times 10^{-1}
\end{aligned}
\]
\[
\mathrm{DTD}_1 = \sqrt{9.9015538 \times 10^{-1}} = 9.9506551 \times 10^{-1}
\]
\[
\mathrm{DTD}_2 = \sqrt{k_{d2}}
\]

where
\[
\begin{aligned}
k_{d2} &= (M_2/R_2)/D_{\mathrm{crit}}\\
  &= (2.00000 \times 10^{30}\,\text{kg}/2.97046 \times 10^{3}\,\text{m}) / 6.73295 \times 10^{26}\,\text{kg/m}\\
  &= 1.00000
\end{aligned}
\]
\[
\mathrm{DTD}_2 = \sqrt{1.00000} = 1.00000
\]
\[
\mathrm{DTD}_1/\mathrm{DTD}_2 = 9.9506551 \times 10^{-1} / 1.00000 = 9.9506551 \times 10^{-1}
\]

With $k_{d2} = 1$, the two-system compactness ratio reduces to System 1's individual compactness.

\medskip\noindent\textbf{GTD ratio from DTD:}
\[
\begin{aligned}
\mathrm{GTD}_{d1} &= \sqrt{1-\mathrm{DTD}_1^2} = \sqrt{9.84462 \times 10^{-3}}\\
  &= 9.92207 \times 10^{-2} = 1-9.00780 \times 10^{-1}
\end{aligned}
\]

\medskip\noindent\textbf{Verify by calculating GTD directly via the Schwarzschild radius ratio:}

Schwarzschild radii:
\[
r_{s1} = 2GM_1/c^2 = 2.97046 \times 10^{3} \text{ m}
\]
\[
r_{s2} = 2GM_2/c^2 = 2.97046 \times 10^{3} \text{ m}
\]

Calculate $k_r$ values from the $r_s/R$ ratio:
\[
\begin{aligned}
k_{r1} &= r_{s1}/R_1 = 2.97046 \times 10^{3}\,\text{m}/3.00000 \times 10^{3}\,\text{m}\\
  &= 9.9015333 \times 10^{-1}
\end{aligned}
\]
\[
k_{r2} = r_{s2}/R_2 = 2.97046 \times 10^{3}\,\text{m}/2.97046 \times 10^{3}\,\text{m} = 1.00000
\]

Calculate GTD via Schwarzschild radius ratio:
\[
\begin{aligned}
\mathrm{GTD}_{r1} &= \sqrt{1-k_{r1}} = \sqrt{9.84530 \times 10^{-3}}\\
  &= 9.92235 \times 10^{-2} = 1-9.00777 \times 10^{-1}\\
\mathrm{GTD}_{r2} &= \sqrt{1-k_{r2}} = \sqrt{1-1.00000} = 0
\end{aligned}
\]

\medskip\noindent\textbf{Time-dilation ratio between System 1 and System 2, computed two ways:} with $\mathrm{GTD}_2 = 0$, the ratio reduces to System 1's individual GTD:
\[
\mathrm{GTD}_{d1} = 9.92207 \times 10^{-2}
\]
\[
\mathrm{GTD}_{r1} = 9.92235 \times 10^{-2}
\]
\[
\begin{aligned}
\text{difference} &= 0.000028 
&\quad \text{(below the margin of error imparted by G)}
\end{aligned}
\]

How does $\mathrm{GTD}_{r1}$ compare to $\mathrm{GTD}_{d1}$? They are the same, confirming that the same compactness ratio $k$ is returned by both the Schwarzschild radius and the DeGerlia compactness ratio, and that both yield the same GTD result.
\end{mdframed}

---


\subsection{Example (Static Mass, Table Case 1)}
\label{subsec:example_static_mass_table_case_1}

\begin{mdframed}
\textbf{Example (Static Mass, Table Case 1):} System 1 is the system being measured; System 2 is a same-mass reference system at a different radius.

\medskip\noindent\textbf{System properties:}

$S_1$: $M_1 = 2.00000 \times 10^{30}$\,kg, $R_1 = 3.00000 \times 10^{3}$\,m, $\rho_1 = 1.76839 \times 10^{19}$\,kg/m$^3$, $I_1 = 7.20000 \times 10^{36}$\,kg$\cdot$m$^2$.

$S_2$: $M_2 = 2.00000 \times 10^{30}$\,kg, $R_2 = 7.00000 \times 10^{8}$\,m, $\rho_2 = 1.39203 \times 10^{3}$\,kg/m$^3$, $I_2 = 3.92000 \times 10^{47}$\,kg$\cdot$m$^2$.

\medskip\noindent\textbf{Calculate GTD ratio via DTD:}
\[
dtd1 = \sqrt{k1_d}
\]

where
\[
\begin{aligned}
k &= (M_1/R_1)/D_{\mathrm{crit}} = (2.00000e30/3.00000e3) / 6.73295e26\\
  &= 9.9015538e-1
\end{aligned}
\]
\[
dtd1 = \sqrt{9.9015538e-1} = 9.9506551e-1
\]
\[
dtd2 = \sqrt{k}
\]

where
\[
\begin{aligned}
k &= (M_2/R_2)/D_{\mathrm{crit}} = (2.00000e30/7.00000e8) / 6.73295e26\\
  &= 4.24352e-6
\end{aligned}
\]
\[
dtd2 = \sqrt{4.24352e-6} = 2.05998e-3
\]
\[
dtd1/dtd2 = 9.9506551e-1 / 2.05998e-3 = 4.82981e2
\]

\medskip\noindent\textbf{GTD ratio from DTD:}
\[
\begin{aligned}
gtg1/gtg2
&= \sqrt{1-dtd1^2}/\sqrt{1-dtd2^2}\\
&= \sqrt{1-(9.9506551e-1)^2}/\sqrt{1-(2.05998e-3)^2}\\
&= \sqrt{1-9.9015536e-1}/\sqrt{1-4.24352e-6}\\
&= \sqrt{9.84464e-3}/\sqrt{9.999957565e-1}\\
&= 9.92220e-2/(9.999978782)\\
&= 9.9220369e-2
\end{aligned}
\]

\medskip\noindent\textbf{Verify by calculataing Gtd directly via the Schwarzschild radius ratio:}

Schwarzschild radii:
\[
r_{s1} = 2GM_1/c^2 = 2.97046 \times 10^{3} \text{ m}
\]
\[
r_{s2} = 2GM_2/c^2 = 2.97046 \times 10^{3} \text{ m}
\]

Calculaete k\_r values from the R\_s/r ratio:
\[
k_{r1} = r_{s1}/R_1 = 2.97046e3/3.00000e3 = 9.9015333e-1
\]
\[
k2_r = r2_s/R2 = 2.97046e3/7.00000e8 = 4.24352e-6
\]

Calculate GTD via Schwarzschild radius ratio:
\[
\begin{aligned}
gtd1 &= \sqrt{1-k1_r} = \sqrt{1-9.9015333e-1} = \sqrt{9.84667e-3}\\
  &= 9.92303e-2 = 1-9.007697e-1\\
gtd2 &= \sqrt{1-k2_r} = \sqrt{1-4.24352e-6} = \sqrt{9.999957565e-1}\\
  &= 9.999978782e-1 = 1 - 2.12180e-6
\end{aligned}
\]
\[
\begin{aligned}
gtd1_r/gtd2_r &= 9.92303e-2\ /\ 9.999978782e-1\\
  &= 9.92305e-2
\end{aligned}
\]

\medskip\noindent\textbf{Time-dilation ratio between System 1 and System 2, computed two ways:}
\[
gtd1_d/gtd2_d = 9.92203e-2
\]
\[
gtd1_r/gtd2_r = 9.92305e-2
\]
\[
\begin{aligned}
\text{difference} &= 0.000002\\
&\quad \text{(below the margin of error imparted by G)}
\end{aligned}
\]

how does gtd1\_r/gtd2\_r compare to gtd1\_d/gtd2\_d? They are the same, confirming that the same compactness ratio $k$ is returned by both the Schwarzschild radius and the DeGerlia compactness ratio, and that both yield the same GTD result.

All values above appear in column $M!=!M$ of Table~\ref{tab:pair_properties} in \ref{app:pair_table}.

\end{mdframed}

