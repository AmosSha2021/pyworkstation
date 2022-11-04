
import sys
import ACOND
import AOTA
import SCOND
import SOTA
import N2xx_Sensitivity
import N2x_Vs_N19x
import Ranging
import N2xx_NB_Sensitivity
import Tx_Power__plotting
def main(argv):
    print("Please choose the station" \
          " from below -\n\n\n")
    print("ACOND Plots(1)")
    print("SCOND Plots (2)")
    print("SOTA Plots (3)")
    print("AOTA Plots (4)")
    print("N2xx_Sensitivity (5)")
    print("N2x_Vs_N19x (6)")
    print("Ranging (7)")
    print("N2xx NB Sensitivity (8)")
    print("Tx_Power__plotting(9)")
    choice = int(input())

    choice_dict = {
        1: ACOND,
        2: SCOND,
        3: SOTA,
        4: AOTA,
        5: N2xx_Sensitivity,
        6: N2x_Vs_N19x,
        7: Ranging,
        8: N2xx_NB_Sensitivity,
        9: Tx_Power__plotting
    }

    choice_dict[choice].Start(argv)
    #AOTA.plot_tc("/Users/hindujaichapuram/Desktop/D64 EVT Arrow Ether 2-step cal main build data/K_STATS", 3, "tc=Ether_Scan tech=ARROW:subtc=EIRP_Corrected")
    #ACOND.plot_tc("/Users/hindujaichapuram/Desktop/D64_ACOND",-30,'TxPower_CW_PreCal')
    # plot_tc(20,'_SNR')
    # plot_tc(0.5,'Mag_flatness')
    #plot_tc("/Users/hindujaichapuram/Documents/Documents/D6x:D1y_P1_Build_data_review /ACOND/Only_Pass/Main_configs/*.csv",-50,'RSSI_Sweep','rate=pkt_type_1','dl=-45')
    # plot_tc_ANT2(5,'TxPower_Cal')
    # plot_tc_ANT2(-30,'RxGainCal_Coeff')
    #plot_tc("/Users/hindujaichapuram/Documents/Documents/D6x:D1y_P1_Build_data_review /ACOND/Only_Pass/DOE_Vs_Main/*.csv",5,'TxPower_Cal')
    #plot_tc("/Users/hindujaichapuram/Documents/Documents/D6x:D1y_P1_Build_data_review /ACOND/Only_Pass/DOE_Vs_Main/*.csv",-30, 'RxGainCal_Coeff')


main(sys.argv)