module model
    using DataStructures
    using Random
    include("fn_graphs.jl")
    using .graphfn
    include("aff_model_fn.jl")
    using .affmodel

    function run_step(p_active::Float32, p_gf::Float32, p_gj::Float32, Nnew_users::Int64, users::Dict{Int64, Vector{Int64}}, groups::Dict{Int64, Vector{Int64}}, network::Dict{Int64,Set{Int64}}, random_linking::String)
            
        """
        this function runs one step of simulation
        """
            nu = length(keys(users))
            Vold = findall(rand(nu) .< p_active)
            # for each user from Vold we pick up group to join according to model
            Vold_groups = old_users_linking(Vold, p_gf, p_gj, users, groups, network, random_linking)
            #update bipartite and affiliation networks
            users, groups, network = update_dict!(Vold, Vold_groups, groups, users, network)

            # first we add new users and link them to random old user
            Vnew = zeros(Int64, Nnew_users)
            for i in 1:Nnew_users
                uid = length(keys(users)) + i
                users_list = keys(users)
                ut = Random.rand(users_list)
                network = add_link!(network, uid, ut)
                Vnew[i] = uid
            end

            # for each user in new Vnew we choose one group to join
            Vnew_groups = new_users_linking(Vnew, p_gf, p_gj, groups, users, network, random_linking)
            #update bipartite and affiliation networks
            users, groups, network = update_dict!(Vnew, Vnew_groups, groups, users, network)

            return users, groups, network
    end

    function initial_configuration()

        """
        before simulation small network with two users is made
        """

        #INITIAL CONFIGURATION
        users = Dict{Int64,Vector{Int64}}()
        groups = Dict{Int64, Vector{Int64}}()
        #initial configuration
        users, groups = add!(users, groups, 1, 1)
        users, groups = add!(users, groups, 2, 2)

        network = Dict{Int64, Set{Int64}}()
        network = add_link!(network, 1, 2)

        return users, groups, network
    end

    function run_growing_model_ts(p_active::Float32, p_gf::Float32, p_gj::Float32, ts::Vector{Int64}, fname::String, random_linking::String)
        """
        this function take time series of new users, model parameters p-active, p-gf, p-gj and run simulation 
        """
        step=1
        users, groups, network = initial_configuration()
        write_in_h5py(fname, step, groups, users)
        
        #println(length(ts))
        for tstp in 1:length(ts)
            #println(tstp)
            Nnew_users = ts[tstp]
            users, groups, network = run_step(p_active, p_gf, p_gj, Nnew_users, users, groups, network, random_linking)
            step+=1
            write_in_h5py(fname, step, groups, users)
        end 
    end
    export run_growing_model_ts
end