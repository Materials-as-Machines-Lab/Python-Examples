#====================================================

# Data plotting functions 

#====================================================

# Reference: https://matplotlib.org/stable/users/explain/quick_start.html#coding-styles

# Package Initialization
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
import numpy as np

BaseStylePath = r"C:\Users\Aiden\OneDrive - Carleton University\Materials as Machines Lab\Current Research\Aiden\Work\Testing Data\mystyle.mplstyle"

#====================================================
# Resistance vs Time Graphs
#====================================================

def RvT_raw_plot(time,resist,ch,samplename,savepath,stylepath=BaseStylePath):
    """
    This FUNCTION takes raw time and resistance data and plots them

    Input:
        resist      ->      [Array]
                            1D Array of resistance values in [ohms]
                                    
        time        ->      [Array]
                            1D Array of time values in [s]

        name        ->      [String]
                            Name that the plot will be saved under
                            
        savepath    ->      [String]
                            file path to directory for this to be saved under
    Output:
        Saves a png plot showing resistance over time.
    """
    # Set plt style to custom template
    plt.style.use(stylepath)   

    """    
    # Set Resistance Limits based on channel defaults
    if ch == 3 or ch == 4:
        ylim = 150
    elif ch == 1 or ch == 2:
        ylim = 150
    """
    
    # Plot Creation
    fig, ax = plt.subplots()
    plot = plt.plot(time, resist,
                    color = 'r', 
                    markerfacecolor = 'red',
                    markeredgecolor = 'red')
    
    ax.set_xlabel("Time [$s$]")
    ax.set_ylabel("Resistance [$\Omega$]")
    ax.set_ylim(bottom=0)
    #plt.rcParams.update({'figure.dpi': '100'})     # Use with plt.show() to avoid weird aspect ratio
    #plt.show()  
    
    plt.savefig(savepath + "\\Plots\\RvT\\" +  samplename + "_RvT_raw_plot.png", bbox_inches='tight', pad_inches=0.1)
    plt.close()

#----------------------------------------------------

def RvT_delta_plot(time,resist,samplename,savepath,stylepath=BaseStylePath):
    """
    This FUNCTION takes delta time and delta resistance data and plots them

    Input:
        resist      ->      [Array]
                            1D Array of resistance values in [ohms]
                                    
        time        ->      [Array]
                            1D Array of time values in [s]

        name        ->      [String]
                            Name that the plot will be saved under
    Output:
        Saves a png plot showing resistance over time.
    """
    # Set plt style to custom template
    plt.style.use(stylepath)
  
    
    fig, ax = plt.subplots()
    plot = plt.plot(time, resist,
                    color = 'r', 
                    markerfacecolor = 'red',
                    markeredgecolor = 'red')
    
    ax.set_xlabel("Time [$\Delta s$]")
    ax.set_ylabel("Resistance Change [$\Delta\Omega$]")
    ax.set_ylim(bottom = -0.5, top = 5)
    ax.set_xlim(left = -10)
    #plt.rcParams.update({'figure.dpi': '100'})     # Use with plt.show() to avoid weird aspect ratio
    #plt.show()  
    
    plt.savefig(savepath + "\\Plots\\RvT\\" +  samplename + "_RvT_delta_plot.png", bbox_inches='tight', pad_inches=0.1)
    plt.close()

#----------------------------------------------------

def RvT_tfil_plot(time,resist,samplename,savepath,stylepath=BaseStylePath):
    """
    This FUNCTION takes time filteredtime and resistance data and plots them

    Input:
        resist      ->      [Array]
                            1D Array of resistance values in [ohms]
                                    
        time        ->      [Array]
                            1D Array of time values in [s]

        name        ->      [String]
                            Name that the plot will be saved under
    Output:
        Saves a png plot showing resistance over time.
    """
    # Set plt style to custom template
    plt.style.use(stylepath)
    
    fig, ax = plt.subplots()
    plot = plt.plot(time, resist,
                    color = 'r', 
                    markerfacecolor = 'red',
                    markeredgecolor = 'red')
    
    ax.set_xlabel("Time [$s$]")
    ax.set_ylabel("Resistance [$\Omega$]")
    ax.set_ylim(bottom=0)
    #plt.rcParams.update({'figure.dpi': '100'})     # Use with plt.show() to avoid weird aspect ratio
    #plt.show()  
    
    plt.savefig(savepath + "\\Plots\\RvT\\" +  samplename + "_RvT_tfil_plot.png", bbox_inches='tight', pad_inches=0.1)
    plt.close()

