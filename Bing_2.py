import astropy.units as u
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, get_body_barycentric_posvel

solar_system_ephemeris.set('builtin')

planet_names = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
planet_masses = [3.3011e23, 4.8675e24, 5.97237e24, 6.4171e23, 1.8982e27, 5.6834e26, 8.6810e25, 1.0243e26] * u.kg

black_hole_mass = 3 * 10 ** 5 * u.kg

for planet_name, planet_mass in zip(planet_names, planet_masses):
    time = Time.now()
    pos, vel = get_body_barycentric_posvel(planet_name, time)
    print(f'{planet_name.capitalize()} position: {pos.to(u.km)}')
    print(f'{planet_name.capitalize()} velocity: {vel.to(u.km/u.s)}')