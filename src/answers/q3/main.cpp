#include <iostream>
#include <set>
#include <vector>
/**
 The prime factors of 13195 are 5, 7, 13 and 29.

 What is the largest prime factor of the number 600851475143 ?
*/
static std::set<std::uint32_t> CreatedPrimeNumbers = {2, 3, 5, 7};

void generatePrimeNumber(std::uint32_t targetNumber)
{
    auto lastPrimeNumber = *std::prev(std::end(CreatedPrimeNumbers));

    if (targetNumber <= lastPrimeNumber) {
        return;
    }

    auto currentNumber = lastPrimeNumber + 1;
    while (true) {
        if (currentNumber > targetNumber) {
            return;
        }

        bool isPrime = true;

        for (auto primeNumber : CreatedPrimeNumbers) {
            if (currentNumber % primeNumber == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            // found
            CreatedPrimeNumbers.insert(currentNumber);
        }

        ++currentNumber;
    }
}

std::set<std::uint32_t> calculatePrimeFactor(std::uint32_t value)
{
    if (CreatedPrimeNumbers.find(value) != std::end(CreatedPrimeNumbers)) {
        return std::set<std::uint32_t>{value};
    }

    std::set<std::uint32_t> factors;

    while (true) {
        bool divided = false;
        for (auto primeNumber : CreatedPrimeNumbers) {
            if (value % primeNumber) {
                factors.insert(primeNumber);
                value = value / primeNumber;
                divided = true;
                break;
            }
        }

        if (divided) {
            continue;
        }

        return std::move(factors);
    }
}

int main()
{
    generatePrimeNumber(13195);
    auto factors = calculatePrimeFactor(13195);

    for (auto factor : factors) {
        std::cout << factor << std::endl;
    }
//    std::cout << "hello" << std::endl;
//    std::cout << "next : " << generatePrimeNumber(7) << std::endl;
    return 0;
}
