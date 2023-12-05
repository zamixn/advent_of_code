
function file_exists(file)
    local f = io.open(file, "rb")
    if f then f:close() end
    return f ~= nil
  end

function isInteger(str)
    return not (str == "" or str:find("%D"))  -- str:match("%D") also works
end

function getFirstNumber(line)
    for i = 1, #line do
        local c = line:sub(i, i)
        if isInteger(c) then
            return tonumber(c)
        end
    end
    return -1;
end

function getLastNumber(line)
    for i = #line, 1, -1 do
        local c = line:sub(i, i)
        if isInteger(c) then
            return tonumber(c)
        end
    end
    return -1;
end

fileName = "1\\part1\\input.txt"
sum = 0;
for line in io.lines(fileName) do 
    content = line
    print("content: " .. content)
    print("first num: " .. getFirstNumber(line))
    print("last num: " .. getLastNumber(line))
    str = getFirstNumber(line) .. getLastNumber(line)
    sum = sum + tonumber(str)
end

print(sum)

