from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the saved model and data
loaded_pipeline = pickle.load(open("D:\Desktop\Car\WEB_PAGE\WEB_PAGE\linear_regression_model.pkl", "rb"))
df = pd.read_csv("D:\Desktop\Car\WEB_PAGE\WEB_PAGE\Cleaned_Car.csv")

# Get unique variants and dealer names
variants = sorted(df['Variant'].dropna().unique())
dealer_names = sorted(df['Dealer_Name'].dropna().str.strip().unique())

# Get unique mileage, rating, and year
mileage = sorted(df['Mileage'].dropna().unique())
rating = sorted(df['Rating'].dropna().unique())
year = sorted(df['Year'].dropna().unique())


@app.route('/')
def index():
    return render_template("index.html", mileage=mileage,
                           rating=rating, year=year)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        variant = request.form.get("variant")
        dealer_name = request.form.get("dealer_name")
        mileage = float(request.form.get("mileage"))
        rating = float(request.form.get("rating"))
        year = int(request.form.get("year"))

        # Check if dealer_name is empty
        if not dealer_name:
            return "Please select a dealer name."

        # Filter the data based on selected variant and dealer name
        selected_data = df[(df['Variant'] == variant) & (df['Dealer_Name'] == dealer_name)]
        
        if selected_data.empty:
            return "No data found for the selected variant and dealer name combination."

        # Prepare the input data for prediction
        new_data = {
            'Variant'
            'Mileage': [mileage],
            'Rating': [rating],
            'Year': [year]
        }

        # Create a DataFrame from the new data
        new_df = pd.DataFrame(new_data)

        # Preprocess the new data using the loaded preprocessor
        new_df_preprocessed = loaded_pipeline.named_steps['preprocessor'].transform(new_df)

        # Make predictions using the loaded model
        predictions = loaded_pipeline.named_steps['regressor'].predict(new_df_preprocessed)

        return str(predictions[0])

    else:
        return "Method Not Allowed"


if __name__ == '__main__':
    app.run(debug=True)
