using HDF5

input_fname = ARGS[1] #hdf5 filename
output_fname = ARGS[2] #this is txt file to save sizes

function export_groups(input_fname)
    h5open(input_fname, "r") do file
    lvl1keys = keys(file)
    N = Int((length(lvl1keys))/2)
    global groups = Dict()
    for step in 1:N
        gd = read(file, "group-degree-s$(step)") 
        for i in 1:length(gd)
            if i in keys(groups)
                push!(groups[i], gd[i])
            else
                groups[i]=[gd[i]]
            end
        end
    end
end
    return groups    
end


function get_rates(g)
    rates = []

    for k in keys(g)
        sizes = g[k]
        for i in 1:(length(sizes)-1)
           push!(rates, sizes[i+1]/sizes[i])
        end

    end
    return rates
end 


input_fname = ARGS[1] #hdf5 filename
output_fname = ARGS[2] #this is txt file to save rates

g = export_groups(input_fname)
rates = get_rates(g)

open(output_fname,"w") do io
    for line in rates
        println(io, line)
    end
   
end
