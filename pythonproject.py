#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  10:50:02 2024

@author: vaibhavprakash
"""


def calculate_carbon_footprint(miles_driven, gas_consumed, electricity_consumed):
    CARBON_PER_MILE = 0.404  # kg CO2 per mile driven
    CARBON_PER_GALLON = 8.887  # kg CO2 per gallon of gasoline
    CARBON_PER_KWH = 0.789  # kg CO2 per kilowatt-hour of electricity

    car_emissions = miles_driven * CARBON_PER_MILE
    gas_emissions = gas_consumed * CARBON_PER_GALLON
    electricity_emissions = electricity_consumed * CARBON_PER_KWH

    total_emissions = car_emissions + gas_emissions + electricity_emissions

    return total_emissions


def main():
    print("Welcome to the Carbon Footprint Calculator!")
    print("This tool estimates your carbon footprint based on your home energy, transportation, and waste.\n")

    miles = float(input("Enter the total number of miles you've driven in the past year: "))
    gas = float(input("Enter the total gallons of gasoline you've consumed in the past year: "))
    electricity = float(input("Enter the total kilowatt-hours of electricity you've consumed in the past year: "))
    
    # Additional questions for more accurate estimation
    print("\nTo provide a more accurate estimate, please answer the following questions:")

    people_in_household = int(input("How many people live in your household? "))
    recycle_percentage = float(input("What percentage of your waste do you recycle? "))
    avg_monthly_gas_bill = float(input("What is your average monthly gas bill (in dollars)? "))
    avg_monthly_electricity_bill = float(input("What is your average monthly electricity bill (in dollars)? "))

    # Additional calculations based on user input
    waste_recycled = (recycle_percentage / 100) * 1000  # Assume 1000 kg of waste generated per year per person
    gas_emissions = avg_monthly_gas_bill * 12 * 0.19  # Average annual CO2 emissions from gas usage
    electricity_emissions = avg_monthly_electricity_bill * 12 * 0.45  # Average annual CO2 emissions from electricity usage
    waste_emissions = (people_in_household * (1000 - waste_recycled)) * 0.63  # Average annual CO2 emissions from waste

    total_emissions = calculate_carbon_footprint(miles, gas, electricity) + gas_emissions + electricity_emissions + waste_emissions

    print(f"\nYour estimated total carbon footprint is approximately {total_emissions:.2f} kg CO2 per year.")


if __name__ == "__main__":
    main()
