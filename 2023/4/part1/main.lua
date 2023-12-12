
function isDigit(str)
    return not (str == "" or str:find("%D"))
end

function printTable(header, tableToPrint, seperator)
    local str = header
    for key, value in pairs(tableToPrint) do
        str = str .. seperator .. key .. ":" .. value 
    end
    print(str)
end

function tableContains(table, value)
    for i = 1, #table do
        if table[i] and table[i] == value then
            return true
        end
    end
    return false
end

function stringRowToNumberList(stringRow)
    local numbers = {}
    local i = 1
    while i <= #stringRow do
        local c = stringRow:sub(i, i)
        if isDigit(c) then
            local str = c
            for j = i + 1, #stringRow do
                local cc = stringRow:sub(j, j)
                if isDigit(cc) then
                    str = str .. cc
                else
                    break
                end
            end
            table.insert(numbers, tonumber(str))
            i = i + #str
        end
        i = i + 1
    end
    return numbers
end


fileName = "4\\part1\\input.txt"

sum = 0
for line in io.lines(fileName) do 
    indexOfColon = string.find(line, ":")
    line = line:sub(indexOfColon + 2, #line)
    indexOfBar = string.find(line, "|")
    winningNumbers = stringRowToNumberList(line:sub(0, indexOfBar - 1))
    myNumbers = stringRowToNumberList(line:sub(indexOfBar + 2, #line))
    printTable("WinningNumbers: ", winningNumbers, ", ")
    printTable("MyNumbers: ", myNumbers, ", ")
    numOfMatchingNums = 0
    for key, num in ipairs(myNumbers) do
        if tableContains(winningNumbers, num) then
            numOfMatchingNums = numOfMatchingNums + 1
        end
    end
    if numOfMatchingNums > 0 then
        points = 2 ^ (numOfMatchingNums - 1)
        sum = sum + points
    end
end

print(sum)