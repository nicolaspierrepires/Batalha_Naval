import numpy as np, math
from scipy.integrate import odeint
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side

mc = 0.340; cr = 3768; ct = 1700; D = 0.059; H = 0.123; Ht = 0.06
A = math.pi*D*H; A1 = math.pi*D*Ht; A2 = A-A1
dl = 0.00009; dT = 0.004; mt = 0.0144; h = 10; kl = 237; kt = 0.06
Tamb = 273.15+19.5; Tr_ini = 273.15+5.0

def modelo_sem(x, t):
    Tr = x[0]; R1 = dl/(kl*A); R2 = 1/(h*A)
    return [1/(mc*cr)*(-(Tr-Tamb)/(R1+R2))]

def modelo_com(x, t):
    Tr, Tt = x
    R1 = dl/(kl*A2); R2 = 1/(h*A2); R3 = dl/(kl*A1); R4 = (dT/2)/(kt*A1); R5 = 1/(h*A1)
    Q1 = (Tamb-Tr)/(R1+R2); Q2 = (Tt-Tr)/(R3+R4); Q3 = (Tamb-Tt)/(R4+R5)
    return [(Q1+Q2)/(mc*cr), (Q3-Q2)/(mt*ct)]

t = np.arange(0, 18980+1, 1)
sem = odeint(modelo_sem, [Tr_ini], t)[:, 0]
com = odeint(modelo_com, [Tr_ini, 273.15+19.0], t)
trc = com[:, 0]; tn = com[:, 1]

wb = Workbook(); ws = wb.active; ws.title = "Temperaturas"
ws.append(["Tempo (s)", "Refrigerante sem neoprene (K)",
           "Refrigerante com neoprene (K)", "Neoprene (K)"])
thin = Side(style="thin", color="BFBFBF")
for c in ws[1]:
    c.font = Font(name="Arial", bold=True, color="FFFFFF")
    c.fill = PatternFill("solid", fgColor="1F4E78")
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
for i in range(0, len(t), 10):
    ws.append([int(t[i]), round(float(sem[i]), 4),
               round(float(trc[i]), 4), round(float(tn[i]), 4)])
for row in ws.iter_rows(min_row=2):
    for j, c in enumerate(row):
        c.font = Font(name="Arial"); c.border = Border(top=thin, bottom=thin, left=thin, right=thin)
        c.alignment = Alignment(horizontal="center")
        c.number_format = "0" if j == 0 else "0.0000"
for col, w in zip("ABCD", [11, 22, 22, 15]):
    ws.column_dimensions[col].width = w
ws.row_dimensions[1].height = 32; ws.freeze_panes = "A2"
ws["F1"] = "Valores calculados pelo modelo (odeint, passo 1 s), amostrados a cada 10 s de 0 a 18980 s (até a linha 1900)."
ws["F2"] = "Tamb = 292,65 K; T inicial refrigerante = 278,15 K (5 °C); T inicial neoprene = 292,15 K (19 °C)."
for k in ("F1", "F2"):
    ws[k].font = Font(name="Arial", italic=True, color="595959")
wb.save("temperaturas_5C_19C_ate_linha1900.xlsx")
print(ws.max_row-1, sem[-1], trc[-1], tn[-1])
