#function to find the smallest prime number
function pfind(pAr)
    ninesum=zeros(length(pAr)-9)
    for j in 1:length(pAr)-9
        for k in 0:8
        ninesum[j]+=pAr[j+k]
        end
    end
    threesum=zeros(length(pAr)-3)
    for j in 1:length(pAr)-3
        for k in 0:2
        threesum[j]+=pAr[j+k]
        end
    end
    out=in(ninesum).(threesum)
    i=1
    val=0
    fiver=0
    while i<length(out)
        if out[i]==true
            val+=1
            if val==5
                fiver=threesum[i]
                break
            else
                i+=1
            end
        else
            i+=1
        end
    end
    fiver
end