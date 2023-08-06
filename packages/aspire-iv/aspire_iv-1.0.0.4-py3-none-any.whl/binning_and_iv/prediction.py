import pandas as pd
import numpy as np
class iv_pred():
    #using Decision tree doing binning
    def binning(df_binning, df_bins, columns, max_depth_,min_samples_split_, min_samples_leaf_,max_leaf_nodes_):
        from sklearn.tree import DecisionTreeClassifier
        feature = []
        feature_bin = []
        for i in range(0,len(columns)):
            column = columns[i] 
            model = DecisionTreeClassifier(max_depth=max_depth_,min_samples_split=min_samples_split_, min_samples_leaf=min_samples_leaf_, max_leaf_nodes =max_leaf_nodes_)
            model.fit(df_binning[column].to_frame(), df_binning.target)
            #print(model.predict_proba(df_binning[columns[i]].to_frame()))
            # taking probability of bad rate as value
            df_binning[column]=model.predict_proba(df_binning[columns[i]].to_frame())[:,1]
            df_bins[column+'_bin'] = df_binning[column]
            feature.append(column)
            feature_bin.append(column+'_bin')
        return df_binning, df_bins, feature, feature_bin


    #bucket distribution
    def num_bucket(df_bins, feature, feature_bin):
        lst = []
        for i in range(len(feature)):
            sorted_data = df_bins.sort_values([feature[i]], ascending = True)
            for j in range(sorted_data[feature_bin[i]].nunique()):
                value = list(sorted_data[feature_bin[i]].unique())[j]
                data = sorted_data[(sorted_data[feature_bin[i]]==value)]
                lst.append({
                    'feature': feature_bin[i],
                    'bin_val' : value,
                    'val':(f'{data[feature[i]].min()} - {data[feature[i]].max()}'),
                    'good':data[data['target']==0].count()[feature[i]],
                    'bad':data[data['target']==1].count()[feature[i]],
                    'bad_rate' : round(((data[data['target']==1].count()[feature[i]])/(data['target'].count()))*100,2)
                })
        d = pd.DataFrame(lst)
        return d

    def cat_bucket(df, feature):
        lst = []
        for i in range(len(feature)):
            for j in range(df[feature[i]].nunique()):
                value = list(df[feature[i]].unique())[j]
                data = df[(df[feature[i]]==value)]
                lst.append({
                    'feature': feature[i],
                    'bin_val' : value,
                    'good':data[data['target']==0].count()[feature[i]],
                    'bad':data[data['target']==1].count()[feature[i]],
                    'bad_rate' : round(((data[data['target']==1].count()[feature[i]])/(data['target'].count()))*100,2)
                })
        d = pd.DataFrame(lst)
        return d

    def calculate_woe_iv(dataset, feature, target):
        lst = []
        for i in range(dataset[feature].nunique()):
            val = list(dataset[feature].unique())[i]
            lst.append({
                'Value': val,
                'All': dataset[dataset[feature] == val].count()[feature],
                'Good': dataset[(dataset[feature] == val) & (dataset[target] == 0)].count()[feature],
                'Bad': dataset[(dataset[feature] == val) & (dataset[target] == 1)].count()[feature]
            })
        dset = pd.DataFrame(lst)
        dset['Distr_Good'] = dset['Good'] / dset['Good'].sum()

        dset['Distr_Bad'] = dset['Bad'] / dset['Bad'].sum()
        dset['WoE'] = np.log(dset['Distr_Good'] / dset['Distr_Bad'])
        dset = dset.replace({'WoE': {np.inf: 0, -np.inf: 0}})
        dset['IV'] = (dset['Distr_Good'] - dset['Distr_Bad']) * dset['WoE']
        iv = dset['IV'].sum()
        
        dset = dset.sort_values(by='WoE')
        
        #return dset if needed
        return iv


    def calculate_woe_iv(dataset, feature, target):
        lst = []
        for i in range(dataset[feature].nunique()):
            val = list(dataset[feature].unique())[i]
            lst.append({
                'Value': val,
                'All': dataset[dataset[feature] == val].count()[feature],
                'Good': dataset[(dataset[feature] == val) & (dataset[target] == 0)].count()[feature],
                'Bad': dataset[(dataset[feature] == val) & (dataset[target] == 1)].count()[feature]
            })
        dset = pd.DataFrame(lst)
        dset['Distr_Good'] = dset['Good'] / dset['Good'].sum()

        dset['Distr_Bad'] = dset['Bad'] / dset['Bad'].sum()
        dset['WoE'] = np.log(dset['Distr_Good'] / dset['Distr_Bad'])
        dset = dset.replace({'WoE': {np.inf: 0, -np.inf: 0}})
        dset['IV'] = (dset['Distr_Good'] - dset['Distr_Bad']) * dset['WoE']
        iv = dset['IV'].sum()
        
        dset = dset.sort_values(by='WoE')
        
        #return dset if needed
        return iv


    # columns = numerical_var
    def DT_binning(dataframe, max_depth_=3,min_samples_split_=40, min_samples_leaf_=30,max_leaf_nodes_ = 6, num_feature= [],cat_feature=[]):
        """
        Input :
        dataframe -> Feature dataframe.
        num_feature = [] -> set to empty, select if you have numerical features :- List[features].
        cat_feature = [] -> set to empty, select if you have categorical features :- List[features].

        Output :
        dataframe with ['var_name','Information_Value']

        __return__:
                    tuple(cal_bad_num,cal_bad_cat,iv_score)

        """
        df = dataframe.copy()
        df_bins = dataframe.copy()
        df_binning = dataframe.copy()
        if num_feature != []:
            df_binning, df_bins, feature, feature_bin = iv_pred.binning(df_binning,df_bins, num_feature, max_depth_,min_samples_split_, min_samples_leaf_,max_leaf_nodes_)
            cal_bad_num = iv_pred.num_bucket(df_bins, feature, feature_bin)
            cal_bad_num = cal_bad_num.set_index(['feature','bin_val'])
        else:
            cal_bad_num = np.nan
        if cat_feature != []:
            cal_bad_cat = iv.cat_bucket(df, cat_feature)
        else:
            cal_bad_cat = np.nan
        
        var = []
        iv=[]
        for i in range (1,len(df_binning.columns)):
            k=iv_pred.calculate_woe_iv(df_binning,df_binning.iloc[:,i].name,'target')
            var.append(df_binning.iloc[:,i].name)
            iv.append(k)
        
        dx=pd.DataFrame()
        dx['var_name'] = var
        dx['Information_Value']=iv
        iv_score = dx.sort_values(['Information_Value'], ascending = False)

        return cal_bad_num,cal_bad_cat,iv_score



