from sklearn.linear_model import LinearRegression


def generate_score(best_results, final_result, default_scores):
  # print(best_results, default_scores)
  model = LinearRegression()
  model.fit([[x] for x in best_results], default_scores)
  result = model.predict([[final_result]])
  return min(result[0], 100)
