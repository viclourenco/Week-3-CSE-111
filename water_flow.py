def  water_column_height (torre_height,tank_height):
  return torre_height + 0.75 * tank_height
  
def pressure_gain_from_water_height(tank_height):
  density = 998.2
  acceleration = 9.80665
  return (density * acceleration * tank_height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
  density = 998.2
  pressure_loss_from_pipe = (-friction_factor * pipe_length * density * (fluid_velocity ** 2)) / (2000 * pipe_diameter)
  return pressure_loss_from_pipe

def  pressure_loss_from_fittings(fluid_velocity, amount_fittings):
  density = 998.2
  pressure_loss_from_fittings = (-0.04 * density * (fluid_velocity**2) * amount_fittings)/2000
  return pressure_loss_from_fittings

def reynolds_number(hydraulic_diameter, fluid_velocity):
  reynolds_number = ((998.2*hydraulic_diameter*fluid_velocity)/0.0010016)
  return reynolds_number

def pressure_loss_from_pipe_reduction(larger_diameter,fluid_velocity, reynolds_number, smaller_diameter):
  k = (0.1 + (50/reynolds_number) * (((larger_diameter/smaller_diameter)**4) - 1))
  pressure_loss_from_pipe_reduction = (-k*998.2*(fluid_velocity**2))
  return pressure_loss_from_pipe_reduction