#----------------------------------------------------

def RvT_cycle_plot(data_in,ch,samplename,savepath,stylepath=BaseStylePath):
    """
    This FUNCTION takes raw time and resistance data and plots them

    Input:
        data                ->      [Dictionary]
                                    Key:    (c) -> c = Cycle #
                                    Value:  (n,ch) -> n = time step, ch = data channel  
                                    
        testparam          ->       [Array]
                                    (ch, t_start, dur_cycle, cyclecount)

        samplename          ->      [String]
                                    Name that the plot will be saved under
                            
        savepath            ->      [String]
                                    file path to directory for this to be saved under
    Output:
        Saves a png plot showing resistance over time.
    """
    # Set plt style to custom template
    plt.style.use(stylepath)
    
    n_c = len(data_in)
    N = 5
    

    '''
    # Prints cycles that are multiples of N (and first and last)
    for c in n_c:
        if c == 0:
            name        = samplename + "-C" + str(c+1)
            time_start  = data_in[c][0,0]
            time        = np.subtract(data_in[c][:,0],time_start)
            resist      = data_in[c][:,ch]
            plt.plot(time, resist, label = name, ls='-')
        elif c+1 % N == 0 and c !=n_c:
            name        = samplename + "-C" + str(c+1)
            time_start  = data_in[c][0,0]
            time        = np.subtract(data_in[c][:,0],time_start)
            resist      = data_in[c][:,ch]
            plt.plot(time, resist, label = name, ls='-')
        elif c == n_c:
            name        = samplename + "-C" + str(c+1)
            time_start  = data_in[c][0,0]
            time        = np.subtract(data_in[c][:,0],time_start)
            resist      = data_in[c][:,ch]
            plt.plot(time, resist, label = name, ls='-')               
    '''
    
    # Plots all cycles when # is below 6, then reduces it to multiples of 5 + first and last
    time = {}
    resist = {} 
    mul = int(np.ceil((n_c-1)/N))
    cycles = list(range(1,mul))    
    if (n_c-1) > N: # If cycles is above 5 we reduce
        
        # Plot first cycle
        name        = samplename + "-C1"
        time_start  = data_in[0][0,0]
        time[0]     = np.subtract(data_in[0][:,0],time_start)
        resist[0]   = data_in[0][:,ch]
        plt.plot(time[0], resist[0],label = name,ls='-')
        
        # Plot in between cycles
        for n in cycles:
            c = (n * N)
            name        = samplename + "-C" + str(c)
            time_start  = data_in[c][0,0]
            time[n]     = np.subtract(data_in[c][:,0],time_start)
            resist[n]   = data_in[c][:,ch]
            plt.plot(time[n], resist[n],label = name,ls='-')
            
        # Plot last cycle
        name        = samplename + "-C" + str(n_c)
        time_start  = data_in[n_c-1][0,0]
        time[mul+1]     = np.subtract(data_in[n_c-1][:,0],time_start)
        resist[mul+1]   = data_in[n_c-1][:,ch]
        plt.plot(time[mul+1], resist[mul+1],label = name,ls='-')
    
            
        plt.xlabel("Time [$s$]")
        plt.ylabel("Resistance [$\Omega$]")
        #plt.ylim(bottom=0)

        # Format Legend
        plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left",
                    borderaxespad=0, ncol=5)

        plt.savefig(savepath + "\\Plots\\RvT\\" +  samplename + "_RvT_cycle_plot.png", bbox_inches='tight', pad_inches=0.1)
        plt.close()
        
  
    else:   # If cycles is below 5 we plot normally

        for c in data_in:
            name        = samplename + "-C" + str(c+1)
            time_start  = data_in[c][0,0]
            time[c] = np.subtract(data_in[c][:,0],time_start)
            resist[c] = data_in[c][:,ch]

            plt.plot(time[c], resist[c], label=name, ls='-')
            
        plt.xlabel("Time [$s$]")
        plt.ylabel("Resistance [$\Omega$]")
        #plt.ylim(bottom=0)

        # Format Legend
        plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left",
                    borderaxespad=0, ncol=5)
            
        plt.savefig(savepath + "\\Plots\\RvT\\" +  samplename + "_RvT_cycle_plot.png", bbox_inches='tight', pad_inches=0.1)
        plt.close()        

