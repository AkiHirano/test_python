import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
y = np.sin(x)

df = pd.DataFrame({'x':x,'y':y})
print(df.head())

plt.plot(df.x, df.y)
plt.show()


