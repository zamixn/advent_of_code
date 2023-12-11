
function file_exists(file)
    local f = io.open(file, "rb")
    if f then f:close() end
    return f ~= nil
end

function splitString(inputString, delimiter)
    local result = {}
    for token in string.gmatch(inputString, "[^" .. delimiter .. "]+") do
        table.insert(result, token)
    end
    return result
end

function max(val1, val2)
    if val1 > val2 then return val1 else return val2 end
end

sum = 0
fileName = "2\\part1\\input.txt"
for lineRaw in io.lines(fileName) do 
    print("line: " .. lineRaw)
    line = lineRaw:gsub("Game ", "")
    colonStart, colonEnd = line.find(line, ":")
    gameId = tonumber(line:sub(0,colonStart - 1))
    content = line:sub(colonStart + 1, #line)
    print(content)
    red = 0
    green = 0
    blue = 0
    games = splitString(content, ";")
    for i, value in ipairs(games) do
        game = value:gsub("%s", "")
        draws = splitString(game, ",")
        for i, value in ipairs(draws) do
            draw = value:gsub("%s", "")
            --print(draw)        
            if string.find(draw, "red") then
                stringVal = draw:gsub("red", "")
                intVal = tonumber(stringVal)
                red = max(red, intVal);
            elseif string.find(draw, "green") then 
                stringVal = draw:gsub("green", "")
                intVal = tonumber(stringVal)
                green = max(green, intVal);
            elseif string.find(draw, "blue") then
                stringVal = draw:gsub("blue", "")
                intVal = tonumber(stringVal)
                blue = max(blue, intVal);
            end
        end

    end
    print('r:', red, 'g:', green, 'b:', blue)
    sum = sum + (red * green * blue)
end

print(sum)

