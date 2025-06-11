#===============================================================================================
# Data Processing Functions
#===============================================================================================

# Imported Libraries
import numpy as np
import pandas as pd

#===============================================================================================
# Extraction Functions
#===============================================================================================

def B1Feather_DataExtract(filepath):
    """
    This FUNCTION extracts CSV data outputed from feather board #1 into float 
    arrays separated by channel within a dictionary. Calibrates resistance readings also.

    INPUT:
        filepath (script)       ->      Raw Script of filepath of text file
                                                Value:  File path of the file to be processed

    OUTPUT:
        data_out (Array)        ->      Array containing data from file
                                            Key: (n,ch) 
                                                - n  = n'th timestep
                                                - ch = channel #
    """
    with open(filepath) as f:
        file = list(f)       # Import data from file
        del file[-1]         # Delete last row to avoid junk (sometimes a row will be cut mid line when shutting down)
        del file[0]          # Delete first row to avoid headers
        
        
            
        # Initialize data
        #data = {} # Dictionary containing output data
        i = 0     # Data line count
        n_dt = len(file)    # Number of data points in file 
        n_ch = 5            # Number of channels
        data = np.zeros([n_dt,n_ch])
        
        
        for line in file:  
            
            fields = line.split(",")        # Takes current line and splits it into the different channels
                        
            # Extract data from each line
            data[(i,0)]   =   (float(fields[0]) / 1000)   # Channel 0 - Time
            data[(i,1)]   =   float(fields[1])            # Channel 1 - Resistance
            data[(i,2)]   =   float(fields[2])            # Channel 2 - Resistance
            data[(i,3)]   =   float(fields[3])            # Channel 3 - Resistance
            data[(i,4)]   =   float(fields[4])            # Channel 4 - Resistance

            # Apply Feather Board calibration
            data[(i,1)]   =   (-0.00005)*(data[(i,1)])**2 + (1.0496)*(data[(i,1)]) - (7.0071)
            data[(i,2)]   =   (data[(i,2)])
            data[(i,3)]   =   (-0.00001)*(data[(i,3)])**2 + (1.0139)*(data[(i,3)]) - (0.634)
            data[(i,4)]   =   (data[(i,4)])      
            
            i += 1
        
    return data

#-----------------------------------------------------------------------------------------------

def B2Feather_DataExtract(filepath):
    """
    This FUNCTION extracts CSV data outputed from feather board #2 into float 
    arrays separated by channel within a dictionary. Calibrates resistance readings also.

    INPUT:
        filepath (script)       ->      Raw Script of filepath of text file
                                                Value:  File path of the file to be processed

    OUTPUT:
        data_out (Array)        ->      Array containing data from file
                                            Key: (n,ch) 
                                                - n  = n'th timestep
                                                - ch = channel #
    """
    with open(filepath) as f:
        file = list(f)       # Import data from file
        del file[-1]         # Delete last row to avoid junk (sometimes a row will be cut mid line when shutting down)
        del file[0]          # Delete first row to avoid headers
        
        
            
        # Initialize data
        #data = {} # Dictionary containing output data
        i = 0     # Data line count
        n_dt = len(file)    # Number of data points in file 
        n_ch = 5            # Number of channels
        data = np.zeros([n_dt,n_ch])
        
        
        for line in file:  
            
            fields = line.split(",")        # Takes current line and splits it into the different channels
                        
            # Extract data from each line
            data[(i,0)]   =   (float(fields[0]) / 1000)   # Channel 0 - Time
            data[(i,1)]   =   float(fields[1])            # Channel 1 - Resistance
            data[(i,2)]   =   float(fields[2])            # Channel 2 - Resistance
            data[(i,3)]   =   float(fields[3])            # Channel 3 - Resistance
            data[(i,4)]   =   float(fields[4])            # Channel 4 - Resistance

            # Apply Feather Board calibration
            data[(i,1)]   =   (-0.000006)*(data[(i,1)])**2 + (1.0267)*(data[(i,1)]) + (-14.281)
            data[(i,2)]   =   (data[(i,2)])
            data[(i,3)]   =   (-0.00001)*(data[(i,3)])**2 + (1.0139)*(data[(i,3)]) - (0.634)
            data[(i,4)]   =   (data[(i,4)])      
            
            i += 1
        
    return data

#-----------------------------------------------------------------------------------------------

