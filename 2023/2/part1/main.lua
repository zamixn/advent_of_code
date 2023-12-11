
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


sum = 0
fileName = "2\\part1\\input.txt"
for lineRaw in io.lines(fileName) do 
    print("line: " .. lineRaw)
    line = lineRaw:gsub("Game ", "")
    colonStart, colonEnd = line.find(line, ":")
    gameId = tonumber(line:sub(0,colonStart - 1))
    content = line:sub(colonStart + 1, #line)
    print(content)
    games = splitString(content, ";")
    isGamePossbile = true
    for i, value in ipairs(games) do
        red = 12
        green = 13
        blue = 14
        game = value:gsub("%s", "")
        draws = splitString(game, ",")
        for i, value in ipairs(draws) do
            draw = value:gsub("%s", "")
            --print(draw)        
            if string.find(draw, "red") then
                stringVal = draw:gsub("red", "")
                intVal = tonumber(stringVal)
                red = red - intVal;
            elseif string.find(draw, "green") then 
                stringVal = draw:gsub("green", "")
                intVal = tonumber(stringVal)
                green = green - intVal;
            elseif string.find(draw, "blue") then
                stringVal = draw:gsub("blue", "")
                intVal = tonumber(stringVal)
                blue = blue - intVal;
            end
        end

        if red < 0 or green < 0 or blue < 0 then
            isGamePossbile = false
        end
    end
    if isGamePossbile then
        sum = sum + gameId
    end
end

print(sum)

