import os
from .equity_curves import *

def generate_filepath(py_filename, output_folder, start_date, end_date, para_dict, para_values):
    start_date_str = datetime.datetime.strptime(start_date, '%Y-%m-%d').strftime("%Y%m%d")
    end_date_str = datetime.datetime.strptime(end_date, '%Y-%m-%d').strftime("%Y%m%d")
    save_name = f'file={py_filename}&date={start_date_str}{end_date_str}'

    for i, key in enumerate(para_dict):
        para = para_values[i]
        if key == 'code':
            if str(para).isdigit():
                para = str(para).zfill(5)

        if isinstance(para, float):
            if para.is_integer():
                para = int(para)

        save_name += f'{key}={str(para)}&'

    filepath = os.path.join(output_folder, f'{save_name[:-1]}.csv')

    return filepath


def plot_equity_curves(filename, output_folder, start_date, end_date, para_dict, result_df, settings):

    app = equity_curves.Plot(filename, output_folder, start_date, end_date, para_dict, result_df, generate_filepath, settings)

    return app