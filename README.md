# Graduation_Project

## English Explanation

This code demonstrates an example of a physical analysis used in a graduation project, by reading data from a CERN ROOT file. The processed data includes properties of muons and jets. The main objective of the project is to calculate the total energy and environmental mass of jets around muons in the data set.

The code first opens the ROOT file using the uproot library and reads the data using the required branch names. Then, it defines functions to calculate the four-momentum of muons and jets, as well as the environmental mass.

The data set consists of properties such as PT, Eta, Phi for muons, and PT, Eta, Phi, Mass for jets. The data set goes through preprocessing steps and is combined with the functions used to calculate the environmental mass.

In the next step, the data set is split into independent variables (muon properties) and the target variable (environmental mass). Then, the data set is divided into training and test sets.

Next, different machine learning models (Random Forest, Linear Regression, SVR) are defined, and permutation importance evaluation is used to calculate the feature importance rankings of these models. The obtained results are printed based on the feature importance rankings.

Finally, various machine learning models (DummyRegressor, KNeighborsRegressor, LinearRegression, etc.) are defined, and these models are evaluated with different performance metrics (mean absolute error, median absolute error, R-squared score, explained variance score). The metric results obtained are collected in a data frame and printed.

### Detailed Explanation

<body>
    <ol>
        <li>Defines a function calculate_muon_momentum that calculates the momentum and energy components of a muon based on its transverse momentum (PT), pseudorapidity (Eta), and azimuthal angle (Phi).</li>
        <li>Defines a function calculate_delta_R that calculates the angular separation (delta R) between two objects given their pseudorapidities and azimuthal angles.</li>
        <li>Defines a function calculate_environment_mass that calculates the environmental mass around a muon by considering the momenta of nearby jets and missing energy. It uses the previously defined functions to calculate the muon momentum and delta R.</li>
        <li>Defines a list of branches to extract from the ROOT file.</li>
        <li>Extracts the data from the ROOT file and converts it into a Pandas DataFrame.</li>
        <li>Calls the calculate_environment_mass function to calculate the environmental mass and adds it as a new column in the DataFrame.</li>
        <li>Splits the DataFrame into input features (X) and the target variable (y).</li>
        <li>Splits the data into training and test sets using train_test_split from scikit-learn.</li>
        <li>Defines a list of models to train, including Random Forest, Linear Regression, and Support Vector Regression.</li>
        <li>Trains each model using the training data and calculates the feature importances using permutation importance.</li>
        <li>Prints the feature importances for each model.</li>
        <li>Defines a list of model names and metric names for evaluation.</li>
        <li>Creates an empty DataFrame to store the evaluation metrics.</li>
        <li>Loops over each model, evaluates it on the test data, and calculates metrics such as mean absolute error, median absolute error, R-squared score, and explained variance score.</li>
        <li>Prints the evaluation metrics for each model.</li>
    </ol>
</body>

## Türkçe Anlatım

Bu kod, CERN ROOT dosyasından veri okuyarak bir bitirme projesinde kullanılan bir fiziksel analiz örneğini göstermektedir. İşlenen veri, muon ve jetlerin özelliklerini içermektedir. Projenin ana hedefi, veri tabanındaki muonun çevresindeki jetlerin toplam enerjisini ve çevresel kütlesini hesaplamaktır.

Kod, öncelikle uproot kütüphanesini kullanarak ROOT dosyasını açar ve gerekli dal adlarını kullanarak verileri okur. Ardından, muon ve jetlerin dört momentumunu hesaplayan ve çevresel kütleyi hesaplayan fonksiyonlar tanımlanır.

Veri seti, muonun özellikleri (PT, Eta, Phi) ve jetlerin özellikleri (PT, Eta, Phi, Kütle) gibi özelliklerden oluşur. Veri seti öncelikle ön işleme adımlarından geçirilir ve çevresel kütleyi hesaplamak için kullanılan fonksiyonlarla birleştirilir.

Sonraki adımda, veri seti bağımsız değişkenler (muon özellikleri) ve hedef değişken (çevresel kütle) olarak ayrılır. Ardından, veri seti eğitim ve test setlerine bölünür.

Daha sonra, farklı makine öğrenimi modelleri (Random Forest, Linear Regression, SVR) tanımlanır ve bu modellerin özellik önem derecelerini hesaplamak için permütasyon önem değerlendirmesi kullanılır. Elde edilen sonuçlar, özellik önem sıralamasına göre yazdırılır.

Son olarak, çeşitli makine öğrenimi modelleri (DummyRegressor, KNeighborsRegressor, LinearRegression, vb.) tanımlanır ve bu modellerin farklı performans metrikleriyle (ortalama mutlak hata, medyan mutlak hata, R-kare skoru, açıklanan varyans skoru) değerlendirilir. Elde edilen metrik sonuçları bir veri çerçevesinde toplanır ve yazdırılır.

### Detaylı Anlatım

<body>
    <ol>
        <li>Bir fonksiyon tanımlayın: calculate_muon_momentum. Bu fonksiyon, bir müonün moment ve enerji bileşenlerini, transvers momentumu (PT), pseudorapidity (Eta) ve azimuthal açısı (Phi) temel alarak hesaplar.</li>
        <li>Bir fonksiyon tanımlayın: calculate_delta_R. Bu fonksiyon, pseudorapidity ve azimuthal açılarına dayanarak, iki nesne arasındaki açısal ayrımı (delta R) hesaplar.</li>
        <li>Bir fonksiyon tanımlayın: calculate_environment_mass. Bu fonksiyon, yakındaki jetlerin momenta ve eksik enerjiyi dikkate alarak, bir müonun çevresel kütlesini hesaplar. Müon momentumunu ve delta R'yi hesaplamak için önceden tanımlanan fonksiyonları kullanır.</li>
        <li>ROOT dosyasından çıkarılacak dalları içeren bir liste tanımlayın.</li>
        <li>ROOT dosyasından verileri çıkarın ve bunları bir Pandas DataFrame'e dönüştürün.</li>
        <li>calculate_environment_mass fonksiyonunu çağırarak çevresel kütleyi hesaplayın ve DataFrame'e yeni bir sütun olarak ekleyin.</li>
        <li>DataFrame'i giriş özellikleri (X) ve hedef değişken (y) olarak ayırın.</li>
        <li>scikit-learn'den train_test_split kullanarak veriyi eğitim ve test setlerine ayırın.</li>
        <li>Random Forest, Linear Regression ve Support Vector Regression gibi eğitilecek modellerin bir listesini tanımlayın.</li>
        <li>Her bir modeli eğiterek, özellik önemini permutasyon önemine göre hesaplayın.</li>
        <li>Her bir model için özellik önemlerini yazdırın.</li>
        <li>Değerlendirme için model adları ve metrik adlarını içeren bir liste tanımlayın.</li>
        <li>Değerlendirme metriklerini saklamak için boş bir DataFrame oluşturun.</li>
        <li>Her bir model için döngü oluşturarak, test verisi üzerinde değerlendirin ve ortalama mutlak hata, medyan mutlak hata, R-kare skoru ve açıklanan varyans skoru gibi metrikleri hesaplayın.</li>
        <li>Her bir model için değerlendirme metriklerini yazdırın.</li>
    </ol>
</body>
