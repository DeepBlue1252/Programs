#include <iostream>
using namespace std;
#include <iomanip>

int main(){
    int rows = 9, i, j, k, x;
    int columns = 9;
    int grid[9][9];
    bool row = true, column = true, boxes = true, box, num;
    int numbers[] = {1,2,3,4,5,6,7,8,9};

//box variables
    int srow, erow, scol, ecol;

    //input
    for(i=0;i<9;i++){
        for(j=0;j<9;j++){
            cin >> x;
            grid[i][j] = x;
        }
    }

    //test
    /*for(i=0;i<9;i++){
        for(j=0;j<9;j++){
            cout<<grid[i][j];
        }
    }
    */

    //check rows
    for(i=0;i<9;i++){
        for(j=0;j<9;j++){
            num = false;
            k=0;
            while(k<9 && num == false){
                if(numbers[j]==grid[i][k]){
                    num = true;
                }else{
                    k++;
                }
            }
            if (num == false){
                row = false;
            }
        }

    }

    //columns
    for(i=0;i<9;i++){
        for(j=0;j<9;j++){
            num = false;
            k=0;
            while(k<9 & num == false){
                if(numbers[j]==grid[k][i]){
                    num = true;
                }
                k++;
            }
            if (num == false){
                column = false;
            }
        }

    }


    //check boxes
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            for(k=0;k<9;k++){
                num = false;
                for(srow = i*3;srow<i*3+3;srow++){
                    for(scol = j*3;scol<j*3+3;scol++){
                        if(numbers[k]==grid[srow][scol]){
                            num = true;
                        }

                    }
                }
                if (num == false){
                    boxes = false;
                }
            }
        }
    }



    if (row && column && boxes){
        cout<<"Solution is good!\n";
    } else {
        cout<<"Wrong solution!\n";
    }


    //input(grid);

    return 0;


}