def DMA_Extract_TF(filepath):          
    """_summary_
    FUNCTION that extracts data from DMA output CSV files into float arrays stored within a dictionary
    Data from DMA -> Time, and force

    INPUT:
        filepath    ->      Type:   Raw Script
                            Value:  File path of the file to be processed

    OUTPUT:
        data        ->      Type: Pandas Dataframe
                            Key: Data ['Points','Elapsed Time ', 'Load   ']
    """
    
    cols = ['Points','Elapsed Time ','Load   ']     # Define column names
    file = pd.read_csv(filepath,usecols=cols)
    
    data = file.dropna()    # Removes empty cells
    
    def signflip(inp):      # Define a function to flip the sign on data
        return inp*-1
    
    newforce = data['Load   ']                     # Extract load values from dataframe
    newforce = newforce.apply(signflip)       # Apply sign flip to all values in new force
    data.update(newforce)                    # Insert modified values back into original dataframe
    
    '''
    with open(filepath) as f:
        file = list(f)      # Import data from file
        n = np.size(file)    # Get length of file
            
        # Initialize data
        time    =   np.zeros(n)
        c1      =   np.zeros(n)
        i       =   0       
        
        for line in file:  # Parse through each line in file
            if not line.strip():    # Skips over any empty lines
                continue
            else:
                fields = line.split() # Takes current line and splits it into the different channels
                        
                time[i]    =   float(fields[0])
                c1[i]      =   float(fields[1])
        
                i += 1    
    
    # Dictionary storage
    data = {
        1 : time,
        2 : c1
    }
    '''
    
    return data

#-----------------------------------------------------------------------------------------------

def DMA_Extract_TFD(filepath):          
    """
    FUNCTION that extracts data from DMA output CSV files into float arrays stored within a dictionary.
    Data from DMA -> Time, Displacement, and force

    INPUT:
        filepath    ->      Type:   Raw Script
                            Value:  File path of the file to be processed

    OUTPUT:
        data        ->      Type: Pandas Dataframe
                            Key: Data ['Points','Elapsed Time ', 'Load   ']
    """
    
    cols = ['Points','Elapsed Time ','Disp     ','Load   ']     # Define column names
    file = pd.read_csv(filepath,usecols=cols)
    
    data = file.dropna()    # Removes empty cells
    
    def signflip(inp):      # Define a function to flip the sign on data
        return inp*-1
    
    # Force Data Cleaning
    newforce = data['Load   ']               # Extract load values from dataframe
    newforce = newforce.apply(signflip)      # Apply sign flip to all values in new force
    data.update(newforce)                    # Insert modified values back into original dataframe
    
    # Displacement Data Cleaning
    newdisp = data['Disp     ']         # Extract disp values from df for editiing
    initdisp = newdisp[0]               # Initial Position Value
    newdisp = newdisp.sub(initdisp)     # Subtract out initial value from all entries
    data.update(newdisp)
    
    
    return data

#-----------------------------------------------------------------------------------------------

#===============================================================================================
# Data Processing Functions
#===============================================================================================

def Feather_timefilter(data_in,t_start,duration):
    """
    This FUNCTION takes data and filters out data based on testing start time and test duration
    
    Args:
        data_out (Array)        ->      Array containing data from file
                                            Key: (n,ch) 
                                                - n  = n'th timestep
                                                - ch = channel #    
        t_start (Float)         ->      Start of testing time
        duration (Float)        ->      Duration of test

    Returns:
        data_out (Array)        ->      Array containing data from file
                                            Key: (n,ch) 
                                                - n  = n'th timestep
                                                - ch = channel #    
    """
    
    # Set up
    t_end       = t_start + duration    # Adds the rough amount of time a test takes to the start time
    n_sys       = np.size(data_in,0)    # Number of time steps
    n_ch        = 5                     # Number of channels
    
    # Initialize 
    i = 0
    data_tmp = np.zeros([n_sys,n_ch])
    
    # Extract relevant data
    for n in range(0,n_sys):
        t_current   = data_in[n,0]    # Takes current steps time
        if t_current >= t_start and t_current <= t_end: # Checks if time is in range
            data_tmp[i,0] = data_in[n,0]  # Channel 0 - Time           
            data_tmp[i,1] = data_in[n,1]  # Channel 1 - Resistance
            data_tmp[i,2] = data_in[n,2]  # Channel 2 - Resistance
            data_tmp[i,3] = data_in[n,3]  # Channel 3 - Resistance
            data_tmp[i,4] = data_in[n,4]  # Channel 4 - Resistance
            i += 1  
    
    # Delete redundant rows of data
    redun = list(range(i,n_sys))
    data_out = np.delete(data_tmp,redun,0)
    
    
    return data_out

