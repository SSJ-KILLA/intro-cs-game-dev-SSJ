# Alrighty so lets go ahead and just take some names from Arcane Odyssey since im not too
# and remember to close them with commas

inventory = {
    "Healing Pot": 1000,
    "Withered Remains": 5,
    "Caustic Fabric": 29304,
    "Kraken Meat": 3,
    "Sunken Essence": 23
}
# Here we're gonna say that we removed the kraken meat and now they have a Prometheus Acrimony
inventory.pop("Kraken Meat")
inventory.update({"Prometheus Acrimony": 1})

print(inventory)