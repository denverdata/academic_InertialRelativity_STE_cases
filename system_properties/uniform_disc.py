"""
Uniform Disc module.

This module provides the UniformDisc class for modeling
uniform disc objects according to Newtonian physics.
"""

from decimal import Decimal
from base_system import BasePhysicalSystem
import constants
import utils

class UniformDisc(BasePhysicalSystem):
    """
    Class representing a uniform disc object.
    
    This class models a uniform disc with constant density
    and optional rotation, following Newtonian physics.
    """
    
    def __init__(self, radius, thickness, mass, rfreq=0, name=None):
        """
        Initialize a uniform disc.
        
        Args:
            radius: Radius of the disc (m)
            thickness: Thickness of the disc (m)
            mass: Mass of the disc (kg)
            rfreq: Optional initial rotational frequency (Hz)
            name: Optional name for the disc object
        """
        super().__init__()
        
        # Set default name based on class description
        if name is not None:
            self.name = name
        else:
            self.name = "Uniform Disc"
        
        # Store input parameters
        self._store_input_param('radius', radius)
        self._store_input_param('thickness', thickness)
        self._store_input_param('mass', mass)
        self._store_input_param('rfreq', rfreq)
        
        # Convert all inputs to Decimal and store as private attributes
        self._radius = self._to_decimal(radius)
        self._thickness = self._to_decimal(thickness)
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
    def thickness(self):
        """Get the thickness value."""
        return self._thickness
        
    @thickness.setter
    def thickness(self, value):
        """Set the thickness value and recalculate properties."""
        self._thickness = self._to_decimal(value)
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
        """Calculate all properties of the uniform disc."""
        # Volume of the disc (V = π * r^2 * h)
        self._properties['volume'] = constants.PI * self.radius**2 * self.thickness
        
        # Density of the disc (ρ = m/V)
        self._properties['density'] = self.mass / self._properties['volume']
        
        # Surface area (A = 2*π*r^2 + 2*π*r*h)
        self._properties['surface_area'] = (
            Decimal('2') * constants.PI * self.radius**2 +
            Decimal('2') * constants.PI * self.radius * self.thickness
        )
        
        # Moment of inertia about axis of least resistance
        # For a uniform disc, this is perpendicular to the disc through its center
        # I = (1/2) * m * r²
        self._properties['moment_of_inertia'] = Decimal('0.5') * self.mass * self.radius**2
        
        
        # Gravitational potential energy (approximation for a disc)
        self._properties['gravitational_potential_energy'] = (
            -constants.G * self.mass * self.mass / self.radius
        )
        
        # Always use rotational frequency for calculations
        rotational_freq = self.rfreq
        self._properties['rotational_frequency'] = rotational_freq
        
        # Rotational period (T = 1/f)
        # For zero frequency, set to infinity (or a very large number for practical use)
        if rotational_freq == Decimal('0'):
            self._properties['rotational_period'] = Decimal('0')  # Representing "undefined" for zero rotation
        else:
            self._properties['rotational_period'] = Decimal('1') / rotational_freq
        
        # Rotational angular velocity (ω = 2π * frequency)
        rotational_angular_velocity = Decimal('2') * constants.PI * rotational_freq
        self._properties['rotational_angular_velocity'] = rotational_angular_velocity
        
        # Rotational tangential velocity at edge (v = r * ω)
        rotational_tangential_velocity = self.radius * rotational_angular_velocity
        self._properties['rotational_tangential_velocity'] = rotational_tangential_velocity
        
        # Rotational kinetic energy (E_rot = 1/2 * I * ω^2)
        moment_of_inertia = Decimal('0.5') * self.mass * self.radius**2
        self._properties['kinetic_energy'] = (
            Decimal('0.5') * moment_of_inertia * rotational_angular_velocity**2
        )
        
        # Angular momentum (L = I * ω)
        self._properties['angular_momentum'] = (
            moment_of_inertia * rotational_angular_velocity
        )
        
        # Add relativistic properties
        # Schwarzschild radius (r_s = 2GM/c^2)
        self._properties['schwarzschild_radius'] = (
            Decimal('2') * constants.G * self.mass / (constants.SPEED_OF_LIGHT ** 2)
        )
        
        # Gravitational time dilation at surface edge (sqrt(1 - 2GM/(rc^2)))
        time_dilation_term = Decimal('2') * constants.G * self.mass / (self.radius * constants.SPEED_OF_LIGHT ** 2)
        
        # For precision, avoid subtraction from 1 when the term is very small
        time_dilation_factor = Decimal('1') - time_dilation_term
        # Ensure we don't try to take square root of negative number
        if time_dilation_factor > Decimal('0'):
            self._properties['gravitational_time_dilation'] = time_dilation_factor.sqrt()
        else:
            # Object is inside its own Schwarzschild radius
            self._properties['gravitational_time_dilation'] = Decimal('0')
    
        # Removed gravity_at_max_radius property as requested
        
        # Total energy (U + K)
        potential = self._properties.get('gravitational_potential_energy', Decimal('0'))
        kinetic = self._properties.get('kinetic_energy', Decimal('0'))
        total_energy = potential + kinetic
        self._properties['total_energy'] = total_energy
    
        # Vibrational frequency calculation
        # f = (1/2π) * sqrt(G*m/(r*h^2))
        # Calculate the vibrational frequency
        #TODO: Comnfirm this formula is correct for a uniform disc
        self._properties['vibrational_frequency'] = (
            (constants.G * self.mass / (self.radius * self.thickness**2)).sqrt() /
            (Decimal('2') * constants.PI)
        )
        
        # f_from_1N - frequency resulting from 1N of torque for 1s about axis of least resistance
        # Angular acceleration from 1N·m torque: α = torque/I = 1/I
        # After 1s, angular velocity ω = α·t = 1/I
        # Frequency f = ω/(2π) = 1/(2π·I)
        self._properties['f_from_1N'] = Decimal('1') / (Decimal('2') * constants.PI * self._properties['moment_of_inertia'])
        
        # V from 1N - velocity resulting from 1N of torque for 1s about axis of least resistance
        # Using the angular velocity ω = 1/I calculated above
        # Linear velocity at edge: v = ω·r = r/I
        self._properties['v_from_1N'] = self.radius / self._properties['moment_of_inertia']
    
    def print_properties(self):
        """Print the properties of the uniform disc."""
        # Print the name first
        print(f"Name: {self.name}")
        
        # Print input properties with no headers
        print(f"Radius: {self._format_output(self._to_decimal(self._input_params.get('radius', '0')))} m")
        print(f"Thickness: {self._format_output(self._to_decimal(self._input_params.get('thickness', '0')))} m")
        print(f"Mass: {self._format_output(self._to_decimal(self._input_params.get('mass', '0')))} kg")
        print(f"Rotational Frequency: {self._format_output(self._to_decimal(self._input_params.get('rfreq', '0')))} Hz")
        
        # Basic properties
        print(f"Surface Area: {self._format_output(self._properties.get('surface_area', Decimal('0')))} m²")
        print(f"Volume: {self._format_output(self._properties.get('volume', Decimal('0')))} m³")
        print(f"Moment Of Inertia: {self._format_output(self._properties.get('moment_of_inertia', Decimal('0')))} kg·m²")
        print(f"Density: {self._format_output(self._properties.get('density', Decimal('0')))} kg/m³")
        
        # Rotational properties - always display
        print(f"Rotational Period: {self._format_output(self._properties.get('rotational_period', Decimal('0')))} s")
        print(f"Rotational Angular Velocity: {self._format_output(self._properties.get('rotational_angular_velocity', Decimal('0')))} rad/s")
        print(f"Rotational Tangential Velocity: {self._format_output(self._properties.get('rotational_tangential_velocity', Decimal('0')))} m/s")
        
        # Gravitational properties
        print(f"Schwarzschild Radius: {self._format_output(self._properties.get('schwarzschild_radius', Decimal('0')))} m")
        time_dilation = self._properties.get('gravitational_time_dilation', Decimal('0'))
        print(f"Gravitational Time Dilation: {time_dilation:.50e} (dimensionless)")
        
        # Energy properties - always show in this order
        print(f"Total Potential Energy: {self._format_output(self._properties['gravitational_potential_energy'])} J")
        print(f"Total Kinetic Energy: {self._format_output(self._properties['kinetic_energy'])} J")
        print(f"Total Energy: {self._format_output(self._properties['total_energy'])} J")
        
        # Harmonic properties
        print(f"Vibrational Frequency: {self._format_output(self._properties['vibrational_frequency'])} Hz")
        
        # 1N Torque Response
        print(f"Frequency from 1N·m Torque (1s): {self._format_output(self._properties.get('f_from_1N', Decimal('0')))} Hz")
        print(f"Velocity from 1N·m Torque (1s): {self._format_output(self._properties.get('v_from_1N', Decimal('0')))} m/s")