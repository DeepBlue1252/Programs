#include <iostream>
#include "Algs.h"
#include <vector>
#include <algorithm>
#include <iomanip>

// to run: g++ main.cpp Algs.cpp -o main && ./main

int main() {

    int vec_type;                   // the type of sort
    int sort_algorithm;             // algorithm that is being used
    int input_length;               // input_length is the length of the vector being filled and sorted
    int vecType = 1;                // vecType is an integer that represents a type of list. Sorted, unsorted, reversed, random
    Sorting Object;                 // initialize class called sort


    while(vecType != 0) {             //enter while loop, 0 is to quit. Got to be sure to empty the vector at the end of the loop
        //Each decision will alter the efficiency of the chosen algorithm.

        std::cout << "1 = Sorted" << std::endl;     // asking user what they want
        std::cout << "2 = Partially Sorted" << std::endl;
        std::cout << "3 = Reversed" << std::endl;
        std::cout << "4 = Random" << std::endl;
        std::cout << "0 = Exit" << std::endl;
        std::cout << std::endl;

        std::cout << "What kind of list do you want to sort (enter 1, 2, 3, 4, 0)? ";
        std::cin >> vecType;
        std::cout << '\n';

        if (vecType == 0) {
            std::cout << ":(" << '\n' << '\n';
        }

        if (vecType != 0) {                                 //Checks to see if the user quits
            std::cout << "--------------------------------------------------------------------------------------------" << '\n' << '\n';;
        }

        if (vecType == 1){                                  //Code for a sorted vector
            std::cout << "Enter the length of your list: ";
            std::cin >> input_length;
            std::cout << '\n' << "--------------------------------------------------------------------------------------------" << '\n' << '\n';;

            Object.buildSorted(input_length);       // call function that creates the sorted vector passing in the original vector and the inputted length

            std::cout << "1 = Insertion Sort" << std::endl;
            std::cout << "2 = Quick Sort" << std::endl;
            std::cout << "3 = Merge Sort" << std::endl;
            std::cout << "4 = Radix Sort" << std::endl;
            std::cout << '\n';

            std::cout << "Which sorting algorithm do you want? ";
            std::cin >> sort_algorithm;
            std::cout << '\n' << '\n';


            if (sort_algorithm == 1){       //Insertion Sort Code
                clock_t t;      // initializes clock function
                t = clock();    // says when the clock started at that time

                Object.insertionSort(input_length);     //calls inerstion sort function using the input length argument

                t = clock() - t; //

                Object.printList(input_length);         //prints sorted vector

                std::cout << std::fixed << std::setprecision(4) << "The insertion sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n';    //prints the time taken to complete the sort
            }

            else if (sort_algorithm == 2){      // Quicksort Code
                clock_t t;
                t = clock();

                int lo = 0;                                                     //declares lo = 0
                int hi = input_length - 1;                                      //declares hi = the length of the vector - 1
                Object.quickSort(input_length, lo, hi);                         //calls quicksort function with the input length, low index, and high index value

                t = clock() - t;

                Object.printList(input_length);                                 //prints sorted list
                std::cout << std::fixed << std::setprecision(4) << "The quick sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n';        //prints the time taken to sort the vector
            }

            else if (sort_algorithm == 3){                                      //Mergesort Code
                int a[input_length];                                            //Declares array to be used when calling the function
                for (int l = 0; l < input_length; l++) {                        //For loop to copy the generated vector into the array
                    a[l] = Object.vec[l];
                }

                clock_t t;                                                      //declares a clock variable
                t = clock();                                                    //Starts the clock
                int *aux = new int[input_length];                               //Declares an empty array pointer of size of the vector
                int lo = 0;                                                     //declares lo = 0
                int hi = input_length - 1;                                      //declares hi = the length of the vector minus 1
                Object.mergeSort(a, aux, lo, hi);                               //calls the mergsort algorithim entering in the array, the empty space array, lo index, and hi index
                t = clock() - t;                                                //stops the clock

                for(unsigned int i = 0; i < input_length; i++) {                //for loop prints the sorted array;
                    std::cout << a[i] << ' ';
                }
                std::cout << '\n' << '\n';
                std::cout << std::fixed << std::setprecision(4) << "The merge sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n'; // prints out the time merge sort algorithim took
            }
            else if (sort_algorithm == 4){      //Radix sort Code
                clock_t t;
                t = clock();

                Object.radixSort(input_length);

                t = clock() - t;

                Object.printList(input_length);
                std::cout << std::fixed << std::setprecision(4) << "The radix sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n';
            }

        }




        else if (vecType == 2) {                                              //Code for a partially sorted vector

            std::cout << "Enter the length of your list: ";
            std::cin >> input_length;
            std::cout << '\n' << "--------------------------------------------------------------------------------------------" << '\n' << '\n';;

            Object.buildPartiallySorted(input_length);

            std::cout << "1 = Insertion Sort" << std::endl;
            std::cout << "2 = Quick Sort" << std::endl;
            std::cout << "3 = Merge Sort" << std::endl;
            std::cout << "4 = Radix Sort" << std::endl;                       //figure this out after all three other algorithms are complete
            std::cout << '\n';

            std::cout << "Which sorting algorithm do you want? ";
            std::cin >> sort_algorithm;
            std::cout << '\n' << '\n';


            if (sort_algorithm == 1){
                clock_t t;
                t = clock();

                Object.insertionSort(input_length);

                t = clock() - t;

                Object.printList(input_length);
                std::cout << std::fixed << std::setprecision(4) << "The insertion sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n';
            }

            else if (sort_algorithm == 2){
                clock_t t;
                t = clock();

                int lo = 0;                                                         //declares lo = 0
                int hi = input_length - 1;                                          //declares hi = the length of the vector - 1
                Object.quickSort(input_length, lo, hi);                             //calls quicksort function with the input length, low index, and high index value

                t = clock() - t;

                Object.printList(input_length);         //prints the sorted vector
                std::cout << std::fixed << std::setprecision(4) << "The quick sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n';    //prints the time taken to sort the vector
            }

            else if (sort_algorithm == 3){                                      //Mergesort Code
                int a[input_length];                                            //Declares array to be used when calling the function
                for (int l = 0; l < input_length; l++) {                        //For loop to copy the generated vector into the array
                    a[l] = Object.vec[l];
                }

                clock_t t;                                                      //declares a clock variable
                t = clock();                                                    //Starts the clock
                int *aux = new int[input_length];                               //Declares an empty array pointer of size of the vector
                int lo = 0;                                                     //declares lo = 0
                int hi = input_length - 1;                                      //declares hi = the length of the vector minus 1
                Object.mergeSort(a, aux, lo, hi);                               //calls the mergsort algorithim entering in the array, the empty space array, lo index, and hi index
                t = clock() - t;                                                //stops the clock

                for(unsigned int i = 0; i < input_length; i++) {                //for loop prints the sorted array;
                    std::cout << a[i] << ' ';
                }
                std::cout << '\n' << '\n';
                std::cout << std::fixed << std::setprecision(4) << "The merge sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n'; // prints out the time merge sort algorithim took
            }

            else if (sort_algorithm == 4){
                clock_t t;
                t = clock();

                Object.radixSort(input_length);

                t = clock() - t;

                Object.printList(input_length);
                std::cout << std::fixed << std::setprecision(4) << "The radix sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n';
            }
        }

        else if (vecType == 3){                                            //REVERSE SORTED
            std::cout << "Enter the length of your list: ";
            std::cin >> input_length;
            std::cout << '\n' << "--------------------------------------------------------------------------------------------" << '\n' << '\n';
            std::cout << "length: " << input_length << '\n';
            Object.buildReversed(input_length);       // call function that creates the sorted vector passing in the original vector and the inputted length

            std::cout << "1 = Insertion Sort" << std::endl;
            std::cout << "2 = Quick Sort" << std::endl;
            std::cout << "3 = Merge Sort" << std::endl;
            std::cout << "4 = Radix Sort" << std::endl;                       //figure this out after all three other algorithms are complete
            std::cout << '\n';

            std::cout << "Which sorting algorithm do you want? ";
            std::cin >> sort_algorithm;
            std::cout << '\n' << '\n';


            if (sort_algorithm == 1){
                clock_t t;
                t = clock();

                Object.insertionSort(input_length);

                t = clock() - t;

                Object.printList(input_length);
                std::cout << std::fixed << std::setprecision(4) << "The radix sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n';
            }

            else if (sort_algorithm == 2){
                clock_t t;
                t = clock();

                int lo = 0;                                                         //decalres lo = 0
                int hi = input_length - 1;                                          //declares hi = the length of the vector - 1
                Object.quickSort(input_length, lo, hi);                             //calls quicksort function with the input length, low index, and high index value

                t = clock() - t;

                Object.printList(input_length);     //prints the sorted vector
                std::cout << std::fixed << std::setprecision(4) << "The quick sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n'; //prints the time taken to sort the vector
            }

            else if (sort_algorithm == 3){                                      //Mergesort Code
                int a[input_length];                                            //Declares array to be used when calling the function
                for (int l = 0; l < input_length; l++) {                        //For loop to copy the generated vector into the array
                    a[l] = Object.vec[l];
                }

                clock_t t;                                                      //declares a clock variable
                t = clock();                                                    //Starts the clock
                int *aux = new int[input_length];                               //Declares an empty array pointer of size of the vector
                int lo = 0;                                                     //declares lo = 0
                int hi = input_length - 1;                                      //declares hi = the length of the vector minus 1
                Object.mergeSort(a, aux, lo, hi);                               //calls the mergsort algorithim entering in the array, the empty space array, lo index, and hi index
                t = clock() - t;                                                //stops the clock

                for(unsigned int i = 0; i < input_length; i++) {                //for loop prints the sorted array;
                    std::cout << a[i] << ' ';
                }
                std::cout << '\n' << '\n';
                std::cout << std::fixed << std::setprecision(4) << "The merge sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n'; // prints out the time merge sort algorithim took
            }

            else if (sort_algorithm == 4){
                clock_t t;
                t = clock();

                Object.radixSort(input_length);

                t = clock() - t;

                Object.printList(input_length);
                std::cout << std::fixed << std::setprecision(4) << "The radix sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n';
            }
        }

        else if (vecType == 4){                                                     //RANDOM SORTED
            std::cout << "Enter the length of your list: ";
            std::cin >> input_length;
            std::cout << '\n' << "--------------------------------------------------------------------------------------------" << '\n' << '\n';
            std::cout << "length: " << input_length << '\n';
            Object.buildRandom(input_length);       // call function that creates the sorted vector passing in the original vector and the inputted length

            std::cout << "1 = Insertion Sort" << std::endl;
            std::cout << "2 = Quick Sort" << std::endl;
            std::cout << "3 = Merge Sort" << std::endl;
            std::cout << "4 = Radix Sort" << std::endl;                       //figure this out after all three other algorithms are complete
            std::cout << '\n';

            std::cout << "Which sorting algorithm do you want? ";
            std::cin >> sort_algorithm;
            std::cout << '\n' << '\n';

            if (sort_algorithm == 1){
                clock_t t;
                t = clock();

                Object.insertionSort(input_length);

                t = clock() - t;

                Object.printList(input_length);
                std::cout << std::fixed << std::setprecision(4) << "The insertion sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n';
            }

            else if (sort_algorithm == 2){
                clock_t t;
                t = clock();

                int lo = 0;                                                           //declares lo = 0
                int hi = input_length - 1;                                            //declares hi = the length of the vector - 1
                Object.quickSort(input_length, lo, hi);                               //calls quicksort function with the input length, low index, and high index value

                t = clock() - t;

                Object.printList(input_length);                                      //prints sorted vector
                std::cout << std::fixed << std::setprecision(4) << "The quick sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n';    //prints the time taken to sort the vector
            }

            else if (sort_algorithm == 3){                                      //Mergesort Code
                int a[input_length];                                            //Declares array to be used when calling the function
                for (int l = 0; l < input_length; l++) {                        //For loop to copy the generated vector into the array
                    a[l] = Object.vec[l];
                }

                clock_t t;                                                      //declares a clock variable
                t = clock();                                                    //Starts the clock
                int *aux = new int[input_length];                               //Declares an empty array pointer of size of the vector
                int lo = 0;                                                     //declares lo = 0
                int hi = input_length - 1;                                      //declares hi = the length of the vector minus 1
                Object.mergeSort(a, aux, lo, hi);                               //calls the mergsort algorithim entering in the array, the empty space array, lo index, and hi index
                t = clock() - t;                                                //stops the clock

                for(unsigned int i = 0; i < input_length; i++) {                //for loop prints the sorted array;
                    std::cout << a[i] << ' ';
                }
                std::cout << '\n' << '\n';
                std::cout << std::fixed << std::setprecision(4) << "The merge sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n'; // prints out the time merge sort algorithim took
            }

            else if (sort_algorithm == 4){
                clock_t t;
                t = clock();

                Object.radixSort(input_length);

                t = clock() - t;

                Object.printList(input_length);
                std::cout << std::fixed << std::setprecision(4) << "The radix sort algorithm took " << ((double)t)/CLOCKS_PER_SEC << " seconds" << '\n' << '\n';
            }

            //Object.printList(input_length);
        }
        // clear the vector here at the end of the while loop
        Object.clearVector();
    }

    return 0;
}