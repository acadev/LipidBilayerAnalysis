'''
A set of functions to generate plots/figures from the lipid bilayer analysis outputs.
These functions use matplotlib (http://matplotlib.org/index.html) along with Seaborn (
https://stanford.edu/~mwaskom/software/seaborn/index.html). 

'''
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import numpy as np


# the default savefig params can be different from the display params
# e.g., you may want a higher resolution, or to make the figure
# background white
sfig_params = { 
    'savefig.dpi' : 300,
    'savefig.format' : 'eps'
    }
mpl.rcParams.update(sfig_params)
params = {'figure.figsize': [6.0, 4.0]}
mpl.rcParams.update(params)
#sns.set_style("whitegrid")
#sns.set_style("white")
#sns.set(context="paper", font="monospace")
sns.set_style("ticks")



def plot_step_vectors(vectors, colors=None, filename='step_vectors.eps',show=False):
    '''
    Generates a single plot with the lipid displacement vectors (or step vectors)
    Takes a single frame of the output from:
        MemSys.StepVector
    Corresponding colors (if multiple lipid types are included) can be 
    generated using:
        MemSys.StepVectorColors
    '''
    sns.set_style("whitegrid")
    x = vectors[:,0]
    y=vectors[:,1]
    vx = vectors[:,2]
    vy = vectors[:,3]
    step_vec_plot = plt.figure()
    if colors is not None:
        plt.quiver(x,y,vx,vy,color=colors)
    else:
        plt.quiver(x,y,vx,vy)
    #plt.title('Lateral Displacement Vectors')
    plt.savefig(filename)
    if show:
        return plt.show()
    return

def plot_msd(msd_dat_list,name_list=None,filename='msd.eps',time_in='ps',time_out='ns',show=False):
    '''
    Generates a single plot with Mean Squared Displacement curves
    Takes outputs from:
        MemSys.CalcMSD 
        MemSys.CalcMSD_parallel
    The outputs are passed to function in a list input: apl_dat_list
    '''
#    params = {
#    'axes.labelsize': 20,
#    'text.fontsize': 20,
#    'legend.fontsize': 20,
#    'xtick.labelsize': 16,
#    'ytick.labelsize': 16,
#    'text.usetex': False,
#    'figure.figsize': [8.0, 6.0]
#    }
#    params = {'figure.figsize': [10.0, 8.0]}
#    mpl.rcParams.update(params)
#        
    i = 0
    for msd_dat in msd_dat_list:
        msd_d = msd_dat.copy()
        t = msd_d[:,0]
        if time_in == 'ps' and time_out == 'ns':
            t/=100.0
        elif time_in == 'ns' and time_out == 'ps':
            t*=100.0
        msd = msd_d[:,1]
        if name_list is not None:
            plt.plot(t, msd, linewidth=2.0,label=name_list[i])
        else:
            plt.plot(t, msd, linewidth=2.0)
        i+=1
        #plt.title("Mean Sqared Displacement vs. Time")
    xlabel = "Time ("+time_out+")"
    plt.xlabel(xlabel)
    plt.ylabel("Distance in XY plane ($\AA^2$)")
    if name_list is not None:
        plt.legend(loc=2)
        
    plt.savefig(filename)
    if show:
        return plt.show()
    return


def plot_area_per_lipid(apl_dat_list,name_list=None,filename='apl.eps',time_in='ps',time_out='ns',show=False):
    '''
    Generates a single plot with area per lipid (apl) curves
    Takes outputs from:
        MemSys.CalcAreaPerLipid_Box 
        MemSys.CalcAreaPerLipid_ClosestNeighborCircle
    The outputs are passed to function in a list input: apl_dat_list
    '''
    i = 0
    for apl_dat in apl_dat_list:
        apl_d = apl_dat.copy()
        t = apl_d[:,0]
        if time_in == 'ps' and time_out == 'ns':
            #print "switching time units from ps to ns"
            t/=100.0
        elif time_in == 'ns' and time_out == 'ps':
            t*=100.0
        apl = apl_d[:,2]
        apl_dev = apl_d[:,3]
        if name_list is not None:
            print "plotting",name_list[i]," with errorbars"
            print t
            print apl
            plt.errorbar(t, apl, yerr=apl_dev,linewidth=2.0,label=name_list[i])
        else:
            plt.errorbar(t, apl, yerr=apl_dev,linewidth=2.0)
        i+=1
        #plt.title("Mean Sqared Displacement vs. Time")
    xlabel = "Time ("+time_out+")"
    plt.xlabel(xlabel)
    plt.ylabel("Area per lipid ($\AA^2$)")
    if name_list is not None:
        plt.legend(loc=2)
        
    plt.savefig(filename)
    if show:
        return plt.show()
    return


