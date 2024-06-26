

vect = CountVectorizer().fit(X_train)


feat = vect.get_feature_names_out()


feature_names = np.array(vect.get_feature_names_out())

sorted_coef_index = model.coef_[0].argsort()





vect = CountVectorizer(min_df = 5, ngram_range = (1,3)).fit(X_train)
X_train_vectorized = vect.transform(X_train)
len(vect.get_feature_names_out())

model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

predictions = model.predict(vect.transform(X_test))
print("Accuracy: ",accuracy_score(y_test, predictions))
