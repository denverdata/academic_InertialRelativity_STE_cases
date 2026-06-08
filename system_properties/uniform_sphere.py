"""
Uniform Sphere module.

This module provides the UniformSphere class for modeling
uniform spherical objects according to Newtonian physics.
"""

from decimal import Decimal
from base_system import BasePhysicalSystem
import constants
import utils

class UniformSphere(BasePhysicalSystem):
    """
    Class representing a uniform spherical object.
    
    This class models a uniform sphere with constant density
    and optional rotation, following Newtonian physics.
    """
    
    def __init__(self, radius, mass, rfreq=0, name=None):
        """
        Initialize a uniform sphere.
        
        Args:
            radius: Radius of the sphere (m)
            mass: Mass of the sphere (kg)
            rfreq: Optional initial rotational frequency (Hz)
            name: Optional name for the sphere object
        """
        super().__init__()
        
        # Set default name based on class description
        if name is not None:
            self.name = name
        else:
            self.name = "Uniform Sphere"
        
        # Store input parameters
        self._store_input_param('radius', radius)
        self._store_input_param('mass', mass)
        self._store_input_param('rfreq', rfreq)
        
        # Convert all inputs to Decimal and store as private attributes
        self._radius = self._to_decimal(radius)
        self._mass = self._to_decimal(mass)
        self._rfreq = self._to_decimal(rfreq)
        
        # Calculate and store system properties
        self._calculate_properties()
    
    # Property getters and setters
    @property
    def radius(self):
        """Get the radius value."""
        return self._radius
        
    @radius.setter
    def radius(self, value):
        """Set the radius value and recalculate properties."""
        self._radius = self._to_decimal(value)
        self._calculate_properties()
        
    @property
    def mass(self):
        """Get the mass value."""
        return self._mass
        
    @mass.setter
    def mass(self, value):
        """Set the mass value and recalculate properties."""
        self._mass = self._to_decimal(value)
        self._calculate_properties()
        
    @property
    def rfreq(self):
        """Get the rotational frequency value."""
        return self._rfreq
        
    @rfreq.setter
    def rfreq(self, value):
        """Set the rotational frequency value and recalculate properties."""
        self._rfreq = self._to_decimal(value)
        self._calculate_properties()
    
    def _calculate_properties(self):
        """Calculate all properties of the uniform sphere."""
        # Volume of the sphere (V = 4/3 * π * r^3)
        self._properties['volume'] = (
            Decimal('4') / Decimal('3') * constants.PI * self.radius**3
        )
        
        # Density of the sphere (ρ = m/V)
        self._properties['density'] = self.mass / self._properties['volume']
        
        # Surface area of the sphere (A = 4 * π * r^2)
        self._properties['surface_area'] = Decimal('4') * constants.PI * self.radius**2
        
        # Moment of inertia about axis of least resistance
        # For a uniform sphere, this is through the center
        # I = (2/5) * m * r²
        self._properties['moment_of_inertia'] = Decimal('2') / Decimal('5') * self.mass * self.radius**2
        
        # Escape velocity (v_esc = sqrt(2*G*m/r))
        self._properties['escape_velocity'] = (
            (Decimal('2') * constants.G * self.mass / self.radius).sqrt()
        )
        
        # Gravitational potential energy at surface (U = -G*m^2/r)
        self._properties['gravitational_potential_energy'] = (
            -constants.G * self.mass * self.mass / self.radius
        )
        
        # NOTE: Gravitational binding energy calculation removed.
        # DO NOT ADD BACK the gravitational binding energy calculation.
        
        # Always use rotational frequency for calculations
        rotational_freq = self.rfreq
        self._properties['rotational_frequency'] = rotational_freq
        
        # Rotational period (T = 1/f)
        # For zero frequency, set to zero (representing "undefined")
    
        self._properties['rotational_period'] = Decimal('0')
        if rotational_freq != Decimal('0'):
            self._properties['rotational_period'] = Decimal('1') / rotational_freq
        
        # Rotational angular velocity (ω = 2π * frequency)
        rotational_angular_velocity = Decimal('2') * constants.PI * rotational_freq
        self._properties['rotational_angular_velocity'] = rotational_angular_velocity
        
        # Rotational tangential velocity at edge (v = r * ω)
        rotational_tangential_velocity = self.radius * rotational_angular_velocity
        self._properties['rotational_tangential_velocity'] = rotational_tangential_velocity
        
        # Rotational kinetic energy (E_rot = 1/2 * I * ω^2)
        # I = 2/5 * m * r^2 for a solid sphere
        moment_of_inertia = Decimal('2') / Decimal('5') * self.mass * self.radius**2
        self._properties['kinetic_energy'] = (
            Decimal('0.5') * moment_of_inertia * rotational_angular_velocity**2
        )
        
        # Angular momentum (L = I * ω)
        # I = 2/5 * m * r^2 for a solid sphere
        self._properties['angular_momentum'] = (
            moment_of_inertia * rotational_angular_velocity
        )
        
        # Add relativistic properties
        # Schwarzschild radius (r_s = 2GM/c^2)
        self._properties['schwarzschild_radius'] = (
            Decimal('2') * constants.G * self.mass / (constants.SPEED_OF_LIGHT ** 2)
        )
        
        # Gravitational time dilation at surface (sqrt(1 - 2GM/(rc^2)))
        time_dilation_term = Decimal('2') * constants.G * self.mass / (self.radius * constants.SPEED_OF_LIGHT ** 2)
        
        # For precision, avoid subtraction from 1 when the term is very small
        if time_dilation_term < Decimal('1e-50'):
            # Use approximation 1 - x/2 for sqrt(1-x) when x is very small
            self._properties['gravitational_time_dilation'] = Decimal('1') - (time_dilation_term / Decimal('2'))
        else:
            time_dilation_factor = Decimal('1') - time_dilation_term
            # Ensure we don't try to take square root of negative number
            if time_dilation_factor > Decimal('0'):
                self._properties['gravitational_time_dilation'] = time_dilation_factor.sqrt()
            else:
                # Object is inside its own Schwarzschild radius
                self._properties['gravitational_time_dilation'] = Decimal('0')
        
        # Removed gravity_at_max_radius property as requested
        
        # Surface gravity (g = G*M/r²)
        self._properties['gravity'] = constants.G * self.mass / (self.radius ** 2)
        
        # Total energy (U + K)
        potential = self._properties['gravitational_potential_energy']
        kinetic = self._properties.get('kinetic_energy', Decimal('0'))
        total_energy = potential + kinetic
        self._properties['total_energy'] = total_energy
        
        # Verification for energy conservation (helpful for debugging)
        energy_sum = potential + kinetic
        if self._properties['total_energy'] != energy_sum:
            print(f"WARNING: Energy calculation discrepancy: {self._properties['total_energy']} != {potential} + {kinetic}")
        
        # Vibrational frequency approximation (simplified model)
        # Using sqrt(G*m/r^3) as approximation for fundamental mode
        self._properties['vibrational_frequency'] = (
            (constants.G * self.mass / (self.radius ** 3)).sqrt() / (Decimal('2') * constants.PI)
        )
        
        # f_from_1N - frequency resulting from 1N of torque for 1s about axis of least resistance
        # Angular acceleration from 1N·m torque: α = torque/I = 1/I
        # After 1s, angular velocity ω = α·t = 1/I
        # Frequency f = ω/(2π) = 1/(2π·I)
        self._properties['f_from_1N'] = Decimal('1') / (Decimal('2') * constants.PI * self._properties['moment_of_inertia'])
        
        # V from 1N - velocity resulting from 1N of torque for 1s about axis of least resistance
        # Using the angular velocity ω = 1/I calculated above
        # Linear velocity at edge: v = ω·r = r/I
        # TODO: This should use angular velocity and radius
        self._properties['v_from_1N'] = self.radius / self._properties['moment_of_inertia']
        
        # Inertial Density (I/V) - moment of inertia divided by volume
        self._properties['inertial_density'] = self._properties['moment_of_inertia'] / self._properties['volume']
        
        # DeGerlia Compactness (m/r) - mass divided by radius
        self._properties['degerlia_compactness'] = self.mass / self.radius
    
    def print_properties(self):
        """Print the properties of the uniform sphere."""
        # Print the name first
        print(f"Name: {self.name}")
        # Print input properties with no headers
        print(f"Radius: {self._format_output(self._to_decimal(self._input_params.get('radius', '0')))} m")
        print(f"Mass: {self._format_output(self._to_decimal(self._input_params.get('mass', '0')))} kg")
        print(f"Rotational Frequency: {self._format_output(self._to_decimal(self._input_params.get('rfreq', '0')))} Hz")
        
        # Basic properties
        print(f"Surface Area: {self._format_output(self._properties.get('surface_area', Decimal('0')))} m²")
        print(f"Volume: {self._format_output(self._properties.get('volume', Decimal('0')))} m³")
        print(f"Moment Of Inertia: {self._format_output(self._properties.get('moment_of_inertia', Decimal('0')))} kg·m²")
        print(f"Density: {self._format_output(self._properties.get('density', Decimal('0')))} kg/m³")
        print(f"Inertial Density (I/V): {self._format_output(self._properties.get('inertial_density', Decimal('0')))} kg/m")
        print(f"DeGerlia Compactness (m/r): {self._format_output(self._properties.get('degerlia_compactness', Decimal('0')))} kg/m")
        
        # Rotational properties - always display
        print(f"Rotational Period: {self._format_output(self._properties.get('rotational_period', Decimal('0')))} s")
        print(f"Rotational Angular Velocity: {self._format_output(self._properties.get('rotational_angular_velocity', Decimal('0')))} rad/s")
        print(f"Rotational Tangential Velocity: {self._format_output(self._properties.get('rotational_tangential_velocity', Decimal('0')))} m/s")
        
        # Gravitational properties
        schwarzschild_radius = self._properties.get('schwarzschild_radius', Decimal('0'))
        print(f"Schwarzschild Radius: {float(schwarzschild_radius):.5e} m")
        time_dilation = self._properties.get('gravitational_time_dilation', Decimal('0'))
        print(f"Gravitational Time Dilation: {time_dilation:.50e} (dimensionless)")
        gravity = self._properties.get('gravity', Decimal('0'))
        print(f"Gravity: {float(gravity):.5e} m/s²")
        
        # Energy properties - always show in this order
        print(f"Total Potential Energy: {self._format_output(self._properties.get('gravitational_potential_energy', Decimal('0')))} J")
        print(f"Total Kinetic Energy: {self._format_output(self._properties.get('kinetic_energy', Decimal('0')))} J")
        print(f"Total Energy: {self._format_output(self._properties.get('total_energy', Decimal('0')))} J")
        
        # Additional energy properties
        # NOTE: Gravitational binding energy output removed.
        # DO NOT ADD BACK the gravitational binding energy output.
        
        # Harmonic properties
        print(f"Vibrational Frequency: {self._format_output(self._properties.get('vibrational_frequency', Decimal('0')))} Hz")
        
        # 1N Torque Response
        print(f"Frequency from 1N·m Torque (1s): {self._format_output(self._properties.get('f_from_1N', Decimal('0')))} Hz")
        print(f"Velocity from 1N·m Torque (1s): {self._format_output(self._properties.get('v_from_1N', Decimal('0')))} m/s")