# Graduation_Project

## Türkçe

Bu kod, CERN ROOT dosyasından veri okuyarak bir bitirme projesinde kullanılan bir fiziksel analiz örneğini göstermektedir. İşlenen veri, muon ve jetlerin özelliklerini içermektedir. Projenin ana hedefi, veri tabanındaki muonun çevresindeki jetlerin toplam enerjisini ve çevresel kütlesini hesaplamaktır.

Kod, öncelikle uproot kütüphanesini kullanarak ROOT dosyasını açar ve gerekli dal adlarını kullanarak verileri okur. Ardından, muon ve jetlerin dört momentumunu hesaplayan ve çevresel kütleyi hesaplayan fonksiyonlar tanımlanır.

Veri seti, muonun özellikleri (PT, Eta, Phi) ve jetlerin özellikleri (PT, Eta, Phi, Kütle) gibi özelliklerden oluşur. Veri seti öncelikle ön işleme adımlarından geçirilir ve çevresel kütleyi hesaplamak için kullanılan fonksiyonlarla birleştirilir.

Sonraki adımda, veri seti bağımsız değişkenler (muon özellikleri) ve hedef değişken (çevresel kütle) olarak ayrılır. Ardından, veri seti eğitim ve test setlerine bölünür.

Daha sonra, farklı makine öğrenimi modelleri (Random Forest, Linear Regression, SVR) tanımlanır ve bu modellerin özellik önem derecelerini hesaplamak için permütasyon önem değerlendirmesi kullanılır. Elde edilen sonuçlar, özellik önem sıralamasına göre yazdırılır.

Son olarak, çeşitli makine öğrenimi modelleri (DummyRegressor, KNeighborsRegressor, LinearRegression, vb.) tanımlanır ve bu modellerin farklı performans metrikleriyle (ortalama mutlak hata, medyan mutlak hata, R-kare skoru, açıklanan varyans skoru) değerlendirilir. Elde edilen metrik sonuçları bir veri çerçevesinde toplanır ve yazdırılır.

## English

This code demonstrates an example of a physical analysis used in a graduation project, by reading data from a CERN ROOT file. The processed data includes properties of muons and jets. The main objective of the project is to calculate the total energy and environmental mass of jets around muons in the data set.

The code first opens the ROOT file using the uproot library and reads the data using the required branch names. Then, it defines functions to calculate the four-momentum of muons and jets, as well as the environmental mass.

The data set consists of properties such as PT, Eta, Phi for muons, and PT, Eta, Phi, Mass for jets. The data set goes through preprocessing steps and is combined with the functions used to calculate the environmental mass.

In the next step, the data set is split into independent variables (muon properties) and the target variable (environmental mass). Then, the data set is divided into training and test sets.

Next, different machine learning models (Random Forest, Linear Regression, SVR) are defined, and permutation importance evaluation is used to calculate the feature importance rankings of these models. The obtained results are printed based on the feature importance rankings.

Finally, various machine learning models (DummyRegressor, KNeighborsRegressor, LinearRegression, etc.) are defined, and these models are evaluated with different performance metrics (mean absolute error, median absolute error, R-squared score, explained variance score). The metric results obtained are collected in a data frame and printed.




