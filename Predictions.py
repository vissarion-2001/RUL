from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.neural_network import MLPRegressor 

class SVM_Regresson:
    def __init__(self, gamma, kernel: str = None, degree: int = 3, C_p: float = None, epsilon: float = None):
        
        if kernel not in ("linear", "poly", "rbf", "sigmoid", "precomputed"):
                raise Exception("The provided kernel does not exist") 
        self.kernel = kernel
        
        if type(degree) != int or degree<0: 
            raise Exception("The degree provided is not a positive integer")
        self.degree = degree 
        
        if gamma not in ("scale","auto"):
            raise Exception("Not expected gamma values")
        self.gamma = gamma

        if type(C_p != float) or C_p<0:
            raise Exception("The C provided is not a positive float")
        self.C_p = C_p

        if type(epsilon) != float or epsilon<0:
            raise Exception("The epsilon provided is not a positive float")     
        self.epsilon = epsilon

        self.model = SVR(kernel=self.kernel, degree = self.degree, gamma = self.gamma, C = self.C_p, epsilon = self.epsilon)

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test):
        return self.model.predict(X_test)
    

class GBR:
    def __init__(self, n_estimators: int = 100, learning_rate: float = 0.1, max_depth: int = 3):
        if type(n_estimators) != int or n_estimators<0:
            raise Exception("The n_estimators provided is not a positive integer")
        self.n_estimators = n_estimators

        if type(learning_rate) != float or learning_rate<0:
            raise Exception("The learning_rate provided is not a positive float")
        self.learning_rate = learning_rate

        if type(max_depth) != int or max_depth<0:
            raise Exception("The max_depth provided is not a positive integer")
        self.max_depth = max_depth

        self.model = GradientBoostingRegressor(n_estimators=self.n_estimators, learning_rate=self.learning_rate, max_depth=self.max_depth)

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test):
        return self.model.predict(X_test)

class RFR:
    def __init__(self, n_estimators: int = 100, max_depth: int = None):
        if type(n_estimators) != int or n_estimators<0:
            raise Exception("The n_estimators provided is not a positive integer")
        self.n_estimators = n_estimators

        if max_depth is not None and (type(max_depth) != int or max_depth<0):
            raise Exception("The max_depth provided is not a positive integer or None")
        self.max_depth = max_depth

        self.model = RandomForestRegressor(n_estimators=self.n_estimators, max_depth=self.max_depth)

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test):
        return self.model.predict(X_test)

class LR:
    def __init__(self):
        self.model = LinearRegression()

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test):
        return self.model.predict(X_test)

class RidgeR:
    def __init__(self, alpha: float = 1.0):
        if type(alpha) != float or alpha<0:
            raise Exception("The alpha provided is not a positive float")
        self.alpha = alpha

        self.model = Ridge(alpha=self.alpha)

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test):
        return self.model.predict(X_test)

class LassoR:
    def __init__(self, alpha: float = 1.0):
        if type(alpha) != float or alpha<0:
            raise Exception("The alpha provided is not a positive float")
        self.alpha = alpha

        self.model = Lasso(alpha=self.alpha)

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test):
        return self.model.predict(X_test)

class ElasticNetR:
    def __init__(self, alpha: float = 1.0, l1_ratio: float = 0.5):
        if type(alpha) != float or alpha<0:
            raise Exception("The alpha provided is not a positive float")
        self.alpha = alpha

        if type(l1_ratio) != float or l1_ratio<0 or l1_ratio>1:
            raise Exception("The l1_ratio provided is not a float between 0 and 1")
        self.l1_ratio = l1_ratio

        self.model = ElasticNet(alpha=self.alpha, l1_ratio=self.l1_ratio)

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test):
        return self.model.predict(X_test)   

class MLP:
    def __init__(self, hidden_layer_sizes: tuple = (100,), activation: str = 'relu', solver: str = 'adam'):
        if type(hidden_layer_sizes) != tuple or not all(isinstance(x, int) and x>0 for x in hidden_layer_sizes):
            raise Exception("The hidden_layer_sizes provided is not a tuple of positive integers")
        self.hidden_layer_sizes = hidden_layer_sizes

        if activation not in ('identity', 'logistic', 'tanh', 'relu'):
            raise Exception("The provided activation function does not exist")
        self.activation = activation

        if solver not in ('lbfgs', 'sgd', 'adam'):
            raise Exception("The provided solver does not exist")
        self.solver = solver

        self.model = MLPRegressor(hidden_layer_sizes=self.hidden_layer_sizes, activation=self.activation, solver=self.solver)

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test):
        return self.model.predict(X_test)