def plot_cluster_dat_number(clust_dat_list,name_list=None,filename='clust_number.eps',time_in='ps',time_out='ns',show=False):
    '''
    Generates a single of the average number of clusters (vs. time)
    using output data from:
        MemSys.CheckClustering     
    The outputs are passed to function in a list input: clust_dat_list
    '''
    i = 0
    for cl_dat in clust_dat_list:
        cl_loc = cl_dat.copy()
        t = cl_loc[:,0]
        if time_in == 'ps' and time_out == 'ns':
            #print "switching time units from ps to ns"
            t/=100.0
        elif time_in == 'ns' and time_out == 'ps':
            t*=100.0
        cl = cl_loc[:,5]
        cl_dev = cl_loc[:,6]
        if name_list is not None:
            #print "plotting",name_list[i]," with errorbars"
            #print t
            #print apl
            plt.errorbar(t, cl, yerr=cl_dev,linewidth=2.0,label=name_list[i])
        else:
            plt.errorbar(t, cl, yerr=cl_dev,linewidth=2.0)
        i+=1
        #plt.title("Mean Sqared Displacement vs. Time")
    xlabel = "Time ("+time_out+")"
    plt.xlabel(xlabel)
    plt.ylabel("Average Number of Clusters")
    if name_list is not None:
        plt.legend(loc=2)
        
    plt.savefig(filename)
    if show:
        return plt.show()
    return

def plot_cluster_dat_size(clust_dat_list,name_list=None,filename='clust_size.eps',time_in='ps',time_out='ns',show=False):
    '''
    Generates a single plot of the average cluster size (vs time)
    using output data from:
        MemSys.CheckClustering     
    The outputs are passed to function in a list input: clust_dat_list
    '''
    i = 0
    for cl_dat in clust_dat_list:
        cl_loc = cl_dat.copy()
        t = cl_loc[:,0]
        if time_in == 'ps' and time_out == 'ns':
            #print "switching time units from ps to ns"
            t/=100.0
        elif time_in == 'ns' and time_out == 'ps':
            t*=100.0
        cl = cl_loc[:,7]
        cl_dev = cl_loc[:,8]
        if name_list is not None:
            #print "plotting",name_list[i]," with errorbars"
            #print t
            #print apl
            plt.errorbar(t, cl, yerr=cl_dev,linewidth=2.0,label=name_list[i])
        else:
            plt.errorbar(t, cl, yerr=cl_dev,linewidth=2.0)
        i+=1
        #plt.title("Mean Sqared Displacement vs. Time")
    xlabel = "Time ("+time_out+")"
    plt.xlabel(xlabel)
    plt.ylabel("Average Size of Cluster (lipids per cluster)")
    if name_list is not None:
        plt.legend(loc=2)
        
    plt.savefig(filename)
    if show:
        return plt.show()
    return


def plot_cluster_maps(clusters, filename='cluster_map.png',show=False):
    '''
    Generates a single plot of the lipid cluster map 
    Takes a single frame of the output from:
        MemSys.ExportClustersForPlotting
    '''
    sns.set_style("whitegrid")
    x = clusters[0]
    y=clusters[1]
    c = clusters[2]
    plt.scatter(x,y,c=c,s=800)
    #plt.title('Lateral Displacement Vectors')
    plt.savefig(filename)
    if show:
        return plt.show()
    return

