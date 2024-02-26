fig, axs = plt.subplots(2, 2, figsize=(14, 12))

sns.countplot(data=data, y='Household_Income', ax=axs[0, 0], order = data['Household_Income'].value_counts().index)
axs[0, 0].set_title('Distribution of Household Income')

sns.countplot(data=data, y='Maternal_Education', ax=axs[0, 1], order = data['Maternal_Education'].value_counts().index)
axs[0, 1].set_title('Distribution of Maternal Education')

sns.countplot(data=data, y='Delivery_Mode', ax=axs[1, 0], order = data['Delivery_Mode'].value_counts().index)
axs[1, 0].set_title('Distribution of Delivery Mode')

sns.countplot(data=data, x='NICU_Stay', ax=axs[1, 1], order = data['NICU_Stay'].value_counts().index)
axs[1, 1].set_title('Distribution of NICU Stay')

plt.tight_layout()
plt.show()

language_counts = data['Language'].value_counts()
fig, ax = plt.subplots()
ax.pie(language_counts, labels=language_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
plt.title('Language Distribution')
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=data, x='Maternal_Age', y='Edinburgh_Postnatal_Depression_Scale', ax=ax)
ax.set_title('Maternal Age vs. Edinburgh Postnatal Depression Scale')
ax.set_xlabel('Maternal Age')
ax.set_ylabel('Edinburgh Postnatal Depression Scale Score')
plt.show()
