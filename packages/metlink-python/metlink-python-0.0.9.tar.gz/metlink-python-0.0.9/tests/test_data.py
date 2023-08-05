import os


def txt_to_csv():
    """Converts all txt files in data to csv files"""
    for file in os.listdir('data/'):
        # add file name to start and end of file, and replace .txt with .csv
        if file.endswith('.txt') or file.endswith('.csv'):
            print(file)
            file_name = file.split('.')[0]
            with open('data/' + file, 'r') as f:
                txt_file = f.read()
            # write python file
            with open('data/' + file_name + '.py', 'w') as f:
                f.write(file_name + ' = """' + txt_file + '"""')
                os.remove('data/' + file)


def test_txt():
    """ Test there are no .txt files in data folder"""
    for file in os.listdir('data/'):
        if file == '__pycache__':
            continue
        if file.endswith('.txt') or file.endswith('.csv'):
            print("There are .txt files in data folder, testing conversion")
            try:
                txt_to_csv()
                print("Conversion successful, retry tests")
            except AssertionError:
                print("There are still .txt or .csv files in data folder")
                break
            assert False
    assert True


# def test_routes_load():
#     """Test that routes load"""
#     from metlink.util.data_controller import DataController
#     data_controller = DataController()
#     assert data_controller.load_data('data/routes.csv')
