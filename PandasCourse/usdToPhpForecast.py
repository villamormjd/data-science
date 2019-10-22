import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_html("https://walletinvestor.com/forex-forecast/usd-php-prediction")
x = []
y = []
z = []
for min, max, closing in zip(data[0]["Minimum rate"], data[0]["Maximum rate"], data[0]["Closing rate"]):
    x.append(min.split(" ")[1])
    y.append(max.split(" ")[1])
    z.append(closing.split(" ")[1])

# plt.plot(x, data[0]["Date"])
# plt.plot(data[0]["Maximum rate"], data[0]["Date"])
plt.plot(data[0]["Date"], x, marker='', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4,
         label="Minimum rate")
plt.plot(data[0]["Date"], y, marker='', color='red', linewidth=2, label="Maximum rate")
plt.plot(data[0]["Date"], z, marker='', color='olive', linewidth=2, linestyle='dashed',
         label="Closing rate")

plt.legend()
plt.tight_layout()
plt.show()

print(data[0].head())
