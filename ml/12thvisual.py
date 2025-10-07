import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split

# Load data
iris = load_iris()
X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Random Forest
rf_clf = RandomForestClassifier(n_estimators=10, max_depth=3, random_state=42)
rf_clf.fit(X_train, y_train)

# Evaluate accuracy on test set
accuracy = rf_clf.score(X_test, y_test)
print(f"Random Forest Test Accuracy: {accuracy * 100:.2f}%")

# Visualize one of the trees in the forest (e.g., the first tree)
plt.figure(figsize=(12,8))
plot_tree(rf_clf.estimators_[0], feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("Visualization of One Decision Tree from the Random Forest")
plt.show()

