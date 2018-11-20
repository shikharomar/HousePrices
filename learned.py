
#####     --Finding top 10 correlating variables for the target--     #####
k = 10 #number of variables for heatmap
cols = corrMatrix.nlargest(k, 'SalePrice')['SalePrice'].index #getting top 10 rows [and then their index names] based on the value of SalePrice from correlation matrix
cm = np.corrcoef(df_train[cols].values.T) #finding their correlation
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
plt.show()
#####          #####

#####     --Counting the number of Null values in the dataset and their removal--     #####
total = df_train.isnull().sum().sort_values(ascending = False)
percent = (df_train.isnull().sum() / df_train.isnull().count()).sort_values(ascending = False)
missing = pd.concat([total, percent], axis =1, keys = ['Total', 'Percent'])

df_train = df_train.drop(missing[missing['Total'] > 1].index, axis =1)  # Removal based on column name(index)
df_train = df_train.drop(df_train.loc[df_train['Electrical'].isnull()].index) # Removal from a particular column based on row index
df_train.isnull().sum().max() # Just checking if all the null values are removed
#####          #####


#####     --Checks for Linear Regression--     #####
    Linear relationship
    Multivariate normality
    No or little multicollinearity
    No autocorrelation
    Homoscedasticity
#####          #####


#####     --Different ways of removing outliers--     #####


#####          #####


#####     --Pipeline--     #####

> Data description
	df.info(), df.describe()
> Removing duplicate rows
	df.duplicate().sum(), df.drop_duplicates() 
> Getting important features, scatter plots and heatmaps
> Checks for Linear Regression assumptions (Normality, Homoscedasticity, Autocorrelation, Multivariate Collinearity, Linear Relationship)
>

#####          #####


