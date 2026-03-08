# Importing Libraries

import h5py
import numpy as np

class Metrics:

    def __init__(self, url: str, unit: int = None, dset: str = None):
        """ Initiazing the data"""

        # Reading the URL File 

        try: 
            self._data = h5py.File(url,"r")
        except FileNotFoundError:
            print("File directory does not exist")
        except TypeError:
            print("The URL is not a string")
        except Exception:
            print("The directory have a problem")
        
        # Unit Analysis

        self._units_dev = np.unique(self._data["A_dev"][:,0])
        self._units_test = np.unique(self._data["A_test"][:,0])

        self._unit = unit

        if dset == "dev" and self._unit not in self._units_dev:
            raise Exception("The unit does not Exist in dev set")
        
        if dset == "test" and self._unit_test not in self._units_test:
            raise Exception("The unit does not exist in test set")
        
        # Capturing Various Datasets

        self._data_unit_ax_data = self._data[f"A_{dset}"][self._data[f"A_{dset}"][:,0] == self._unit] # Auxialary_Data
        self._data_unit_model_hp_p = self._data[f"T_{dset}"][self._data[f"A_{dset}"][:,0] == self._unit] # Model Health Parameters
        self._data_unit_measurements = self._data[f"X_s_{dset}"][self._data[f"A_{dset}"][:,0] == self._unit] # Measurements
        self._data_unit_virtual_sensors = self._data[f"X_v_{dset}"][self._data[f"A_{dset}"][:,0] == self._unit] # Virtual Sensors
        self._dataRLU = self._data[f"Y_{dset}"][self._data[f"A_{dset}"][:,0] == self._unit] # RLU Data 
        self._data_descriptods = self._data[f"W_{dset}"][self._data[f"A_{dset}"][:,0] == self._unit] # Descriptors Dataset
        self._full_data_unit = np.concatenate((self._data_unit_ax_data, self._data_unit_model_hp_p, self._data_unit_measurements, self._data_unit_virtual_sensors, self._dataRLU, self._data_descriptods), axis = 1)

        # Cycles of Unit and Lengths of each Cycle

        self._cycles_unit = np.unique(self._data_unit_ax_data[:,1])
        lst_cycles_lengths = [self._data_unit_ax_data[self._data_unit_ax_data[:,1]==c].shape[0] for c in self._cycles_unit]

        dict_idx_cycle = [str(int(c)) for c in self._cycles_unit]

        self._cycles_lengths = dict(zip(dict_idx_cycle, lst_cycles_lengths))

    def quantity_per_cycle(self, cycle_number: int = None, quantity: str = None):

        """ Function for Capturing the Data of a Specific Cycle and Quantity """

        if cycle_number not in self._cycles_unit:
            raise Exception("The cycle number does not exist in the unit")
        
        if quantity not in ["measurements", "virtual_sensors", "model_hp_p", "descriptors"]:
            raise Exception("The quantity does not exist, please choose from measurements, virtual_sensors, model_hp_p, descriptors")


        if quantity == "measurements":
                return self._data_unit_measurements[self._data_unit_ax_data[:,1] == cycle_number]
            
        if quantity == "virtual_sensors": 
                return self._data_unit_virtual_sensors[self._data_unit_ax_data[:,1] == cycle_number]
            
        if quantity == "model_hp_p":
                return self._data_unit_model_hp_p[self._data_unit_ax_data[:,1] == cycle_number] 
            
        if quantity == "descriptors":
                return self._data_descriptods[self._data_unit_ax_data[:,1] == cycle_number]
        
    def flight_class_per_cycle(self, cycle_number: int = None):

        """ Function for Capturing the Flight Class of a Specific Cycle """

        if cycle_number not in self._cycles_unit:
            raise Exception("The cycle number does not exist in the unit")
            
        return np.unique(self._data_unit_ax_data[self._data_unit_ax_data[:,1] == cycle_number][:,2])
        
