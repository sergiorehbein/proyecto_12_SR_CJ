import numpy as np

# Define the number of data points
n = 1000
x = np.linspace(-1, 1, n)
x_positive = np.linspace(0, 1, n)[1:]  # Exclude zero for log and sqrt functions
y = np.linspace(-1, 1, n)

# Nguyen benchmark functions
def nguyen1(x):
    return x**3 + x**2 + x

def nguyen2(x):
    return x**4 + x**3 + x**2 + x

def nguyen3(x):
    return x**5 + x**4 + x**3 + x**2 + x

def nguyen4(x):
    return x**6 + x**5 + x**4 + x**3 + x**2 + x

def nguyen5(x):
    return np.sin(x**2) * np.cos(x) - 1

def nguyen6(x):
    return np.sin(x) + np.sin(x + x**2)

def nguyen7(x):
    # Exclude -1 to avoid log(0)
    return np.log(x + 1) + np.log(x**2 + 1)

def nguyen8(x):
    # Start from a very small positive number to avoid sqrt of negative numbers
    return np.sqrt(x)

def nguyen9(x, y):
    return np.sin(x) + np.sin(y**2)

def nguyen10(x, y):
    return 2 * np.sin(x) * np.cos(y)

# Función para guardar los datos de x y los resultados en dos columnas en un archivo de texto
def save_to_txt(x_data, y_data, filename):
    # Combinar x_data y y_data en un solo array con dos columnas
    combined_data = np.column_stack((x_data, y_data))
    np.savetxt(filename, combined_data, fmt='%f')

# Función para guardar los datos de x, y y los resultados en tres columnas en un archivo de texto
def save_to_txt_multi(x_data, y_data, results, filename):
    # Asegúrate de que x_data y y_data estén aplanados si son matrices bidimensionales
    x_data_flat = x_data.flatten()
    y_data_flat = y_data.flatten()
    
    # Combinar x_data, y_data y results en un solo array con tres columnas
    combined_data = np.column_stack((x_data_flat, y_data_flat, results.flatten()))
    np.savetxt(filename, combined_data, fmt='%f')



# Generate data for each function
data_nguyen1 = nguyen1(x)
data_nguyen2 = nguyen2(x)
data_nguyen3 = nguyen3(x)
data_nguyen4 = nguyen4(x)
data_nguyen5 = nguyen5(x)
data_nguyen6 = nguyen6(x)
data_nguyen7 = nguyen7(x_positive)
data_nguyen8 = nguyen8(x_positive)
xx_positive, yy = np.meshgrid(x_positive, y)
data_nguyen9 = nguyen9(xx_positive, yy)
data_nguyen10 = nguyen10(xx_positive, yy)



# Llamar a la función save_to_txt para guardar los datos de Nguyen1
save_to_txt(x, data_nguyen1, 'Nguyen1.txt')
save_to_txt(x,data_nguyen2, 'Nguyen2.txt')
save_to_txt(x,data_nguyen3, 'Nguyen3.txt')
save_to_txt(x,data_nguyen4, 'Nguyen4.txt')
save_to_txt(x,data_nguyen5, 'Nguyen5.txt')
save_to_txt(x,data_nguyen6, 'Nguyen6.txt')
save_to_txt(x,data_nguyen7, 'Nguyen7.txt')
save_to_txt(x,data_nguyen8, 'Nguyen8.txt')




# Guardar los datos de Nguyen9 y Nguyen10
save_to_txt_multi(xx_positive, yy, data_nguyen9, 'Nguyen9.txt')
save_to_txt_multi(xx_positive, yy, data_nguyen10, 'Nguyen10.txt')
