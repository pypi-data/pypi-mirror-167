# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 14:07:51 2020

@author: wujian
"""

import copy
import statsmodels.api as sm
import numpy as np
from sklearn.metrics import roc_curve,roc_auc_score

from risk_model_maidou.build_model import *



class ensembel_logit:
    def __init__(self,y,data,ci,col): 
        self.y=y
        self.data=data.copy()
        self.ci=ci
        self.cr=[]
        self.co=[]
        self.cres=[]
        self.col=col

        self.cr1=[]
        self.co1=[]
        self.cres1=[]
    def _train(self,n,rate):
        y=self.y
        self.data['1']=1
        cr=[]
        co=[]
        cres=[]
        cc=[]
        for c in self.ci:
            aaa=stepwise(Data=self.data,Data1=self.data,col=c,y=self.y)    
            aaa.s_interfect()
            am=0 
            for l in range(n):
                cq=aaa.generate()
                if cq=='break':
                    break
                if aaa.best_auc-am>rate:
                    am=aaa.best_auc
                else:
                    break
            coooo=aaa.best
            logit = sm.Logit(self.data[y],self.data[coooo+['1']])          
            result = logit.fit()
            res=result.summary()
            self.data['p_'+str(self.ci.index(c))]=result.predict(self.data[coooo+['1']])
            self.data['p_'+str(self.ci.index(c))]=self.data['p_'+str(self.ci.index(c))].apply(lambda x:-np.log(1/x-1))
            cc.append('p_'+str(self.ci.index(c)))
            cr.append(result)
            co.append(coooo)            
            cres.append(res)
            
        logit = sm.Logit(self.data[y],self.data[cc+['1']])                  
        result = logit.fit()
        res=result.summary()
            
        self.cr=cr
        self.co=co
        self.cres=cres
        self.cr.append(result)
        self.co.append(cc)
        self.cres.append(res)
        
        return self

    def _train1(self,n,rate):
        self.data['1']=1

        aaa=stepwise(Data=self.data,Data1=self.data,col=self.col,y=self.y)    
        aaa.s_interfect()
        am=0
 
        for l in range(n):
            cq=aaa.generate()
            if cq=='break':
                break
            if aaa.best_auc-am>rate:
                am=aaa.best_auc
            else:
                break
        coooo=aaa.best
        logit = sm.Logit(self.data[self.y],self.data[coooo+['1']])                  
        result = logit.fit()
        res=result.summary()
#        logit = sm.Logit(self.data[y],self.data[cc+['1']])          
#        result = logit.fit()
#        res=result.summary()            
        self.cr1=result
        self.co1=coooo
        self.cres1=res        
        return self
        
        
    def _predict(self,data1):
        if len(self.co)==0:
            print ('have not train the model') 
            return None
        else:
            for i in range(len(self.cr))[:-1]:
                data1['p_'+str(i)]=self.cr[i].predict(data1[self.co[i]+['1']])
                data1['p_'+str(i)]=data1['p_'+str(i)].apply(lambda x:-np.log(1/x-1))

            data1['p_re']=self.cr[-1].predict(data1[self.co[-1]+['1']])
            return data1['p_re']
    def predict(self,data1):
        if len(self.co)==0:
            print ('have not train the model') 
            return None
        else:
            for i in range(len(self.cr))[:-1]:
                data1['p_'+str(i)]=self.cr[i].predict(data1[self.co[i]+['1']])
                data1['p_model_'+str(i)]=self.cr[i].predict(data1[self.co[i]+['1']])

                data1['p_'+str(i)]=data1['p_'+str(i)].apply(lambda x:-np.log(1/x-1))
                

            data1['p_re']=self.cr[-1].predict(data1[self.co[-1]+['1']])
            for l in self.co[-1]:
                del data1[l]
            return data1

    def _predict1(self,data1):
        if len(self.co1)==0:
            print ('have not train the model') 
            return None
        else:
            data1['p_s']=self.cr1.predict(data1[self.co1+['1']])
            return data1['p_s']
                



def sore_trains(data,me1,predict,coo):
#    dat1=data.copy()
#    for j in  coo:
#            dat1[j]=0
#    dat1['1']=0
#    dat1['p_mid']=predict(dat1)
#    dat1['mid_score']=dat1['p_mid'].apply(lambda x:(np.log(1/x-1)/np.log(2)-np.log(20)/np.log(2))*20+600).apply(int)    
#    constant1=dat1['mid_score'].mean()


    dat1=data.copy()
    try:
        del dat1['1']
    except:
        pass
    for j in  coo:
            dat1[j]=0
    dat1['1']=1
    dat1['p_mid']=predict(dat1[coo+['1']])
    dat1['mid_score']=dat1['p_mid'].apply(lambda x:(np.log(1/x-1)/np.log(2)-np.log(20)/np.log(2))*20+600).apply(int)    
    constant=dat1['mid_score'].mean()

        
    scor=[]    
    for l in coo:
        dat1=data.copy()
        try:
            del dat1['1']
        except:
            pass
        dat1['1']=1

        for j in  coo:
            if j!=l:
                dat1[j]=0
        dat1['p_mid']=predict(dat1[coo+['1']])
        dat1['mid_score']=dat1['p_mid'].apply(lambda x:(np.log(1/x-1)/np.log(2)-np.log(20)/np.log(2))*20+600).apply(int)-constant    
#        dat1['mid_score']=dat1['p_mid'].apply(lambda x:(np.log(1/x-1)/np.log(2))*20).apply(int)
        mid=dat1.groupby(l)['mid_score'].mean()
        
        mid=pd.DataFrame(mid)
        cd=me1[me1['var']==l].copy()
        cd['1']=range(len(cd))
        cd['WOE']=cd['WOE']+cd['1']/100000
        cd['in']=cd.index
        cd.index=cd['WOE']
        cd['WOEs']=mid['mid_score']
        cd.index=cd['in']

        scor.append(cd)
        dat1=data.copy()
    
    score_=pd.concat(scor)
    score_['constant']=constant
    del score_['in']
    return score_

    

    
def score_pr(m,messa,out_in_list):
    m=m.copy()
    col=list(messa['var'].unique())
    m['score']=int(0)
#    k=col[2]    
    for k in col:

        cd=messa[messa['var']==k].copy()
        cd['1']=range(len(cd))
        cd['WOE']=cd['WOEs']
        cd['WOE']=cd['WOE']+cd['1']/100000

        dc=dict()
#        l=1
        for l in range(len(cd)):                
            dc[list(cd['WOE'])[l]]=cd['Bin'][l].replace(')','').replace('(','').replace(']','').split(',')
            if len(dc[list(cd['WOE'])[l]])==1:
                dc[list(cd['WOE'])[l]]=dc[list(cd['WOE'])[l]][0]
        for woe in dc:
            if len(dc[woe])!=2:
                match_case = re.compile("\(|\)|\[|\]")
                end_points = match_case.sub('', dc[woe]).split(', ')
                dc[woe] = end_points
            
        for l in dc:
            if len(dc[l])==1:
                out_in_list.append(dc[l][0])

        m[k+'_s']= list(map(lambda x: var_woe(x, dc, out_in_list), m[k].map(lambda x: float(x))))
        m[k+'_s']= m[k+'_s'].apply(int)
        m['score']=m[k+'_s'].apply(int)+m['score'].apply(int)
    
    m['score']=m['score']+int(messa['constant'].mean())
    m['constant']=int(messa['constant'].mean())
    return m    
