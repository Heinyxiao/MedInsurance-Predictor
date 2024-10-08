# MedInsurance-Predictor

## Project Overview
This project predicts healthcare insurance charges based on personal attributes, lifestyle factors, and geographic information. By analyzing features like age, gender, body mass index (BMI), family size, smoking habits, and region, the goal is to build machine learning models that accurately estimate insurance costs and provide insights into the key drivers of healthcare expenses.

## Key Features:
- **Data Analysis and Visualization**: Exploratory data analysis (EDA) to understand trends, relationships, and distributions in the data.
- **Feature Engineering**: Transforming categorical variables, scaling features, and creating polynomial terms.
- **Machine Learning Models**: Implementing linear regression, polynomial regression, and regularized models (Ridge, Lasso, ElasticNet) to predict healthcare charges.
- **Evaluation**: Cross-validation, learning curves, and performance metrics like RMSE and R² to validate model accuracy and generalization.

## Data Source
The dataset used in this project is publicly available on Kaggle: [Healthcare Insurance Dataset](https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance/data).

## Project Structure
- **`data/`**: Contains the dataset files (train and test data).
- **`notebooks/`**: Jupyter notebooks with the data analysis, model training, and evaluation steps.
- **`src/`**: Python scripts for data preprocessing, feature engineering, model building, and evaluation.
- **`results/`**: Model outputs, including learning curves, RMSE values, and predictions.
- **`README.md`**: This file with an overview of the project.
- **`requirements.txt`**: List of dependencies and Python packages used in the project.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Heinyxiao/MedInsurance-Predictor.git
   cd healthcare-insurance-prediction
   ```
2. Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```
3. Open the Jupyter notebooks to run the analysis and model training:
   ```bash
   jupyter notebook notebooks/MedInsurance_Predictor.ipynb
   ```
4. Alternatively, you can run the Python scripts for training models:
   ```bash
   python src/MedInsurance_Predictor.py
   ```
5. Run the Interactive Web App: This project includes an interactive web app where users can input their personal data to predict healthcare insurance prices.
   ```bash
   pip install streamlit
   streamlit run app.py
   ```

## Model Evaluation
The best-performing model in this project was Polynomial Regression (degree=2) with Lasso Regularization:

**Test RMSE**: 4,726.90

**Test R²**: 0.852



## Future Improvements
Incorporating more advanced machine learning models (e.g., Random Forest, Gradient Boosting).
Performing feature selection and experimenting with interaction terms.
Further tuning regularization parameters for improved accuracy.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



