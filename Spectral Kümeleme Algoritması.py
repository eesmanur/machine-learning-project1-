import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.cluster import SpectralClustering
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score, adjusted_rand_score, mutual_info_score

df = pd.read_csv('After_Feature_Sel.csv')

X = df.drop(columns=['NObeyesdad_Obesity_Type_I']).values
y = df['NObeyesdad_Obesity_Type_I'].values

kf = KFold(n_splits=10, shuffle=True, random_state=42)

def evaluate_metrics_for_class(X, y, y_class):
    silhouette_scores = []
    calinski_harabasz_scores = []
    davies_bouldin_scores = []
    ari_scores = []
    mi_scores = []

    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        X_train_class = X_train[y_train == y_class]
        X_test_class = X_test[y_test == y_class]

        if len(X_train_class) == 0 or len(X_test_class) == 0:
            continue

        spectral = SpectralClustering(n_clusters=3, random_state=42)
        cluster_labels = spectral.fit_predict(X_train_class)

        test_cluster_labels = spectral.fit_predict(X_test_class)

        silhouette = silhouette_score(X_test_class, test_cluster_labels)
        calinski_harabasz = calinski_harabasz_score(X_test_class, test_cluster_labels)
        davies_bouldin = davies_bouldin_score(X_test_class, test_cluster_labels)
        ari = adjusted_rand_score(y_test[y_test == y_class], test_cluster_labels)
        mi = mutual_info_score(y_test[y_test == y_class], test_cluster_labels)

        silhouette_scores.append(silhouette)
        calinski_harabasz_scores.append(calinski_harabasz)
        davies_bouldin_scores.append(davies_bouldin)
        ari_scores.append(ari)
        mi_scores.append(mi)

    mean_silhouette_score = np.mean(silhouette_scores)
    mean_calinski_harabasz_score = np.mean(calinski_harabasz_scores)
    mean_davies_bouldin_score = np.mean(davies_bouldin_scores)
    mean_ari_score = np.mean(ari_scores)
    mean_mi_score = np.mean(mi_scores)

    return mean_silhouette_score, mean_calinski_harabasz_score, mean_davies_bouldin_score, mean_ari_score, mean_mi_score

def evaluate_clustering(X, y):

    classes = np.unique(y)

    metrics_by_class = {}

    for y_class in classes:
        metrics_by_class[y_class] = evaluate_metrics_for_class(X, y, y_class)

    return metrics_by_class

metrics_by_class = evaluate_clustering(X, y)

for class_label, metrics in metrics_by_class.items():
    print(f"\nMetrics for class {class_label}:")
    print(f'Mean Silhouette Score: {metrics[0]}')
    print(f'Mean Calinski-Harabasz Score: {metrics[1]}')
    print(f'Mean Davies-Bouldin Score: {metrics[2]}')
    print(f'Mean Adjusted Rand Index: {metrics[3]}')
    print(f'Mean Mutual Information: {metrics[4]}')