#----------------------------------------------------
    
def RvT_comb_plot(data_in,testparam,savepath,stylepath=BaseStylePath):
    """
    This FUNCTION takes multiple time and resistance data and plots them

    Input:
        data_in         ->      [Dictionary]
                                    Key: (s) -> s = sample #
                                    Value: (t,R1,R2,R3,R4)
                                        0 - t  = time step
                                        1 - R1 = Resistance channel 1
                                        2 - R2 = Resistance channel 2
                                        3 - R3 = Resistance channel 3
                                        4 - R4 = Resistance channel 4
                                    
        testparam       ->      [Dictionary]
                                    Key: (s) -> s = sample #
                                    Value:  (ch,t_start,dur_cycle,cyclecount)
                                            0 - ch          = channel for resistance measurement
                                            1 - t_start     = test start time
                                            2 - dur_cycle   = duration of each cycle
                                            3 - cyclecount  = number of cycles
        
        savepath        ->      [String]
                                    File path to directory for this to be saved under
    Output:
        Saves a png plot showing resistance over time of all samples.
    """
    # Set plt style to custom template
    plt.style.use(stylepath)
    
    # Sizes
    n_s = len(data_in)
    
    # Test Duration
    TDur = round(float(testparam[0][2] * testparam[0][3]))
    
    for s in range(0,n_s): # Loops through samples
        samplename = "S" + str(s+1) + "_"
        ch = testparam[s][0]
        if ch == 3 or ch == 4:
            ylim = 150
        elif ch == 1 or ch == 2:
            ylim = 150    
        time_start = data_in[s][0,0]
        time = np.subtract(data_in[s][:,0],time_start)
        resistance = data_in[s][:,ch]
        plt.plot(time,resistance, ls = "-", label="S"+str(s+1))
        

        # Format Legend
        plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left",
                    borderaxespad=0, ncol=7)
        
        # Format Axis
        plt.xlabel("Time [$s$]")
        plt.ylabel("Resistance [$\Omega$]")
        plt.ylim(bottom = -10, top = ylim)
        plt.xlim(left = -10, right = TDur)
        plt.savefig(savepath + "\\Plots\\RvT\\" + samplename + "RvT_comb_plot.png", bbox_inches='tight', pad_inches=0.1)
    plt.close()
    
#----------------------------------------------------
    
def RvT_combdelta_plot(data_in,testparam,savepath,stylepath=BaseStylePath):
    """
    This FUNCTION takes multiple time and resistance data and plots them

    Input:
        data_in         ->      [Dictionary]
                                    Key: (s) -> s = sample #
                                    Value: (t,R1,R2,R3,R4)
                                        0 - t  = time step
                                        1 - R1 = Resistance channel 1
                                        2 - R2 = Resistance channel 2
                                        3 - R3 = Resistance channel 3
                                        4 - R4 = Resistance channel 4
                                    
        testparam       ->      [Dictionary]
                                    Key: (s) -> s = sample #
                                    Value:  (ch,t_start,dur_cycle,cyclecount)
                                            0 - ch          = channel for resistance measurement
                                            1 - t_start     = test start time
                                            2 - dur_cycle   = duration of each cycle
                                            3 - cyclecount  = number of cycles
        
        savepath        ->      [String]
                                    File path to directory for this to be saved under
    Output:
        Saves a png plot showing resistance over time of all samples.
    """
    # Set plt style to custom template
    plt.style.use(stylepath)
    
    # Sizes
    n_s = len(data_in)
    
    # Test Duration
    TDur = round(float(testparam[0][2] * testparam[0][3]))
    
    for s in range(0,n_s): # Loops through samples
        samplename = "S" + str(s+1) + "_"
        ch = testparam[s][0]   
        time_start = data_in[s][0,0]
        res_start = data_in[s][0,ch]
        time = np.subtract(data_in[s][:,0],time_start)
        resistance = np.subtract(data_in[s][:,ch],res_start)
        plt.plot(time,resistance, ls = "-", label="S"+str(s+1))
        

        # Format Legend
        plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left",
                    borderaxespad=0, ncol=7)
        
        # Format Axis
        plt.xlabel("Time [$s$]")
        plt.ylabel("Resistance Change [$\Delta\Omega$]")
        plt.ylim(bottom = 0, top = 20)
        plt.xlim(left = -10, right = TDur)
        plt.savefig(savepath + "\\Plots\\RvT\\" + samplename + "RvT_combdelta_plot.png", bbox_inches='tight', pad_inches=0.1)
    plt.close()
    
