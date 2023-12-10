
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

fileName = "3\\part1\\input.txt"
grid = {}
lineIndex = 1;
for line in io.lines(fileName) do 
    grid[lineIndex] = {}
    for i = 1, #line do
        local c = line:sub(i,i)
        grid[lineIndex][i] = c
    end
    lineIndex = lineIndex + 1
end

rowCount = #grid
columnCount = #grid[1]

emptySymbol = '.'
print(columnCount, " X ", rowCount)
--printGrid()

sum = 0
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
                    x = x + 1
                    if (not bNeighboursSymbol) and neighboursSymbol(xx, y) then
                        bNeighboursSymbol = true
                    end
                else
                    break
                end
            end
            if bNeighboursSymbol then
                sum = sum + tonumber(str)
            end
            --print(str, bNeighboursSymbol)
        end
        x = x + 1
    end
    y = y + 1
end

print(sum)