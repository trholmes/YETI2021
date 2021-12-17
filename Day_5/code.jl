
function fib()
    fibs=zeros(50)
    fibs[1]=0
    fibs[2]=1
    for i in 3:length(fibs)
        fibs[i]=fibs[i-1]+fibs[i-2]
    end
    fibs
end

function findn(fibs)
    holder=zeros(2)
    odds,evens,breaker=0,0,0
    for i in 1:length(fibs)
        if iseven(fibs[i])==true
            evens+=1
            if evens==9
                holder[1]=fibs[i]
                breaker+=1
            end
        elseif isodd(fibs[i])==true
            odds+=1
            if odds==6
                holder[2]=fibs[i]
                breaker+=1
            end
        end

        if breaker==2
            break
        end
    end
    n=holder[1]/holder[2]
end

function imageread(values,n)
    svals=collect(values)
    height=length(svals)/(6*n)
    out=Array{Lab}(undef,Int(height),Int(n))
    fvals=zeros(length(svals))
    @threads for i in 1:length(svals)
        fvals[i]=parse(Int,svals[i],base=16)
    end
    fval=Int.(fvals)
    k=1
    j=1
    for i in 0:Int((length(fval)/6)-1)
        if k==n+1
            k=1
            j+=1
        end
        v1=(fval[Int((i*6)+1)]+fval[Int((i*6)+2)])/30
        v2=(fval[Int((i*6)+3)]+fval[Int((i*6)+4)])/30
        v3=(fval[Int((i*6)+5)]+fval[Int((i*6)+6)])/30
        out[j,k]=RGB{Float64}(v1,v2,v3)
        k+=1
    end
    out,height
end