#----------------------------------------------------
    
def RvT_combraw_plot(data_in,testparam,savepath,stylepath=BaseStylePath):
    """
    This FUNCTION takes multiple time and resistance data and plots them

    Input:
        data_in         ->      [Dictionary]
                                    Key: (s) -> s = sample #
                                    Value: (t,R1,R2,R3,R4)
                                        0 - t  = time step
                                        1 - R1 = Resistance channel 1
                                        2 - R2 = Resistance channel 2
                                        3 - R3 = Resistance channel 3
                                        4 - R4 = Resistance channel 4
                                    
        testparam       ->      [Dictionary]
                                    Key: (s) -> s = sample #
                                    Value:  (ch,t_start,dur_cycle,cyclecount)
                                            0 - ch          = channel for resistance measurement
                                            1 - t_start     = test start time
                                            2 - dur_cycle   = duration of each cycle
                                            3 - cyclecount  = number of cycles
        
        savepath        ->      [String]
                                    File path to directory for this to be saved under
    Output:
        Saves a png plot showing resistance over time of all samples.
    """
    # Set plt style to custom template
    plt.style.use(stylepath)
    
    n_s = len(data_in)
    
    for s in range(0,n_s): # Loops through samples
        samplename = "S" + str(s+1) + "_"
        ch = testparam[s][0]
        #time_start = data_in[s][0,0]
        #time = np.subtract(data_in[s][:,0],time_start)
        time = data_in[s][:,0]
        resistance = data_in[s][:,ch]
        plt.plot(time,resistance, ls = "-", label="S"+str(s+1))
        

    # Format Legend
    plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left",
                borderaxespad=0, ncol=7)
        
    # Format Axis
    plt.xlabel("Time [$s$]")
    plt.ylabel("Resistance [$\Omega$]")
    #plt.ylim(bottom = 300, top = 600)
    plt.xlim(left = -10)
    plt.savefig(savepath + "\\Plots\\RvT\\" + "RvT_combraw_plot.png", bbox_inches='tight', pad_inches=0.1)
    plt.close()

    
#====================================================
# Resistance vs Force vs Time Graphs
#====================================================

#----------------------------------------------------

def RvFvT_raw_plot(rtime,rdata,ftime,fdata,samplename,savepath):
    """
    This FUNCTION takes raw resistance and force data and plots them against time.

    INPUT:
        rdata       ->      [Array]
                            1D Array of resistance values in [ohms]
                                    
        rtime       ->      [Array]
                            1D Array of time values in [s]
                            
        fdata       ->      [Array]
                            1D Array of force values in [N]
                                    
        ftime       ->      [Array]
                            1D Array of time values in [s]

        samplename  ->      [String]
                            Name that the plot will be saved under
        savepath    ->      [String]
                            File path to directory for this to be saved under                            
    OUTPUT:
        Saves a png plot showing resisitance over time and force over time.
    """
    
    # Setup figures
    fig, ax1 = plt.subplots(layout='constrained')   # Initiate figure and first axis (plot)
    ax2 = ax1.twinx()           # Initiate a 2nd axis that shares the same x-axis
    
    # Synching time starts
    rtime_start = rtime[0]
    delta_rtime = np.subtract(rtime,rtime_start)

    # Plot Generation
    ax2.plot(ftime,fdata,                       # Create force vs time plot
                color = 'k',
                ls = '--', 
                markerfacecolor = 'k',
                markeredgecolor = 'k',
                label = 'Force',
                zorder = 10)

    ax1.plot(delta_rtime, rdata,                # Create resistance vs time plot     
                color = 'r',
                ls = '-',
                markerfacecolor = 'r',
                markeredgecolor = 'r',
                label = 'Resistance',
                zorder = 1)

    # Plot Formating
    ax1.set_xlabel("Time [$s$]")                                    # Time axis label
    ax1.set_ylabel("Resistance [$\Omega$]")                         # Resistance axis label 
    #ax1.set_ylim(ymax = 1000)                                      # Resistance axis limits
    ax1.set_ymargin(0.2)                                            # Resistance axis margins (gives padding around edges based on multiplier)
    
    ax2.set_ylabel("Applied Force [N]")                               # Force axis label
    ax2.set_ylim(ymin = -10, ymax = 260)                              # Force axis limits
    
    fig.legend(bbox_to_anchor=(0.05, 1.02, 1, 0.2), 
                loc="lower left",  
                borderaxespad=0, 
                ncol=7)   
   
    ax1.set_zorder(ax2.get_zorder()+1)
    ax1.set_frame_on(False)
    
    plt.savefig(savepath + "\\Plots\\RvFvT\\" + samplename + "_RvFvT_plot.png", bbox_inches='tight', pad_inches=0.1)
    plt.close()

