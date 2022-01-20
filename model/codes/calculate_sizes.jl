using HDF5

input_fname = ARGS[1] #hdf5 filename
output_fname = ARGS[2] #this is txt file to save sizes

h5open(input_fname, "r") do file
    lvl1keys = keys(file)
    N = Int((length(lvl1keys))/2)
    step = N
    global sizes = read(file, "group-degree-s$(step)")   
end

open(output_fname,"w") do io
    for line in sizes
        println(io, line)
    end
   
end
