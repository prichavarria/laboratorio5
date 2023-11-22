import argparse

from PIL import Image
import cv2
import numpy 

#Funcion que se encarga de indicar los argumentos para el programa
def parse_args():
    parser = argparse.ArgumentParser(description="Procesamiento de Imagenes")
    parser.add_argument("--biblioteca", choices=["PIL", "OpenCV"])
    parser.add_argument("--imagen", required=True, help="Ruta de la imagen")
    return parser.parse_args()


#Funcion que se encarga de llamar a las otras funciones para ejecutar el programa 
def main():
    args = parse_args()

    try:
        imagen = get_imagen(args.biblioteca, args.imagen)
    except FileNotFoundError:
        print(f"No se encontró el archivo '{args.imagen}'.")
        return
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")
        return

    try:
        mostrar_imagen(imagen)
    except Exception as e:
        print(f"Error al mostrar la imagen: {e}")


#Funcion que se encarga de obtener la imagen segun la biblioteca seleccionada
def get_imagen(biblioteca, imagen):
    if biblioteca == "PIL":
        return Image.open(imagen)
    elif biblioteca == "OpenCV":
        return cv2.imread(imagen)
    else:
        raise ValueError(f"Biblioteca no valida: {biblioteca}")


#Funcion que se encarga de mostrar la imagen segun la biblioteca seleccionada
def mostrar_imagen(imagen):
    if isinstance(imagen, Image.Image):
        imagen.show()
    elif isinstance(imagen, numpy.ndarray):
        cv2.imshow("Imagen", imagen)
        cv2.waitKey(10000)
        cv2.destroyWindow("Imagen")
    else:
        raise TypeError(f"No se puede mostrar la imagen. El tipo de dato es: {type(imagen)}")


#Se llama a la funcion main para iniciar el programa
if __name__ == "__main__":
    main()

