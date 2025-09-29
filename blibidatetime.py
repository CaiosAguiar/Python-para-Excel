# Importações
import datetime
from datetime import date, time, datetime, timedelta

# ======================
# 📅 Criação de Objetos
# ======================

# Data
d = date(2025, 8, 19)
print("Data:", d)

# Horário
t = time(14, 30, 45)
print("Hora:", t)

# Data + Hora
dt = datetime(2025, 8, 19, 14, 30, 45)
print("Data e Hora:", dt)

# Agora
agora = datetime.now()
print("Agora:", agora)

# ======================
# 🔑 Acessando valores
# ======================
hoje = date.today()
print("Ano:", hoje.year)
print("Mês:", hoje.month)
print("Dia:", hoje.day)

# ======================
# 🛠️ Formatação
# ======================
print("Formatado:", agora.strftime("%d/%m/%Y %H:%M:%S"))

# String → datetime
data_str = "19/08/2025 18:15"
data_convertida = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
print("Convertida:", data_convertida)

# ======================
# ⏳ Operações com timedelta
# ======================
ontem = hoje - timedelta(days=1)
amanha = hoje + timedelta(days=1)
print("Ontem:", ontem)
print("Hoje:", hoje)
print("Amanhã:", amanha)

# ======================
# 🔍 Comparação de datas
# ======================
d1 = datetime(2025, 8, 19, 14, 0)
d2 = datetime(2025, 8, 19, 16, 0)
if d1 < d2:
    print("d1 é mais cedo que d2")

# ======================
# ⏰ Timestamp
# ======================
ts = datetime.now().timestamp()
print("Timestamp atual:", ts)

# Timestamp → datetime
dt_from_ts = datetime.fromtimestamp(ts)
print("Datetime a partir do timestamp:", dt_from_ts)

# ======================
# 📏 Diferença entre datas
# ======================
d1 = date(2025, 8, 19)
d2 = date(2024, 8, 19)
dif = d1 - d2
print("Diferença em dias:", dif.days)
