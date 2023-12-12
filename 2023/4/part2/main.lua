
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


fileName = "4\\part2\\input.txt"

cardId = 1
cardToCardCopies = {} 
cardsToOpen = {}
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
    cardToCardCopies[cardId] = {}
    for i = 1, numOfMatchingNums do
        table.insert(cardToCardCopies[cardId], cardId + i)
    end
    cardsToOpen[cardId] = 1
    cardId = cardId + 1
end

print("> Cards to card copies:")
for i = 1, #cardToCardCopies do
    printTable(i .. ": ", cardToCardCopies[i], ", ")
end


for cId = 1, cardId - 1 do
    cardsToCopy = cardToCardCopies[cId]
    cardsToAdd = cardsToOpen[cId]
    for key, cardToCopy in ipairs(cardsToCopy) do
        cardsToOpen[cardToCopy] = cardsToOpen[cardToCopy] + cardsToAdd
    end
end

sum = 0
for i = 1, #cardsToOpen do
    sum = sum + cardsToOpen[i]
end
print(sum)