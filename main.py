from plotting_class import * 
from metrics import *
from Predictions import * 

if __name__ == "__main__":
    url = "C:\\Users\\velis\\Downloads\\archive (6)\\N-CMAPSS_DS05.h5"
    unit = 1
    dset = "dev"
    selected_cycles = ["1", "2", "3"]

    plot_obj = Plot_obj(url, unit, dset, selected_cycles=selected_cycles)
    # plot_obj.time_series_plt(vector="PS30")
    # plot_obj.box_plot_quant(vector="PS30")
    # plot_obj.barplot_of_flight_class()
    plot_obj.correlation_heatmap(["T24","T30","T48","T50"])