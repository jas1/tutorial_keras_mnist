# keras tutorial

el objetivo es lograr hacer andar keras simple con mnist. 
la idea es acercarme un poco al know how de lo que esta sucediendo con un bug en otro caso de uso similar.

## tutorial a seguir

https://victorzhou.com/blog/keras-cnn-tutorial/

el tutorial sigue mnist.

agregados: 

mi plus es ponerlo en conda y que sea replicable
tambien problar lo de venv que me recomendaron.

- guardar el modelo en json
- cargar paths en .env via python-dotenv
python-dotenv --use-feature=2020-resolver

# para usar dot env.

hay que crear un archivo .env

## linux:

touch .env

## para editar el archivo .env

luego editar el archivo y agregar las variables: 

KERAS_TUTORIAL_WEIGHTS_H5="nombre_archivo_pesos.h5"
KERAS_TUTORIAL_MODEL_JSON="nombre_archivo_modelo.json"

los nombres de los archivos pueden ser cualquiera.
los de las variables no , o sino editar todos los archivos donde se usen 
en este caso 02 y 03

# conda

https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

cd /home/julio/Dropbox/julio_box/educacion/autodidacta/20201108_keras_tutorial

conda create --name tutorial_keras

conda activate tutorial_keras

o

source activate tutorial_keras

# version en la que esta tensorflow disponible:

conda install python==3.7

## pip

conda install pip

which pip 

pip install tensorflow numpy mnist python-dotenv --use-feature=2020-resolver

# archivos

- setup
- clean / features
- model build / save
- predict
