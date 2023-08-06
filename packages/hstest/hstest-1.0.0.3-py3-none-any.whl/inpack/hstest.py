# CTGAN 
import warnings
import warnings
from ctgan import CTGANSynthesizer
from pycaret.classification import *
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import ADASYN

warnings.simplefilter(action='ignore', category=FutureWarning)

with warnings.catch_warnings():
    # ignore all caught warnings
    warnings.filterwarnings("ignore")
    # execute code that will generate warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)


class imbalance:
    
    def __init__(self,train_data, test_data):

    
    #def print_df(train_data, test_data):
        self.train_data = train_data 
        self.test_data = test_data
        
        def imbalance_CTGAN(train_data):
            #print(sum(train_data.Group==0), sum(train_data.Group==1) )
            #print(sum(test_data.Group==0), sum(test_data.Group==1) )

            train_data_0= train_data[train_data.Group==0]
            train_data_1= train_data[train_data.Group==1]

            ### len(train_data_0)-len(train_data_1)개 생성
            random_sample= len(train_data_0)-len(train_data_1)

            data = train_data_1
            ctgan = CTGANSynthesizer(epochs=100)
            ctgan.set_random_state(123)
            ctgan.fit(data,['Group'])
            samples_129_1 = ctgan.sample(random_sample)
            samples_129_1.Group = 1
            train_129 = pd.concat([train_data_1 ,samples_129_1 ], axis = 0 )
            train_data_ctgan =pd.concat([train_data_0 , train_129], axis = 0)
            return train_data_ctgan

        # ADASYN

        def imbalance_ADASYN(train_data):

            ada = ADASYN(random_state=42)
            X, y = train_data.drop("Group", axis = 1), train_data.Group
            X_res, y_res = ada.fit_sample(X, y)
            df_X_res = pd.DataFrame(X_res)
            df_y_res = pd.DataFrame(y_res)
            df_X_res.columns = X.columns
            #df_y_res.columns
            train_data_adasyn = pd.concat([df_X_res, df_y_res.Group] , axis = 1)

            return train_data_adasyn

        # UNDERSAMPLING 

        def imbalance_UNDER(train_data):
            train_data_0= train_data[train_data.Group==0]
            train_data_1= train_data[train_data.Group==1]

            test_data_0= test_data[test_data.Group==0]
            test_data_1= test_data[test_data.Group==1]
            train_data_under = pd.concat([train_data_0.sample(len(train_data_1)),train_data_1], axis = 0).reset_index(drop= True)
            return train_data_under

        #SMOTE

        def imbalance_SMOTE(train_data):

            smote = SMOTE(random_state=0)
            X_train_over,y_train_over = smote.fit_sample(train_data.drop('Group', axis = 1),train_data.Group)
            train_data_smote = pd.concat([X_train_over, y_train_over], axis = 1) 
            return train_data_smote
            # Pycaret 

        # Model Run

        def ttt(model, train, test):

            def pycaret_acc(trd,ted):
                warnings.filterwarnings('ignore')
                clf = setup(data = trd, test_data = ted, target='Group',
                        data_split_shuffle=True, silent=True, normalize= True, fix_imbalance = False, session_id=42) 

                best_1 = compare_models(sort = 'Accuracy', n_select = 1, exclude=['xgboost','dummy','svm','ridge'])


            pycaret_acc(model(train), test)
            target_acc = pull()['Accuracy'][0]
            target_model = pull()['Model'][0]
            return target_acc,target_model
        
        list_im = [imbalance_UNDER, imbalance_SMOTE, imbalance_ADASYN, imbalance_CTGAN]

        tmp = 0
        name = 0 
        i_iter = 0
        list_ls= []
        for i in iter(list_im):
            acc, model = ttt(i,train_data, test_data)
            idr = str(i.__name__)
            if tmp > acc:
                tmp = tmp
                name = model

                #model = i.target_model
            else : 
                tmp = acc
                name = model
                i_iter = str(i)
            list_ls.append([acc, model, idr])

        print(tmp, name, i_iter)  #1
        df_ls = pd.DataFrame(list_ls)
        print(df_ls)
        number = df_ls.index[  df_ls[0] == max(df_ls[0]) ]
        print(df_ls.iloc[number]) #2