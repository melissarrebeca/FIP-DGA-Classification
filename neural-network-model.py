from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.models import load_model
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

split_num = 1
for train_index, test_index in skf.split(scaled_train_samples, int_scaled_train_labels):
    X_train, X_test = scaled_train_samples[train_index], scaled_train_samples[test_index]
    y_train, y_test = int_scaled_train_labels[train_index], int_scaled_train_labels[test_index]
    
    # Criar e treinar o modelo
    model = create_functional_model()
    history = model.fit(X_train, y_train, epochs=500, batch_size=25, verbose=2)
    
    # Salvar o modelo
    model_filename = f'model_split_{split_num}.h5'  # Salvar como formato .h5
    model.save(model_filename)
    
    print(f"Modelo do split {split_num} salvo como {model_filename}")
    
    split_num += 1

# Carregar o modelo
model_filename = 'model_split_1.h5'  # ou o nome do arquivo do seu modelo final
loaded_model = load_model(model_filename)

# Realizar predições
y_pred = loaded_model.predict(scaled_test_samples)
y_pred_classes = np.argmax(y_pred, axis=1)

# Avaliar o modelo
test_loss, test_accuracy = loaded_model.evaluate(scaled_test_samples, int_scaled_test_labels, verbose=0)
print(f"Acurácia no conjunto de teste: {test_accuracy:.4f}")
print(f"Perda no conjunto de teste: {test_loss:.4f}")

# Imprimir relatório de classificação
print("\nRelatório de Classificação:")
print(classification_report(int_scaled_test_labels, y_pred_classes))

# Criar e plotar matriz de confusão
cm = confusion_matrix(int_scaled_test_labels, y_pred_classes)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Matriz de Confusão')
plt.ylabel('Rótulo Verdadeiro')
plt.xlabel('Rótulo Previsto')
plt.show()

# Se você quiser salvar métricas ou resultados em um arquivo
with open('test_results.txt', 'w') as f:
    f.write(f"Acurácia no conjunto de teste: {test_accuracy:.4f}\n")
    f.write(f"Perda no conjunto de teste: {test_loss:.4f}\n")
    f.write("\nRelatório de Classificação:\n")
    f.write(classification_report(int_scaled_test_labels, y_pred_classes))
