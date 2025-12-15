// arca_langlib/bridges/boost_bridge.cpp
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <iostream>

extern "C" {

// Пример функции: умножение матриц
void multiply_matrix(double* A, double* B, double* C, int n) {
    using namespace boost::numeric::ublas;
    matrix<double> mA(n,n), mB(n,n), mC(n,n);

    // Заполнение матриц
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            mA(i,j) = A[i*n+j];
            mB(i,j) = B[i*n+j];
        }
    }

    // Умножение
    mC = prod(mA, mB);

    // Запись результата
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            C[i*n+j] = mC(i,j);
        }
    }
}

}
