
#vigenere decryption
function decryption(code)
    key=["B","I","J","O","U"]
    cleancode=split(uppercase(code),"")
    cleankey=repeat(key,length(cleancode))[1:length(cleancode)]
    a=zeros(length(cleancode))
    b=zeros(length(cleancode))
    c=zeros(length(cleancode))
    solution=zeros(length(cleancode))
    decoded=zeros(length(cleancode))
    @threads for i in 1:length(cleancode)
        a[i]=parse(Int,cleancode[i],base=36)
        b[i]=parse(Int,cleankey[i],base=36)
        a[i]+=10
        if a[i]>35
            a[i]-=36
        end
        decoded[i]=(abs(a[i]-b[i]+36))%36
    end
    c=Int.(decoded)
    solution=Array{String}(undef,length(c))
    @threads for i in 1:length(c)
        solution[i]=string(c[i],base=36)
    end
    solution=join(solution)
    solution
end


#vigenere encryption function
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
        encoded[i]-=10
        if encoded[i]<0
            encoded[i]+=36
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