#----------------------------------------------------

def RvFvT_delta_plot(rtime,rdata,ftime,fdata,samplename,savepath):
    """
    This FUNCTION takes delta resistance and force data and plots them against time.

    Input:
        rdata       ->      [Array]
                            1D Array of resistance values in [ohms]
                                    
        rtime       ->      [Array]
                            1D Array of time values in [s]
                            
        fdata       ->      [Array]
                            1D Array of force values in [N]
                                    
        ftime       ->      [Array]
                            1D Array of time values in [s]

        samplename  ->      [String]
                            Name that the plot will be saved under
    Output:
        Saves a png plot showing resisitance over time and force over time.
    """
    
    # Setup figures
    fig, ax1 = plt.subplots()   # Initiate figure and first axis (plot)
    ax2 = ax1.twinx()           # Initiate a 2nd axis that shares the same x-axis
    
    # Synching time starts
    rtime_start = rtime[0]
    delta_rtime = np.subtract(rtime,rtime_start)

    # Plot Generation
    ax2.plot(ftime,fdata,                       # Create force vs time plot
                color = 'k',
                ls = '--', 
                markerfacecolor = 'k',
                markeredgecolor = 'k',
                label = 'Force',
                zorder = 10)

    ax1.plot(delta_rtime, rdata,                # Create resistance vs time plot     
                color = 'r',
                ls = '-',
                markerfacecolor = 'r',
                markeredgecolor = 'r',
                label = 'Resistance',
                zorder = 1)

    # Plot Formating
    ax1.set_xlabel("Time [$s$]")                                    # Time axis label
    ax1.set_ylabel("Resistance Change [$\Delta\Omega$]")            # Resistance axis label 
    #ax1.set_ylim(ymax = 1000)                                      # Resistance axis limits
    ax1.set_ymargin(0.2)                                            # Resistance axis margins (gives padding around edges based on multiplier)
    
    ax2.set_ylabel("Applied Force [N]")                               # Force axis label
    ax2.set_ylim(ymin = -25, ymax = 275)                              # Force axis limits
    
    fig.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left",  
                    borderaxespad=0, ncol=7)   
   
    ax1.set_zorder(ax2.get_zorder()+1)
    ax1.set_frame_on(False)
    
    plt.savefig(savepath + "\\Plots\\RvFvT\\" + samplename + "_RvFvT_plot.png", bbox_inches='tight', pad_inches=0.1)
    plt.close()

#----------------------------------------------------

