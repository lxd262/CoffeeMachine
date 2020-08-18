spin, elec_charge = input(), input()
if spin == "1/2" and elec_charge == "-1/3":
    ans = "Strange Quark"
elif spin == "1/2" and elec_charge == "2/3":
    ans = "Charm Quark"
elif spin == "1/2" and elec_charge == "-1":
    ans = "Electron Lepton"
elif spin == "1/2" and elec_charge == "0":
    ans = "Neutrino Lepton"
elif spin == "1" and elec_charge == "0":
    ans = "Photon Boson"
print(ans)
