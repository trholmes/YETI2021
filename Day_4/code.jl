function vigenere()
    codex=Array{Any}(undef,36,2)
    for i in 0:25
        codex[i+1,1]=uppercase(string(i+10,base=36))
        codex[i+1,2]=i
    end
    for i in 0:9
        codex[i+27,1]=string(i)
        codex[i+27,2]=i+26
    end
    codex
end

function decrypt(code,codex)
    key=[["B",0],["I",0],["J",0],["O",0],["U",0]]
    scode=split(uppercase(code),"")
    
    @threads for i in 1:length(key)
        @threads for j in 1:length(codex)
            if codex[j,1]==key[i][1]
                key[i][2]=codex[j,2]
                break
            end
        end
    end
    skey=repeat(key,length(scode))[1:length(scode)]
    ncode=zeros(length(scode))
    @threads for i in 1:length(scode)
        @threads for j in 1:length(codex)
            if codex[j,1]==scode[i]
                ncode[i]=codex[j,2]
                break
            end
        end
    end
    
    decoded=zeros(length(ncode))
    @threads for i in 1:length(ncode)
        @inbounds decoded[i]=(abs(ncode[i]+skey[i][2])+36)%36
    end

    sdecode=Array{String}(undef,length(decoded))
    @threads for i in 1:length(decoded)
        @threads for j in 1:length(codex)
            if codex[j,2]==decoded[i]
                sdecode[i]=codex[j,1]
                break
            end
        end
    end
    sdecode=join(sdecode)
end