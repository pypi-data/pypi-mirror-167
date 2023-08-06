import os
import numpy as np
import pandas as pd
from pathlib import Path


def getSpecificSignalCSV(path_sim, model_name, simNumber, list_Signals):

    simulationSignalsToPlot = pd.DataFrame()

    for i in range(len(simNumber)):
        for n in range(len(list_Signals)):
            path_simulationSignals = os.path.join(path_sim + str(simNumber[i]) + '.csv')
            # Importing csv
            simulationSignals = np.genfromtxt(path_simulationSignals, dtype=str, delimiter=',', skip_header=0)
            simulationSignals = simulationSignals.tolist()
            simulationSignals = pd.DataFrame(simulationSignals)
            simulationSignals.set_index(0, inplace=True)
            simulationSignal = list(simulationSignals.loc[list_Signals[n]])
            simulationSignal.insert(0, list_Signals[n] + '_' + str(simNumber[i]))
            simulationSignal = [simulationSignal]
            temp_frame = pd.DataFrame(simulationSignal)
            temp_frame.set_index(0, inplace=True)
            simulationSignalsToPlot = simulationSignalsToPlot.append(temp_frame)

    return simulationSignalsToPlot


def get_signals_from_csv(full_name_file: str, list_signals):
    '''
    Reads a csv file and returns a dataframe with the selected signals
    :param full_name_file: full path to the csv file
    :param list_signals: list of signals to read
    :return: dataframe with the selected signals
    '''

    if type(list_signals) == str: list_signals = [list_signals]           # If only one signal is passed as an argument, make it a list

    all_signals_df = pd.read_csv(full_name_file)                          # read file into a dataframe
    all_signals_df.columns = all_signals_df.columns.str.replace(' ', '')  # eliminate whitespaces from the column names
    list_signals = [x.replace(' ', '') for x in list_signals]             # eliminate whitespaces from the signal names as well
    return all_signals_df[list_signals]


def load_parameters_from_csv(full_name_file: str, name_row: str, path_model_library: str, case_model: str, flag_write_file: bool):
    '''
    Reads a csv file and returns a dataframe with the selected signals
    :param full_name_file: full path to the csv file with the parameters
    :param name_row: this is a string indentifying the correct row in the csv file
    :param path_model_library: path of the steam_models folder where the items are located
    :param case_model: conductor, magnet, or circuit
    :return: 
    '''

    # Load csv file as dataframe
    
    # Identify the correct model input yaml file (use path_model_library and case_model and the circuit name from the dataframe)
    model_name = 'RCS' # this needs to be read from the input csv file 'RCS'
    model_file_name = f'modelData_{model_name}.yaml'
    full_path_file = Path(os.path.join(path_model_library, case_model + 's', model_name, 'input', model_file_name)).resolve()
    
    # Import model yaml file as a dict
    
    # Loop through the columns of the dataframe and change the parameters that correspond to dataframe columns
    
    # Optionally write an output file (don't overwrite the model yaml file)

    # return: ?
    
    pass
    


# print(get_signals_from_csv('C:/cernbox/steam-models-dev/viewer/RCS/RCS.csv',[]))
# def gettime_vectorCSV(path_sim, simNumber):
#
#     path_simulationSignals = os.path.join(path_sim + str(simNumber[0]) + '.csv')
#     # Importing csv
#     simulationSignals = np.genfromtxt(path_simulationSignals, dtype=str, delimiter=',', skip_header=0)
#     simulationSignals = simulationSignals.tolist()
#     simulationSignals = pd.DataFrame(simulationSignals)
#     simulationSignals.set_index(0, inplace=True)
#     simulationSignal = list(simulationSignals.loc['ï»¿time_vector'])
#     simulationSignal.insert(0, 'time_vector')
#     simulationSignal = [simulationSignal]
#     simulationSignalsToPlot = pd.DataFrame(simulationSignal)
#     simulationSignalsToPlot.set_index(0, inplace=True)
#     return simulationSignalsToPlot

# def writeTdmsToCsv(self, path_output: Path, dictionary: {}):
#     """
#         This function writes the signals of the signal_data dictionary of this class of a TDMS file to a specific csv file.
#         dictionary for header with names of the groups and signal that are used in the TDMS file
#         header: Groupname_signalname, ....
#     """
#     # Get signal
#     # signal_output = getspecificSignal(path_tdms, group_name, signal_name)
#     # np.savetxt(path_output, signal_output, delimiter=",")
#     # headers, units,...
#
#     header = []
#     for group in dictionary.keys():
#         for channel in dictionary[group]:
#             header.append(group + '_' + channel)
#
#     tdms_df = pd.DataFrame(self.signal_data)
#     tdms_df.to_csv(path_output, header=header, index=False)