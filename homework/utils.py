import os
import pandas as pd

def pregunta_01():
    # Definir rutas
    base_path = 'files/input'
    output_path = 'files/output'

    create_directory(output_path)

    # Procesar train y test
    train_data = data_processing(base_path=base_path, directory='train', text_column='phrase', label_column='sentiment')
    test_data = data_processing(base_path=base_path, directory='test', text_column='phrase', label_column='sentiment')

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

def data_processing(path, directory, text_column='text', label_column='label', file_extension='.txt',encoding='utf-8'):
    """
    Reads text files from a specified directory structure and returns a list of dictionaries
    containing the text and corresponding labels.
    """
    data = []
    split_path = os.path.join(path, directory)

    for label in os.listdir(split_path):
        label_path = os.path.join(split_path, label)
        if os.path.isdir(label_path):
            data.extend(
                _read_texts_from_directory(label_path, label, text_column, label_column, file_extension, encoding)
            )

    return data

def _read_texts_from_directory(dir_path, label, text_column, label_column, file_extension, encoding):
    """
    Reads text files from a directory and returns a list of dictionaries
    with the text content and corresponding label.
    """
    entries = []
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)

        if os.path.isfile(file_path) and filename.endswith(file_extension):
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read().strip()
                entries.append({text_column: content, label_column: label})

    return entries

def create_csv_file(data, file_path, filename):
    """
    Creates a CSV file from a list of dictionaries and saves it to the specified path.
    """
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(file_path, filename), index=False)