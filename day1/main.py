from math import floor

def read_data():
    with open("input","r") as f:
        fuel_strs = f.readlines()
        return [int(x) for x in fuel_strs]

def fuel_required(mass):
    return floor(mass/3)-2


def fuel_required_with_mass(mass):
    required_fuel = fuel_required(mass)
    if required_fuel < 0:
        return 0
    return required_fuel+fuel_required_with_mass(required_fuel)

def main():
    data = read_data()
    fuel_sum = sum(map(fuel_required,data))
    print(f"Part 1: Required fuel = {fuel_sum}")

    fuel_sum_with_mass = sum(map(fuel_required_with_mass,data))
    print(f"Part 2: Required fuel with mass = {fuel_sum_with_mass}")

if __name__ == '__main__':
    main()