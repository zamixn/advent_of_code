
function file_exists(file)
    local f = io.open(file, "rb")
    if f then f:close() end
    return f ~= nil
  end

function isInteger(str)
    return not (str == "" or str:find("%D"))  -- str:match("%D") also works
end

numberWords = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}

function checkForNumberWord(line, index)
    for n = 1, #numberWords do  

        local j = 1;
        for i = index, #line do
            if j > #numberWords[n] then
                break
            end
            if line:sub(i, i) ~= numberWords[n]:sub(j, j) then
                break
            end
            if j == #numberWords[n] then
                return n
            end
            j = j + 1
        end

    end
    return -1
end

function checkForLastNumberWord(line, index)
    for n = 1, #numberWords do  

        if index - #numberWords[n] + 1 <= 0 then 
            goto continue
        end

        local j = 1;
        for i = index - #numberWords[n] + 1, #line do
            if j > #numberWords[n] then
                break
            end
            if line:sub(i, i) ~= numberWords[n]:sub(j, j) then
                break
            end
            if j == #numberWords[n] then
                return n
            end
            j = j + 1
        end
        ::continue::
    end
    return -1

end

function getFirstNumber(line)
    for i = 1, #line do
        local c = line:sub(i, i)
        if isInteger(c) then
            return tonumber(c)
        else
            local n = checkForNumberWord(line, i)
            if n ~= -1 then
                return n;
            end
        end
    end
    return -1;
end

function getLastNumber(line)
    for i = #line, 1, -1 do
        local c = line:sub(i, i)
        if isInteger(c) then
            return tonumber(c)
        else
            local n = checkForLastNumberWord(line, i)
            if n ~= -1 then
                return n
            end
        end
    end
    return -1;
end

fileName = "1\\part2\\input.txt"
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

