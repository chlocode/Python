def water_column_height(tower_height, tank_height):
    """Calculates the height of  a column of water from a tower height and
    a tank wall height.
    Parameter(s): tower height, tank height
    Return: height of water column
    """
    height = tower_height + ((3 * tank_height) / 4)
    return height

def pressure_gain_from_water_height(height, EARTH_ACCELERATION_OF_GRAVITY, WATER_DENSITY):
    """Calculates the pressure caused by Earth's gravity pulling on the water
    stored in an elevated tank.
    Parameter(s): height
    Return: Pressure caused by gravity
    """
    pressure = ((WATER_DENSITY  * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000)
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity, WATER_DENSITY):
    """Calculates the water pressure lost due to friction between the water
    and the walls of a pipe that it flows through
    Parameter(s): pipe_diameter, pipe_length, friction_factor, fluid_velocity
    Return: lost water pressure
    """
    lost_pressure = (((-1 * friction_factor) * pipe_length * WATER_DENSITY * (fluid_velocity ** 2)) / (2000 * pipe_diameter))
    return lost_pressure

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings, WATER_DENSITY):
    """Calculates the water pressure lost because of fittings in the pipeline
    Parameter(s): fluid_velocity, quantity_fittings, WATER_DENSITY
    Return: lost pressure
    """
    lost_pressure = (-0.04 * WATER_DENSITY * (fluid_velocity ** 2) * quantity_fittings) / 2000
    return lost_pressure

def reynolds_number(hydraulic_diameter, fluid_velocity, WATER_DENSITY):
    """Calculates the Reynolds number for a pipe with water flowing through it
    Parameter(s): hydraulic_diameter, fluid_velocity
    Return: Reynolds number
    """
    reynolds_number = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / 0.0010016
    return reynolds_number

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter, WATER_DENSITY):
    """Calculates the water pressure lost because of water moving from a pipe
    with a large diameter into a pipe with a smaller diameter.
    Parameter(s): larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter
        return: pressure loss
    """
    K = ((0.1 + (50 /reynolds_number)) * (((larger_diameter / smaller_diameter) ** 4) - 1))
    pressure_loss = -(K * WATER_DENSITY * (fluid_velocity ** 2)) / 2000
    return pressure_loss

def kpa_to_psi(value):
    """Converts kilopascal value to psi
    Parameter(s): value
    Return: psi
    """
    psi = value * 0.145038
    return psi

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height, EARTH_ACCELERATION_OF_GRAVITY, WATER_DENSITY)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity, WATER_DENSITY)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity, WATER_DENSITY)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles, WATER_DENSITY)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER, WATER_DENSITY)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity, WATER_DENSITY)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house in psi: {kpa_to_psi(pressure):.2f} psi")


if __name__ == "__main__":
    main()


