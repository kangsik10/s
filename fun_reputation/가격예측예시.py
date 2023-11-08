# Hypothetical feature set for Terry Adkins' artwork
adkins_features = pd.DataFrame({
    'Artist': ['Terry Adkins'],
    'Artwork Genre': ['Contemporary'],
    'Artwork Size': ['Large'],
    'Artwork Material': ['Mixed Media'],
    'Artwork Condition': ['Good']
})

# Predict the price using the trained pipeline
adkins_predicted_price = pipeline.predict(adkins_features)
print(f"The predicted price for Terry Adkins' artwork is: ${adkins_predicted_price[0]:,.2f}")
