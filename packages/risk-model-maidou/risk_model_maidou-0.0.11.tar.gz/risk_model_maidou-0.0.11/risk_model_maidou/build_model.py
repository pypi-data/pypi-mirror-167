# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 14:07:51 2020

@author: wujian
"""


import copy
import statsmodels.api as sm
from sklearn.metrics import roc_curve,roc_auc_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from itertools import combinations



def ff(best,x1,x2):
    dd=list(x1.keys())
    dr=dict()
    for l in dd:
        j=0
        for k in x1[l]:
            print(k)
            if k in best:
                j=j+1
        dr[l]=j
    for l in dd:
        dr[l]=x2[l]-dr[l]
    return dr
  
#from bin_new import *

class stepwise(object):
    def __init__(self, Data,Data1, col,y):
        # ...
#        self.max_num = 15
#        self.max_actions = 3
        self.col=col
#        self.tree=dict()
        self.col_set=[]
#        self.col_dic=dict()
        self.Data=Data.copy()
        self.Data1=Data1.copy()
#        self.baseline=baseline
        self.y=y
#        self.aselect=pd.DataFrame()
        self.best=[]
#        self.bbest=[]
        self.best_auc=0
#        self.bbest_auc=0
    def s_interfect(self):
        # ...        
        self.Data['1']=1
        self.Data1['1']=1
        return self
    def generate(self):
        # ...        
        cx=list(set(self.col)-set(self.best))
        mm='NA'
        for l in cx:
            try:
                ccc=self.best+[l]
                logit = sm.Logit(self.Data[self.y],self.Data[ccc+['1']])
                result = logit.fit()
                res=result.summary()
                if len(ccc)>1:                
                    aa=self.Data[ccc].corr(method='spearman')
                    
                    mx=aa[aa[l]!=1][l].max()
                else:
                    mx=0
                if self.test(res) and abs(mx)<.6:
                    rre=result.predict(self.Data[ccc+['1']])
                    self.Data['p']=rre    
                    self.Data['p']=self.Data['p'].fillna(0)   

    #                self.col_set.append(set(ccc))               
                    rrre=result.predict(self.Data1[ccc+['1']])
                    self.Data1['p']=rrre 
                    self.Data1['p']=self.Data1['p'].fillna(0)   
                    

                    au=roc_auc_score(np.array(self.Data[self.y]),np.array(self.Data['p']))*0.5+\
                            roc_auc_score(np.array(self.Data1[self.y]),np.array(self.Data1['p']))*0.5
                    if au>self.best_auc:
                        mm=l
                        self.best_auc=au
            except:
                pass
#                return ccc,au
#            else:
#                return self.generate(ccc[:-1])
        if mm!='NA':
            self.best=self.best+[mm]
            return 'verbesset'
        else:
            return 'break'
    def test(self,res): 
        # ...            
        sd=str(res).split('\n')
        cs=[]
        for i in sd[12:-1]:
            cn=i.split(' ')
            cc=copy.copy(cn)
            for i in cn:
                if i=='':
                    cc.remove(i)
            cs.append(cc)
        dic=dict()
        for i in cs:
            dic[i[0]]=i                    
        a0=[]
        a1=[]
        for i in dic:
            if i!='1':
                a0.append(float(dic[i][4]))
                a1.append(float(dic[i][1]))
        if max(a0)>0.05 or min(a1)<0:
            return False
        else:
            return True

            
class stepwise1(object):
    def __init__(self, Data,Data1, col,y,d1,d2,dd):
        # ...
#        self.max_num = 15
#        self.max_actions = 3
        self.col=col
        self.d1=d1
        
        self.d2=d2

        
        #        self.tree=dict()
        self.col_set=[]
#        self.col_dic=dict()
        self.Data=Data.copy()
        self.Data1=Data1.copy()
#        self.baseline=baseline
        self.y=y
#        self.aselect=pd.DataFrame()
        self.best=[]
#        self.bbest=[]
        self.best_auc=0
        self.e=dd
#        self.bbest_auc=0
    def s_interfect(self):
        # ...        
        self.Data['1']=1
        self.Data1['1']=1
#        d2=dict()
        dk=list(self.d1.keys())
        for l in dk:
            cc=[]
            for j in self.d1[l]:
                if j in self.col:
                   cc.append(j)
            self.d1[l]=cc
        return self        
    
    def generate(self):
        # ...        
        mm='NA'
        df=ff(self.best,self.d1,self.d2)
        ddf=pd.DataFrame(index=list(df.keys()))
        ddf['v']=list(df.values())
        ddf=ddf.sort_values(by='v',ascending=False)
        ddf['vv']=ddf.index
        mi=ddf['v'].max()
        if self.e:
            mi=0
        if mi<=0:
            cx=list(set(self.col)-set(self.best))
        else:
            cx=list(set(self.d1[ddf.iloc[0]['vv']])-set(self.best))

        for l in cx:
            try:
                ccc=self.best+[l]
                logit = sm.Logit(self.Data[self.y],self.Data[ccc+['1']])
                result = logit.fit()
                res=result.summary()
                
                if len(ccc)>1:                
                    aa=self.Data[ccc].corr(method='spearman')
                    
                    mx=aa[aa[l]!=1][l].max()
                else:
                    mx=0
                if self.test(res) and abs(mx)<.5:
                    rre=result.predict(self.Data[ccc+['1']])
                    self.Data['p']=rre    
                    self.Data['p']=self.Data['p'].fillna(0)   

    #                self.col_set.append(set(ccc))               
                    rrre=result.predict(self.Data1[ccc+['1']])
                    self.Data1['p']=rrre 
                    self.Data1['p']=self.Data1['p'].fillna(0)   
                    

                    au=roc_auc_score(np.array(self.Data[self.y]),np.array(self.Data['p']))*0.5+\
                            roc_auc_score(np.array(self.Data1[self.y]),np.array(self.Data1['p']))*0.5
                    if au>self.best_auc:
                        mm=l
                        self.best_auc=au
                
                    
                        
            except:
                pass
#                return ccc,au
#            else:
#                return self.generate(ccc[:-1])
        if mm!='NA':
            self.best=self.best+[mm]
            self.ddi=dict()
            for l in list(self.d1.keys()):
                j=0
                for k in self.d1[l]:
                    if k in self.best:
                        j=j+1
                self.ddi[l]=j

            return 'verbesset'
        else:
            return 'break'
    def test(self,res): 
        # ...            
        sd=str(res).split('\n')
        cs=[]
        for i in sd[12:-1]:
            cn=i.split(' ')
            cc=copy.copy(cn)
            for i in cn:
                if i=='':
                    cc.remove(i)
            cs.append(cc)
        dic=dict()
        for i in cs:
            dic[i[0]]=i                    
        a0=[]
        a1=[]
        for i in dic:
            if i!='1':
                a0.append(float(dic[i][4]))
                a1.append(float(dic[i][1]))
        if max(a0)>0.05 or min(a1)<0:
            return False
        else:
            return True
            
            

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy



class MonteCarlo(object):
    def __init__(self, Data,Data1, col,y,baseline=0):
        # ...
        self.max_num = 15
        self.max_actions = 3
        self.col=col
        self.tree=dict()
        self.col_set=[]
        self.col_dic=dict()
        self.Data=Data.copy()
        self.Data1=Data1.copy()
        self.baseline=baseline
        self.y=y
#        self.aselect=pd.DataFrame()
        self.best=[]
        self.bbest=[]
        self.best_auc=0
        self.bbest_auc=0
    def s_interfect(self):
        # ...        
        self.Data['1']=1
        self.Data1['1']=1
        return self
    def first_action(self,asc=[]):
        # ...
        pii=pd.DataFrame()
        au=[]
        co=[]
        for l in self.col:
            if l not in asc:
                ccc=asc+[l]+['1']
                try:
                    logit = sm.Logit(self.Data[self.y],self.Data[ccc])
                    result = logit.fit()
                    rre=result.predict(self.Data[ccc])
                    self.Data['p']=rre
                    rrre=result.predict(self.Data1[ccc])
                    self.Data1['p']=rrre
                    co.append(l)               
                    au.append(roc_auc_score(np.array(self.Data[self.y]),np.array(self.Data['p']))*0.5+\
                              roc_auc_score(np.array(self.Data1[self.y]),np.array(self.Data1['p']))*0.5)
                except:
                    pass
        pii[0]=co
        pii[1]=au
        pii=pii.sort_values(by=1)
        pii=pii.sort_values(by=1,ascending=False)
        self.col_set=list(pii.iloc[:20][0])
#        self.aselect=self.aselect.append(pii.iloc[:10])
        if asc==[]:
            self.baseline=np.mean(pii.iloc[:20][1])
        self.col_dic=dict()    
        for l in self.col_set:
            a=dict()
            a[tuple([l])]=list(pii[pii[0]==l][1])[0]            
            self.col_dic[l]=a
        self.col_set=[]
        return self    
    def update_leaves(self,x,l=3):
        # ...
        ca=list(set(self.col)-set(x))
        k=randint(0, len(ca)-1)   
        l=l-1
        if l>=0:
            return self.update_leaves(x+[ca[k]],l)
        else:
            return x
        
    def generate(self,ccc):
        # ...        
        if set(ccc) not in self.col_set:
            logit = sm.Logit(self.Data[self.y],self.Data[ccc+['1']])
            result = logit.fit()
            res=result.summary()
            if self.test(res):
                rre=result.predict(self.Data[ccc+['1']])
                self.Data['p']=rre    
                rrre=result.predict(self.Data1[ccc+['1']])
                self.Data1['p']=rrre    
                self.col_set.append(set(ccc))               
                au=roc_auc_score(np.array(self.Data[self.y]),np.array(self.Data['p']))*0.5+\
                        roc_auc_score(np.array(self.Data1[self.y]),np.array(self.Data1['p']))*0.5
                return ccc,au
            else:
                return self.generate(ccc[:-1])
        else:
            return ccc,0
    def test(self,res): 
        # ...            
        sd=str(res).split('\n')
        cs=[]
        for i in sd[12:-1]:
            cn=i.split(' ')
            cc=copy.copy(cn)
            for i in cn:
                if i=='':
                    cc.remove(i)
            cs.append(cc)
        dic=dict()
        for i in cs:
            dic[i[0]]=i                    
        a0=[]
        a1=[]
        for i in dic:
            if i!='1':
                a0.append(float(dic[i][4]))
                a1.append(float(dic[i][1]))
        if max(a0)>0.05 or min(a1)<0:
            return False
        else:
            return True
    def random_spread(self,x,k,epoch=20):
#        epoch=10
        auc=[]
        for l in range(epoch):
            try:
                c=self.update_leaves(x)
                a,b=self.generate(c)
                if b>np.log((self.baseline+0.05)/self.baseline):
                    auc.append(b)
                if b>self.bbest_auc:
                    self.bbest_auc=b
                    self.bbest=c
            except:
                pass
        if len(auc)>0:
            return np.mean(auc)
        else:
            return 0
    def deep_spread(self):
        better='Na'
        self.bbest=[]
        self.bbest_auc=0
        for l in self.col_dic:
            ccc=self.best+[l]
            score=self.random_spread(ccc,len(ccc))
            if score>self.best_auc:
                better=l
                self.best_auc=score
        if better!='Na':
            self.best=self.best+[better]
            self.first_action(self.best)
            print (len(self.best))
            return self
        else:
            print ('Done')
            return 'Done'            
    def deep_spread_1(self):
        better='Na'
#        self.bbest=[]
#        self.bbest_auc=0
        ca=list(set(self.col)-set(self.best))
        cacol=[]
        for l in range(15):
            k=randint(0, len(ca)-1)
            if k not in cacol:
                cacol.append(k)
            else:
                k=randint(0, len(ca)-1)                
            ccc=self.best+[ca[k]]
            score=self.random_spread(ccc,len(ccc),15)
            if score>self.best_auc:
                better=ca[k]
                self.best_auc=score
        if better!='Na':
            self.best=self.best+[better]
            self.col_set=[]
#            self.first_action(self.best)
            return self
        else:
            print ('Done')
            return 'Done'


