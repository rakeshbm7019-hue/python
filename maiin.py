from importlib import import_module


try:
	load_iris = import_module("sklearn.datasets").load_iris
	train_test_split = import_module("sklearn.model_selection").train_test_split
	RandomForestClassifier = import_module("sklearn.ensemble").RandomForestClassifier
	accuracy_score = import_module("sklearn.metrics").accuracy_score
except ModuleNotFoundError as error:
	if error.name and error.name.startswith("sklearn"):
		raise SystemExit(
			"scikit-learn is not installed. Run: python -m pip install scikit-learn"
		) from error
	raise

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
