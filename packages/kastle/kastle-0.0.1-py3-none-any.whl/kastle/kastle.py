from unicodedata import name
import featuretools as ft
import  pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import *
from sklearn import *
from sklearn.linear_model import LinearRegression as LR 
import warnings
warnings.filterwarnings("ignore")

lr_model = LR()
# Kuaishou Automated Sql Table Lighting Engineering
class KASTLE:
    # es = None
    target_column_name = ''
    df = None
    agg_primitives=['sum', 'median','mean']
    lr_model = LR()
    model_lgb = None
    feature_matrix, feature_names = (None, None)
    feature_list = None
    target = None

    def __init__(self,csv_file_path=None, target_column_name='') -> None:#load_from_csv
        if(isinstance (csv_file_path, str)):
            df = pd.read_csv(csv_file_path)
        else:
            df = csv_file_path
    # sample if to big
        target = df[[target_column_name]].copy()
        features = df.drop(columns = target_column_name)
    # current numeric only
        features = features.select_dtypes([np.number]).copy()
    # U
        es = ft.EntitySet(id = target_column_name)
    # index need to be smarter
        es.add_dataframe(dataframe_name = target_column_name, dataframe = features, index = 'Unnamed: 0')
        trans_primitives=['add_numeric', 'subtract_numeric', 'multiply_numeric', 'divide_numeric']
        agg_primitives=['sum', 'median','mean']
    
        feature_matrix, feature_names = ft.dfs(entityset=es, 
                                            target_dataframe_name = target_column_name, 
                                            max_depth = 1, 
                                            verbose = 1,
                                            agg_primitives=agg_primitives,
                                            trans_primitives=trans_primitives,
                                            n_jobs = 8)

    # current numeric only
        categorical_features = np.where(feature_matrix.dtypes == 'object')[0]
        for i in categorical_features:
            feature_matrix.iloc[:,i] = 0#feature_matrix.iloc[:,i].astype('str')


        model_lgb = lgb.LGBMRegressor(iterations=5000, learning_rate=0.05, depth=6, eval_metric='RMSE', random_seed=7)
        # 训练模型
        model_lgb.fit(feature_matrix, target)#, early_stopping_rounds=1000)
        model_lgb.booster_.feature_name()#.plot_importance()
        lgb.plot_importance(model_lgb,max_num_features=6)

        feature_list = pd.DataFrame({'Value':model_lgb.feature_importances_,'Feature':feature_matrix.columns.to_list()}).sort_values(by="Value",ascending=False).Feature.to_list()[:14]
        pd.DataFrame({'Importance':model_lgb.feature_importances_,'Feature':feature_matrix.columns.to_list()}).sort_values(by="Importance",ascending=False).to_csv(f"feature_importance_for_{target_column_name}.csv",index =False)
        print("Feature list:\n" + str(feature_list))
        print("succeed !")
        self.df = df
        self.target_column_name = target_column_name
        self.lr_model = lr_model
        self.model_lgb = model_lgb
        self.feature_matrix, self.feature_names = (feature_matrix, feature_names)
        self.feature_list = feature_list
        self.target = target

    def kamled_df(self):
    
    #   same column not considered
        return pd.concat([self.df,self.feature_matrix[self.feature_list[:min(6,len(self.feature_list))]]],axis=1)

    def important_features(self):

    #   need to be reindexed
        return pd.read_csv(f"feature_importance_for_{self.target_column_name}.csv")
        # return pd.DataFrame({'Importance':self.model_lgb.feature_importances_,'Feature':self.feature_matrix.columns.to_list()}).sort_values(by="Importance",ascending=False)

    def excel_formula(self):
        self.lr_model.fit(self.feature_matrix[self.feature_list[:6]], self.target)
        print(f"\nExcel_formula:\nALPHA30 = {self.lr_model.intercept_[0]} + " + "\n + ".join ([f"[{self.feature_list[i].upper()}]* {self.lr_model.coef_[0][i]} " for i in range(len(self.lr_model.coef_[0]))]))


if __name__ == '__main__':
    kaml = KASTLE('/Users/will/Downloads/alpha30_base.csv','alpha30_last7d_avg')
    kaml.excel_formula()
    kaml.kamled_df()
    kaml.important_features()

    # df = pd.read_csv('/Users/will/Downloads/df.csv')
    # kaml = KAML(df,'alpha30')
    # kaml.excel_formula()

