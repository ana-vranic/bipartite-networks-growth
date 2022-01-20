module affmodel
    using Random
    using HDF5
    include("fn_graphs.jl")
    using .graphfn

    function new_users_linking(Vnew::Vector{Int64}, p_gf::Float32, p_gj::Float32, groups::Dict{Int64, Vector{Int64}}, users::Dict{Int64, Vector{Int64}}, network::Dict{Int64,Set{Int64}}, random_linking::String )
        #Vnew_group = []
        l = length(Vnew)
        int = length(groups)
        Vnew_group = zeros(Int64, l)
        for i in 1:l
        #for nuser in Vnew
            nuser = Vnew[i]
            if rand() < p_gf
                gid = int + 1
                int+=1
                #push!(Vnew_group, gid)
                Vnew_group[i] = gid
            else
                if rand() < p_gj
                    friend = collect(network[nuser])[1]
                    friend_groups = users[friend]
                    gid = Random.rand(friend_groups)
                    #push!(Vnew_group, gid)
                    Vnew_group[i] =gid
                else
                    if random_linking=="random"
                        gid = Random.rand(keys(groups))
                    
                        #push!(Vnew_group, gid)
                        Vnew_group[i] = gid
                    else 
                        if random_linking=="preferential"
                            gid = preferential_choice(keys(groups), groups)
                            #push!(Vnew_group, gid)
                            Vnew_group[i] = gid
                        else
                            print("random or preferential")
                        end
                    end 
                       
                end
            end
        end
        return Vnew_group
    end


    function old_users_linking(Vold::Vector{Int64}, p_gf::Float32, p_gj::Float32, users::Dict{Int64, Vector{Int64}}, groups::Dict{Int64, Vector{Int64}}, network::Dict{Int64,Set{Int64}}, random_linking::String)
        l = length(Vold)
        #Vold_groups = []
        Vold_groups = zeros(Int64, l)
        int = length(groups)
        for i in 1:l
            nuser = Vold[i]
        #for nuser in Vold
            if rand() < p_gf
                gid = int + 1
                int += 1
                Vold_groups[i] = gid
                #push!(Vold_groups, gid)
            else
                if rand() < p_gj
                    #old user should have more than one friends
                    gid = affiliation_choice(nuser, network, users)
                    Vold_groups[i] = gid

                else
                    gid = random_choice(nuser, users, groups, random_linking)
                    #push!(Vold_groups, gid) 
                    Vold_groups[i] = gid
                end
            end
        end
        return Vold_groups
    end

    function random_choice(nuser::Int64, users::Dict{Int64, Vector{Int64}}, groups::Dict{Int64, Vector{Int64}}, random_linking::String)
        vuser_groups = users[nuser]
        choose_from = setdiff(Set(keys(groups)), Set(vuser_groups))
        if length(choose_from)>0
            if random_linking=="random"
                gid = Random.rand(choose_from)
            else
                if random_linking=="preferential"
                    gid = preferential_choice(choose_from, groups)
                else 
                println("random linking is random or preferential")   
                end
            end 
        else
            gid = -1
        end
       return gid
    end 

    function choose_group_affiliation(nuser::Int64, network::Dict{Int64,Set{Int64}}, users::Dict{Int64, Vector{Int64}})
        # first collect friends groups
        friends_groups = Int64[]
        vuser_friends = Set(network[nuser])
        vuser_groups = users[nuser]
        for fu in vuser_friends
            append!(friends_groups, users[fu])
        end
        for vg in vuser_groups
            friends_groups = remove!(friends_groups, vg)
        end     
        # if there is any group left we choose from friends groups
        # othervise user wont join any group
        if length(friends_groups)>0
            gid = Random.rand(friends_groups)
        else
            gid = -1
        end
        return gid
    end


    function affiliation_choice(nuser::Int64, network::Dict{Int64,Set{Int64}}, users::Dict{Int64, Vector{Int64}})
        # first collect friends groups
    
        vuser_friends = network[nuser]
        vuser_groups = users[nuser]
        
        friends_groups = Dict{Int64, Int64}()
        
        for fu in vuser_friends
            fug = users[fu]
            for x in fug
                if !(x in vuser_groups)
                    if x in keys(friends_groups)
                        friends_groups[x] +=1
                    else
                        friends_groups[x] = 1
                    end
                end
            end
        end
        
        if length(friends_groups)>0
            
            total_sum = 0
            for (g, v) in friends_groups
                total_sum+=v    
            end
            
            randsum = rand()*total_sum
            lower_b = 0
            gid=-1
            for (key, val) in friends_groups
                gid = key
                upper_b = lower_b+val
                if (randsum > lower_b) && (randsum <= upper_b)
                    break
                else
                    lower_b+=val 
                end
            end  
        else
            gid = -1
        end
            
        return gid  
    end

    
  function preferential_choice(choose_from, groups::Dict{Int64, Vector{Int64}})
        sizes = Dict()
        total_sum = 0
        for g in choose_from
            sizes[g]=length(groups[g])
            total_sum+=length(groups[g])
        end
       randsum = total_sum*rand()
       lower_b = 0
       g=-1
       for (key, val) in sizes
            g = key
            upper_b = lower_b+val
            if (randsum > lower_b) && (randsum <= upper_b)
                break
            else
                lower_b+=val 
            end
        end
       return g
  end

  function remove!(a, item)
        deleteat!(a, findall(x->x==item, a))
  end
    
export new_users_linking, random_choice, old_users_linking

end
