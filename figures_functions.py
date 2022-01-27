import matplotlib.pyplot as plt
import powerlaw
import powerlaw
from powerlaw import plot_pdf, Fit
import json
import numpy as np

st_parameters = {
"xylabel_size":14, 
"xyticks_size": 12,
"legend_size":12,
"title_size":16,
"line_w":3,
    
}
   
def plot_data_fit(data, xlabel, ylabel, fitting="lognormal", tip="data", color="red"):
    
   
    data = [x for x in data if x>0]
    plot_pdf(data, linestyle=':',linewidth=st_parameters["line_w"]+2, label=tip, color=color)
    
    fit = Fit(data, xmin=min(data), discrete=False)
    
    if fitting=='powerlaw':
        fit.power_law.plot_pdf( linestyle='--', color=color, label = '%s-power-law'%tip)
    elif fitting=='lognormal':
        fit.lognormal.plot_pdf( linestyle='--', linewidth=st_parameters["line_w"], color=color, label = 'lognormal fit')
        #print(fit.lognormal.mu, fit.lognormal.sigma)
    elif fitting =='pl+ln':
        fit.power_law.plot_pdf( linestyle='--',color=color, label = '%s-power-law'%tip,)
        fit.lognormal.plot_pdf( linestyle='-', color=color, label = '%s-lognormal'%tip)
            
    plt.xlabel(xlabel, fontsize=st_parameters["xylabel_size"])
    plt.ylabel(ylabel, fontsize=st_parameters["xylabel_size"])
    plt.xticks(fontsize=st_parameters["xyticks_size"])
    plt.yticks(fontsize=st_parameters["xyticks_size"])
    plt.legend(ncol=1, fontsize=st_parameters["legend_size"], frameon=False)
    
def plot_line(data, xlabel, ylabel, color, label):
    
    plt.plot(data, lw=st_parameters["line_w"], color=color, label=label)
    
    plt.xlabel(xlabel, fontsize=st_parameters["xylabel_size"])
    plt.ylabel(ylabel, fontsize=st_parameters["xylabel_size"])
    plt.xticks(fontsize=st_parameters["xyticks_size"])
    plt.yticks(fontsize=st_parameters["xyticks_size"])
    
def plot_rate_size(data, xlabel, ylabel, color):
    
    plt.plot(data[:,0],data[:,1], '.', lw=st_parameters["line_w"], color=color)
    
    plt.xlabel(xlabel, fontsize=st_parameters["xylabel_size"])
    plt.ylabel(ylabel, fontsize=st_parameters["xylabel_size"])
    plt.xticks(fontsize=st_parameters["xyticks_size"])
    plt.yticks(fontsize=st_parameters["xyticks_size"])
    #plt.legend(ncol=1, fontsize=st_parameters["legend_size"], frameon=False)
    plt.xscale('log')
    

def plot(dictionary, keymin, keymax, xlabel, ylabel, color_dict):
    
    keys = sorted([int(x) for x in list(dictionary.keys())])
    
    for key in keys:
    
        if int(key)>=keymin and int(key)<=keymax:

            data = dictionary[str(key)]
            data = [x for x in data if x>0]
            plot_pdf(data, linestyle=':',linewidth=st_parameters["line_w"]+2, label=key, )#color=color_dict[str(key)])
            
    plt.xlabel(xlabel, fontsize=st_parameters["xylabel_size"])
    plt.ylabel(ylabel, fontsize=st_parameters["xylabel_size"])
    plt.xticks(fontsize=st_parameters["xyticks_size"])
    plt.yticks(fontsize=st_parameters["xyticks_size"])
    plt.legend(ncol=5, fontsize=st_parameters["legend_size"], bbox_to_anchor=(2, -0.3), frameon=False)
    #plt.legend(ncol=5, fontsize=12, bbox_to_anchor=(2, -0.3), frameon=False)
    
def plot_data_model(data, model, xlabel, ylabel, color):
    
    data = [x for x in data if x>0]
    model_p = [x for x in model[0] if x>0]
    
    plot_pdf(data, linestyle=":", linewidth=st_parameters["line_w"]+2, label="data", color=color)
    plot_pdf(model_p, linestyle='--',color=color, lw=st_parameters["line_w"], label = "pa=%s\n pg=%s\n paff=%s"%(model[1][0], model[1][1], model[1][2]))
    
    plt.xlabel(xlabel, fontsize=st_parameters["xylabel_size"])
    plt.ylabel(ylabel, fontsize=st_parameters["xylabel_size"])
    plt.xticks(fontsize=st_parameters["xyticks_size"])
    plt.yticks(fontsize=st_parameters["xyticks_size"])
    
    plt.legend(ncol=1, fontsize=st_parameters["legend_size"], frameon=False)
    
    

    
