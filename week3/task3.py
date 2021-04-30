import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix


 


dfx = pd.read_csv('F:/Class 09/week3/python-and-data-science-tools-main/week3/SMSSpamCollection.txt',header=None, delimiter = "\t", names=['s','t'])


 

dfx.head()


 

 

plt.figure(figsize=(8, 6))

x_axis = dfx['s'].unique()
y_axis = dfx['s'].value_counts()

plt.bar(x_axis, y_axis)
plt.show()


# In[5]:

# specify target with y_axis
# split database in train and test parts
X = dfx['t']
y = dfx['s']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# In[6]:


X_test.shape


# In[7]:


X_train.shape, y_train.shape, X_test.shape, y_test.shape 


#Convert a collection of text documents to a matrix of token counts

#This implementation produces a sparse representation of the counts using scipy.sparse.csr_matrix.


vect = CountVectorizer(min_df=5, ngram_range=(2, 5), analyzer='char_wb')
vect.fit(X_train)


# In[9]:


X_train_vect = vect.transform(X_train)


# In[10]:


X_test_vect = vect.transform(X_test)


# In[11]:

# use LogisticRegression for fitting our dataset

model = LogisticRegression(C=100, max_iter=300)
model.fit(X_train_vect, y_train)
pred = model.predict(X_test_vect)


# In[12]:

# https://en.wikipedia.org/wiki/Confusion_matrix
print('Logistic Regression\n')
print(confusion_matrix(y_test, pred))


# In[ ]:
