
#vigenere forward function given a code.
function encrypt(code)
    cleancode=split(uppercase(code),"")
    key=["B","I","J","O","U"]
    cleankey=repeat(key,length(cleancode))[1:length(cleancode)]
    a=zeros(length(cleancode))
    b=zeros(length(cleancode))
    c=zeros(length(cleancode))
    encoded=zeros(length(cleancode))
    solution=zeros(length(cleancode))
    @threads for i in 1:length(cleancode)
        a[i]=parse(Int,cleancode[i],base=36)
        b[i]=parse(Int,cleankey[i],base=36)
        encoded[i]=abs(a[i]+b[i]+36)%36
        encoded[i]+=10
        if encoded[i]>35
            encoded[i]-=36
        end        
    end
    c=Int.(encoded)
    solution=Array{String}(undef,length(c))
    @threads for i in 1:length(c)
        solution[i]=string(c[i],base=36)
    end
    solution=join(solution)
    solution
end

function decrypt(code)
    cleancode=split(uppercase(code),"")
    key=["B","I","J","O","U"]
    cleankey=repeat(key,length(cleancode))[1:length(cleancode)]
    a=zeros(length(cleancode))
    b=zeros(length(cleancode))
    c=zeros(length(cleancode))
    encoded=zeros(length(cleancode))
    solution=zeros(length(cleancode))
    @threads for i in 1:length(cleancode)
        a[i]=parse(Int,cleancode[i],base=36)
        b[i]=parse(Int,cleankey[i],base=36)
        a[i]-=10
        if a[i]<0
            a[i]+=36
        end
        encoded[i]=abs(a[i]-b[i]+36)%36        
    end
    c=Int.(encoded)
    solution=Array{String}(undef,length(c))
    @threads for i in 1:length(c)
        solution[i]=string(c[i],base=36)
    end
    solution=join(solution)
    solution
end