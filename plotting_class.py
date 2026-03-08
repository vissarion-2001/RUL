import h5py 
import matplotlib.pyplot as plt 
import seaborn as sns
from metrics_class import Metrics
import numpy as np
import pandas as pd

class Plot_obj(Metrics):
    def __init__(self, url: str, unit: int = None, dset: str = None, selected_cycles: list[str] = None):
        super().__init__(url, unit, dset)

        """ Initializing the data for Plotting """ 

        # List of vectors per Quantities

        self.selected_cycles = selected_cycles
        self._data_vectors = ["unit", "cycle", "Flight_class", "Healthy_state", "fan_eff_mod",\
                                       "fan_flow_mod", "LPC_eff_mod", "LPC_flow_mod", "HPC_eff_mod",\
                                        "HPC_flow_mod", "HPT_eff_mod", "HPT_flow_mod", "LPT_eff_mod",\
                                        "LPT_flow_mod","Wf", "Nf", "Nc", "T24","T30","T48","T50","P15",\
                                        "P2","P21","P24","PS30","P40","P50","T40","P30","P45","W21","W22",\
                                        "W25","W31","W32","W48","W50","SmFan","SmLPC","phi","RLU","alt",\
                                        "Mach","TRA","T2"]
        
        self.s_int = [int(c) for c in selected_cycles]
        self.indexes_cycles = [self._data_unit_ax_data[:,1] == c for c in self.s_int]
        self.id_c = np.zeros(self.indexes_cycles[0].shape[0])
        for i in self.indexes_cycles:
            self.id_c += i  
        self.id_c = self.id_c.astype(bool)
        self._cycles_lengths =  [self._cycles_lengths[c] for c in selected_cycles]

    def time_series_plt(self, vector: str = None):

        """ This functions plots the time series of the selected cycles"""
        
        "Capturing the Indexes of the Selected Cycles and Vector for Plotting"

        try: 
            if vector not in self._data_vectors:
                raise Exception("The vector does not exist in the data vectors")
            plot_data = self._full_data_unit[self.id_c, self._data_vectors.index(vector)]
        except TypeError:
            print("The vector should be a string")
        
        fig, ax = plt.subplots()
        ax.plot(plot_data)
        if len(self.selected_cycles)>1:
            ax.vlines(x=self._cycles_lengths[0], ymin=plot_data.min(), ymax=plot_data.max(), colors='r', linestyles='dashed')
            for c in range(1, len(self._cycles_lengths[1:-1])+1):
                ax.vlines(x=sum(self._cycles_lengths[:c+1]), ymin=plot_data.min(), ymax=plot_data.max(), colors='r', linestyles='dashed')
        ax.set_ylabel(vector)
        ax.set_xlabel("Time")
        plt.show()

    def box_plot_quant(self, vector: str = None):

        """ This function plot the BoxPlot of selected quantity"""

        try:
            if vector not in self._data_vectors:
                raise Exception("The vector does not exist in the data vectors")
            plot_data = self._full_data_unit[self.id_c, self._data_vectors.index(vector)]
        except TypeError:
            print("The vector should be a string")
            
        fig, ax = plt.subplots()
        ax.boxplot(x=plot_data)
        ax.set_ylabel(f"Distribution of {vector}")
        ax.set_xlabel(vector)
        plt.show()
        
    def barplot_of_flight_class(self):

        """ This function will create a barplot of the count of each flight class for each unit """

        class_fl = {}

        # Unique Flight Class 

        fl_cl = np.unique(self._data_unit_ax_data[:,2])

        for key in fl_cl:
            class_fl[str(int(key))] = 0

        for c in self._cycles_unit:
            class_fl[str(int(self.flight_class_per_cycle(c)))] += 1
            
        fig, ax = plt.subplots(nrows=1, ncols=2)
        ax[0].bar(class_fl.keys(), class_fl.values())
        ax[1].pie(class_fl.values(), labels=class_fl.keys(), autopct='%1.1f%%')
        ax[0].set_xlabel("Flight Class")
        ax[0].set_ylabel("Count of Flight Class")
        ax[1].set_xlabel("Flight Class")
        ax[1].set_ylabel("Count of Flight Class")
        plt.show()

    def correlation_heatmap(self, lst_vectors: list = None):

        ind = []
        for f in lst_vectors:
            if f not in self._data_vectors:
                raise Exception(f"The {f} does not exist in the dataset")
            ind.append(self._data_vectors.index(f))
            
        corr_features = self._full_data_unit[:,ind]

        df = pd.DataFrame(corr_features, columns=lst_vectors)

        corr_matrix = df.corr(numeric_only=True)

        sns.heatmap(data=corr_matrix, annot=True)
        plt.show()



            
            

                

            


        

    
    

