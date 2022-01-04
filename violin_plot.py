import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc
import statistics

# 폰트(Fonts 파일 확인할 것)
font_path = "C:/Windows/Fonts/SSM_BG.ttf"
font_path_2 = 'C:/Windows/Fonts/SSM_HG.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
font_2 = font_manager.FontProperties(fname=font_path_2).get_name()
plt.rc('font', family=font, size=12)
# plt.rc('axes', unicode_minus=False)
sns.set(rc = {'figure.figsize':(15,8)})

sns.set(font=font, rc={"axes.unicode_minus":False}, style="darkgrid")
df = pd.read_excel("D:/바이올린 그래프용_2011_2021.xlsx", "2011_제외")
# print(df)
accept = []
deny = []
money = df['money']

for i in range(0, len(df['고지 여부'])):
    if df['고지 여부'][i] == '고지':
        accept.append(money[i])
    else:
        deny.append(money[i])

accept_line = statistics.median(accept)
deny_line = statistics.median(deny)

# violin plot
sns.violinplot(x=df["money"], y=df["고지 여부"])
sns.stripplot(x=df["money"], y=df["고지 여부"], color = '#aaaaaa')

plt.axvline(x=deny_line, color='coral', linestyle='--', linewidth=3)
plt.axvline(x=accept_line, color='skyblue', linestyle='--', linewidth=3)
plt.xlabel('현재가액 (단위: 천원)', labelpad=15 , fontdict={'family': font_2, 'size': 18})
plt.xlim(-1500000, 5000000)
plt.ylabel('고지여부', labelpad=15, fontdict={'family': font_2, 'size': 18})
plt.show()
