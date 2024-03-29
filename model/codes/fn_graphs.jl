module graphfn
    using Random
    using HDF5
    using StatsBase

    function add_link!(network::Dict{Int64,Set{Int64}}, u1::Int64, u2::Int64)
        """
        function to add new link in social network
        arguments: network: adj list of social network in form of disctionary
                   u1, u2: nodes to make link between them

        output:
               updated network

        """
        #this function add users u1 and u2 to the affiliation network
        if u1 in keys(network)
            push!(network[u1], u2)
         else
             network[u1]=Set(u2)
         end

         if u2 in keys(network)
             push!(network[u2], u1)
         else
             network[u2]=Set(u1)
         end
    return network
    end

    function add!(users::Dict{Int64, Vector{Int64}}, groups::Dict{Int64, Vector{Int64}}, u::Int64, g::Int64)
        """
        function to add new link in bipartite network
        arguments: users, groups: adj list of bipartite partitions in form of disctionary
                   u, g: user and group id to make link between them

        output:
               updated users and groups

        """
        if u in keys(users)
            push!(users[u], g)
        else
            users[u]=[g]
        end

        if g in keys(groups)
            push!(groups[g], u)
        else
            groups[g]=[u]
        end
    return users, groups
    end 


    function update_dict!(Vnew::Vector{Int64}, Vnew_groups::Vector{Int64}, groups::Dict{Int64, Vector{Int64}}, users::Dict{Int64, Vector{Int64}}, network::Dict{Int64,Set{Int64}})

        """
        for given list of nodes Vnew and choosen groups Vnew_groups, this function update bipartite and social network 
            
        arguments: groups, users, network: adj list of bipartite partitions and social network
                   Vnew: Vector of users
                   Vnew_groups: Vector of groups

        autput:
               updated groups, users, network

        """
        for i in 1:length(Vnew_groups)
            uid = Vnew[i]
            gid = Vnew_groups[i]
            if gid>0
               
                # 
                users, groups = add!(users, groups, uid, gid)
            
                # new user in the group will link with sample of group members 
                users_all = groups[gid]
                if length(users_all)< 25
                    k = length(users_all)
                else
                    k = 25
                end
                users_sample = sample(users_all, k, replace = false)
                #users_sample = sample(users_all, floor(Int, length(users_all)*per_sample), replace = false)
                for ug in users_sample
                    network = add_link!(network, uid, ug)
                end
            
            end
        end
    return users, groups, network

    end

    function get_sizes(groups::Dict{Int64, Vector{Int64}})
        """
        this function takes groups partition, and for each group calculate its size at current timestamp
        """
        #degree of partition 
        #return: vector of degrees
        #size = zeros(Int64, length())
        ll =  sort(collect(keys(groups)))
        sizes = zeros(Int64, length(ll))
        for i in 1:length(ll)
            g = ll[i]
            sizes[i] = length(groups[g])
            #push!(size, length(groups[g]))
        end
        #sizei = [Int(i) for i in sizes]
        return sizes
    end



    function write_in_h5py(fname::String, step::Int64, groups::Dict{Int64, Vector{Int64}}, users::Dict{Int64, Vector{Int64}})
        """
        after aeach timestamp we write sizes of users and groups  in h5py format
        """
        h5open(fname, "cw") do file
            f = get_sizes(users)
            write(file, "user-degree-s$(step)", f)
            ff = get_sizes(groups)
            write(file, "group-degree-s$(step)", ff)
        end
    end 

export add_link!, add!, update_dict!, get_sizes, write_in_h5py

end
