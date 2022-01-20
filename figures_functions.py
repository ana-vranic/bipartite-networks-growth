import matplotlib.pyplot as plt
import powerlaw
import matplotlib.pyplot as plt
import powerlaw
from powerlaw import plot_pdf, Fit
import json

            
def plot_data_fit(data, xlabel, ylabel, fitting="lognormal", tip="data", color="red"):
    
   
    data = [x for x in data if x>0]
    plot_pdf(data, linestyle=':',linewidth=5, label=tip, color=color)
    
    fit = Fit(data, xmin=min(data), discrete=False)
    
    if fitting=='powerlaw':
        fit.power_law.plot_pdf( linestyle='--', color=color, label = '%s-power-law'%tip)
    elif fitting=='lognormal':
        fit.lognormal.plot_pdf( linestyle='--', linewidth=3, color=color, label = 'lognormal fit')
        #print(fit.lognormal.mu, fit.lognormal.sigma)
    elif fitting =='pl+ln':
        fit.power_law.plot_pdf( linestyle='--',color=color, label = '%s-power-law'%tip,)
        fit.lognormal.plot_pdf( linestyle='-', color=color, label = '%s-lognormal'%tip)
            
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(ncol=1, fontsize=12, frameon=False)
    
def plot_line(data, xlabel, ylabel, color):
    
    plt.plot(data, lw=3, color=color)
    
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    #plt.legend(ncol=1, fontsize=12)
    
def plot_rate_size(data, xlabel, ylabel, color):
    
    plt.plot(data[:,0],data[:,1], '.', lw=3, color=color)
    
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    #plt.legend(ncol=1, fontsize=12)
    plt.xscale('log')
    

def plot(dictionary, keymin, keymax, xlabel, ylabel):
    
    keys = sorted([int(x) for x in list(dictionary.keys())])
    
    for key in keys:
    
        if int(key)>=keymin and int(key)<=keymax:

            data = dictionary[str(key)]
            data = [x for x in data if x>0]
            plot_pdf(data, linestyle=':',linewidth=5, label=key)
            
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(ncol=5, fontsize=12, bbox_to_anchor=(2, -0.3), frameon=False)
    
    
def plot_sizes_rates_in_row(data, year1, year2):

    lab = {"cityLondon": "Meetup: London", "cityNY": "Meetup: New York", "reddit2017": "Subreddits", "reddit2012": "Subreddits",}
    xlab = {"sizes": r"$Size/Size_0$", "logrates": r"$Lograte/Lograte_0$"}
    ylab = {"sizes": r"$P(Size/Size_0)$", "logrates": r"$P(Lograte/Lograte_0)$"}

    parameters = list(data.keys())

    plt.figure(figsize = (10, 6))
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.3, hspace=0.3)
    i = 1
    for param in parameters:

        communities = list(data[param].keys())
        xlabel = xlab[param]; 
        for category in communities:

            plt.subplot(2,3,i)

            dictionary = data[param][category]

            if i==1 or i==4:
                ylabel = ylab[param]
            else:
                ylabel = ""

            plot(dictionary, year1, year2, xlabel, ylabel )
            if i!=5:
                 plt.legend().set_visible(False)
            
            if i<4:
                plt.title(lab[category], fontsize=16)

            i+=1
            
            
def plot_sizes_rates_in_column(data, year1, year2):

    lab = {"cityLondon": "Meetup: London", "cityNY": "Meetup: New York", "reddit2017": "Subreddits", "reddit2012": "Subreddits",}
    xlab = {"sizes": r"$Size/Size_0$", "logrates": r"$Lograte/Lograte_0$"}
    ylab = {"sizes": r"$P(Size/Size_0)$", "logrates": r"$P(Lograte/Lograte_0)$"}

    parameters = list(data.keys())
    communities = list(data[parameters[0]].keys())

    plt.figure(figsize = (10, 12))
    i = 1
    for category in communities:
        for param in parameters:

            communities = list(data[param].keys())
             
            plt.subplot(3,2,i)

            dictionary = data[param][category]
            
            if i> 4:
                xlabel = xlab[param]
            else:
                xlabel= ""
  
            ylabel = ylab[param]
            plot(dictionary, year1, year2, xlabel, ylabel)
            if i==1 or i==3 or i==5:
                plt.title(lab[category], fontsize=20, y=0.26, x =-0.2, rotation = 90)

            i+=1
            

    
def plot_statistics_row(data, color_dict):

    lab = {"cityLondon": "Meetup: London", "cityNY": "Meetup: New York", "reddit2017": "Subreddits", "reddit2012": "Subreddits"}
    xlab = {"p_sizes": r"$Size$", "p_logrates": r"$Lograte$", "Ngroups":"Time(months)", "rate_size": "Size"}
    ylab = {"p_sizes": r"$P(Size)$", "p_logrates": r"$P(Lograte)$", "Ngroups":"N groups", "rate_size":"LogRate"}

    parameters = list(data.keys())

    plt.figure(figsize = (10, 12))
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.4, hspace=0.4)
    i = 1
    
    for param in parameters:

        communities = list(data[param].keys())
        for category in communities:
            plt.subplot(4,3,i)
            if i<4: 
                plt.title(lab[category], fontsize=16)
            
            dictionary = data[param][category]
            
            if i==1 or i==4 or i==7 or i==10:
                ylabel=ylab[param]
            else:ylabel = " "
            
            
            if param[0]=="p":
                plot_data_fit(dictionary, xlab[param], ylabel, color=color_dict[category])
                if (i!=4) and (i!=7):
                    plt.legend().set_visible(False)
                    
            else:
                if param=="Ngroups":
                    plot_line(dictionary, xlab[param], ylabel, color=color_dict[category])
                else:
                    if param=="rate_size":
                        plot_rate_size(dictionary, xlab[param], ylabel, color=color_dict[category])
                    
          
            i+=1
