using DelimitedFiles
# get data from the file
datapath = abspath("../../Day_1/data/FourVectorTest.csv")
vec4s = readdlm(datapath, ',', Float64)
# calculate the angles
phis = Vector{Float64}(undef, size(vec4s,1))
etas = Vector{Float64}(undef, size(vec4s,1))
for i = 1:size(phis, 1)
    p = sqrt(vec4s[i, 1] * vec4s[i, 1] + vec4s[i, 2] * vec4s[i, 2] + vec4s[i, 3] * vec4s[i, 3])
    phis[i] = acos(vec4s[i, 1] / p)
    etas[i] = atanh(vec4s[i, 3] / p)
end
# initialize backend
using Plots
gr()
Plots.GRBackend()

histogram2d(phis, etas, nbins = 200, scale)

savefig("../data/phi-v-eta-jl.png")