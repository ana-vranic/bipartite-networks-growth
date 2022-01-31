using DataStructures
using Random
include("fn_graphs.jl")
using .graphfn
include("aff_model_fn.jl")
using .affmodel
include("main_model.jl")
using .model


p_a = parse(Float32, ARGS[1]) #probability of active users
p_g = parse(Float32, ARGS[2]) #group_formation
p_aff = parse(Float32, ARGS[3]) #group_joining
random_linking = ARGS[4]

input_file = ARGS[5]
output_name = ARGS[6]
nsamples = parse(Int64, ARGS[7])


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
    @time run_growing_model_ts(p_a, p_g, p_aff, ts, output_file, random_linking)
end
