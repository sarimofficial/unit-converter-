import streamlit as st
# Functions
def convert_distance(from_unit, to_unit, value):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34
    }
    result = value * units[from_unit] / units[to_unit]
    return result


def Temperature(rom_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value -32) * 5/9
    else:
        result = value
    return result

def Weight_distance(from_unit, to_unit, value):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def Pressure_distance(from_unit, to_unit, value):
    units = {
        "Pascal": 1,
        "Kilopascal": 1000,
        "Bar": 100000,
        "PSI": 6894.76
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def Temperature_distance(from_unit, to_unit, value):
    units = {
        "Celsius": 1,
        "Fahrenheit": 33.8
    }
    result = value * units[from_unit] / units[to_unit]
    return result


            

#UI
st.title("Unit Converter")
category =st.selectbox("Select Category",["Distance","Temperature","Weight","Pressure"])

if category == "Distance":
    from_unit = st.selectbox("from",["Meters","Kilometers","Feet","Miles"])
    to_unit = st.selectbox("To",["Meters","Kilometers","Feet","Miles"])
    value =st.number_input ("Enter Value")
    if st.button("Convert"):
        result = convert_distance(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} = {result:2f} {to_unit}")
       
elif category == "Weight":
    from_unit = st.selectbox("from",["Kilograms","Grams","Pounds","Ounces"])
    to_unit = st.selectbox("To",["Kilograms","Grams","Pounds","Ounces"])
    value =st.number_input ("Enter Value")
    if st.button("Convert"):
        result = Weight_distance(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} = {result:2f} {to_unit}")

elif category == "Pressure":
    from_unit = st.selectbox("from",["Pascal","Kilopascal","Bar","PSI"])
    to_unit = st.selectbox("To",["Pascal","Kilopascal","Bar","PSI"])
    value =st.number_input ("Enter Value")
    if st.button("Convert"):
        result = Pressure_distance(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} = {result:2f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("from",["Celsius","Fahrenheit"])
    to_unit = st.selectbox("To",["Celsius","Fahrenheit"])
    value =st.number_input ("Enter Value")
    if st.button("Convert"):
        result = Temperature_distance(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} = {result:2f} {to_unit}")  




# Footer
st.markdown("---")
st.write("© 2025 **Created by Muhammad Sarim **. All rights reserved.")
