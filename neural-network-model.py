import csv
import collections
import copy

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
import sklearn.metrics as metrics

from tensorflow import keras
from tensorflow.keras.models import Model, Sequential, load_model, save_model
from tensorflow.keras.layers import Activation, Dense, Input, Dropout, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy, Precision, Recall, F1Score

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, precision_recall_fscore_support, ConfusionMatrixDisplay
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold, RandomizedSearchCV
from scikeras.wrappers import KerasClassifier
from scipy.stats import uniform, randint

# leitura dos registros de treinamento
csv_path_training_gases = "C:/Users/melis/OneDrive/IC/IC-ML-Codes-2/.venv/terceira-tentativa/separated_data/train_samples.csv"
with open(csv_path_training_gases, mode = 'r') as file:
    csv_reader_training_gases = csv.reader(file)
    next(csv_reader_training_gases)

    train_samples = []
    for row in csv_reader_training_gases:
        train_samples.append(row)
        
csv_path_training_faults = "C:/Users/melis/OneDrive/IC/IC-ML-Codes-2/.venv/terceira-tentativa/separated_data/train_labels.csv"
with open(csv_path_training_faults, mode = 'r') as file:
    csv_reader_training_faults = csv.reader(file)
    next(csv_reader_training_faults)

    train_labels = []
    for row in csv_reader_training_faults:
        train_labels.append(row)

# normalização dos gases
train_samples = np.array(train_samples)
train_labels = np.array(train_labels)
scaler = MinMaxScaler(feature_range=(0,1))
scaled_train_samples = scaler.fit_transform(train_samples)
scaled_train_samples = np.array(scaled_train_samples)

# normalização das falhas
train_labels = train_labels.flatten()
int_scaled_train_labels = (train_labels.astype(float)-1).astype(int)
int_scaled_train_labels = np.array(int_scaled_train_labels)

# estrutura da rede neural
def create_functional_model():
    inputs = Input(shape=(5,))
    x = Dense(128, activation='relu')(inputs)
    x = Dropout(0.2)(x)
    x = Dense(64, activation='relu')(x)
    x = Dropout(0.2)(x)
    x = Dense(64, activation='sigmoid')(x)
    x = Dropout(0.2)(x)
    outputs = Dense(7, activation='softmax')(x)
    
    model = Model(inputs=inputs, outputs=outputs)
    model.compile(optimizer=Adam(learning_rate=0.001),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

functional_model = create_functional_model()
history = functional_model.fit(scaled_train_samples, int_scaled_train_labels, epochs=3000, batch_size=25, verbose=2)

# plotagem das métricas de treinamento
def plot_training_history(history):
    acc = history.history['accuracy']
    loss = history.history['loss']
    epochs = range(1, len(acc) + 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    fig.suptitle('Métricas de Treinamento')

    ax1.plot(epochs, acc, 'bo-', label='Acurácia de Treinamento')
    ax1.set_title('Acurácia de Treinamento')
    ax1.set_xlabel('Épocas')
    ax1.set_ylabel('Acurácia')
    ax1.legend()

    ax2.plot(epochs, loss, 'ro-', label='Perda de Treinamento')
    ax2.set_title('Perda de Treinamento')
    ax2.set_xlabel('Épocas')
    ax2.set_ylabel('Perda')
    ax2.legend()

    if 'val_accuracy' in history.history:
        val_acc = history.history['val_accuracy']
        val_loss = history.history['val_loss']
        ax1.plot(epochs, val_acc, 'g-', label='Acurácia de Validação')
        ax2.plot(epochs, val_loss, 'm-', label='Perda de Validação')
        ax1.legend()
        ax2.legend()

    plt.tight_layout()
    plt.show()

plot_training_history(history)

# preparando a cross validation
# imprimindo os índices utilizados
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
splits = []
for train_index, test_index in skf.split(scaled_train_samples, int_scaled_train_labels):
    splits.append((train_index, test_index))
for i, (train_index, test_index) in enumerate(splits):
    print(f"Split {i+1} - Índices de Treino: {train_index}, Índices de Teste: {test_index}")

# treinando o modelo com cross validation
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
split_num = 1
for train_index, test_index in skf.split(scaled_train_samples, int_scaled_train_labels):
    X_train, X_test = scaled_train_samples[train_index], scaled_train_samples[test_index]
    y_train, y_test = int_scaled_train_labels[train_index], int_scaled_train_labels[test_index]
    
    model = create_functional_model()
    history = model.fit(X_train, y_train, epochs=500, batch_size=25, verbose=2)
    model_filename = f'model_split_{split_num}.h5'
    model.save(model_filename)
    
    print(f"Modelo do split {split_num} salvo como {model_filename}")
    split_num += 1

# leitura dos registros de teste
csv_path_testing_gases = "C:/Users/melis/OneDrive/IC/IC-ML-Codes-2/.venv/terceira-tentativa/separated_data/test_samples.csv"
with open(csv_path_testing_gases, mode = 'r') as file:
    csv_reader_testing_gases = csv.reader(file)
    next(csv_reader_testing_gases)

    test_samples = []
    for row in csv_reader_testing_gases:
        test_samples.append(row)

csv_path_testing_faults = "C:/Users/melis/OneDrive/IC/IC-ML-Codes-2/.venv/terceira-tentativa/separated_data/test_labels.csv"
with open(csv_path_testing_faults, mode = 'r') as file:
    csv_reader_testing_faults = csv.reader(file)
    next(csv_reader_testing_faults)

    test_labels = []
    for row in csv_reader_testing_faults:
        test_labels.append(row)

# normalizaão dos gases de teste
test_samples = np.array(test_samples)
test_labels = np.array(test_labels)
scaler = MinMaxScaler(feature_range=(0,1))
scaled_test_samples = scaler.fit_transform(test_samples)
scaled_test_samples = np.array(scaled_test_samples)

# normalização das falhas de teste
test_labels = test_labels.flatten()
int_scaled_test_labels = (test_labels.astype(float)-1).astype(int)
int_scaled_test_labels = np.array(int_scaled_test_labels)

# realizando predições
model_filename = 'model_split_1.h5'
loaded_model = load_model(model_filename)

y_pred = loaded_model.predict(scaled_test_samples)
y_pred_classes = np.argmax(y_pred, axis=1)

# avaliando o modelo
test_loss, test_accuracy = loaded_model.evaluate(scaled_test_samples, int_scaled_test_labels, verbose=0)
print(f"Acurácia no conjunto de teste: {test_accuracy:.4f}")
print(f"Perda no conjunto de teste: {test_loss:.4f}")
print("\nRelatório de Classificação:")
print(classification_report(int_scaled_test_labels, y_pred_classes))

# matriz de confusão
cm = confusion_matrix(int_scaled_test_labels, y_pred_classes)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Matriz de Confusão')
plt.ylabel('Rótulo Verdadeiro')
plt.xlabel('Rótulo Previsto')
plt.show()

# salvando os resultados em um arquivo
with open('test_results.txt', 'w') as f:
    f.write(f"Acurácia no conjunto de teste: {test_accuracy:.4f}\n")
    f.write(f"Perda no conjunto de teste: {test_loss:.4f}\n")
    f.write("\nRelatório de Classificação:\n")
    f.write(classification_report(int_scaled_test_labels, y_pred_classes))
