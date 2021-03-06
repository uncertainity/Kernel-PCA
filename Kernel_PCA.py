import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist,squareform
from scipy import exp
from scipy.linalg import eigh
from sklearn.datasets import make_moons
from sklearn.decomposition import PCA

def rbf_kernel_pca(X,gamma,n_components):
    sq_dists = pdist(X,"sqeuclidean")
    mat_sq_dists = squareform(sq_dists)
    K = exp(-gamma*mat_sq_dists)
    N = K.shape[0]
    one_matrix = np.ones((N,N))/N
    K = K - one_matrix@K - K@one_matrix + one_matrix@K@one_matrix
    eigvals,eigvecs = eigh(K)
    eigvals, eigvecs = eigvals[::-1], eigvecs[:, ::-1]
    X_pc = np.column_stack([eigvecs[:,i] for i in range(n_components)])
    
    return X_pc

def make_moons_():
    X,y = make_moons(n_samples = 100, random_state = 123)
    plt.scatter(X[y==0,0],X[y==0,1],color = "Red",marker = "^",alpha = 0.5)
    plt.scatter(X[y==1,0],X[y==1,1],color = "Blue",marker = "o",alpha = 0.5)
    plt.tight_layout()
    plt.show()
    return X,y

X,y = make_moons_()
scikit_pca = PCA(n_components = 2)
X_spca = scikit_pca.fit_transform(X)

fig,ax = plt.subplots(nrows = 1,ncols = 2,figsize = (7,3))
ax[0].scatter(X_spca[y==0,0],X_spca[y == 0,1],color = "red",marker = "^",alpha = 0.5)
ax[0].scatter(X_spca[y==1,0],X_spca[y == 1,1],color = "blue",marker = "o",alpha = 0.5)
ax[1].scatter(X_spca[y==0,0],np.zeros(50)+0.02,color = "red",marker = "^",alpha = 0.5)
ax[1].scatter(X_spca[y==1,0],np.zeros(50)-0.02,color = "blue",marker = "o",alpha = 0.5)
ax[0].set_xlabel("PC1")
ax[0].set_ylabel("PC2")
ax[1].set_xlabel("PC1")
plt.tight_layout()
plt.show()

X_kpca = rbf_kernel_pca(X,gamma = 15,n_components = 2)
fig,ax = plt.subplots(nrows = 1,ncols = 2,figsize = (7,3))
ax[0].scatter(X_kpca[y==0,0],X_kpca[y == 0,1],color = "red",marker = "^",alpha = 0.5)
ax[0].scatter(X_kpca[y==1,0],X_kpca[y == 1,1],color = "blue",marker = "o",alpha = 0.5)
ax[1].scatter(X_kpca[y==0,0],np.zeros(50)+0.02,color = "red",marker = "^",alpha = 0.5)
ax[1].scatter(X_kpca[y==1,0],np.zeros(50)-0.02,color = "blue",marker = "o",alpha = 0.5)
ax[0].set_xlabel("PC1")
ax[0].set_ylabel("PC2")
ax[1].set_xlabel("PC1")
plt.tight_layout()
plt.show()


def kernelPCA1(X,gamma,n_components):
    sq_dists = pdist(X, 'sqeuclidean')    
    # Convert pairwise distances into a square matrix.
    mat_sq_dists = squareform(sq_dists)    
    # Compute the symmetric kernel matrix.
    K = exp(-gamma * mat_sq_dists)    
    # Center the kernel matrix.
    N = K.shape[0]
    one_n = np.ones((N,N)) / N
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)    
    # Obtaining eigenpairs from the centered kernel matrix
    # scipy.linalg.eigh returns them in ascending order
    eigvals, eigvecs = eigh(K)
    eigvals, eigvecs = eigvals[::-1], eigvecs[:, ::-1]    
    # Collect the top k eigenvectors (projected examples)
    X_pc = np.column_stack([eigvecs[:, i] for i in range(n_components)])    
    return X_pc

X_pc = kernelPCA1(X,15,2)
fig,ax = plt.subplots(nrows = 1,ncols = 2,figsize = (7,3))
ax[0].scatter(X_pc[y==0,0],X_pc[y == 0,1],color = "red",marker = "^",alpha = 0.5)
ax[0].scatter(X_pc[y==1,0],X_pc[y == 1,1],color = "blue",marker = "o",alpha = 0.5)
ax[1].scatter(X_pc[y==0,0],np.zeros(50)+0.02,color = "red",marker = "^",alpha = 0.5)
ax[1].scatter(X_pc[y==1,0],np.zeros(50)-0.02,color = "blue",marker = "o",alpha = 0.5)
ax[0].set_xlabel("PC1")
ax[0].set_ylabel("PC2")
ax[1].set_xlabel("PC1")
plt.tight_layout()
plt.show()

a = np.array([[1,2],[3,4]])
b = np.array([[3,2],[2,2]])
c = a.dot(b)
print(c)
d = a@b
print(d)



