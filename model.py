from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS # CORS for handling Cross-Origin Resource Sharing
import pickle 

# Create a Flask application instance
app = Flask(__name__)

# Enable CORS for all routes, allowing requests from any origin
CORS(app,resources={r"/*":{"origins":"*"}})

# model = pickle.load(open('movies_', 'rb'))
model = pickle.load(open('movies_dict.pkl', 'rb'))
# movie_similarity = pickle.load(open('movie_similarity.pkl', 'rb'))
movies = pd.DataFrame(model)

# def get_movie_recommendation(movie_name):
#     movie_index = movies[movies['title'] == movie_name].index[0]
#     distances = movie_similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x : x[1])[1:6]

#     recommand_movie = []

#     for movie in movies_list:
#         movie_info = []
#         movie_info.append(str(movies.iloc[movie[0]].movie_id))
#         movie_info.append(movies.iloc[movie[0]].title)
#         movie_info.append(movies.iloc[movie[0]].tags)
        
#         # print(movies.iloc[movie[0]].movie_id)
#         # movie_info.append(movies.iloc[movie[0]])
#         recommand_movie.append(movie_info)
    
#     return recommand_movie

  

# Define a route for handling HTTP GET requests to the root URL

@app.route('/', methods=['GET'])
def get_data():
    data = {
        "message":"API is Running"
    }
    return jsonify(data)

# Define a route for making predictions
@app.route('/loadallmovies', methods=['POST'])
def loadallmovies():
    try:
        # prediction = model.predict(query_df)
        movies_info = movies['title'].values
        # data = request.get_json()
        # movie_name = pd.DataFrame([data])
        return jsonify({
            'Prediction': list(movies_info),
            # 'Recommand_Movie' : get_movie_recommendation(movie_name)
        })
    except Exception as e:
        return jsonify({'error': str(e)})
    
    
# @app.route('/recommendedmovies', methods=['POST'])
# def getMovies():
#     try:
#         # prediction = model.predict(query_df)
#         # movies_info = movies['title'].values
#         data = request.get_json()
#         # movie_name = pd.DataFrame([data])
#         print(f"movie_name: {data}")
#         return jsonify({
#             'Recommended_Movies': list(get_movie_recommendation(data))
#             # 'Recommand_Movie' : get_movie_recommendation(movie_name)
#         })
#     except Exception as e:
#         return jsonify({'error': str(e)})
  
# # Define a route for making predictions
# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # prediction = model.predict(query_df)
#         movies_info = movies['title'].values
#         # data = request.get_json()
#         # movie_name = pd.DataFrame([data])
#         return jsonify({
#             'Prediction': list(movies_info),
#             # 'Recommand_Movie' : get_movie_recommendation(movie_name)
#         })
#     except Exception as e:
#         return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)