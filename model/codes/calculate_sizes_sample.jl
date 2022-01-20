using HDF5

function read_file(input_fname)
   
   h5open(input_fname, "r") do file
       lvl1keys = keys(file)
       N = Int((length(lvl1keys))/2)
       step = N
       global sizes = read(file, "group-degree-s$(step)")   
    end
return sizes
end



input = ARGS[1] #hdf5 filename
output_fname = ARGS[2] #this is txt file to save sizes
nsamples = parse(Int64, ARGS[3])
merge_sizes = []
for i in 1:nsamples
   input_fname = "$(input)_$(i).h5py"
   S = read_file(input_fname)
   #global merge_sizes = cat(1, merge_sizes, S)
   append!(merge_sizes, S)
end


open(output_fname,"w") do io
    for line in merge_sizes
        println(io, line)
    end
end
