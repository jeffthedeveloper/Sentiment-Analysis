import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Carregar as avaliações dos usuários
ratings = pd.read_csv('data/ratings.csv')

# Criar a matriz de avaliações
user_ratings = ratings.pivot(index='userId', columns='itemId', values='rating').fillna(0)

# Calcular a similaridade entre usuários
cos_sim = cosine_similarity(user_ratings)

# Função para recomendar itens com base na similaridade
def recommend(user_id, num_recommendations=3):
    user_idx = user_id - 1
    similar_users = cos_sim[user_idx]
    similar_users_idx = similar_users.argsort()[-num_recommendations:][::-1]
    
    recommendations = []
    for idx in similar_users_idx:
        recommendations.append(user_ratings.iloc[idx].idxmax())
    
    return recommendations

print(recommend(1))
