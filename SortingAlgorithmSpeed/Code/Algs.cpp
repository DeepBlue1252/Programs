#include <iostream>
#include <algorithm>
#include "Algs.h"
#include "time.h"
#include <cmath>
#include <iomanip>
#include <sstream>
#include <string>
#include <cstring>


void Sorting::buildSorted(int length) {
    for(unsigned int i = 0; i < length; i++) {          // pushes numbers from 0 to the inputted length from user into a vector
        this->vec.push_back(i);
    }
}

void Sorting::buildPartiallySorted(int length) {

    for(unsigned int i = 0; i < length; i++) {          // pushes numbers from 0 to the inputted length from user into a vector
        this->vec.push_back(i);
    }

    std::random_shuffle(this->vec.begin(), this->vec.end());    // shuffles every element in the vector

    //this creates a partially sorted vector with the middle third sorted and the first and last thirds unsorted
    std::sort(this->vec.begin() + (this->vec.size() / 3), this->vec.end() - (this->vec.size() / 3));    // sorts the first and last thirds of the vector

}

void Sorting::buildReversed(int length) {
    for(int i = (length - 1); i >= 0; i--) {        // pushes from the inputted number down to zero into a vector
        this->vec.push_back(i);
    }

    // this loop outputs the current vector if we want to check what it looks like before being sorted
    /*for(unsigned int i = 0; i < length; i++) {
        std::cout << this->vec[i] << ' ';
    }
    std::cout << '\n';*/
}

void Sorting::buildRandom(int length) {

    for(int i = (length - 1); i >= 0; i--) {        // pushes from the inputted number down to zero into a vector
        this->vec.push_back(i);
    }

    std::random_shuffle(this->vec.begin(), this->vec.end());    // shuffles every element in the array to create randomness

}

void Sorting::insertionSort(int length) {
    int temp;
    unsigned int i, j;

// insertion sort loops through the vector with an inner loop and at each iteration of i compares it with j
// j is iterating in reverse so that it can check if each current variable in j is less than or not to the variable at the previous position

    for(i = 0; i < length; i++) {       // loop through the vector using i
        for(j = i; j > 0; j--) {        // loop through the vector using j inside of the i loop to sort individual elements
            if (this->vec[j] < this->vec[j - 1]) {  // checks if vec at position j is less than vec at position j - 1
                temp = this->vec[j];                // assigns a temp variable
                this->vec[j] = this->vec[j - 1];    // swaps the vector j and j - 1 positions
                this->vec[j - 1] = temp;            // swaps the j - 1 with the temp variable
            }
            else {
                break;  // this break will break the program out of the inner for loop if there are no more j variables that are less than the current j
            }
        }
    }
}

//The Quicksort function takes in the array length, the lowest, and highest index as arguments
//Quicksort is recurssive, so it breaks our array down into subarrays and sorts it based off of a pivot value retrieved from the partition function.

void Sorting::quickSort(int length, int lo, int hi) {

    if (hi <= lo){      //This is the base case of the function. If the low index is ever higher or equal to the highest index, we will return.
        return;
    }

    int p = partition(lo, hi);      //We call the partition function in order to grab our pivot value.


    quickSort(length, lo, p - 1);   //Recursively sorts one half the array

    quickSort(length, p + 1, hi);   //Recursively sorts the other half of the array


}

int Sorting::partition(int lo, int hi){

    //Both i and j values will be used to compare values within the array, and are based off of our high and low index.
    //They will be incremented and decremented depending on whether or not their respective values in the array meet the requirements of the while loops below.

    int i = lo;
    int j = hi + 1;

    while(1){           //Will always run as 1 = True

        while(this->vec[++i] < this->vec[lo]){          //Checks to see if vec[i] is less than vec[lo]. i will also be incremented.
            if(i == hi){                                //Checks to see if i == hi. If at any point vec[++i] < vec[lo], then the loop will go until i == hi.
                break;
            }
        }

        while(this->vec[lo] < this->vec[--j]){          //Checks to see if vec[lo] is less than vec[--j]. j will be decremented.
            if(j == lo){                                //Checks to see if j == lo. If at any point vec[lo] < vec[--j], then the loop will go until j == lo.
                break;
            }
        }

        if(i >= j){                                     //if i >= j then the loop will break.
            break;
        }

        std::swap(this->vec[i], this->vec[j]);          //swaps vec[i] with vec[j]

    }

    std::swap(this->vec[lo], this->vec[j]);             //swaps vec[lo] with vec[j]


    return j;                                           //return the pivot value j
}




void Sorting::mergeSort(int *a, int *aux, int lo, int hi) {

    if (hi <= lo){                                      // this is the base case condition if met then it means we have reached one single node (one number)

        return;

    }

    int mid = lo + (hi - lo) / 2;                       // this declares the mid point where you will split the array

    mergeSort(a, aux, lo, mid);                         //recursivly calling the merge sort function with the first half of the array passed in

    mergeSort(a, aux, mid+1, hi);                       //recursivly calling the merge sort functuon with a (base array), aux (the empty space array), mid+1 (the mid point at the low end of the array, high as in the furthest point

    merge(a, aux, lo, mid, hi);                         //calls merge after the entire tree is created passes in a (original array), aux(the empty array )
}


void Sorting::merge(int *a, int *aux, int lo, int mid, int hi){

    std::memcpy(aux + lo, a + lo , (hi-lo+1) * sizeof(int));            //coppies the array

    int i = lo, j = mid + 1;                                            //startas the merge process where we put back together the items in the place they are meant to be

    for (int k = lo ; k <= hi; k++){                                    //loops through the length of each tree branch

        if (i > mid){                                                   // condition if the lo is less than the mid value
            a[k] = aux[j++];
        }

        else if (j > hi) {                                              // condition if the mid point is greater than the hi value
            a[k] = aux[i++];
        }

        else if (aux[j] < aux[i]) {                                     // then compares the coppied array values and sees if the next value past the mid point plus one
            a[k] = aux[j++];
        }

        else{                                                           // conditions if nothing else is met
            a[k] = aux[i++];
        }
    }
}




void Sorting::radixSort(int length){
    int max = this->vec[0];
    int i, digit;
    for(i=0;i<length;i++){
        if(this->vec[i]>max){
            max = this->vec[i];
        }
    }

    for(digit=1;max/digit>0;digit*=10){
        countingSort(length,digit);
        //printList(length);
    }
}
void Sorting::countingSort(int length, int digit){
    int i, j, counting[10], prefixSum[10], total=0, output[length];
    //sets all counts to 0
    for(i=0;i<10;i++){
        counting[i] = 0;
    }
    //Iterates place of digits
    for(i=0;i<length;i++){
        counting[(this->vec[i]/digit)%10]++;
    }
    //Prefix sum
    for(i=0;i<10;i++){
        total += counting[i];
        prefixSum[i] = total;
    }
    //Sort
    for(i=length-1;i>=0;i--){
        prefixSum[(this->vec[i]/digit)%10]--;
        output[prefixSum[(this->vec[i]/digit)%10]] = this->vec[i];
    }
    //set values
    for(i=0;i<length;i++){
        this->vec[i] = output[i];
    }
}





void Sorting::printList(int length) {             //  prints out the vector
    for(unsigned int i = 0; i < length; i++) {
        std::cout << this->vec[i] << ' ';
    }
    std::cout << '\n' << '\n';
}

void Sorting::clearVector() {
    this->vec.clear();              // clears the vector at the end of each while loop
}