import streamlit as st
import joblib
import numpy as np

# Đọc mô hình từ file
model = joblib.load('knn_model.joblib')

# Tiêu đề
st.title("DỰ ĐOÁN CHẤT LƯỢNG SỮA")

# Nhập liệu từ người dùng
pH = st.number_input('pH', min_value=0.0, max_value=14.0, value=7.0)
min_ph = 3
max_ph = 9.5
pH = (pH - min_ph) / (max_ph - min_ph) 

temperature = st.number_input('Temperature (°C)', min_value=0.0, max_value=90.0, value=40.0)
temperature_max, temperature_min = 90 , 34
temperature = (temperature - temperature_min) / (temperature_max - temperature_min) 


taste = st.selectbox('Taste', [1,0])
odor = st.selectbox('Odor', [1,0])
fat = st.selectbox('Fat', [1,0])
turbidity = st.selectbox('turbidity', [1,0])
colour = st.number_input('Colour', min_value=0.0, max_value= 255.0 , value=245.0)
colour_max , colour_min = 255.0,240.0
colour = (colour - temperature_min) / (temperature_max - temperature_min) 




# Chuyển đổi input thành định dạng phù hợp
input_data = np.array([[pH, temperature, taste, odor, fat, turbidity,colour ]])

# Dự đoán
if st.button('Dự đoán'):
    result = {0: "High", 1: "Low", 2: "Medium"}
    prediction = model.predict(input_data)
    
    # Hiển thị kết quả với chữ to hơn
    st.markdown(f"<h2 style=' color: green;'>Chất lượng dự đoán: {result[prediction[0]]}</h2>", unsafe_allow_html=True)
