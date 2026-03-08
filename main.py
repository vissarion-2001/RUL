from plotting_class import * 
from metrics_class import *
from Predictions_class import * 

if __name__ == "__main__":
    url = "C:\\Users\\velis\\Downloads\\archive (6)\\N-CMAPSS_DS08c-008.h5"
    unit = 3
    dset = "dev"
    selected_cycles = [str(i) for i in range(1,54)]

    # metr_obj = Metrics(url=url, unit=1)
    plot_obj = Plot_obj(url, unit, dset, selected_cycles=selected_cycles)
    plot_obj.time_series_plt(vector="LPC_flow_mod")
    # plot_obj.box_plot_quant(vector="PS30")
    # plot_obj.barplot_of_flight_class()
    # plot_obj.correlation_heatmap()

    # metrics_obj = Metrics(url, unit, dset)