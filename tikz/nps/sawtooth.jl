using Flux, Flux.Tracker
using NeuralProcesses, NeuralProcesses.Experiment
using Distributions
using Plots
using Random
using PyCall

@pyimport pickle

function save(path, obj)
    out = open(path, "w")
    pickle.dump(obj, out)
    close(out)
end

convcnp = NeuralProcesses.untrack(best_model("models/convcnp/loglik/sawtooth.bson"))
convnp = NeuralProcesses.untrack(best_model("models/convnp/loglik/sawtooth.bson"))

p = Sawtooth()

xt = collect(range(-2, 2, length=600))
yt = reshape(rand(p(xt, 1e-10)), :)
inds = sort(randperm(length(xt))[1:7])
xc = xt[inds]
yc = yt[inds]

save("sawtooth/data.pickle", Dict(
    "xc" => xc,
    "yc" => yc,
    "xt" => xt,
    "yt" => yt
))

xc = reshape(xc, :, 1, 1)
yc = reshape(yc, :, 1, 1)
xt = reshape(xt, :, 1, 1)
yt = reshape(yt, :, 1, 1)

# Embedding:
xz = convcnp.encoder.disc(xc, xt, margin=16f0)
xz, z = code(convcnp.encoder.coder[1], xc, yc, xz)

inds = reshape((xz .>= -2) .& (xz .<= 2), :)
plot(xz[inds, 1, 1], z[inds, 1, 1])
save("sawtooth/embedding.pickle", Dict(
    "xz" => xz[inds, 1, 1],
    "z1" => z[inds, 1, 1],
    "z2" => z[inds, 2, 1]
))

xz, z = code(convcnp.encoder.coder[2], xz, z, xz)
z = NeuralProcesses.sample(z, num_samples=1)

# CNN:
xz, z = code(convcnp.decoder[1], xz, z, xt)
save("sawtooth/embedding_cnn.pickle", Dict(
    "xz" => xz[inds, 1, 1],
    "z1" => z[inds, 1, 1],
    "z2" => z[inds, 2, 1]
))

xz, z = code(convcnp.decoder[2], xz, z, xt)
xz, z = code(convcnp.decoder[3], xz, z, xt)

xc = reshape(xc, :)
yc = reshape(yc, :)
xt = reshape(xt, :)
yt = reshape(yt, :)

μ = reshape(mean(z), :)
σ = reshape(std(z), :)

# Prediction:
save("sawtooth/pred.pickle", Dict(
    "xt" => xt,
    "mu" => μ,
    "std" => σ
))

# Also predict with ConvNP:
_, _, _, samples = predict(convnp, xc, yc, xt; margin=16f0)
save("sawtooth/pred_convnp.pickle", Dict(
    "xt" => xt,
    "samples" => samples
))