#-----------------------------------------------------------------------------------------------

def Feather_cyclecut(data_in,t_start,dur_cycle,cyclecount):
    """
    This FUNCTION takes data from the feather board and seperates the data in each channel by a specified number of cycles
    
    INPUT:
        data_in (Array)                 ->      Array containing data from file
                                                    Key: (n,ch) 
                                                        - n  = n'th timestep
                                                        - ch = channel #    
        t_start (Float)                 ->      Start of testing time
        dur_cycle (Float)               ->      Duration of each cycle
        cyclecount (Float)              ->      Number of cycles

    OUTPUTS:
        data_out (Dictionary)           ->      Dictionary containing modified data from feather
                                                    Key:    (c) 
                                                            - c = Cycle #
                                                    Value:  (n,ch) 
                                                            - n  = n'th timstep
                                                            - ch = channel # 
    """
    n_sys = np.size(data_in,0)                  # Number of time steps
    n_ch  = 5                                   # Number of data channels
    data_out = {}                               # Initialize final data dictionary
        
    for c in range(0,cyclecount):                   # Loop over cycles
        data_tmp = np.zeros([n_sys,n_ch])         # Initialize temp array for storing data into dictionary
        i=0
        cycle_start = t_start + c*dur_cycle 
        cycle_end   = t_start + (c+1)*dur_cycle    
        for n in range(0,n_sys):                    # Loop over data points
            t = data_in[n,0]
            if cycle_start <= t < cycle_end:        # Check if time is within a cycle 
                data_tmp[i,0] = data_in[n,0]   # Channel 0 - Time
                data_tmp[i,1] = data_in[n,1]   # Channel 1 - Resistance
                data_tmp[i,2] = data_in[n,2]   # Channel 2 - Resistance
                data_tmp[i,3] = data_in[n,3]   # Channel 3 - Resistance
                data_tmp[i,4] = data_in[n,4]   # Channel 4 - Resistance
                i += 1   
        redun = list(range(i,n_sys))
        
        if np.delete(data_tmp,redun,0).any():
            data_out[c] = np.delete(data_tmp,redun,0)
    
    return data_out

#-----------------------------------------------------------------------------------------------

def Feather_DeltaConvert(data_in):
    """
    This FUNCTION takes data and converts it to change in by taking the difference between each
    entry to its initial entry.

    Args:
        data_in (Array)        ->      Array containing data from file
                                            Key:    (s) Sample #
                                            Value: (n,ch) 
                                                    - n  = timestep
                                                    - ch = channel # (0-5)   
    Returns:
        data_out (Array)        ->      Array containing data from file
                                            key:    (s) Sample #
                                            Value: (n,ch) 
                                                    - n  = timestep
                                                    - ch = channel #    
    """
    # Initialize 
    n_sys = len(data_in)     # Length of input data
    data_out = data_in.copy()               # Initialize dictionary for output data
    initial = {}
        
    # Generate Initial Values
    initial[0] = data_in[0,0]    # Channel 0 - Time
    initial[1] = data_in[0,1]    # Channel 1 - Resistance
    initial[2] = data_in[0,2]    # Channel 2 - Resistance
    initial[3] = data_in[0,3]    # Channel 3 - Resistance
    initial[4] = data_in[0,4]    # Channel 4 - Resistance  
        
    # Take difference of each value to each channel's initial data          
    data_out[:,0] = np.subtract(data_in[:,0], initial[0])  # Channel 0 - Time
    data_out[:,1] = np.subtract(data_in[:,1], initial[1])  # Channel 1 - Resistance
    data_out[:,2] = np.subtract(data_in[:,2], initial[2])  # Channel 2 - Resistance
    data_out[:,3] = np.subtract(data_in[:,3], initial[3])  # Channel 3 - Resistance
    data_out[:,4] = np.subtract(data_in[:,4], initial[4])  # Channel 4 - Resistance
    
    return data_out

#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------