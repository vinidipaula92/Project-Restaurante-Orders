import csv


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f'Extensão inválida: "{path_to_file}"')
    try:
        with open(path_to_file) as f:
            reader = csv.reader(f)
            file_reader = [row for row in reader]
            return file_reader
    except (FileNotFoundError):
        raise FileNotFoundError(f'Arquivo inexistente: "{path_to_file}"')
