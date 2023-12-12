import streamlit as st

st.title("SVD image compression")

# Add file uploader
uploaded_img = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_img is not None:
    st.image(uploaded_img, caption="Original image", use_column_width=True)
    img = imageio.imread(uploaded_img)
    st.write(f"Image shape: {img.shape}")
    
    # Add slider for selecting k
    k = st.slider('Select k', 1, img.shape[0], 20)
    
    # Apply SVD compression
    U, S, V = np.linalg.svd(img)
    compressed_img = U[:, :k] @ np.diag(S[:k]) @ V[:k, :]
    
    # Show compressed image
    st.image(compressed_img, caption=f"Compressed image with k={k}", use_column_width=True)
    
    # Show energy retained
    total_energy = np.sum(S**2)
    energy_k = np.sum(S[:k]**2)
    st.write(f"Energy retained: {100*energy_k/total_energy:.2f}%")

