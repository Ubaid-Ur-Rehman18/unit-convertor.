import streamlit as st
import base64

# Unit conversion functions
def convert_units(value, from_unit, to_unit, unit_dict):
    return value * unit_dict[from_unit] / unit_dict[to_unit]

# Unit Dictionaries
LENGTH_UNITS = {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001, "Mile": 1609.34, "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254}
WEIGHT_UNITS = {"Kilogram": 1, "Gram": 0.001, "Milligram": 0.000001, "Pound": 0.453592, "Ounce": 0.0283495}

def temperature_converter(value, from_unit, to_unit):
    conversions = {
        ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
        ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
        ("Celsius", "Kelvin"): lambda x: x + 273.15,
        ("Kelvin", "Celsius"): lambda x: x - 273.15,
        ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
        ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32
    }
    return conversions.get((from_unit, to_unit), lambda x: x)(value)

# Streamlit UI
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🌍 Unit Converter 🔄</h1>
    <hr style='border: 1px solid #ddd;'>
""", unsafe_allow_html=True)

conversion_type = st.selectbox("Select conversion type:", ["Length", "Weight", "Temperature"])

unit_dict, units = None, []
if conversion_type == "Length":
    unit_dict, units = LENGTH_UNITS, list(LENGTH_UNITS.keys())
elif conversion_type == "Weight":
    unit_dict, units = WEIGHT_UNITS, list(WEIGHT_UNITS.keys())
elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]

from_unit, to_unit = st.selectbox("From:", units), st.selectbox("To:", units)
value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, unit_dict) if conversion_type != "Temperature" else temperature_converter(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

# Footer with Watermark
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 14px; color: gray;'>
        Created with ❤️ by <b>Ubaid-Ur-Rehman</b>
    </p>
    <p style='text-align: center; font-size: 12px; color: lightgray;'>
        © 2025 | All Rights Reserved
    </p>
""", unsafe_allow_html=True)
