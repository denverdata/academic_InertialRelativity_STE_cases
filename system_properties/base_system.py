"""
Base class for physical systems.

This module provides a base class with common functionality for
all physical system implementations.
"""

from decimal import Decimal
import utils
import constants
import csv

class BasePhysicalSystem:
    """
    Base class for physical systems.
    
    This class provides common functionality for converting values to Decimal,
    formatting output, and defining the interface for all physical systems.
    """
    def __init__(self):
        """Initialize the base physical system."""
        self._properties = {}
        self._input_params = {}
        self._dataset_config = None
        self._series_data = None
        self._input_params = {}
        self._name = "Unnamed System"  # Default name
    
    def _to_decimal(self, value):
        """
        Convert a value to Decimal.
        
        Args:
            value: Value to convert
            
        Returns:
            Decimal: Decimal representation of the value
        """
        return utils.to_decimal(value)
    
    def _format_output(self, value):
        """
        Format a value for output in scientific notation with 8 digits past decimal.
        
        Args:
            value: Value to format
            
        Returns:
            str: Formatted value in scientific notation
        """
        return utils.format_scientific(value)
    
    @property
    def name(self):
        """Get the name of the system."""
        return self._name
        
    @name.setter
    def name(self, value):
        """Set the name of the system."""
        self._name = str(value)
    
    def _store_input_param(self, name, value):
        """Store an input parameter with its original value."""
        if value is not None:
            # Store the original string representation
            self._input_params[name] = str(value)
    
    def get_properties(self):
        """
        Get all properties of the system as a dictionary.
        
        Returns:
            dict: Dictionary of property names and their formatted values
        """
        formatted_properties = {}
        for key, value in self._properties.items():
            formatted_properties[key] = self._format_output(value)
        
        return formatted_properties
    def get_formatted_properties(self):
        """
        Get all properties of the system as a dictionary with formatted values.
        
        Returns:
            dict: Dictionary of property names and their formatted values
        """
        # Format input parameters
        formatted_properties = {}
        
        # Add name first
        formatted_properties['Name'] = self.name
        
        if self._input_params:
            for key, value in self._input_params.items():
                formatted_key = key.replace('_', ' ').title()
                formatted_properties[formatted_key] = value
        
        # Format calculated properties
        for key, value in self._properties.items():
            formatted_key = key.replace('_', ' ').title()
            formatted_properties[formatted_key] = self._format_output(value)
        
        return formatted_properties
    
    def print_properties(self):
        """
        Placeholder for subclass implementation.
        Each system should override this method with its own implementation.
        """
        raise NotImplementedError("Subclasses must implement print_properties()")
        
    def configure_dataset(self, param_name, start_value, end_value, other_props=None):
        """
        Configure the dataset parameters for generating a data series.
        
        Args:
            param_name (str): Name of the parameter to vary
            start_value: Starting value for the parameter range
            end_value: Ending value for the parameter range
            other_props (list, optional): List of other property names to include in the dataset
        """
        # Validate parameter name exists
        if param_name not in self._input_params and not hasattr(self, param_name):
            raise ValueError(f"Parameter '{param_name}' does not exist in this system")
        
        # Validate start < end
        start_decimal = self._to_decimal(start_value)
        end_decimal = self._to_decimal(end_value)
        if start_decimal >= end_decimal:
            raise ValueError(f"Start value ({start_value}) must be less than end value ({end_value})")
        
        # Store configuration
        self._dataset_config = {
            'type': 'single',
            'param': param_name,
            'start': start_decimal,
            'end': end_decimal,
            'other_props': other_props or []
        }
        
        # Reset any existing data
        self._series_data = None
    
    def configure_dual_dataset(self, param1, start1, end1, param2, start2, end2, other_props=None):
        """
        Configure the dataset for varying two parameters.
        
        Args:
            param1 (str): First parameter name to vary
            start1: Starting value for first parameter
            end1: Ending value for first parameter
            param2 (str): Second parameter name to vary
            start2: Starting value for second parameter
            end2: Ending value for second parameter
            other_props (list, optional): List of other property names to include
        """
        # Validate parameters exist
        for param in [param1, param2]:
            if param not in self._input_params and not hasattr(self, param):
                raise ValueError(f"Parameter '{param}' does not exist in this system")
        
        # Validate ranges
        start1_decimal = self._to_decimal(start1)
        end1_decimal = self._to_decimal(end1)
        start2_decimal = self._to_decimal(start2)
        end2_decimal = self._to_decimal(end2)
        
        if start1_decimal >= end1_decimal:
            raise ValueError(f"Start value for {param1} ({start1}) must be less than end value ({end1})")
        if start2_decimal >= end2_decimal:
            raise ValueError(f"Start value for {param2} ({start2}) must be less than end value ({end2})")
        
        # Store configuration
        self._dataset_config = {
            'type': 'dual',
            'param1': param1,
            'start1': start1_decimal,
            'end1': end1_decimal,
            'param2': param2,
            'start2': start2_decimal,
            'end2': end2_decimal,
            'other_props': other_props or []
        }
        
        # Reset any existing data
        self._series_data = None
        
    def generate_series(self, intervals):
        """
        Generate a data series by varying the configured parameter.
        
        Args:
            intervals (int): Number of intervals to generate data for
            
        Returns:
            list: List of data points
        """
        if not self._dataset_config:
            raise ValueError("Dataset not configured. Call configure_dataset() first.")
        
        if intervals <= 0:
            raise ValueError("Number of intervals must be positive")
        
        if self._dataset_config['type'] == 'single':
            return self._generate_single_param_series(intervals)
        else:
            raise ValueError("For dual parameter datasets, use generate_series_3d()")
    
    def generate_series_3d(self, intervals_x, intervals_y):
        """
        Generate a 3D data series by varying two parameters.
        
        Args:
            intervals_x (int): Number of intervals for first parameter
            intervals_y (int): Number of intervals for second parameter
            
        Returns:
            list: List of data points
        """
        if not self._dataset_config or self._dataset_config['type'] != 'dual':
            raise ValueError("Dual dataset not configured. Call configure_dual_dataset() first.")
        
        if intervals_x <= 0 or intervals_y <= 0:
            raise ValueError("Number of intervals must be positive")
        
        return self._generate_dual_param_series(intervals_x, intervals_y)
    
    def _generate_single_param_series(self, intervals):
        """
        Generate data series for a single parameter variation.
        
        Args:
            intervals (int): Number of intervals
            
        Returns:
            list: List of data points
        """
        config = self._dataset_config
        param_name = config['param']
        start_value = config['start']
        end_value = config['end']
        other_props = config['other_props']
        
        # Calculate step size
        step = (end_value - start_value) / Decimal(intervals)
        
        # Store original parameter value
        original_value = None
        if hasattr(self, param_name):
            original_value = getattr(self, param_name)
        
        # Generate data points
        data_points = []
        
        for i in range(intervals + 1):
            # Calculate parameter value for this step
            param_value = start_value + step * Decimal(i)
            
            # Set parameter value
            if hasattr(self, param_name):
                setattr(self, param_name, param_value)
            
            # Recalculate properties
            self._calculate_properties()
            
            # Create data point
            data_point = {param_name: self._format_output(param_value)}
            
            # Add requested properties
            for prop in other_props:
                if prop in self._properties:
                    data_point[prop] = self._format_output(self._properties[prop])
            
            data_points.append(data_point)
        
        # Restore original parameter value if needed
        if original_value is not None:
            setattr(self, param_name, original_value)
            self._calculate_properties()
        
        # Store generated data
        self._series_data = data_points
        
        return data_points
    
    def _generate_dual_param_series(self, intervals_x, intervals_y):
        """
        Generate data series for a dual parameter variation.
        
        Args:
            intervals_x (int): Number of intervals for first parameter
            intervals_y (int): Number of intervals for second parameter
            
        Returns:
            list: List of data points
        """
        config = self._dataset_config
        param1 = config['param1']
        start1 = config['start1']
        end1 = config['end1']
        param2 = config['param2']
        start2 = config['start2']
        end2 = config['end2']
        other_props = config['other_props']
        
        # Calculate step sizes
        step1 = (end1 - start1) / Decimal(intervals_x)
        step2 = (end2 - start2) / Decimal(intervals_y)
        
        # Store original parameter values
        original_value1 = None
        original_value2 = None
        if hasattr(self, param1):
            original_value1 = getattr(self, param1)
        if hasattr(self, param2):
            original_value2 = getattr(self, param2)
        
        # Generate data points
        data_points = []
        
        for i in range(intervals_x + 1):
            param1_value = start1 + step1 * Decimal(i)
            
            for j in range(intervals_y + 1):
                param2_value = start2 + step2 * Decimal(j)
                
                # Set parameter values
                if hasattr(self, param1):
                    setattr(self, param1, param1_value)
                if hasattr(self, param2):
                    setattr(self, param2, param2_value)
                
                # Recalculate properties
                self._calculate_properties()
                
                # Create data point
                data_point = {
                    param1: self._format_output(param1_value),
                    param2: self._format_output(param2_value)
                }
                
                # Add requested properties
                for prop in other_props:
                    if prop in self._properties:
                        data_point[prop] = self._format_output(self._properties[prop])
                
                data_points.append(data_point)
        
        # Restore original parameter values if needed
        if original_value1 is not None:
            setattr(self, param1, original_value1)
        if original_value2 is not None:
            setattr(self, param2, original_value2)
        self._calculate_properties()
        
        # Store generated data
        self._series_data = data_points
        
        return data_points
        
    def to_csv(self, filename, data=None):
        """
        Export data to CSV.
        
        Args:
            filename (str): Output file path
            data (list, optional): Data to export. If None, uses the last generated series.
        """
        # Use provided data or last generated data
        export_data = data or self._series_data
        
        if not export_data:
            raise ValueError("No data to export. Generate data first.")
        
        # Determine headers from first data point
        headers = list(export_data[0].keys())
        
        # Write to CSV
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(export_data)
        
        return True