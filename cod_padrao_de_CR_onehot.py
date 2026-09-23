# Categoria Rara
import pandas as pd

df = pd.read_csv("data_OneHot_Marital_status.csv", sep=";")

df.columns = df.columns.str.strip()

df["Application mode"] = df["Application mode"].apply(
    lambda x: "1st phase - general contingent" if x == 1
    else "2nd phase - general contingent" if x == 17
    else "Other"
)

print(df["Application mode"].value_counts())

#outra celula
df.to_csv("data.csv", sep=";", index=False) # salva no bd e muda o nome dele, lembra disso

# one hot
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("data_Categoriarara(Nacionality).csv", sep=";") # ler o bd

encoder = OneHotEncoder(sparse_output=False) # cria o OneHotEncoder

nacionality_encoded = encoder.fit_transform(df[["Nacionality"]]) # fazendo as matrizes

nomes = encoder.get_feature_names_out(["Nacionality"]) # guardando os nomes das novas colunas na variavel nomes

nacionality_df = pd.DataFrame( #Transformando o resultado em DataFrame
    nacionality_encoded,
    columns=nomes,
    index=df.index
)

df = pd.concat([df.drop(columns=["Nacionality"]), nacionality_df], axis=1) #Removendo a coluna antiga e juntando as novas

print(df.head()) #mostra as primeiras 5 linhas do DataFrame pra ver se deu certo


#outra celula
df.to_csv("data_OneHot_Nacionality.csv", sep=";", index=False) # salva no bd