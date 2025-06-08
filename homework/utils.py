import os
import pandas as pd

def pregunta_01():
    # Definir rutas
    base_path = 'files/input'
    output_path = 'files/output'

    create_directory(output_path)

    # Procesar train y test
    train_data = data_processing('train', base_path)
    test_data = data_processing('test', base_path)

    # Guardar en CSV
    create_csv_file(train_data, output_path, 'train_dataset.csv')
    create_csv_file(test_data, output_path, 'test_dataset.csv')

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        #elimar contenido previo
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)

def data_processing(split, base_path):
        datos = []
        for sentimiento in ['positive', 'negative', 'neutral']:
            carpeta = os.path.join(base_path, split, sentimiento)
            if not os.path.exists(carpeta):
                continue
            for archivo in os.listdir(carpeta):
                if archivo.endswith('.txt'):
                    ruta = os.path.join(carpeta, archivo)
                    with open(ruta, 'r', encoding='utf-8') as f:
                        texto = f.read().strip()
                        datos.append({'phrase': texto, 'target': sentimiento})
        return datos

def create_csv_file(data, file_path, filename):
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(file_path, filename), index=False)