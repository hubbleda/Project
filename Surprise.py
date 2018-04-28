
# coding: utf-8

# In[14]:

import pandas as pd

data = pd.read_csv('finalreviews.csv',header=None)
data.head()


# In[15]:

from surprise import Dataset
from surprise import Reader

reader = Reader(line_format='user item rating', sep=',')
data = Dataset.load_from_file('finalreviews.csv', reader=reader)
data.raw_ratings[:5]
data.build_full_trainset()


# In[20]:

from surprise import NMF
from surprise.model_selection import train_test_split
from surprise import Dataset
from surprise.model_selection import cross_validate
from surprise.model_selection import KFold

algo = NMF(n_factors=20, n_epochs=500, random_state=1)
trainSet = data.build_full_trainset()
algo.fit(trainSet)
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=10, verbose=True)


# In[17]:

from surprise import accuracy
f = open(r'C:\Users\david_e1h8mr5\Desktop\prototype.txt')
testset =[]
tup = ()
i=0
for line in f:
    info=line.strip().split(',')
    if info!=[""]:
        info[2]=float(info[2])
        info[2]=int(info[2])
        info=tuple(info)
        testset.append(info)
        i+=1

print("actual number of lines= "+str(i))
f.close()
testset = trainSet.build_testset()
pred = algo.test(testset)
accuracy.rmse(pred), accuracy.mae(pred)


# In[ ]:

pred_file= open("C:\\Users\\david_e1h8mr5\\Desktop\\pred.txt","w")
for prediction in pred:
    user=prediction[0]
    book=prediction[1]
    actual_rating=prediction[2]
    recc_rating=prediction[3]
    if actual_rating==0:
        write_str=str(user)+","+str(book)+","+str(actual_rating)+","+str(recc_rating)+"\n"
        pred_file.write(write_str)
pred_file.close()
print("done")

# In[ ]:

from surprise import SVD
algo = SVD(n_factors=20, n_epochs=500, random_state=1)
trainSet = data.build_full_trainset()
algo.fit(trainSet)
cross_validate(algo,data,measures=['RMSE', 'MAE'], cv=10, verbose=True)


# In[ ]:

testset = trainSet.build_testset()
pred = algo.test(testset)
accuracy.rmse(pred, verbose=True), accuracy.mae(pred, verbose=True)


# In[ ]:

from surprise import KNNBasic

algo = KNNBasic(n_factors=20, n_epochs=500, random_state=1)
trainSet = data.build_full_trainset()
algo.fit(trainSet)
cross_validate(algo,data,measures=['RMSE', 'MAE'], cv=10, verbose=True)


# In[ ]:

testset = trainSet.build_testset()
pred = algo.test(testset)
accuracy.rmse(pred, verbose=True), accuracy.mae(pred, verbose=True)


# In[12]:

from surprise import BaselineOnly

cross_validate(BaselineOnly(), data, verbose=True)


# In[25]:


testset = trainSet.build_testset()
pred = algo.test(testset)
accuracy.rmse(pred, verbose=True), accuracy.mae(pred, verbose=True)




