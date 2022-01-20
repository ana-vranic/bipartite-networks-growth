using HDF5


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


input = ARGS[1] #hdf5 filename
output_fname = ARGS[2] #this is txt file to save rates
output_fname_l = ARGS[3] #logrates
nsamples = parse(Int64, ARGS[4])

merge_rates = []
for i in 1:nsamples
   input_fname = "$(input)_$(i).h5py"
   g = export_groups(input_fname)
   rates = get_rates(g)
   #global merge_rates = cat(1, merge_rates, rates)
   append!(merge_rates, rates)
end



open(output_fname,"w") do io
    for line in merge_rates
        println(io, line)
    end
   
end

lr = [log(x) for x in merge_rates]

open(output_fname_l,"w") do io
    for line in lr
        println(io, line)
    end

end

