using DataStructures
using Random
include("fn_graphs.jl")
using .graphfn
include("aff_model_fn.jl")
using .affmodel
include("main_model.jl")
using .model


p_active = parse(Float32, ARGS[1]) #probability of active users
p_gf = parse(Float32, ARGS[2]) #group_formation
p_gj = parse(Float32, ARGS[3]) #group_joining
p_sample = parse(Float32, ARGS[4]) # the size of sample for linking in aff network
random_linking = ARGS[5]
input_file = ARGS[6]
output_name = ARGS[7]
nsamples = parse(Int64, ARGS[8])


# import ts of new users
f = open(input_file)
lines = readlines(f)
steps = length(lines)

ts = zeros(Int64, steps)

for i in 1:steps
    ts[i] = parse(Int32, lines[i])
end

#fname = "London_pactive$(p_active)_pnewgroup$(p_gf)_affjoin$(p_gj)_sample$(p_sample)_r.hdf5"

for i in 1:nsamples
    output_file = "$(output_name)_$(i).h5py"
    @time run_growing_model_ts(p_active, p_gf, p_gj, ts, "True", p_sample, output_file, random_linking)
end
