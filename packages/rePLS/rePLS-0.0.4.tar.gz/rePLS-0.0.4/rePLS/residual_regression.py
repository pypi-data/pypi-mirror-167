import numpy as np
import copy 
from sklearn.base import BaseEstimator, ClassifierMixin, RegressorMixin
from sklearn.linear_model import LinearRegression
from sklearn.cross_decomposition import PLSRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline,make_pipeline
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score

class rePLS(BaseEstimator, RegressorMixin):

    def __init__(self,Z,n_components):
        self.Z = Z
        self.n_components= n_components
        #initial model for calculating residual 
        self.reg_Zy = LinearRegression()
        self.reg_ZX = LinearRegression()
        
        #residual regression
        self.residual_model = PLSRegression(n_components=n_components)


            
    def fit(self, X, y=None):
        #fit LR
        self.reg_Zy.fit(self.Z, y)
        self.reg_ZX.fit(self.Z, X)        
        
        #Calculate residuals        
#         y_residuals = y - self.reg_Zy.predict(self.Z)
#         X_residuals = X - self.reg_ZX.predict(self.Z)
        
        self.beta_Zy = self.reg_Zy.coef_.T
        beta_ZX = self.reg_ZX.coef_.T
        y_residuals = y - self.Z@self.beta_Zy
        X_residuals = X - self.Z@beta_ZX
        
        #Regession model for residual 
        
        self.residual_model.fit(X_residuals, y_residuals)
        

        self.P = self.residual_model.x_loadings_ 
        self.Q = self.residual_model.y_loadings_
        
        #coefficients are not affected by confounders
        self.PQ = self.residual_model.coef_

        
    
    def predict(self, X, y=None,Z=None):        
        if Z is None:
            Z = self.Z
        self.reg_ZX.fit(Z, X)     
        X_residuals = X - Z@self.reg_ZX.coef_.T
        preds = self.residual_model.predict(X_residuals) + Z@self.beta_Zy 
        
        return np.array(preds) 

class rePCR(BaseEstimator, RegressorMixin):

    def __init__(self,Z,n_components):
        self.Z = Z
        self.n_components = n_components
        #initial model for calculating residual 
        self.reg_Zy = LinearRegression()
        self.reg_ZX = LinearRegression()
        
        #residual regression
        self.residual_model = make_pipeline(PCA(n_components=n_components), LinearRegression())


            
    def fit(self, X, y=None):
        #fit LR
        self.reg_Zy.fit(self.Z, y)
        self.reg_ZX.fit(self.Z, X)        
        
        #Calculate residuals        
#         y_residuals = y - self.reg_Zy.predict(self.Z)
#         X_residuals = X - self.reg_ZX.predict(self.Z)
        
        self.beta_Zy = self.reg_Zy.coef_.T
        beta_ZX = self.reg_ZX.coef_.T
        y_residuals = y - self.Z@self.beta_Zy
        X_residuals = X - self.Z@beta_ZX
        
        #Regession model for residual         
        self.residual_model.fit(X_residuals, y_residuals)
        


    
    def predict(self, X, y=None,Z=None):        
        if Z is None:
            Z = self.Z
        self.reg_ZX.fit(Z, X)     
        X_residuals = X - Z@self.reg_ZX.coef_.T
        preds = self.residual_model.predict(X_residuals) + Z@self.beta_Zy 
        
        return np.array(preds) 
class reMLR(BaseEstimator, RegressorMixin):

    def __init__(self,Z):
        self.Z = Z
        
        #initial model for calculating residual 
        self.reg_Zy = LinearRegression()
        self.reg_ZX = LinearRegression()
        
        #residual regression
        self.residual_model = LinearRegression()


            
    def fit(self, X, y=None):
        #fit LR
        self.reg_Zy.fit(self.Z, y)
        self.reg_ZX.fit(self.Z, X)        
        
        #Calculate residuals        
#         y_residuals = y - self.reg_Zy.predict(self.Z)
#         X_residuals = X - self.reg_ZX.predict(self.Z)
        
        self.beta_Zy = self.reg_Zy.coef_.T
        beta_ZX = self.reg_ZX.coef_.T
        y_residuals = y - self.Z@self.beta_Zy
        X_residuals = X - self.Z@beta_ZX
        
        #Regession model for residual         
        self.residual_model.fit(X_residuals, y_residuals)
        


    
    def predict(self, X, y=None,Z=None):        
        if Z is None:
            Z = self.Z
        self.reg_ZX.fit(Z, X)     
        X_residuals = X - Z@self.reg_ZX.coef_.T
        preds = self.residual_model.predict(X_residuals) + Z@self.beta_Zy 
        
        return np.array(preds) 
    