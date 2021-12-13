#Day 1 YETI coding challenge. 
#This goes along with the Jupyter notebook output.ipynb
function md5func(input)
    i=0
    output=" "
    key="1"
    while i==0
        md5sum = hexdigest("md5",key)
        if md5sum==input
            i=1
            output=key
        else
            i=0
            key=string((parse(Int, key, base=62))+1,base=62)
        end
    end
    output
end