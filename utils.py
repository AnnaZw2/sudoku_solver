import csv
import statistics
import csv
import statistics
#Funkcja pomocnicza do wczytania danych z pliku csv i analizy wyników
# Inicjalizuj listy wyników i czasów trwania dla populacji 500 i 1500
def helper(filename):
    results_500 = []
    durations_500 = []
    zero_results_500 = 0
    results_1500 = []
    durations_1500 = []
    zero_results_1500 = 0

    
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['sol_per_pop'] == '500':
          
                results_500.append(float(row['solution_fitness']))
                durations_500.append(float(row['duration']))
                if float(row['solution_fitness']) == 0:
                    zero_results_500 += 1
            elif row['sol_per_pop'] == '1500':
 
                results_1500.append(float(row['solution_fitness']))
                durations_1500.append(float(row['duration']))
                if float(row['solution_fitness']) == 0:
                    zero_results_1500 += 1

    # Wyświetl wyniki dla populacji 500
    print("Populacja 500:")
    print("Średni wynik fitness function:", statistics.mean(results_500))
    print("Mediana fitness function:", statistics.median(results_500))
    print("Dominanta fitness function:", statistics.mode(results_500))
    print("Odchylenie standardowe:", statistics.stdev(results_500))
    print("Liczba zerowych wyników:", zero_results_500)
    print("Średni czas trwania:", statistics.mean(durations_500), "sekund")

    # Wyświetl wyniki dla populacji 1500
    print("Populacja 1500:")
    print("Średni wynik fitness function:", statistics.mean(results_1500))
    print("Mediana fitness function:", statistics.median(results_1500))
    print("Dominanta fitness function:", statistics.mode(results_1500))
    print("Odchylenie standardowe:", statistics.stdev(results_1500))
    print("Liczba zerowych wyników:", zero_results_1500)
    print("Średni czas trwania:", statistics.mean(durations_1500), "sekund")

