function colors(path) 
    f = io.open(path, "r")
    if not f then return {} end
    colors = {}
    for l in f:lines() do 
        for k, v in l:gmatch("(%w+)%s*=%s*(%w+)") do
            colors[k] = v
        end
    end
    f:close()
    return colors
end