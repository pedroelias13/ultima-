// moleculas_cpp.cpp

#include <iostream>
#include <string>
#include <map>
#include <sstream>
#include <vector>

class Molecula {
public:
    // Constructor que acepta la fórmula química
    Molecula(std::string formula) : formula(formula) {
        calcular_composicion();
        peso_molecular = calcular_peso_molecular();
    }

    // Método para obtener el peso molecular
    double get_peso_molecular() {
        return peso_molecular;
    }

    // Método para obtener la composición de la molécula
    std::map<std::string, int> get_composicion() {
        return composicion;
    }

private:
    std::string formula;
    double peso_molecular;
    std::map<std::string, int> composicion;

    // Método para calcular el peso molecular basado en la fórmula
    double calcular_peso_molecular() {
        double peso = 0.0;
        for (const auto& [elemento, cantidad] : composicion) {
            peso += peso_elemental[elemento] * cantidad;
        }
        return peso;
    }

    // Método para calcular la composición de la fórmula química
    void calcular_composicion() {
        std::istringstream ss(formula);
        std::string token;

        while (ss >> token) {
            std::string elemento;
            int cantidad = 1;

            for (char& c : token) {
                if (isupper(c)) {
                    if (!elemento.empty()) {
                        composicion[elemento] += cantidad;
                    }
                    elemento += c;
                } else if (islower(c)) {
                    elemento += c;
                } else if (isdigit(c)) {
                    cantidad = c - '0';
                    composicion[elemento] += cantidad;
                    elemento.clear();
                }
            }
            if (!elemento.empty()) {
                composicion[elemento] += cantidad;
            }
        }
    }

    // Mapa de pesos atómicos
    std::map<std::string, double> peso_elemental = {
        {"H", 1.008}, {"O", 16.00}, {"C", 12.01} // Agrega más elementos según sea necesario
    };
};

int main() {
    Molecula mol("H2O");
    std::cout << "Peso molecular de H2O: " << mol.get_peso_molecular() << " g/mol" << std::endl;

    auto composicion = mol.get_composicion();
    std::cout << "Composición de H2O:" << std::endl;
    for (const auto& [elemento, cantidad] : composicion) {
        std::cout << elemento << ": " << cantidad << std::endl;
    }
    return 0;
}
