import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def calculate_class_metrics(confusion_matrix, class_of_interest):
    n_classes = len(confusion_matrix)
    
    # Calculating TP, FP, FN, TN for the class of interest
    TP = confusion_matrix.iloc[class_of_interest, class_of_interest]
    FP = confusion_matrix.iloc[:, class_of_interest].sum() - TP
    FN = confusion_matrix.iloc[class_of_interest, :].sum() - TP
    TN = confusion_matrix.values.sum() - TP - FP - FN
    
    # Calculating metrics for the class of interest
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    sensitivity = TP / (TP + FN) if (TP + FN) != 0 else 0
    specificity = TN / (TN + FP) if (TN + FP) != 0 else 0
    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    f1_score = 2 * (precision * sensitivity) / (precision + sensitivity) if (precision + sensitivity) != 0 else 0
    
    return {
        'TP': TP,
        'TN': TN,
        'FP': FP,
        'FN': FN,
        'Accuracy': accuracy,
        'Sensitivity (Recall)': sensitivity,
        'Specificity': specificity,
        'Precision': precision,
        'F1-Score': f1_score
    }

def plot_confusion_matrix(confusion_matrix, class_of_interest):
    plt.figure(figsize=(12, 10))
    sns.heatmap(confusion_matrix,
                annot=True,
                fmt='d',
                cmap='Blues')
    plt.title(f'Confusion Matrix - Class of Interest: {class_of_interest}')
    plt.ylabel('True Class')
    plt.xlabel('Predicted Class')
    
    # Highlight the class of interest
    plt.axhline(y=class_of_interest, color='red', linestyle='--')
    plt.axvline(x=class_of_interest, color='red', linestyle='--')
    
    plt.show()

# Create confusion matrix 
np.random.seed(42)  # For reproducibility
example_matrix = np.random.randint(0, 20, size=(10, 10))
np.fill_diagonal(example_matrix, np.random.randint(30, 50, size=10))

# Convert to DataFrame
classes = [f'Class {i}' for i in range(10)]
example_matrix = pd.DataFrame(
    example_matrix,
    index=classes,
    columns=classes
)

# Define class of interest
class_of_interest = 3

# Plot the confusion matrix
plot_confusion_matrix(example_matrix, class_of_interest)

# Calculate and show metrics for the class of interest
metrics = calculate_class_metrics(example_matrix, class_of_interest)

# Display results
print(f"\nEvaluation Metrics for Class {class_of_interest}:")
print("-" * 50)
print(f"True Positives (TP): {metrics['TP']}")
print(f"True Negatives (TN): {metrics['TN']}")
print(f"False Positives (FP): {metrics['FP']}")
print(f"False Negatives (FN): {metrics['FN']}")
print("-" * 50)
for metric, value in metrics.items():
    if metric not in ['TP', 'TN', 'FP', 'FN']:
        print(f'{metric}: {value:.4f}')