def plot_sizes_rates_in_row(data, year1, year2, color_dict):

    lab = {"cityLondon": "Meetup: London", "cityNY": "Meetup: New York", "reddit2017": "Subreddits", "reddit2012": "Subreddits",  "reddit2012a": "Subreddits"}
    xlab = {"sizes": r"$Size/Size_0$", "logrates": r"$Lograte/Lograte_0$"}
    ylab = {"sizes": r"$P(Size/Size_0)$", "logrates": r"$P(Lograte/Lograte_0)$"}

    parameters = list(data.keys())

    plt.figure(figsize = (10, 6))
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.4, hspace=0.4)
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

            plot(dictionary, year1, year2, xlabel, ylabel, color_dict )
            if i!=5:
                 plt.legend().set_visible(False)
            
            if i<4:
                plt.title(lab[category], fontsize=st_parameters["title_size"])

            i+=1


    
def plot_statistics_row(data, color_dict):

    lab = {"cityLondon": "Meetup: London", "cityNY": "Meetup: New York", "reddit2017": "Subreddits", "reddit2012": "Subreddits",  "reddit2012a": "Subreddits"}
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
                plt.title(lab[category], fontsize=st_parameters["title_size"])
            
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
                    plot_line(dictionary, xlab[param], ylabel, color_dict[category], "")
                else:
                    if param=="rate_size":
                        plot_rate_size(dictionary, xlab[param], ylabel, color=color_dict[category])
                    
          
            i+=1
            

def plot_model_and_data_row(data_dict, color_dict):


    plt.figure(figsize=(10, 7))
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.4, hspace=0.4)

    lab = {"cityLondon": "Meetup: London", "cityNY": "Meetup: New York", "reddit2017": "Subreddits", 
           "reddit2012": "Subreddits",  "reddit2012a": "Subreddits"}
    xlab = {"sizes": r"$Size/Size_0$", "logrates": r"$Lograte/Lograte_0$", "newusers":"time(months)"}
    ylab = {"sizes": r"$P(Size/Size_0)$", "logrates": r"$P(Lograte/Lograte_0)$", "newusers": "New users"}
    i=1


    param = "sizes"
    data_s = data_dict["%s_data"%param]
    data_m = data_dict["%s_model"%param]
    comms = list(data_s.keys())
    for comm in comms:
        plt.subplot(2, 3, i)
        

        xlabel=xlab[param]
        if i==1:
            ylabel=ylab[param]
        else:
            ylabel=""
        plot_data_model(data_s[comm], data_m[comm], xlabel, ylabel, color_dict[comm])
        plt.title(lab[comm], fontsize=st_parameters["title_size"])
        i+=1

    param = "logrates"
    data_s = data_dict["%s_data"%param]
    data_m = data_dict["%s_model"%param]
    comms = list(data_s.keys())
    for comm in comms:
        plt.subplot(2, 3, i)
        xlabel=xlab[param]
        if i==4:
            ylabel=ylab[param]
        else:
            ylabel=""
        plot_data_model(data_s[comm], data_m[comm], xlabel, ylabel, color_dict[comm])
        i+=1
        
        
def plot_time_series(data_dict, color_dict):


    plt.figure(figsize=(10, 9))
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.4, hspace=0.4)

    lab = {"cityLondon": "Meetup: London", "cityNY": "Meetup: New York", "reddit2017": "Subreddits", 
           "reddit2012": "Subreddits",  "reddit2012a": "Subreddits"}
    xlab = {"sizes": r"$Size/Size_0$", "logrates": r"$Lograte/Lograte_0$", "newusers":"time(months)", 
            "oldusers_totalusers":"time(months)", "newgroups_activeusers":"time(months)"}
    ylab = {"sizes": r"$P(Size/Size_0)$", "logrates": r"$P(Lograte/Lograte_0)$", "newusers": "New users", 
            "oldusers_totalusers":"Old users/Total users", "newgroups_activeusers":"New groups/Active users"}
    i=1

    param = "newusers"
    data_s = data_dict[param]
    comms = list(data_s.keys())

    for comm in comms:
        plt.subplot(3, 3, i)

        xlabel= ""
        if i==1:
            ylabel=ylab[param]
        else:
            ylabel=""

        plot_line(data_s[comm], xlabel, ylabel, color_dict[comm], "")
        plt.title(lab[comm], fontsize=st_parameters["title_size"])
        i+=1
        
    param = "oldusers_totalusers"
    data_s = data_dict[param]
    comms = list(data_s.keys())

    for comm in comms:
        plt.subplot(3, 3, i)

        xlabel=""
        if i==4:
            ylabel=ylab[param]
        else:
            ylabel=""
        med = np.median(data_s[comm])
        plot_line(data_s[comm], xlabel, ylabel, color_dict[comm], "pa = %.2f"%med)
        plt.legend(fontsize=st_parameters["legend_size"],  frameon=False)

       
        i+=1
        
    param = "newgroups_activeusers"
    data_s = data_dict[param]
    comms = list(data_s.keys())

    for comm in comms:
        plt.subplot(3, 3, i)

        xlabel=xlab[param]
        if i==7:
            ylabel=ylab[param]
        else:
            ylabel=""
        med = np.median(data_s[comm].dropna())
        print(med)
        
        plot_line(data_s[comm], xlabel, ylabel, color_dict[comm], "pg = %.3f"%med)
        plt.legend(fontsize=st_parameters["legend_size"],  frameon=False)
       
        i+=1