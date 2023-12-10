
function printGrid()
    for i = 1, #grid do 
        local str = ''
        for j = 1, #grid[i] do
            str = str .. grid[i][j]
        end
        print(str)
    end
end

function isDigit(x, y)
    local str = grid[y][x]
    return not (str == "" or str:find("%D"))
end

function isSymbol(x, y)
    return not (isDigit(x, y) or grid[y][x] == emptySymbol) 
end

function indexHasNumber(x, y)
    return not (indexToNumberMatrix[y][x] == nil or indexToNumberMatrix[y][x] == '')
end

function neighboursSymbol(x, y)
    if x > 1 and isSymbol(x - 1, y) then return true end
    if x < columnCount and isSymbol(x + 1, y) then return true end
    if y > 1 and isSymbol(x, y - 1) then return true end
    if y < rowCount and isSymbol(x, y + 1) then return true end
    if x > 1 and y > 1 and isSymbol(x - 1, y - 1) then return true end
    if x < columnCount and y < rowCount and isSymbol(x + 1, y + 1) then return true end
    if x > 1 and y < rowCount and isSymbol(x - 1, y + 1) then return true end
    if x < columnCount and y > 1 and isSymbol(x + 1, y - 1) then return true end
    return false
end

function contains(table, value)
    for i = 1, #table do
        if table[i] and table[i] == value then
            return true
        end
    end
    return false
end

fileName = "3\\part2\\input.txt"
grid = {}
indexToNumberMatrix = {}
lineIndex = 1;
for line in io.lines(fileName) do 
    grid[lineIndex] = {}
    indexToNumberMatrix[lineIndex] = {}
    for i = 1, #line do
        local c = line:sub(i,i)
        grid[lineIndex][i] = c
    end
    lineIndex = lineIndex + 1
end

rowCount = #grid
columnCount = #grid[1]

emptySymbol = '.'
gearSumbol = '*'
print(columnCount, " X ", rowCount)
printGrid()

y = 1
while y <= rowCount do
    x = 1
    --print(x, y, grid[y][x])
    while x <= columnCount do
        if isDigit(x, y) then
            bNeighboursSymbol = neighboursSymbol(x, y)
            str = grid[y][x]
            for xx = x + 1, columnCount do
                if isDigit(xx, y) then
                    str = str .. grid[y][xx]
                    if (not bNeighboursSymbol) and neighboursSymbol(xx, y) then
                        bNeighboursSymbol = true
                    end
                else
                    break
                end
            end
            if bNeighboursSymbol then
                num = tonumber(str)
                for xx = x, x + #str - 1 do
                    indexToNumberMatrix[y][xx] = num 
                end
            end
            x = x + #str
            --print(str, bNeighboursSymbol)
        end
        x = x + 1
    end
    y = y + 1
end

totalSum = 0
neighbourIndexes = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}, {-1, -1}, {1, 1}, {-1, 1}, {1, -1}}
for y = 1, rowCount do
    for x = 1, columnCount do
        c = grid[y][x]
        sum = 0
        if c == gearSumbol then
            neighbouringNumbers = {}
            for n = 1, 8 do
                xx = x + neighbourIndexes[n][1]
                yy = y + neighbourIndexes[n][2]
                if indexHasNumber(xx, yy) then
                    num = indexToNumberMatrix[yy][xx]
                    if not contains(neighbouringNumbers, num) then
                        table.insert(neighbouringNumbers, num)
                        print(x, y, num)
                        if sum == 0 then 
                            sum = num 
                        else
                            sum = sum * num
                        end
                    end
                end
            end
        end
        if neighbouringNumbers and #neighbouringNumbers == 2 then
            totalSum = totalSum + sum
        elseif neighbouringNumbers and #neighbouringNumbers > 2 then
            print("!!!! ERROR more than two numbers")
        end
    end
end
print(totalSum)