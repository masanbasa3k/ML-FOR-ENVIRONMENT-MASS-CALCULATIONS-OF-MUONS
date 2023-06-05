import uproot
import pandas as pd
import math
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import mean_absolute_error, median_absolute_error, r2_score, explained_variance_score


root_dosyasi = 'FCCeh_Kut01_Kct01.root'

file = uproot.open(root_dosyasi)
tree = file['Delphes;1']


def calculate_muon_momentum(dataframe):
    # PT, Eta ve Phi değerlerini alın
    muon_PT = dataframe['Muon/Muon.PT']
    muon_Eta = dataframe['Muon/Muon.Eta']
    muon_Phi = dataframe['Muon/Muon.Phi']
    
    # Enerji bileşenlerini hesaplayın
    px = muon_PT * dataframe.apply(lambda row: math.cos(row['Muon/Muon.Phi']), axis=1)
    py = muon_PT * dataframe.apply(lambda row: math.sin(row['Muon/Muon.Phi']), axis=1)
    theta = dataframe.apply(lambda row: 2 * math.atan(math.exp(-row['Muon/Muon.Eta'])), axis=1)
    pz = muon_PT * dataframe.apply(lambda row: math.sinh(row['Muon/Muon.Eta']), axis=1)
    mass = 0.10566  # Muon kütlesi (GeV)
    E = (px**2 + py**2 + pz**2 + mass**2) ** 0.5
    
    # Enerjiyi DataFrame'e ekleyin
    dataframe['Muon/Muon.Energy'] = E
    
    return dataframe

def calculate_delta_R(eta1, phi1, eta2, phi2):
    d_eta = eta1 - eta2
    d_phi = phi1 - phi2
    
    # Phi farkını -pi ile pi aralığına sınırlayın
    d_phi = (d_phi + np.pi) % (2 * np.pi) - np.pi
    
    delta_R = np.sqrt(d_eta**2 + d_phi**2)
    
    return delta_R


def calculate_environment_mass(dataframe):
    # Muonun dört momentumunu hesaplayın
    muon_momentum = calculate_muon_momentum(dataframe)
    muon_PT = muon_momentum['Muon/Muon.PT']
    muon_Eta = muon_momentum['Muon/Muon.Eta']
    muon_Phi = muon_momentum['Muon/Muon.Phi']
    muon_Energy = muon_momentum['Muon/Muon.Energy']
    
    # Jetlerin PT, Eta ve Phi değerlerini alın
    jet_PT = dataframe['Jet/Jet.PT']
    jet_Eta = dataframe['Jet/Jet.Eta']
    jet_Phi = dataframe['Jet/Jet.Phi']
    
    # Muonun yakınındaki jetleri bulun
    delta_R = calculate_delta_R(jet_Eta, jet_Phi, muon_Eta, muon_Phi)
    jets_near_muon = dataframe[delta_R < 0.4]
    
    # Jetlerin toplam dört momentumunu hesaplayın
    jet_px = jets_near_muon.apply(lambda row: row['Jet/Jet.PT'] * np.cos(row['Jet/Jet.Phi']), axis=1)
    jet_py = jets_near_muon.apply(lambda row: row['Jet/Jet.PT'] * np.sin(row['Jet/Jet.Phi']), axis=1)
    jet_pz = jets_near_muon.apply(lambda row: row['Jet/Jet.PT'] * np.sinh(row['Jet/Jet.Eta']), axis=1)
    jet_energy = jets_near_muon.apply(lambda row: (row['Jet/Jet.PT']**2 + row['Jet/Jet.Mass']**2)**0.5 * np.cosh(row['Jet/Jet.Eta']), axis=1)
    jet_total_px = jet_px.sum()
    jet_total_py = jet_py.sum()
    jet_total_pz = jet_pz.sum()
    jet_total_energy = jet_energy.sum()
    
    # Muonun çevresindeki eksik enerjiyi hesaplayın
    missing_ET = dataframe['MissingET/MissingET.MET']
    missing_ET_phi = dataframe['MissingET/MissingET.Phi']
    missing_ET_px = missing_ET.to_numpy() * np.cos(missing_ET_phi.to_numpy())
    missing_ET_py = missing_ET.to_numpy() * np.sin(missing_ET_phi.to_numpy())
    
    # Çevresel kütleyi hesaplayın
    env_px = jet_total_px + missing_ET_px
    env_py = jet_total_py + missing_ET_py
    env_pz = jet_total_pz
    env_energy = jet_total_energy + missing_ET
    
    env_mass_squared = env_energy**2 - env_px**2 - env_py**2 - env_pz**2
    env_mass = np.sqrt(np.maximum(env_mass_squared, 0))
    
    env_mass -= muon_Energy
    
    return env_mass

branches = ['Muon/Muon.PT', 
         'Muon/Muon.Eta', 
         'Muon/Muon.Phi',
         'Jet/Jet.PT', 
         'Jet/Jet.Eta', 
         'Jet/Jet.Phi',
         'Jet/Jet.Mass',
         'MissingET/MissingET.MET',
         'MissingET/MissingET.Phi',]

branchDatas=[]
for i in branches:
    temp = tree.get(i).array().tolist()
    temp_list = []
    for index in range(len(temp)):
        if len(temp[index]) != 0 :
            temp_list.append(temp[index][0])
        else:
            temp_list.append(0)
    branchDatas.append(temp_list)

tree = {}
for i in range(len(branchDatas)):
  tree[branches[i]] = branchDatas[i]

df = pd.DataFrame(tree)
df = df.fillna(0)
df = df[df['Muon/Muon.PT'] != 0]

environment_mass = calculate_environment_mass(df)
# print(environment_mass)

df['environment_mass'] = environment_mass

# Bağımsız değişkenler (giriş özellikleri) ve hedef değişken (çevresel kütlesi) olarak ayırma
X = df[['Muon/Muon.PT', 'Muon/Muon.Eta', 'Muon/Muon.Phi']]
y = df['environment_mass']

# Veri setini eğitim ve test setleri olarak bölmek
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelleri tanımlama
models = [
    ("Random Forest", RandomForestRegressor()),
    ("Linear Regression", LinearRegression()),
    ("Support Vector Regression", SVR())
]

# Modelleri eğitme ve özellik işaretçelerini hesaplama
for name, model in models:
    model.fit(X_train, y_train)
    result = permutation_importance(model, X_test, y_test, n_repeats=10, random_state=42)
    feature_importance = result.importances_mean
    sorted_indices = np.argsort(feature_importance)[::-1]
    sorted_features = X.columns[sorted_indices]
    sorted_importance = feature_importance[sorted_indices]
    print(f'\n{name} Modeli Özellik İşaretçeleri:')
    for i, feature in enumerate(sorted_features):
        print(f'{feature}: {sorted_importance[i]}')


modelnames = [
    'DummyRegressor()', 
    'KNeighborsRegressor()',
    'LinearRegression()', 
    'SVR()',
    'MLPRegressor(hidden_layer_sizes=(16, 16))',
    'DecisionTreeRegressor()', 
    'GradientBoostingRegressor()',
    'XGBRegressor()',
    'CatBoostRegressor()'
]

metricnames = [
    'mean_absolute_error', 
    'median_absolute_error',
    'r2_score',
    'explained_variance_score',
]

metrics = pd.DataFrame(index=modelnames, columns=metricnames)

for modelname in modelnames:
    model = eval(modelname)
    pred_test = model.fit(X_train, y_train).predict(X_test)
    
    for metricname in metricnames:
        metrics.loc[modelname, metricname] = eval(f'{metricname}(y_test, pred_test)')

print(metrics)