def RvFvT_comb_plot(rdata,ftime,fdata,testparam,savepath):
    """
    This FUNCTION takes raw resistance and force data and plots them against time.

    INPUT:
        rdata       ->      [Array]
                            1D Array of resistance values in [ohms]
                            
        ftime       ->      [Array]
                            1D Array of force values in [s]
                            
        fdata       ->      [Array]
                            1D Array of force values in [N]
        
       testparam    ->      [Dictionary]
                            Dicitonary storing testing parameters
                                Key:    (s) Sample #
                                Value:  (ch,t_start,dur_cycle,cyclecount)
                                            0 - ch          = channel for resistance measurement
                                            1 - t_start     = test start time
                                            2 - dur_cycle   = duration of each cycle
                                            3 - cyclecount  = number of cycles
                                            4 - Include     = if false exclude sample from graphs
                                            5 - Reason      = Reason for disclusion
                                    
        samplename  ->      [String]
                            Name that the plot will be saved under
                            
        savepath    ->      [String]
                            File path to directory for this to be saved under    
                            
    OUTPUT:
        Saves a png plot showing resisitance over time and force over time.
    """
    # Setup figures
    n_s = len(rdata)                                    # Number of samples
    fig, ax1 = plt.subplots(layout='constrained')       # Initiate figure and first axis (plot)
    ax2 = ax1.twinx()                                   # Initiate a 2nd axis that shares the same x-axis  
    at_txt = "$\mathbf{Excluded}$ $\mathbf{Data:}$"     # Initiate text to be included if any data is discluded
    
    # Plot Formating
    ax1.set_xlabel("Time [$s$]")                                    # Time axis label
    #ax1.set_xlim(xmin=-20)                                         # Time axis limits
    ax1.set_xmargin(0.025)                                          # Time axis margins
    ax1.set_ylabel("Resistance [$\Omega$]")                         # Resistance axis label 
    #ax1.set_ylim(ymin = -150)                                      # Resistance axis limits
    ax1.set_ymargin(0.2)                                            # Resistance axis margins (gives padding around edges based on multiplier)
            
    ax2.set_ylabel("Applied Force [N]")                             # Force axis label
    ax2.set_ylim(ymin = -10, ymax = 260)                            # Force axis limits
        
    # Set the force plot into the background
    ax1.set_zorder(ax2.get_zorder()+1)
    ax1.set_frame_on(False)    
    
    # Force Plot
    ax2.plot(ftime,fdata,                       
                    color = 'k',
                    ls = '--', 
                    markerfacecolor = 'k',
                    markeredgecolor = 'k',
                    label = "Force")
    
    ax2.legend(bbox_to_anchor=(0.035, 1.02, 1, 0.2),
                loc="lower left", 
                borderaxespad=0,
                ncol=7)
    
    # Resistance Plots
    for s in range(0,n_s): # Loops through samples
        include = testparam[s][4]
        if include == True:
            # Set up
            samplename = "S" + str(s+1) + "_"
            ch = testparam[s][0]
            time_start = rdata[s][0,0]
            
            # Data
            time = np.subtract(rdata[s][:,0],time_start)    # Sets time data to zero based on start time
            resistance = rdata[s][:,ch]
            
            # Resistance plots        
            ax1.plot(time,resistance,
                    ls = "-",
                    label="S"+str(s+1))
            
            # Legend        
            ax1.legend(bbox_to_anchor=(0.1, 1.02, 1, 0.2),
                    loc="lower left", 
                    borderaxespad=0,
                    ncol=7) 
            plt.savefig(savepath + "\\Plots\\RvFvT\\" + samplename + "RvFvT_comb_plot.png", bbox_inches='tight', pad_inches=0.1)
        
        elif include == False:   
            at_txt += "\nSample " + str(s+1) + " - " + testparam[s][5]  # Adds line of text per excluded sample with reason 
            
        # Excluded Samples Text Box
        at = AnchoredText(at_txt,
                          frameon = True , 
                          loc = 'lower right',
                          borderpad=0.75)
        at.patch.set_boxstyle("round,pad=0.,rounding_size=0.3")
        ax1.add_artist(at)       
        
    fig.savefig(savepath + "\\Plots\\RvFvT\\" + "Fin_RvFvT_comb_plot.png", bbox_inches='tight', pad_inches=0.1)      
        
    plt.close() 
    
#----------------------------------------------------

#====================================================
# Resistance vs Force Plots
#====================================================

def RvF_plot(force,resist,samplename,savepath):
    """
    This FUNCTION takes force and resistance data and plots them

    Input:
        resist      ->      [Array]
                            1D Array of resistance values in [ohms]
                                    
        force       ->      [Array]
                            1D Array of time values in [N]

        samplename  ->      [String]
                            Name that the plot will be saved under
    Output:
        Saves a png plot showing resisitance over force.
    """
    
    
    fig, ax = plt.subplots()
    plot = plt.plot(force, resist, 
                    color = 'b',
                    markerfacecolor = 'b',
                    markeredgecolor = 'b')
    
    ax.set_xlabel("Applied Force [N]")
    ax.set_ylabel("Resistance Change [$\Delta\Omega$]")

    #plt.rcParams.update({'figure.dpi': '100'})     # Use with plt.show() to avoid weird aspect ratio
    #plt.show()  
    
    plt.savefig(savepath + "\\Plots\\RvF\\" + samplename + "_RvF_plot.png", bbox_inches='tight', pad_inches=0.1)
    plt.close()
    
