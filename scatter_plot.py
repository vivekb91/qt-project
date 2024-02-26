import pandas as pd
import seaborn as sns

fig, axs = plt.subplots(2, 2, figsize=(14, 12))

sns.scatterplot(data=data, x='PROMIS_Anxiety', y='Edinburgh_Postnatal_Depression_Scale', ax=axs[0, 0])
axs[0, 0].set_title('PROMIS Anxiety vs. Edinburgh Postnatal Depression Scale')

sns.scatterplot(data=data, x='Birth_Weight', y='Gestational_Age_At_Birth', ax=axs[0, 1])
axs[0, 1].set_title('Birth Weight vs. Gestational Age at Birth')

sns.scatterplot(data=data, x='Birth_Weight', y='Birth_Length', ax=axs[1, 0])
axs[1, 0].set_title('Birth Weight vs. Birth Length')

sns.scatterplot(data=data, x='Birth_Length', y='Gestational_Age_At_Birth', ax=axs[1, 1])
axs[1, 1].set_title('Birth Length vs. Gestational Age at Birth')

plt.tight_layout()
plt.show()