#====================================================
# Force vs Displacement Plots
#====================================================

def FvD_plot(disp,force,samplename,savepath,stylepath=BaseStylePath):
    """
    This FUNCTION takes raw resistance and force data and plots them against time.

    INPUT:
        disp       ->       [Array]
                            1D Array of displacement values in [mm]
                            
        force       ->      [Array]
                            1D Array of force values in [N]
                                    
        samplename  ->      [String]
                            Name that the plot will be saved under
        savepath    ->      [String]
                            File path to directory for this to be saved under                            
    OUTPUT:
        Saves a png plot showing resisitance over time and force over time.
    """
    # Set plt style to custom template
    plt.style.use(stylepath)
    
    # Setup figures
    fig, ax = plt.subplots(layout='constrained')   # Initiate figure and first axis (plot)
    
    # Plot Formating
    ax.set_xlabel("Displacement [$mm$]")                        # Displacement axis label
    ax.set_ylabel("Force [$N$]")                                # Force axis label 
    ax.set_ymargin(0.2)                                         # Force axis margins (gives padding around edges based on multiplier)
        
    # Force Plot
    ax.plot(disp,force,                       
                    color = 'k',
                    ls = '--', 
                    markerfacecolor = 'k',
                    markeredgecolor = 'k',
                    label = "Force")
        
    fig.savefig(savepath + "\\Plots\\FvD\\" + samplename + "_FvD_plot.png", bbox_inches='tight', pad_inches=0.1)      
    
    plt.close() 
  
#----------------------------------------------------

def FvD_comb_plot(data,testparam,savepath):
    """
    This FUNCTION takes raw resistance and force data and plots them against time.

    INPUT:
        rdata       ->      [Array]
                            1D Array of resistance values in [ohms]
                            
        fdata       ->      [Array]
                            1D Array of force values in [N]
                                    
        samplename  ->      [String]
                            Name that the plot will be saved under
        savepath    ->      [String]
                            File path to directory for this to be saved under                            
    OUTPUT:
        Saves a png plot showing resisitance over time and force over time.
    """
    # Setup figures
    n_s = len(rdata)            # Number of samples
    fig, ax1 = plt.subplots(layout='constrained')   # Initiate figure and first axis (plot)
    ax2 = ax1.twinx()           # Initiate a 2nd axis that shares the same x-axis  
    
    # Plot Formating
    ax1.set_xlabel("Time [$s$]")                                    # Time axis label
    ax1.set_ylabel("Resistance [$\Omega$]")                         # Resistance axis label 
    ax1.set_ylim(ymin = -150, ymax = 1000)                          # Resistance axis limits
    ax1.set_ymargin(0.2)                                            # Resistance axis margins (gives padding around edges based on multiplier)
        
    ax2.set_ylabel("Applied Force [N]")                             # Force axis label
    ax2.set_ylim(ymin = -10, ymax = 260)                            # Force axis limits
        
    # Set the force plot into the background
    ax1.set_zorder(ax2.get_zorder()+1)
    ax1.set_frame_on(False)    
    
    # Force Plot
    ax2.plot(ftime,fdata,                       
                    color = 'k',
                    ls = '--', 
                    markerfacecolor = 'k',
                    markeredgecolor = 'k',
                    label = "Force")
    
    # Plots
    for s in range(0,n_s): # Loops through samples
        if s == 2:      # Forces code over sample 3 as it failed tests
            continue
        samplename = "S" + str(s+1) + "_"
        ch = testparam[s][0]
        time_start = rdata[s][0,0]
        
        time = np.subtract(rdata[s][:,0],time_start)
        resistance = rdata[s][:,ch]
        
        # Resistance plots        
        ax1.plot(time,resistance,
                 ls = "-",
                 label="S"+str(s+1))
        
              
    # Legend Formating    
    fig.legend(bbox_to_anchor=(0.05, 1.02, 1, 0.2),
                loc="lower left", 
                borderaxespad=0,
                ncol=7)   
        
    fig.savefig(savepath + "\\Plots\\FvD\\" + "FvD_comb_plot.png", bbox_inches='tight', pad_inches=0.1)      
   
    plt.close() 
  
#----------------------------------------------------

#====================================================
# Displacement vs Time Plots
#====================================================

def DvT_plot(time,disp_in,samplename,savepath,stylepath=BaseStylePath):
    """
    This FUNCTION takes raw resistance and force data and plots them against time.

    INPUT:
        rdata       ->      [Array]
                            1D Array of resistance values in [ohms]
                            
        fdata       ->      [Array]
                            1D Array of force values in [N]
                                    
        samplename  ->      [String]
                            Name that the plot will be saved under
        savepath    ->      [String]
                            File path to directory for this to be saved under                            
    OUTPUT:
        Saves a png plot showing resisitance over time and force over time.
    """
    # Set plt style to custom template
    plt.style.use(stylepath)    
    
    # Setup figures
    fig, ax = plt.subplots(layout='constrained')   # Initiate figure and first axis (plot)
    
    # Plot Formating
    ax.set_ylabel("Displacement [$mm$]") 
    ax.set_xlabel("Time [$s$]") 
    ax.set_ymargin(0.2)             
         
    # Force Plot
    ax.plot(time,disp_in,                       
                    color = 'b',
                    ls = '-', 
                    markerfacecolor = 'b',
                    markeredgecolor = 'b',
                    label = "Displacement")
        
    fig.savefig(savepath + "\\Plots\\DvT\\" + samplename + "_DvT_plot.png", bbox_inches='tight', pad_inches=0.1)      
    
    plt.close()     


#====================================================
# Force vs Displacement vs Time Plots
#====================================================    

#----------------------------------------------------

def FvDvT_comb_plot(data,savepath,stylepath=BaseStylePath):
    """
    This FUNCTION takes raw resistance and force data and plots them against time.

    INPUT:
        rdata       ->      [Array]
                            1D Array of resistance values in [ohms]
                            
        fdata       ->      [Array]
                            1D Array of force values in [N]
                                    
        samplename  ->      [String]
                            Name that the plot will be saved under
        savepath    ->      [String]
                            File path to directory for this to be saved under                            
    OUTPUT:
        Saves a png plot showing resisitance over time and force over time.
    """
    # Set plt style to custom template
    plt.style.use(stylepath)    
    
    # Setup figures
    fig, ax1 = plt.subplots(layout='constrained')   # Initiate figure and first axis (plot)
    ax2 = ax1.twinx()                               # Initiate a 2nd axis that shares the same x-axis  
    
    # Plot Formating
    ax1.set_xlabel("Time [$s$]")                                    # ax1 x-axis label
    ax2.set_ylabel("Applied Force [$N$]")                           # ax2 y-axis label 
    #ax1.set_ylim(ymin = -150, ymax = 1000)                         # ax1 y-axislimits
    ax1.set_ymargin(0.2)                                            # Axis margins (gives padding around edges based on multiplier)
    ax1.set_ylabel("Displacement [$mm$]")                           # ax1 y-axis label
    #ax2.set_ylim(ymin = -10, ymax = 260)                           # ax2 y-axis limits
        
    # Set the ax2 plot into the background
    ax1.set_zorder(ax2.get_zorder()+1)
    ax1.set_frame_on(False)    
    
   
    # Plots
    for s in data: # Loops through samples

        samplename = "S" + str(s+1)
        
        time    = data[s]['Elapsed Time ']
        disp    = data[s]['Disp     ']

        # Displacement Plots
        ax1.plot(time,disp,                       
                    ls = '--', 
                    label = samplename)
    
    # Force Plot
    force   = data[s]['Load   ']
    ax2.plot(time,force,
                color = 'k',
                markerfacecolor = 'k',
                markeredgecolor = 'k',
                ls = "-",
                label = "Force")    

        
              
    # Legend Formating    
    fig.legend(bbox_to_anchor=(0.05, 1.02, 1, 0.2),
                loc="lower left", 
                borderaxespad=0,
                ncol=8)   
        
    fig.savefig(savepath + "\\Plots\\FvDvT\\" + "FvDvT_comb_plot.png", bbox_inches='tight', pad_inches=0.1)      
    
    plt.close() 
    